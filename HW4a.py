import urllib.request
import json


def GithubApi(username):
    try:
        # retrieve the list of repositories for the user
        url = f"https://api.github.com/users/{username}/repos"
        req = urllib.request.urlopen(url)
        githubResponse = json.loads(req.read().decode())

        # if no public repos then return No repos message.
        if len(githubResponse) == 0:
            return "No Repos"

        # loop to fetch all public repos and then count number of commits repos have.
        for repository in githubResponse:
            repo_name = repository['name']
            commits_url = repository['commits_url'].split("{")[0]
            req = urllib.request.urlopen(commits_url)
            repoResponse = json.loads(req.read().decode())

            # print the name, description, and number of commits for each repo
            print(f"Repo: {repo_name}\nDescription: {repository['description']}\nNumber of commits: {len(repoResponse)}\n")

        return "success"

    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "GitHub User doesn't exist!!"
        else:
            return ("ERROR:-", e)
    except Exception as e:
        return ("ERROR:-", e)


# DEMO TESTING
#For demo testing uncomment the below 3 lines.

"""userInput = input("Enter Github Username: ")
message = GithubApi(userInput)
print(message)"""
