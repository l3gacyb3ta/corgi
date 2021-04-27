"""DOGGO CLI

Usage:
    corgi.py
    corgi.py <path>
    corgi.py --list-files

Options:
    <path>  Optional path argument.

"""
import requests, os
import magic                    # magic for mime types
from docopt import docopt       # cli


token = os.environ["TOKEN"]                     # Get the token from an OS variable
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/octet-stream'}  # Setup auth header
baseUrl = "https://pat.doggo.ninja/v1/"         # Convience 
mime = magic.Magic(mime=True)                   # setup mime getter

def main():
    """
    A cli for doggo.ninja.
    """
    pass

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
    mimeType = mime.from_file(path) #mime type
    params = {"mimeType" : mimeType, "originalName" : path} #setup params

    toFile = open(path, "rb") # file to upload
    r = requests.post(baseUrl + 'upload', params=params, headers=headers, files = {"file": toFile}) #ehhh requests
    return r.json() #debug
    #return mimeType

# print(uploadfile())

# print(getuser())
# getfiles()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DOGGO 1.0')
    if arguments['<path>']:
        print(uploadfile(arguments['<path>']))
    else:
        print(arguments)