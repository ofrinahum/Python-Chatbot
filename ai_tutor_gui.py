# ai_tutor_gui.py
import streamlit as st
from chat_test import chat_with_gpt, detect_mode

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Python Tutor", page_icon="🧑‍💻", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
<style>
.stApp {background: linear-gradient(to right, #FFDEE9, #B5FFFC); font-family: 'Comic Sans MS', cursive, sans-serif;}
.chat-container {max-height: 500px; overflow-y: auto; padding: 10px;}
</style>
""", unsafe_allow_html=True)

# --- CHAT BUBBLE FUNCTION ---
def display_message(message, is_user=False):
    bg_color = "#FFE4E1" if is_user else "#FFFFFF"
    align = "right" if is_user else "left"
    st.markdown(
        f"""
        <div style="background-color: {bg_color}; padding: 12px; border-radius: 12px;
                    margin: 5px 0px; text-align: {align}; font-size: 16px;">
        {message.replace('\n','<br>')}
        </div>
        """, unsafe_allow_html=True
    )

# --- TITLE & INSTRUCTIONS ---
st.title("🧑‍💻 AI Python Tutor")
st.write("Paste Python or Java code, or ask a question. The AI tutor remembers the conversation!")

# --- INITIALIZE MEMORY ---
if "memory" not in st.session_state:
    st.session_state.memory = []  # Each item: (role, content, mode)

# --- CHAT HISTORY CONTAINER ---
chat_container = st.container()

# --- USER INPUT ---
user_input = st.chat_input("Type your message here...")

if user_input:
    mode = detect_mode(user_input)
    st.session_state.memory.append(("user", user_input, mode))

    # Combine conversation for AI
    conversation_history = ""
    for role, content, _ in st.session_state.memory:
        conversation_history += f"{role}: {content}\n"

    # Get AI response
    response, tokens_used, estimated_cost = chat_with_gpt(conversation_history, mode)
    st.session_state.memory.append(("tutor", response, mode))

    # Optional: show token usage info
    st.info(f"Tokens used: {tokens_used} | Estimated cost: ${estimated_cost:.5f}")

# --- DISPLAY CHAT HISTORY ---
with chat_container:
    for role, message, mode in st.session_state.memory:
        if role == "tutor":
            # Define which sections to show per mode
            mode_sections = {
                "explain": ["Concept Explanation:", "Code Example:"],
                "debug": ["Debugging Feedback:", "Corrected Code:", "Practice Exercise:"],
                "exercise": ["Practice Exercise:"],
                "feedback": ["Feedback:", "Suggested Next Steps:"]
            }
            sections_to_show = mode_sections.get(mode, [])
            displayed = False

            for sec in sections_to_show:
                if sec in message:
                    start = message.find(sec)
                    # Find the start of next section or end of message
                    end_candidates = [message.find(s, start+1) for s in sections_to_show if message.find(s, start+1) != -1]
                    end = min([i for i in end_candidates if i != -1] + [len(message)])
                    content = message[start:end].strip()

                    if sec in ["Corrected Code:", "Code Example:", "Practice Exercise:"]:
                        # Strip header and preserve indentation
                        code_content = content.replace(sec, "").strip()
                        code_content = "\n".join([line.rstrip() for line in code_content.splitlines()])
                        with st.expander(sec, expanded=True):
                            st.code(code_content, language="python")
                    else:
                        # Escape HTML for non-code sections
                        text_content = content.replace(sec, "").strip()
                        text_content = text_content.replace("<","&lt;").replace(">","&gt;")
                        with st.expander(sec, expanded=True):
                            st.write(text_content)

                    displayed = True
            if not displayed:
                display_message(message, is_user=False)
        else:
            display_message(message, is_user=True)

# --- FOOTER ---
st.markdown("""
---
*Tip:* Input clears after sending. Responses are tailored to the question type.
Code sections preserve indentation and are safe for Java → Python translations.
""")
