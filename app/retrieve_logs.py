import sqlite3
import csv
import re
from datetime import datetime

# Define the path for your SQLite database and output CSV
db_path = 'D:\\Work\\Gre\\UTD\\Courses\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\logs\\app_logs.db'
csv_output_path = 'D:\\Work\\Gre\\UTD\\Courses\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\logs\\logs_for_analysis.csv'

def extract_client_feedback(message):
    """Extract client_id and satisfactory information from the message."""
    # Regex to match the feedback message and extract client_id and satisfactory
    match = re.search(r"Received feedback: client_id=(\d+), satisfactory=(True|False)", message)
    if match:
        client_id = match.group(1)
        satisfactory = match.group(2) == 'True'  # Convert string "True"/"False" to boolean
        return client_id, satisfactory
    return None, None

def retrieve_and_export_logs():
    """Retrieve logs from the database and export to CSV."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query all logs
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    # Prepare to write to CSV
    with open(csv_output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'level', 'client_id', 'satisfactory'])  # Header for CSV

        # Process each log entry
        for log in logs:
            timestamp = log[0]  # Assuming timestamp is in the first column
            level = log[1]      # Log level is in the second column
            message = log[2]    # Log message is in the third column

            # Extract client_id and satisfactory status if the message contains feedback
            client_id, satisfactory = extract_client_feedback(message)

            if client_id is not None:
                # Write the log entry with client_id and satisfactory to CSV
                writer.writerow([timestamp, level, client_id, satisfactory])

    conn.close()

# Run the function to retrieve and export logs to CSV
if __name__ == "__main__":
    retrieve_and_export_logs()
