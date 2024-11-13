from pydantic import BaseModel

class Query(BaseModel):
    question: str
    client_id: int

class ActionPlan(BaseModel):
    client_id: int
    plan: str

class Feedback(BaseModel):
    client_id: int
    is_satisfactory: bool  # True if the user is satisfied, False if refinement is needed
