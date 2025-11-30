from google.adk.agents import SequentialAgent, ParallelAgent
from .sub_agents.scanning_agent import scanning_agent
from .sub_agents.architecture_agent import architecture_agent
from .sub_agents.docs_agent import docs_agent
from .sub_agents.performance_agent import performance_agent
from .sub_agents.security_agent import security_agent
from .sub_agents.synthesis_agent import synthesis_agent
from .sub_agents.comment_agent import comment_agent


parallel_code_review_team = ParallelAgent(
    name="ParallelCodeReviewTeam",
    sub_agents=[architecture_agent, docs_agent, performance_agent,security_agent],
)

root_agent = SequentialAgent(
    name="ReviewSystem",
    sub_agents=[scanning_agent, parallel_code_review_team,synthesis_agent,comment_agent],
)
