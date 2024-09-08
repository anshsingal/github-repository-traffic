# import sys
# print("inline arguments are:")
# print("\n".join(sys.argv))

import os
import requests
from datetime import datetime 

PAT = os.environ['PERSONAL_ACCESS_TOKEN']

headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {PAT}", "X-GitHub-Api-Version": "2022-11-28"}
repo_url = "https://api.github.com/repos/anshsingal/SeQUeNCe-research"

clones = requests.get(url = repo_url+"/traffic/clones", headers = headers).json()
referral_paths = requests.get(url = repo_url+"/traffic/popular/paths", headers = headers).json()
referrer_sources = requests.get(url = repo_url+"/traffic/popular/referrers", headers = headers).json()
views = requests.get(url = repo_url+"/traffic/views", headers = headers).json()

if not os.path.isfile("insights.csv"):
    insights_file = open("insights.csv", "a+")
    insights_file.write("Date,Number of Clones,Unique cloners,Number of views,Unique viewers\n")
else:
    insights_file = open("insights.csv", "a")

if not os.path.isfile("meta_data.csv"):
    meta_data_file = open("meta_data.csv", "a+")
    meta_data_file.write("Date,Meta Data\n")
else:
    meta_data_file = open("meta_data.csv", "a")

insights_file.write(f"{datetime.today().strftime('%m-%d-%y')},{clones['count']},{clones['uniques']},{views['count']},{views['uniques']}\n")
meta_data_file.write(f'{datetime.today().strftime('%m-%d-%y')},"{[clones,views,referral_paths,referrer_sources]}"\n')


# print("direct access:")
# print(clones)

# print("indirwecrt access")
# f = open("temp_clones.txt", "r")
# print(f.read())
