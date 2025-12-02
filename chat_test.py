# chat_test.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def detect_mode(user_input):
    """
    Detect the tutoring mode:
    - exercise: practice problems
    - debug: errors or code issues
    - explain: conceptual questions
    - feedback: general guidance
    """
    user_lower = user_input.lower()

    # Exercise keywords
    exercise_keywords = [
        'exercise', 'practice', 'problem', 'challenge', 'task', 'quiz',
        'assignment', 'example', 'create a problem', 'write a function',
        'make a program', 'generate a challenge'
    ]

    # Debug / error keywords only
    debug_keywords = [
        'wrong', 'error', "doesn't work", 'bug', 'issue', 'problem in code',
        'syntax', 'exception', 'traceback', 'fix this'
    ]

    # Explain / conceptual keywords
    explain_keywords = [
        'explain', 'describe', 'define', 'meaning of', 'purpose',
        'concept', 'understand', 'difference', "what is", "how"
    ]

    # Detection order
    if any(k in user_lower for k in exercise_keywords):
        return 'exercise'
    elif any(k in user_lower for k in debug_keywords):
        return 'debug'
    elif any(k in user_lower for k in explain_keywords):
        return 'explain'
    else:
        return 'feedback'


def chat_with_gpt(user_input, mode):
    """Send structured prompt to ChatGPT based on mode
    Returns: (response_text, tokens_used, estimated_cost)
    """
    if mode == 'debug':
        prompt = f"""
You are a Python tutor.
Analyze the following code snippet for errors, explain the issue, and provide a corrected version.
If this code is Java, translate it to proper Python syntax:
- Remove all semicolons (;) and curly braces ({{}}).
- Use proper Python indentation and syntax.

User input:
{user_input}

Response format:
Debugging Feedback:
Corrected Code (plain text, properly indented Python code):
Practice Exercise (optional):
"""
    elif mode == 'exercise':
        prompt = f"""
You are a Python tutor.
Create a thoughtful Python practice exercise based on the following topic or request:
{user_input}

Response format:
Practice Exercise (plain text, properly formatted Python code if relevant):
"""
    elif mode == 'explain':
        prompt = f"""
You are a Python tutor.
Explain the following concept in simple terms and provide a Python code example if relevant:

User input:
{user_input}

Response format:
Concept Explanation:
Code Example (optional):
"""
    else:  # feedback / general
        prompt = f"""
You are a Python tutor.
Provide helpful feedback and guidance based on the user input:

User input:
{user_input}

Response format:
Feedback:
Suggested Next Steps:
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Python tutor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600
        )

        response_text = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        estimated_cost = tokens_used * 0.002 / 1000

        return response_text, tokens_used, estimated_cost

    except Exception as e:
        return f"Error communicating with OpenAI API: {e}", 0, 0
