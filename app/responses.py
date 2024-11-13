# responses.py

responses = {
    "Create an action plan": (
        "Action Plan for a Family of 3 in Richardson, TX\n\n"
        "Background:\n"
        "- Location: Richardson, TX 75081\n"
        "- Age: 42\n"
        "- Annual Income: $72,000\n"
        "- Debts: $1,000\n"
        "- Expenses: $4,000\n"
        "- Assets: $0\n\n"
        "Goals:\n"
        "- Pay off debts\n"
        "- Build savings\n"
        "- Retire comfortably\n"
        "- Provide for children's education\n\n"
        "Steps:\n"
        "1. Create a Budget\n"
        "2. Pay Off Debts\n"
        "3. Build Savings\n"
        "4. Invest for Retirement\n"
        "5. Plan for Children's Education\n"
        "6. Seek Professional Advice\n\n"
        "Timeline:\n"
        "- 1-3 months: Create budget and identify debt repayment plan.\n"
        "- 6-12 months: Pay off high-interest debt and build emergency savings.\n"
        "- 1-5 years: Contribute consistently to savings and retirement accounts.\n"
        "- 5-10 years: Start planning for children's education.\n"
        "- 10-20 years: Focus on long-term retirement planning and investment.\n\n"
        "Monitoring and Evaluation:\n"
        "Regularly review budget, track debt repayment, and seek professional advice as needed."
    )
}

def get_action_plan_template():
    """Retrieve the action plan template."""
    return responses["Create an action plan"]

def get_predefined_response(question):
    """Retrieve a predefined response based on the question."""
    return responses.get(question, "No predefined response available.")
