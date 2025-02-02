__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from workflow import ProductDiscoveryWorkflow
#from config import load_config

from openai import OpenAI

def format_results(results):
    """
    Formats the results from the workflow into readable sections.
    """
    try:
        if isinstance(results, list) and len(results) > 0: 
            formatted_output = ""
            for task in results:
                formatted_output += f"### {task.description}\n\n" 
                formatted_output += f"{task.output.summary}\n\n"  # Use task.output.summary 
                formatted_output += f"Raw Output:\n{task.output.raw}\n\n"
                if task.output.json_dict:
                    formatted_output += f"JSON Output:\n{json.dumps(task.output.json_dict, indent=2)}\n\n"
                if task.output.pydantic:
                    formatted_output += f"Pydantic Output:\n{task.output.pydantic}\n\n"
            return formatted_output

        return "No detailed outputs could be extracted from the workflow results."

    except Exception as e:
        return f"Error formatting results: {str(e)}"

def main():
    #load_config()
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    st.title("Product Discovery Lifecycle Automation")
    
    # Input fields
    #openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    #print("openai_api_key")
    #if openai_api_key:
    #openai_api_key = st.secrets['OPENAI_API_KEY']
    #if validate_openai_key(openai_api_key):
        #st.session_state['OPENAI_API_KEY'] = openai_api_key
        #st.success("OpenAI API loaded successfully")
    business_idea = st.text_input("Enter your business idea:")
    target_user_group = st.text_input("Enter target user group:")
    
    if st.button("Generate Product Discovery Report"):
        if business_idea and target_user_group:
            workflow = ProductDiscoveryWorkflow(business_idea, target_user_group)
            results = workflow.run_workflow()
            st.subheader("Summary of Results")
            st.write(results.raw)
        else:
            st.warning("Please enter business idea and target user group.")
    #else:
        #st.error("Invalid OpenAI API Key.Please check your configuration.")

if __name__ == "__main__":
    main()