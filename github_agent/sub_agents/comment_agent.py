from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def add_pr_comment(
    owner: str,
    repo: str,
    pr_number: int,
    comment_body: str,
) -> dict:
    """
    Add a comment to a GitHub Pull Request.
    
    Args:
        owner: Repository owner (username or organization)
        repo: Repository name
        pr_number: Pull request number
        comment_body: The comment text to add
        token: GitHub personal access token
        
    Returns:
        dict: Response from GitHub API containing comment details
        
    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    data = {
        "body": comment_body
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    return response.json()

comment_agent = Agent(
    model='gemini-2.5-flash',
    name='comment_agent',
    description='A helpful assistant for creating a github comment.',
    instruction="""A helpful assistant for creating a github comment,
    The content of the comment is {code_review}
    to the github repo {Diff.Repo}"
    the PR number is {Diff.PR_num}. use the tool add_pr_comment to post the comment""",
    tools=[add_pr_comment]
)
