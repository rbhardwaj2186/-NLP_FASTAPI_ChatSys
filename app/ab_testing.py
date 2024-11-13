import pandas as pd
from scipy import stats
import re
from datetime import datetime

def load_data(file_path):
    """Load data from the CSV file."""
    data = pd.read_csv(file_path)
    # Convert timestamp to datetime type with the correct format
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')
    return data


def extract_client_feedback(message):
    """Extract client_id and satisfactory information from the message."""
    match = re.search(r"Received feedback: client_id=(\d+), satisfactory=(True|False)", message)
    if match:
        client_id = match.group(1)
        satisfactory = match.group(2) == 'True'  # Convert string "True"/"False" to boolean
        return client_id, satisfactory
    return None, None

def perform_ab_testing(data):
    """Perform A/B testing on the provided data."""

    # Segment by Client Type (New vs Returning)
    data['client_segment'] = data['client_id'].apply(lambda x: 'New' if x == 0 else 'Returning')

    # Segment by Time of Day (Morning, Afternoon, Evening)
    def get_time_of_day(hour):
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Afternoon'
        else:
            return 'Evening'

    data['time_of_day'] = data['timestamp'].dt.hour.apply(get_time_of_day)

    # Calculate satisfaction rates for Client Segment A/B Test
    group_a = data[data['client_segment'] == 'New']
    group_b = data[data['client_segment'] == 'Returning']
    group_a_satisfaction_rate = group_a['satisfactory'].value_counts(normalize=True).get(True, 0)
    group_b_satisfaction_rate = group_b['satisfactory'].value_counts(normalize=True).get(True, 0)

    # Perform Chi-Squared Test for Client Segment
    contingency_table_segment = pd.crosstab(data['satisfactory'], data['client_segment'])
    chi2_stat_segment, p_val_segment, dof_segment, expected_segment = stats.chi2_contingency(contingency_table_segment)

    # Calculate satisfaction rates for Time of Day A/B Test
    group_morning = data[data['time_of_day'] == 'Morning']
    group_afternoon = data[data['time_of_day'] == 'Afternoon']
    group_evening = data[data['time_of_day'] == 'Evening']
    morning_satisfaction_rate = group_morning['satisfactory'].value_counts(normalize=True).get(True, 0)
    afternoon_satisfaction_rate = group_afternoon['satisfactory'].value_counts(normalize=True).get(True, 0)
    evening_satisfaction_rate = group_evening['satisfactory'].value_counts(normalize=True).get(True, 0)

    # Perform Chi-Squared Test for Time of Day
    contingency_table_time = pd.crosstab(data['satisfactory'], data['time_of_day'])
    chi2_stat_time, p_val_time, dof_time, expected_time = stats.chi2_contingency(contingency_table_time)

    return {
        "Client Segment Satisfaction Rates": {
            "New Clients": group_a_satisfaction_rate,
            "Returning Clients": group_b_satisfaction_rate,
            "p_value": p_val_segment,
            "conclusion": "Significant difference" if p_val_segment < 0.05 else "No significant difference"
        },
        "Time of Day Satisfaction Rates": {
            "Morning": morning_satisfaction_rate,
            "Afternoon": afternoon_satisfaction_rate,
            "Evening": evening_satisfaction_rate,
            "p_value": p_val_time,
            "conclusion": "Significant difference" if p_val_time < 0.05 else "No significant difference"
        }
    }
