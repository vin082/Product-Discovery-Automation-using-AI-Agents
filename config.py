import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")