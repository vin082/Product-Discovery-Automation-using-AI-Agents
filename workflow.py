from crewai import Crew, Process
from agents import (
    create_idea_researcher, create_user_researcher, 
    create_assumptions_analyst, create_backlog_generator, 
    create_summarizer_agent
)
from tasks import 
    create_market_research_task, create_user_research_task, 
    create_assumptions_task, create_backlog_task, 
    create_summarizer_task
)

class ProductDiscoveryWorkflow:
    def __init__(self, business_idea, target_user_group):
        self.business_idea = business_idea
        self.target_user_group = target_user_group
        self.crew = None
        
        # Initialize Agents
        self.idea_researcher = create_idea_researcher()
        self.user_researcher = create_user_researcher()
        self.assumptions_analyst = create_assumptions_analyst()
        self.backlog_generator = create_backlog_generator()
        self.summarizer_agent = create_summarizer_agent()

    def run_workflow(self):
        # Create Tasks
        market_research_task = create_market_research_task(self.business_idea, self.idea_researcher)
        user_research_task = create_user_research_task(self.target_user_group, self.user_researcher)
        assumptions_task = create_assumptions_task(self.business_idea, self.assumptions_analyst)
        backlog_task = create_backlog_task(self.business_idea, self.backlog_generator)
        summarizer_task = create_summarizer_task(self.summarizer_agent, [market_research_task, user_research_task, assumptions_task, backlog_task])

        # Create Crew and run workflow
        self.crew = Crew(
            agents=[
                self.idea_researcher, 
                self.user_researcher, 
                self.assumptions_analyst, 
                self.backlog_generator,
                self.summarizer_agent
            ],
            tasks=[
                market_research_task, 
                user_research_task, 
                assumptions_task, 
                backlog_task,
                summarizer_task
            ],
            verbose=True,
            process=Process.sequential
        )
        
        # Execute the workflow
        results = self.crew.kickoff()
        return results