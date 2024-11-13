import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
import logging

# Load environment variables
_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI model with the provided API key
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

# Define the system and user messages for the prompt template
system_template = "Refine the following action plan based on client needs, without asking for further response"
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=system_template),
    HumanMessage(content="{context}")
])

# Chain the prompt template and LLM
action_plan_chain = prompt_template | llm

# Setup logger for tracking the GPT response refinement process
logger = logging.getLogger("uvicorn")

def generate_gpt_response(predefined_response: str, client_context: str):
    """Generate a refined response using GPT, based on a predefined action plan."""
    prompt = f"Refine the following action plan based on client needs:\n\n{predefined_response}\n\nClient Context: {client_context}"

    logger.info(f"Refining response using GPT with prompt: {prompt}")

    try:
        # Pass the prompt directly to the model (no need to wrap it in a dictionary)
        response = llm.invoke(prompt)  # Pass prompt as a string

        # Log the full response for inspection
        logger.info(f"Response received from GPT: {response}")

        # Check if the response is an AIMessage object (adjusted based on your model's response)
        if hasattr(response, 'content'):
            refined_response = response.content  # Directly access the 'content' attribute of AIMessage
        elif isinstance(response, str):
            refined_response = response  # If it's already a string, use it directly
        else:
            refined_response = "Error: Invalid response format from GPT."

        logger.info(f"Refined response received: {refined_response}")
        return refined_response

    except Exception as e:
        logger.error(f"Error while generating GPT response: {e}")
        return f"There was an error while refining the response. Error: {e}"  # Return detailed error for debugging
