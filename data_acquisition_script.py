# import sys
# print("inline arguments are:")
# print("\n".join(sys.argv))

import os
PAT = os.environ['PERSONAL_ACCESS_TOKEN']

import requests
headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {PAT}", "X-GitHub-Api-Version": "2022-11-28"}
repo_url = "https://api.github.com/repos/anshsingal/sequence-analytics"

clones = requests.get(url = repo_url+"/traffic/clones", headers = headers).json()
print("direct access:")
print(clones)

# print("indirwecrt access")
# f = open("temp_clones.txt", "r")
# print(f.read())
