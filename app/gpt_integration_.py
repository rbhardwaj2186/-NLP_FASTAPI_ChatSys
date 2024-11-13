import os
from dotenv import load_dotenv, find_dotenv
from langchain import HuggingFaceHub
import logging

# Load environment variables
_ = load_dotenv(find_dotenv())
hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")  # Ensure this matches the environment variable name

# Initialize the Hugging Face model with the correct token parameter
llm = HuggingFaceHub(
    repo_id="gpt2",  # Replace with your desired model, e.g., "bigscience/bloom-560m"
    huggingfacehub_api_token=hf_api_key,  # Pass the token as huggingfacehub_api_token
    model_kwargs={"temperature": 0.7}
)

# Setup logger for tracking the GPT response refinement process
logger = logging.getLogger("uvicorn")


def generate_gpt_response(predefined_response: str, client_context: str):
    """Generate a refined response using the Hugging Face model based on predefined action plan and client context."""
    # Combine the predefined response with client context to form the full context
    prompt = f"Refine the following action plan based on client needs:\n\n{predefined_response}\n\nClient Context:\n{client_context}"

    # Log the process of sending a prompt
    logger.info(f"Refining response using GPT with prompt: {prompt}")

    # Generate the refined response
    try:
        response = llm(prompt)

        # If response is a string, directly use it
        if isinstance(response, str):
            refined_response = response
        else:
            # If response is a more complex structure, extract text from it
            refined_response = response.get("text", "Error: No response text found")

        # Log the refined response
        logger.info(f"Refined response received: {refined_response}")
        return refined_response

    except Exception as e:
        logger.error(f"Error while generating GPT response: {e}")
        return "There was an error while refining the response. Please try again later."

