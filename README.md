# Yolanda Hybrid III: AI-Powered Conversational Assistant

Yolanda Hybrid III is an AI-driven conversational assistant designed to enhance client interactions through natural language understanding and intelligent response refinement. Leveraging NLP, Machine Learning, and FastAPI, this project integrates data-driven insights with a robust architecture, facilitating high-quality customer service experiences.

## Project Overview

Yolanda Hybrid III combines AI technologies, NLP, and data analytics to refine client interactions across channels. Key functionalities include summarizing chat logs, A/B testing to optimize client satisfaction, and detailed insights into client interaction patterns.

### Key Features

1. **NLP Pipeline for Contextual Understanding**:
   - **Intent Recognition and Summarization**: Uses Hugging Face’s BART model for summarizing chat logs, capturing essential context for refined responses.
   - **Customizable Response Templates**: Responses are tailored using OpenAI's GPT models, offering adaptable conversational flows.

2. **Data Insights & A/B Testing**:
   - **Satisfaction Analysis**: A/B testing on new vs. returning clients to uncover satisfaction patterns and optimize response strategies.
   - **Time-Series Analysis**: Examines interaction trends over time, identifying peak hours to allocate resources efficiently.

3. **Scalable API Architecture**:
   - **FastAPI Framework**: Enables efficient request handling with modular structure and asynchronous capabilities.
   - **Pydantic for Data Validation**: Ensures reliable data parsing and validation for consistent API responses.

## Directory Structure

```plaintext
Yolanda_Hybrid_III/
│
├── app/
│   ├── main.py                       # Core FastAPI application with defined endpoints
│   ├── ab_testing.py                 # A/B testing logic for client insights
│   ├── gpt_integration.py            # GPT model integration for response refinement
│   ├── logging_config.py             # Custom logging configuration
│   ├── nlp.py                        # NLP pipeline for context extraction and summarization
│   ├── models.py                     # Pydantic models for data validation
│   ├── responses.py                  # Predefined responses and templates
│   └── database_handler.py           # Database interactions with SQLite
│
├── data/                             # Data storage for chat logs and auxiliary datasets
├── logs/                             # Log files and database for analysis
├── requirements.txt                  # Dependencies list
├── .env                              # Environment variables for API keys
└── README.md                         # Project documentation
