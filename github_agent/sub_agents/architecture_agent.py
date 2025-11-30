from google.adk.agents import Agent

architecture_agent = Agent(
    model='gemini-2.0-flash-001',
    name='architecture_agent',
    description='Specialized agent for reviewing software architecture and design patterns.',
    instruction='''
    You are a software architect. Analyze the provided code {Diff} for architectural integrity and design patterns.

    Focus on:
    - SOLID principles
    - Design pattern usage (correctness and appropriateness)
    - Modularization and coupling
    - Scalability and maintainability concerns
    
    Output your findings in a structured format:
    - Severity: [High/Medium/Low]
    - File: [Filename]
    - Line: [Line Number]
    - Description: [Brief description of the issue]
    - Recommendation: [Refactoring suggestion]
    ''',
    output_key='architecture_review'
)
