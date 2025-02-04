from github import Github

# token
token = "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"
g = Github(token)

user = g.get_user("devops-catchup")

# List All Repository
for repo in user.get_repos():
    print(f"Repository Name : {repo}")

