from crewai import Task

def create_market_research_task(business_idea, agent):
    return Task(
        description=f"""Conduct detailed market research for the business idea: {business_idea}
        Provide:
        - Total Addressable Market (TAM)
        - Serviceable Addressable Market (SAM)
        - Serviceable Obtainable Market (SOM)
        - Comprehensive competitive analysis""",
        agent=agent,
        expected_output="Detailed market research report with TAM, SAM, SOM, and competitive analysis"
    )

def create_user_research_task(target_user_group, agent):
    return Task(
        description=f"""Identify user segments for the target group: {target_user_group}
        Create detailed user personas including:
        - Demographics
        - Psychographics
        - Pain points
        - Potential solutions
        - User journey map""",
        agent=agent,
        expected_output="Comprehensive user research analysis document"
    )

def create_assumptions_task(business_idea, agent):
    return Task(
        description=f"""Analyze assumptions for the business idea: {business_idea}
        - Identify key assumptions in the business idea
        - Prioritize assumptions using value vs effort. If value is 5(High) and effort is 1(low), it should be the highest priority.
        - Develop a comprehensive plan to validate assumptions
        - Assess potential risks
        - Provide strategic insights
        - Develop strategic OKR's""",
        agent=agent,
        expected_output="Prioritized assumptions and risk assessment report"
    )

def create_backlog_task(business_idea, agent):
    return Task(
        description=f"""Generate product backlog for: {business_idea}
        - Create initial product backlog
        - Identify features 
        - Map features to user needs
        - Prioritize features using MoSCoW method
        - Define user stories for identified features in Agile user story format. 
        - Prioritize development items""",
        agent=agent,
        expected_output="Comprehensive product backlog with prioritized user stories"
    )

def create_summarizer_task(agent, context_tasks):
    return Task(
        description="""Report the results in a comprehensive manner from product discovery workflow and provide details as below in a detailed and structured manner. Do not miss any critical information.
        - Market Research Report
        - User Research Report- Include detailed user personas
        - Assumptions Analysis Report-Always include OKR's
        - Product Backlog Report""",
        agent=agent,
        expected_output="Detailed Agent Outputs in a readable and structured manner.",
        context=context_tasks
    )