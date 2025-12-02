## OFRI NAHUM- COSC 461 FINAL PROJECT ##
📘 AI Python Tutor — Detailed Setup & Running Instructions

This document provides step-by-step instructions for installing, configuring, and running the AI Python Tutor application.
Follow these steps exactly to run the Streamlit interface correctly.

✅ 1. Install Python

You must have Python 3.9 or higher installed.

Check your version:

python --version

or on macOS:

python3 --version


If you do not have Python installed, download it from: https://www.python.org/downloads/

✅ 2. Install Required Python Packages

Open a terminal in the project folder and run:

pip install streamlit openai

If your system uses python3, run:

pip3 install streamlit openai


This installs:

Streamlit (used for the GUI)

The OpenAI client library


✅ 3. Add Your OpenAI API Key

Open the file:

config.py

Inside, you will see:

OPENAI_API_KEY = "INSERT_YOUR_KEY_HERE"


Replace the placeholder text with your own API key:

OPENAI_API_KEY = "sk-123abcYOURKEYHERE"


✅ 4. Run the AI Tutor

In a terminal inside the project directory, run:

streamlit run ai_tutor_gui.py


Streamlit will:

Start a local server

Automatically open the app in your browser

If it doesn’t open automatically, Streamlit will show a URL, usually:

http://localhost:8501


Open that link manually if needed.



✅ 5. Using the Tutor

Once the app is running:

Type a question or paste code into the text box

The system automatically detects the intent

The response will be structured into sections based on the input catagory:

Concept Explanation

Code Example

Debugging Feedback

Practice Exercise

Examples you can try:

“Explain Python loops”

“Why is this code not working? for i in range(5) print(i)”

“Give me an exercise about lists”

“Can you check my answer?”

✅ 6. Common Issues & Fixes
❗ Streamlit command not found

Install Streamlit again:

pip install streamlit

❗ App says “invalid API key”

Double-check config.py has a real key:

OPENAI_API_KEY = "your_actual_key_here"

❗ Browser does not open automatically

Copy/paste the URL from the terminal, e.g.:

http://localhost:8501

❗ Using Python 2 accidentally

Always use:

python3

or

pip3