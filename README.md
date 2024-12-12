# NLP_FASTAPI_CHATSYS: AI-Powered Conversational Assistant

NLP_FASTAPI_ChatSys is an AI-driven conversational assistant designed to enhance client interactions through natural language understanding and intelligent response refinement. Leveraging NLP, Machine Learning, and FastAPI, this project integrates data-driven insights with a robust architecture, facilitating high-quality customer service experiences.

## Project Overview
![ddds](https://github.com/user-attachments/assets/84a15f48-79bb-489e-9671-788fd4c663dd)

NLP_FASTAPI_ChatSys combines AI technologies, NLP, and data analytics to refine client interactions across channels. Key functionalities include summarizing chat logs, A/B testing to optimize client satisfaction, and detailed insights into client interaction patterns.

![image_d3](https://github.com/user-attachments/assets/736a0105-a514-4cbe-824f-7799ade01b63)

NLP_FASTAPI_ChatSys Workflow Process

![df12](https://github.com/user-attachments/assets/18a79edf-37a9-42a3-82ec-4b8db27ad50c)


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

  ## Flow of data flow

  ![13b](https://github.com/user-attachments/assets/21f13cc0-5523-4c1c-aaba-097655bc0fac)


  
  ![13c](https://github.com/user-attachments/assets/e1597502-e789-4f2a-850a-18d86a849e2a)
  

  
  ![13d](https://github.com/user-attachments/assets/559b0496-a0a8-4e6b-a481-3eee01f7716c)



  ![13e](https://github.com/user-attachments/assets/789cdf46-b65e-4c7c-854e-5a49f5819bc9)


  
  ![13f](https://github.com/user-attachments/assets/5b52a747-3e13-46ab-b4e3-f42afda22f83)



  
  ![13g](https://github.com/user-attachments/assets/0f3c0f61-05d3-4645-a8ff-896b7f61bc61)


## Directory Structure

```plaintext
NLP_FASTAPI_ChatSys/
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


```

Getting Started
Prerequisites

    Python 3.8+
    FastAPI
    Hugging Face Transformers
    TensorFlow/PyTorch
    SQLite for logging and analysis

Installation

    Clone the Repository:

git clone https://github.com/rbhardwaj2186/NLP_FASTAPI_ChatSys.git
cd NLP_FASTAPI_ChatSys

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:

    Update .env with API keys for OpenAI and other services.

Run the Application:

    uvicorn app.main:app --reload

API Endpoints

    /query: Handles client queries, passing through the NLP pipeline for summarization and GPT refinement.
    /feedback: Records feedback, triggering A/B testing analysis based on client satisfaction.
    /visualization/*: Provides satisfaction and trend visualizations as PNG images for client usage analysis.

Technical Highlights
1. Pydantic Models

Pydantic models ensure input validation and serialization in FastAPI, enabling robust and consistent data handling. Key models include:

    Query: Validates client queries.
    ActionPlan: Structures action plans.
    Feedback: Tracks client satisfaction.

2. NLP Pipeline

The NLP workflow integrates summarization, intent recognition, and topic modeling, leveraging transformers for contextual understanding and response adaptability.
3. A/B Testing and Visualization

A/B testing identifies satisfaction trends among new vs. returning clients. Seaborn and Matplotlib power visualizations of satisfaction rates and time-series data, aiding client behavior analysis.
Future Plans

    Enhanced User Personalization: Implement CORS for API integration to serve premium users with on-demand features.
    Continuous Feedback Integration: Incorporate user feedback loops to refine AI-driven responses based on real-time interactions.

Contributing

We welcome contributions! Please fork the repository and submit a pull request with any improvements or new features.
License

This project is licensed under the Private License. No Duplication is Entertained.
