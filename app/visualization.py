import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import io

def load_data(file_path="D:\\Work\\Gre\\UTD\\Courses\\Winter\\Projects\\LLM\\LLM_Fine_Tuning\\LLM_Fine_Tuning\\Yolanda_Hybrid_III\\logs\\logs_for_analysis.csv"):
    """Load data from CSV file."""
    return pd.read_csv(file_path)

# 1. Visualization: Satisfaction by Client
def plot_satisfaction_by_client(data):
    """
    This function generates a count plot of satisfaction by client_id.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='client_id', hue='satisfactory')
    plt.title('Satisfaction by Client')
    plt.xlabel('Client ID')
    plt.ylabel('Count of Feedback')
    plt.legend(title="Satisfaction", labels=['Not Satisfactory', 'Satisfactory'])
    # Save plot to a buffer and return
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# 2. Visualization: Time Series Trend of Usage
def plot_time_series_trend(data):
    """
    This function generates a time series plot of feedback based on timestamps.
    """
    # Convert timestamp to datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%d-%m-%Y %H:%M')

    # Resample the data to hourly frequency and count the number of entries
    time_series_data = data.resample('H', on='timestamp').size()

    plt.figure(figsize=(12, 6))
    time_series_data.plot()
    plt.title('Time Series Trend of Feedback')
    plt.xlabel('Time')
    plt.ylabel('Number of Feedback Entries')
    plt.grid(True)
    # Save plot to a buffer and return
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# Main function to generate and save all visualizations
def generate_visualizations():
    # Load data
    data = load_data()

    # Generate Satisfaction by Client Plot
    satisfaction_buf = plot_satisfaction_by_client(data)

    # Generate Time Series Trend Plot
    time_series_buf = plot_time_series_trend(data)

    # Save the plots as images (optional, if you want to save them locally)
    satisfaction_buf.seek(0)
    with open('satisfaction_by_client.png', 'wb') as f:
        f.write(satisfaction_buf.read())

    time_series_buf.seek(0)
    with open('time_series_trend.png', 'wb') as f:
        f.write(time_series_buf.read())

# Run the visualization generation
if __name__ == "__main__":
    generate_visualizations()
