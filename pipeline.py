from crewai import Crew
from agents import create_agents
from tasks import create_tasks

def create_crew(agents, tasks):
    """Create the CrewAI crew with the specified agents and tasks."""
    return Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

def run_nutrition_advisor(user_info):
    """Run the nutrition advisor pipeline."""
    # Create agents
    nutritionist, medical_specialist, diet_planner = create_agents()
    
    # Create tasks based on user info
    tasks = create_tasks(nutritionist, medical_specialist, diet_planner, user_info)
    
    # Create crew and execute tasks
    crew = create_crew([nutritionist, medical_specialist, diet_planner], tasks)
    result = crew.kickoff()
    
    return result.output
