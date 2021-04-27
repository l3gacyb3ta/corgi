import requests, os
import magic           # magic for mime types

token = os.environ["TOKEN"]                     # Get the token from an OS variable
headers = {'Authorization': 'Bearer ' + token}  # Setup auth header
baseUrl = "https://pat.doggo.ninja/v1/"         # Convience 
mime = magic.Magic(mime=True)                   # setup mime getter

def getuser():
    """Gets the username."""
    r = requests.get(baseUrl + 'me', headers=headers)
    return r.json()['name']

def getfiles():
    """Get the uploaded files."""
    r = requests.get(baseUrl + 'files', headers=headers)
    return r.json()

def uploadfile(path):
    """Upload the file given in the path."""
    mimeType = mime(path)
    params = {"mimeType" : mimeType, "originalName" : path}
    r = requests.post(baseUrl + 'uploads', params=params, headers=headers)
    return r.json()

uploadfile("UNLICENSE")

# print(getuser())
# getfiles()