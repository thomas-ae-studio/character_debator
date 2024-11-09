import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.title("Trump vs. Vance Debate Simulator")

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "turn" not in st.session_state:
    st.session_state.turn = "Trump"
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = "Discuss the current state of the economy."

def generate_response(speaker, prompt):
    """Generate a response from the specified speaker using OpenAI's API."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are {speaker}."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def continue_debate():
    """Simulate the next round in the debate, alternating responses."""
    if st.session_state.turn == "Trump":
        response = generate_response("Donald Trump", st.session_state.last_prompt)
        st.session_state.conversation.append(("Trump", response))
        st.session_state.turn = "Vance"
        st.session_state.last_prompt = response
    else:
        response = generate_response("J.D. Vance", st.session_state.last_prompt)
        st.session_state.conversation.append(("Vance", response))
        st.session_state.turn = "Trump"
        st.session_state.last_prompt = response

# Display conversation
st.write("Press 'Next Round' to continue the debate between Trump and Vance.")

if st.button("Next Round"):
    continue_debate()

# Show the conversation
for speaker, text in st.session_state.conversation:
    st.write(f"**{speaker}:** {text}")