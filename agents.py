from crewai import Agent
from tools import DuckDuckGoSearchTool
print("DuckDuckGosearchtool imported successfully")

def create_idea_researcher():
    return Agent(
        role='Market Research Specialist',
        goal='Conduct comprehensive market research for the business idea',
        backstory='Expert in market analysis and competitive landscape assessment',
        tools=[DuckDuckGoSearchTool()],
        verbose=True
    )

def create_user_researcher():
    return Agent(
        role='User Segmentation Expert',
        goal='Identify and define precise user segments and personas',
        backstory='Skilled in user research and persona development',
        tools=[DuckDuckGoSearchTool()],
        verbose=True
    )

def create_assumptions_analyst():
    return Agent(
        role='Strategic Assumptions Analyst',
        goal='Analyze and prioritize business assumptions and potential risks',
        backstory='Experienced in identifying business opportunities and potential challenges',
        verbose=True
    )

def create_backlog_generator():
    return Agent(
        role='Product Backlog Specialist',
        goal='Generate comprehensive product backlog and user stories',
        backstory='Expert in agile product development and user story creation',
        verbose=True
    )

def create_summarizer_agent():
    return Agent(
        role='Reporting',
        goal="""Report the results from product discovery workflow and provide summary as below:
        - Market Research Report
        - User Research Report
        - Assumptions Analysis Report
        - Product Backlog Report""",
        backstory='Expert in comprehensive reporting information',
        verbose=True
    )