# data_retrieval.py
import os
import sys
sys.path.append(str('D:\\Work\\Gre\\UTD\\Courses\\Winter\Projects\\LLM\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\app'))

from .utils import load_csv_data
from .responses import get_action_plan_template
from .gpt_integration import generate_gpt_response
from .nlp import retrieve_context  # Import NLP context retrieval
import logging

# Load user and financial data once at startup
user_data = load_csv_data('data/user_database_detailed.csv')
financial_data = load_csv_data('data/financial_document_detailed.csv')


def retrieve_data_for_client(client_id):
    """Retrieve user and financial data for a client by ID."""
    user_info = user_data[user_data["Client ID"] == client_id]
    financial_info = financial_data[financial_data["Client ID"] == client_id]
    return user_info, financial_info


def generate_action_plan(client_id):
    """Generate an action plan based on retrieved data and chat context."""
    user_info, financial_info = retrieve_data_for_client(client_id)
    chat_context = retrieve_context(client_id)  # Get chat context via NLP

    if not user_info.empty and not financial_info.empty:
        # Data retrieval success
        action_plan_template = get_action_plan_template()
        formatted_response = action_plan_template.format(
            location=user_info["Location"].values[0],
            age=user_info["Age"].values[0],
            income=user_info["Income"].values[0],
            debts=user_info["Debts"].values[0],
            expenses=user_info["Expenses"].values[0]
        )
        return f"{formatted_response}\n\nClient Context:\n{chat_context}"
    else:
        # Data retrieval failure, use GPT fallback with chat context
        logging.error(f"Insufficient data for Client ID: {client_id}")
        action_plan_template = get_action_plan_template()
        human_content = f"Refined query for Client ID {client_id}, based on partial or no data. Context: {chat_context}"
        return generate_gpt_response(action_plan_template, human_content)
