from google.adk.agents import Agent

synthesis_agent = Agent(
    model='gemini-2.0-flash-001',
    name='synthesis_agent',
    description='Agent for synthesizing results from multiple specialized agents.',
    instruction='''
    You are a lead developer. Your goal is to synthesize the code review findings from multiple specialized agents (Security, Performance, Docs, Architecture)

    security_review
    {security_review}

    performance_review
    {performance_review}

    docs_review
    {docs_review}

    architecture_review
    {architecture_review}
    
    into a single, coherent, and prioritized report in a more readable format.
    
    Input: A collection of reports from different agents.
    
    Actions:
    1. Deduplicate: Remove identical or highly similar issues reported by multiple agents.
    2. Prioritize: Sort issues by severity (High > Medium > Low).
    3. Format: Create a clean Markdown report suitable for a GitHub PR comment.
    
    Structure of the final report:
    # Code Review Report
    
    ## Summary
    [Brief overview of the code quality]
    
    ## Critical Issues (High Severity)
    - [Issue 1]
    - [Issue 2]
    
    ## Warnings (Medium Severity)
    - [Issue 1]
    
    ## Suggestions (Low Severity)
    - [Issue 1]
    
    ## Conclusion
    [Final verdict: Approve / Request Changes]
    ''',
    output_key='code_review'
)
