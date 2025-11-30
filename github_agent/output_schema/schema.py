from pydantic import BaseModel, Field

class GithubPR(BaseModel):
    """Represents a GitHub Pull Request with changes"""
    Repo:str=Field(
        description="Represents the Github repo for which the scanning is going on"
    )
    PR_num:int=Field(
        description="Represents the PR number of the pull request"
    )
    Files:list[str]=Field(
        description="Contains the file names changed in the latest PR as a list of strings"
    )
    Difference:str=Field(
        description="contains the entire diff of every file in the pull request "
    )