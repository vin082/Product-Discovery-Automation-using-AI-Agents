import os
from dotenv import load_dotenv
import streamlit as st

def load_config():
    load_dotenv()
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")