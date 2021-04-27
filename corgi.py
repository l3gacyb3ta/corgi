import requests, os

token = os.environ["TOKEN"]
headers = {'Authorization': 'Bearer ' + token}
baseUrl = "https://pat.doggo.ninja/v1/"

def getuser():
    r = requests.get(baseUrl + 'me', headers=headers)
    return r.json()['name']

def getfiles():
    r = requests.get(baseUrl + 'files', headers=headers)
    return r.json()



print(getuser())

getfiles()