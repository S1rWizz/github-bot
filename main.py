#Creation of auto commit bot 
from github import Auth
from github import Github
from github import GithubIntegration
import os
from dotenv import load_dotenv

load_dotenv()
token=os.environ.get("tok")

auth = Auth.Token("access_token")
g = Github(auth=auth)
g.get_user().login

print(g)