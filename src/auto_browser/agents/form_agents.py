from crewai import Agent
from tools.form_tools import fill_field, submit_form
from langchain.tools import Tool

def create_field_agent(field, value):
    # Create a properly formatted tool
    fill_tool = Tool(
        name=f"fill_{field}_field",
        func=lambda: fill_field(field, value),
        description=f"Tool to fill the {field} field with the provided value"
    )
    
    return Agent(
        role=f'{field.replace("#", "").title()} Specialist',
        goal=f'Fill {field} field with {value}',
        backstory=f"You are an expert at filling {field} fields in forms accurately.",
        tools=[fill_tool],
        verbose=True
    )

def create_submit_agent():
    # Create a properly formatted submit tool
    submit_tool = Tool(
        name="submit_form",
        func=submit_form,
        description="Tool to submit the completed form"
    )
    
    return Agent(
        role='Form Submitter',
        goal='Submit completed form',
        backstory="You are an expert at submitting forms once all fields are properly filled.",
        tools=[submit_tool],
        verbose=True
    )