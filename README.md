## Record GitHub repository traffic analytics

This repository saves GitHub traffic analytics past the two week limit put by GitHub. This is based on a similar soolution by sangonzal (repository-traffic-action) but only uses GitHub actions to regularly commit a repository's traffic analytics in csv files. 

### Setup:
1. Clone 
2. Generate a Peronal Access Token (PAT) by going to Settings -> Developer Settings -> Personal Access Tokens -> Generate new token. You will need to grant "repo" permission to the PAT. This PAT belongs to the account whose traffic data you want to momitor. 
3. Save the PAT as a secret in the repository where you'll be saving the traffic data: Go to Repository settings -> Secrets and variables -> Actions -> New repository secret and add the secret with the name "TRAFFIC_ACTION_TOKEN". 
