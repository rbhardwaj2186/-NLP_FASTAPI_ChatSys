import requests

# Define the FastAPI endpoint URLs
query_url = "https://your-fastapi-service.com/query"
feedback_url = "https://your-fastapi-service.com/feedback"

def get_action_plan(question, client_id):
    response = requests.post(
        query_url,
        json={"question": question, "client_id": client_id}
    )
    return response.json()

def send_feedback(client_id, is_satisfactory):
    response = requests.post(
        feedback_url,
        json={"client_id": client_id, "is_satisfactory": is_satisfactory}
    )
    return response.json()

# Example of using the functions
action_plan_response = get_action_plan("Create an action plan", 101)
print(action_plan_response)

# Sending feedback (e.g., if the user is unsatisfied)
refined_plan_response = send_feedback(101, False)
print(refined_plan_response)
