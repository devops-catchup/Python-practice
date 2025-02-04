from github import Github

# token
token = "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"
g = Github(token)

user = g.get_user()

# Create New Repository
repo_name = "Python-Assignments"
repo = user.create_repo(repo_name)

print(f"Repository : {repo_name} Created Successfully")