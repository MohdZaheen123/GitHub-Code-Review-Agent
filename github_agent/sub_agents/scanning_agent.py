from google.adk.agents import Agent
from ..tools.tools import github_tools
from ..output_schema.schema import GithubPR
from dotenv import load_dotenv
import os 

load_dotenv()


scanning_agent = Agent(
    model="gemini-2.5-pro",
    name="scanning_agent",
    instruction=f"""You are a help full assistant that retrives the latest PR from a github repo
    {os.getenv('GITHUB_REPO')} and returns the files changed and  the combined diff for all the files in the pull request.
    IMPORTANT: When calling tools, use their exact names without any prefix.
    For example, use 'list_pull_requests', NOT 'scanning_agent.list_pull_requests'.
    """,
    tools=[github_tools],
    output_schema=GithubPR,
    output_key="Diff"
)
