from github import Github

# token
token = "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"
g = Github(token)

# fetch the Github UserName
user = g.get_user()
print(f"username : {user.login}")

# fetch all public repos
print(f"Public Repos : {user.public_repos}")

# fetch the followers on github account
print(f"Followers: {user.followers}")



