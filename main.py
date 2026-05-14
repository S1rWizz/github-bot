#Creation of auto commit bot 
from github import Auth
from github import Github
from github import GithubIntegration
import os
from dotenv import load_dotenv

load_dotenv()
access_token=os.environ.get("tok")

auth = Auth.Token(access_token)

# Public Web Github
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)
