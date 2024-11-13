from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import os
import sys
from .models import Query, Feedback
from .responses import get_predefined_response
from .gpt_integration import generate_gpt_response
from .nlp import retrieve_context  # Importing from nlp.py
from .logging_config import setup_logging
from .ab_testing import perform_ab_testing, load_data
from .visualization import plot_satisfaction_by_client, generate_visualizations, plot_time_series_trend
import logging
import sqlite3

# Set up logging
setup_logging()

# Create a logger
logging.basicConfig(level=logging.DEBUG) # Will capture Infor, error, warning..
logger = logging.getLogger("uvicorn")

# Example of logging an error
try:
    # Simulating an error
    x = 1 / 0
except ZeroDivisionError as e:
    logger.error(f"Error occurred: {e}")

# Temporary storage to hold responses for refinement
response_storage = {}

app = FastAPI()


@app.post("/query")
async def handle_query(query: Query):
    """Handle client query and return the appropriate action plan."""
    # Log the request
    logger.info(f"Received request: POST /query with client_id={query.client_id}, question={query.question}")

    # Step 1: Retrieve the predefined response
    predefined_response = get_predefined_response(query.question)

    if predefined_response:
        # Retrieve context using NLP (summarized client conversation)
        client_context = retrieve_context(query.client_id)  # Get the context for this client

        # Store the response and context using client ID to simulate session storage
        response_storage[query.client_id] = {
            'response': predefined_response,
            'context': client_context
        }

        # Log the response
        logger.info(f"Returning predefined response for client_id={query.client_id}")

        # Return the predefined response along with the client context
        return {"response": predefined_response, "context": client_context}

    # If no predefined response exists, log and return a 404 error
    logger.error(f"No predefined response found for question: {query.question}")
    raise HTTPException(status_code=404, detail="Query not recognized")


@app.post("/feedback")
async def handle_feedback(feedback: Feedback):
    """Handle feedback to refine the action plan using GPT if needed."""
    # Log the feedback received
    logger.debug(f"Received feedback: client_id={feedback.client_id}, satisfactory={feedback.is_satisfactory}")

    # Check if there is an existing response for the client ID
    stored_data = response_storage.get(feedback.client_id)

    if stored_data:
        predefined_response = stored_data['response']
        client_context = stored_data['context']

        # If the user is satisfied, log and return the initial response
        if feedback.is_satisfactory:
            logger.info(f"Client {feedback.client_id} is satisfied with the response.")
            return {"response": predefined_response, "context": client_context}

        # If the user is not satisfied, refine the response using GPT
        else:
            logger.info(f"Client {feedback.client_id} is not satisfied. Refining the response using GPT.")

            try:
                refined_response = generate_gpt_response(predefined_response,
                                                         client_context)  # Include context with GPT refinement
                logger.info(f"Refined response for client_id={feedback.client_id}: {refined_response}")
                return {"response": refined_response, "context": client_context}

            except Exception as e:
                logger.error(f"Error while generating refined response: {e}")
                return {"response": "There was an error while refining the response. Please try again later.",
                        "context": client_context}

    # Log and return a 404 error if no initial response exists
    logger.error(f"No initial response found for client_id={feedback.client_id}")
    raise HTTPException(status_code=404, detail="No initial response found for this client ID.")


@app.get("/logs")
async def get_logs():
    """Retrieve logs from the database."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("logs/app_logs.db")
        cursor = conn.cursor()

        # Query all logs
        cursor.execute("SELECT * FROM logs")
        logs = cursor.fetchall()

        # Format the logs into a list of dictionaries for easy JSON response
        log_entries = [
            {"timestamp": log[0], "level": log[1], "message": log[2]}
            for log in logs
        ]

        conn.close()

        # Return logs as a JSON response
        return {"logs": log_entries}

    except sqlite3.OperationalError as e:
        raise HTTPException(status_code=500, detail=f"Error while retrieving logs: {e}")

# Load the data for A/B testing
data = load_data('D:\\Work\\Gre\\UTD\\Courses\\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\logs\\logs_for_analysis.csv')

@app.get("/ab_test")
async def ab_test():
    """Endpoint to perform A/B testing."""
    try:
        ab_test_results = perform_ab_testing(data)
        return ab_test_results
    except Exception as e:
        logger.error(f"Error during A/B testing: {e}")
        raise HTTPException(status_code=500, detail="Error during A/B testing")

@app.get("/visualization/satisfaction-by-client")
async def satisfaction_by_client():
    buf = plot_satisfaction_by_client(data)
    return StreamingResponse(buf, media_type="image/png")

@app.get("/visualization/time-series-trend")
async def time_series_trend():
    buf = plot_time_series_trend(data)
    return StreamingResponse(buf, media_type="image/png")