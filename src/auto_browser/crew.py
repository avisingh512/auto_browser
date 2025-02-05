from crewai import Crew, Task
import json
from agents.form_agents import create_field_agent, create_submit_agent

with open('data/form_data.json') as f:
    form_data = json.load(f)

def create_form_crew():
    agents = [create_field_agent(f, v) for f, v in form_data.items()]
    agents.append(create_submit_agent())
    
    tasks = [
        Task(
            description=f'Fill {field} field',
            agent=agent,
            expected_output=f'Confirmation that {field} was filled'
        ) for field, agent in zip(form_data.keys(), agents)
    ]
    
    tasks.append(Task(
        description='Submit the completed form',
        agent=agents[-1],
        expected_output='Form submission confirmation'
    ))
    
    return Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )