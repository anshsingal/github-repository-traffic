## Record GitHub repository traffic analytics

This repository saves GitHub traffic analytics past the two week limit put by GitHub. This is based on a similar soolution by sangonzal (repository-traffic-action) but only uses GitHub actions to regularly commit a repository's traffic analytics in csv files. 

### Setup:
1. Clone this repository and push it onto GitHub wherever you want to store the traffic data. You are only intersted in the data_acquisition_secret.py and .github/workflows/insights_workflow.yml files. The scripts generate the insights.csv and meta_data.csv files automatically. 
2. Generate a Peronal Access Token (PAT) by going to Settings -> Developer Settings -> Personal Access Tokens -> Generate new token. You will need to grant "repo" permission to the PAT. This PAT belongs to the account whose traffic data you want to momitor. 
3. Save the PAT as a secret in the repository where you'll be saving the traffic data: Go to Repository settings -> Secrets and variables -> Actions -> New repository secret and add the secret with the name "TRAFFIC_ACTION_TOKEN". 
4. Update the Name and email address in the .github/workflows/insights_workflow.yml which would be used to validate the commit.

And Voila, the script will run on the Monday of every fortnight recording the traffic data from the past 2 weeks.  
