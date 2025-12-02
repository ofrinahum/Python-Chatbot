## OFRI NAHUM- COSC 461 FINAL PROJECT##
🧠 AI Python Tutor: A Streamlit-based AI tutor for introductory Python programming.

📌 Overview: 
This project implements an AI-powered tutoring system designed to assist beginners learning Python.
The tutor can:

1. Explain Python concepts
2. Debug simple code snippets
3. Provide annotated example code
4. Generate practice exercises
5. Give feedback on student responses
6. Convert Java code to Python code

The system uses the OpenAI API along with custom intent detection to determine what kind of help the user is asking for.

📁 Project Structure
├── ai_tutor_gui.py      # Streamlit web interface
├── tutor.py             # Tutoring logic + intent detection
├── config.py            # API key placeholder
├── README.md            # Project overview

🔧 Requirements:
1. Python 3.9+
2. OpenAI API key
3. Streamlit
4. openai Python package

Install dependencies:

pip install streamlit openai

🔑 API Key Setup

Open config.py and replace:

OPENAI_API_KEY = "INSERT_YOUR_KEY_HERE"

with your own API key.


▶️ Running the Tutor (Streamlit GUI)

Run the app with:

streamlit run ai_tutor_gui.py

This will open a browser window with the AI Tutor interface.


🧠 Features Implemented

1. Concept Explainer: clear explanations of Python basics
2. Code Example Generator: annotated Python examples
3. Error Debugger: identifies and explains mistakes in user code
4. Exercise Creator: produces practice tasks
5. Feedback Provider: evaluates students’ answers and encourages improvement
6. Intent Classification: determines whether the user wants explanation, debugging, exercises, etc.
7. Structured Responses: consistently formats the output into sections

📌 Notes
1. Uses the official OpenAI API.
2. No keys or sensitive credentials are stored in the repo.
3. GUI allows clean and user-friendly interactions.