import sys
print("inline arguments are:")
print("\n".join(sys.argv))

import os
print(os.environ['TOKEN'])

import requests
response = requests.get(url = "https://api.github.com/repos/anshsingal/sequence-analytics/traffic/clones", headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {os.environ['TOKEN']}", "X-GitHub-Api-Version": "2022-11-28"})
print("direct access:")
print(response.json())

print("indirwecrt access")
f = open("temp_clones.txt", "r")
print(f.read())
