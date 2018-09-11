import requests
import pandas as pd
from pandas.io.json import json_normalize

# set login information
login = {
    'username': (None, 'raidar account'),
    'password': (None, 'raidar password'),
}

# request access token
token = requests.post('https://www.gw2raidar.com/api/v2/token', files=login)
# define authentication
authentication = 'token ' + token.json()['token']

# request encounter data
headers = {'Authorization': authentication}

# initialize data frame
encounters = pd.DataFrame()
# initialize URL
url = "https://www.gw2raidar.com/api/v2/encounters"

# query api, appending results to data frame
while url != None:
    r = requests.get(url, headers = headers)
    results = r.json()['results']
    results_df = json_normalize(results)
    encounters = encounters.append(results_df)
    url = r.json()['next']

# reset index of encounters
encounters.reset_index()

# export to csv
encounters.to_csv("encounters_test.csv", index = False)
