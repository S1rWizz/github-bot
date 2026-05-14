#Creation of auto commit bot 
from github import Auth
from github import Github
from github import GithubIntegration
import os
from dotenv import load_dotenv

auth = Auth.Login("user_login", "password")
g = Github(auth=auth)
g.get_user().login

load_dotenv()

user=os.environ.get("user")
pw=os.environ.get("pass")

print(user,pw)