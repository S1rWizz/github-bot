#Creation of auto commit bot 
from github import Auth
from github import Github
from github import GithubIntegration
import os
from dotenv import load_dotenv

load_dotenv()
access_token=os.environ.get("tok")
repo_name=os.environ.get("repo_name")
commit_mssg=os.environ.get("commit_message")
content=os.environ.get("content")



auth = Auth.Token(access_token)
g = Github(auth=auth)

flag=0
try:
    for repo in g.get_user().get_repos():
        if repo.name==repo_name:
            print(f"Repo '{repo_name}' found!")
            flag=1
            break

    if flag==0:
        print(f"Repo '{repo_name}' not found... crosscheck the name (case sensitive)")
    
    repo = g.get_user().get_repo(repo_name)
    contents = repo.get_contents("README.md")
    repo.update_file(contents.path, commit_mssg, content, contents.sha)

    print("Completed Successfully..")

except Exception as e:
    print("ERROR!!")
    print("Check your token.. is it in quotes? all perms enabled?")

