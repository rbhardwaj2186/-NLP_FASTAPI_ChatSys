import os
from transformers import pipeline

# Define cache directory for Hugging Face models
CACHE_DIR = os.getenv("TRANSFORMERS_CACHE", "E:/pip_cache")  # Update to your preferred directory

# Load a summarization model from Hugging Face Transformers without cache_dir
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def load_chat_log(file_path="D:\\Work\\Gre\\UTD\\Courses\\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\data\\formatted_chat_log.txt"):
    """Load the chat log content from the specified file path."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Chat log file not found at {file_path}.")
        return None


def extract_client_conversation(client_id, chat_log):
    """Extract conversation lines specific to a client from the chat log."""
    if chat_log is None:
        return None
    # Filter lines in the chat log for the specified client ID
    client_conversations = [
        line for line in chat_log.split("\n") if f"Client ID: {client_id}" in line
    ]
    return " ".join(client_conversations) if client_conversations else None


def summarize_conversation(conversation_text, max_length=80, min_length=12):
    """Summarize a given conversation text."""
    if not conversation_text:
        return "No conversation found for this client."

    try:
        summary = summarizer(conversation_text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        print(f"Error: Summarization failed - {e}")
        return "Unable to summarize conversation."


def retrieve_context(client_id, chat_log_path="D:\\Work\\Gre\\UTD\\Courses\\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\data\\formatted_chat_log.txt"):
    """Retrieve context for a specific client by summarizing their chat history."""
    chat_log = load_chat_log(chat_log_path)
    conversation_text = extract_client_conversation(client_id, chat_log)
    return summarize_conversation(conversation_text)


# Example usage
if __name__ == "__main__":
    client_id = 101  # Replace with actual client ID for testing
    summary = retrieve_context(client_id)
    print(summary)
