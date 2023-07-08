import os, json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from json import loads
from os import urandom

from requests import post

# Generate a random session ID
sessionId = urandom(10).hex()

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "Referer": "https://p2.v50.ltd/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

def get_answer(question: str) -> str:
    try:
        params = {
        "prompt": question,
        "options": {},
        "systemMessage": "You are AlphaAI, a large language model trained by Shajada Alif. Follow the user's instructions carefully. Respond using markdown.",
        "temperature": 0.8,
        "top_p": 1,
        "model": "capybara",
        "user": None
        }
        reply = ''
        chunk = post('https://p2.v50.ltd/api/chat-process', headers=headers, data=json.dumps(params))
        if 200 in chunk.status_code:
                 reply+=chunk.text
        return reply
    except Exception as e:
        # Return error message if an exception occurs
        return f'An error occurred: {e}. Please Contact Shajada0.'

# Set page configuration and add header
st.set_page_config(
    page_title="Alpha AI",
    initial_sidebar_state="expanded",
    page_icon="💀",
    menu_items={
        'Get Help': 'https://www.facebook.com/Shajada0',
        'Report a bug': "https://www.facebook.com/Shajada0",
        'About': "Alpha AI 5.0 By Shajada"
    }
)
st.header('Alpha AI 5.0 By Shajada')

# Add text area for user input and button to get answer
question_text_area = st.text_area(
    '🤖 Input :', placeholder='Explain')
if st.button('🧠 Think'):
    answer = get_answer(question_text_area)
    # Display answer
    st.caption("Answer :")
    st.markdown(answer)

# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
