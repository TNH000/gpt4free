import os, json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from json import loads
from os import urandom

from requests import post

# Generate a random session ID
sessionId = urandom(10).hex()

# Set up headers for the API request
headers = {
    'Accept': 'text/event-stream',
    'Accept-Language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://ora.ai/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'token': 'null',
}

def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        params = {"chatbotId":"d9afd8ee-f6d3-4717-8aae-35e2dfe88de5","input":question,"userId":"66336d6d-0b9a-4921-850b-e52252490d84","provider":"OPEN_AI","config":False,"includeHistory":True}
        
        reply = ''
    # Send request to the API and process the response
        chunk = post('https://ora.ai/api/conversation', params=params, headers=headers, verify=False, stream=True).text:
        if 'response' in chunk:
                 data = json.loads(chunk)
                 reply+=['response']
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
