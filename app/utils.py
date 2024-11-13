# utils.py
import pandas as pd

def load_csv_data(file_path):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def load_chat_log(file_path):
    """Load and parse chat log for client context."""
    with open(file_path, "r") as f:
        return f.read()
