"""DOGGO.NINJA CLI

Usage:
    corgi.py
    corgi.py ls
    corgi.py user
    corgi.py upload [-d | --dir] <path>
    corgi.py delete [--all] [<originalName>]
    corgi.py -v

Options:
    <path>  Optional path argument.
    <originalName>  The original name of the file to be manipulated.

"""

import requests, os
import magic                   # magic for mime types
from docopt import docopt      # cli

try:
  token = os.environ["TOKEN"]  # Get the token from an OS variable
except:
  print("Token ENV var not defined.")
  exit()

headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/octet-stream'}  # Setup auth header
baseUrl = "https://pat.doggo.ninja/v1/"         # Convience 
mime = magic.Magic(mime=True)                   # setup mime getter

# magic function from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof(num, suffix='B'):
  for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
      if abs(num) < 1024.0:
          return "%3.1f %s%s" % (num, unit, suffix)
      num /= 1024.0
  return "%.1f %s%s" % (num, 'Yi', suffix)

def getuser():
  # Gets the username.
  r = requests.get(baseUrl + 'me', headers=headers)
  return r.json()

def getfiles():
  # Get the uploaded files.
  r = requests.get(baseUrl + 'files', headers=headers)
  return r.json()

def uploadfile(path):
  # Upload the file given in the path.
  mimeType = mime.from_file(path) #mime type
  params = {"mimeType" : mimeType, "originalName" : path} #setup params

  toFile = open(path, "rb") # file to upload
  r = requests.post(baseUrl + 'upload', params=params, headers=headers, files = {"file": toFile}) #ehhh requests
  return r.json() #debug

def uploaddir(path):
  # thanks stackoverflow for file walking code 
  for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
     uploadfile(os.path.join(root, name))

def printfiles(json): # pretty print the files
  text = ""
  if json == []:
    # Error handling
    return "No files."
  
  for i in json:
    # Text concatination
    text = text + "Name: " + i['originalName'] + "\n" + "Url: " + i['url'] + '\n' + '-' * 35 + "\n"
  
  return text

def printuser(json): # pretty print the user info
  text = """Username: {uname}
Usage:    {usage}
Admin:    {admin}"""
  return text.format(uname = json['name'], usage = sizeof(json['usage']), admin = json['admin'])

def delete(originalName):
  """Delete a file based on og name"""
  shortfiles = getfiles()    # get the uploaded files
  short = "____"             # setup shortname
  for i in shortfiles:
    if i['originalName'] == originalName:
      short = i['shortName'] # if a name matches, then set the shortname
  
  if short == "____":        # if there was no shortname, then return an error
    return "File not found."

  r = requests.delete(baseUrl + 'file/' + short, headers=headers) #ehhh requests
  
  if r.json() == {}:         # if there's no response, it works! 
    return originalName + " deleted."
  else:                      # otherwise, there was an error we didn't catch, so return the json.
    return "Error: " + r.json()

def deleteall():     # deletes every single file on doggo.ninja
  files = getfiles() # grab the file info
  shorts = {}

  for i in files:
    # get all the shorts
    shorts[i['shortName']] = i['originalName']

  if shorts == []:
    # error catcher
    return "No files to delete."
  
  for short in shorts.keys():
    # delete each file in the shorts
    r = requests.delete(baseUrl + 'file/' + short, headers=headers)
    if r.json() == {}:
      print(shorts[short] + " deleted.")
    else:
      print("Error: " + r.json())
  return "Mass delete finished"

def printargs(json):  # make args look nice
  for i in json.keys():
    print("{argument} : {value}".format(argument=i, value=json[i]))

def parse():
  version = 'Corgi 1.1' # version
  arguments = docopt(__doc__, version=version)
  
  if arguments['<path>']:
    # if there's a path, then upload
    if arguments['-d'] or arguments['--dir']:
      # If it's a directory, then it will uploaded
      print(uploaddir(arguments['<path>']))

    else:
      # Otherwise, just upload a file
      print(uploadfile(arguments['<path>']))

  elif arguments['ls']:
    # Shows all the files you have
    print(printfiles(getfiles()))

  elif arguments['delete']:
    # Delete a file
    if arguments['--all']:
      # If it's all, then delete all files
      conf = ""
      while not conf.lower() in ['y','n']:
        # Make sure you want to delete.
        conf = input("Are you 100% sure? (y/n) ")
      
      if conf.lower() == "y":
        # If their sure, then DELETE
        print(deleteall())

      else:
        # I just thought this was funny
        print("That's ok! Good catch.")
    
    else:
      # just a normal delete
      print(delete(arguments['<originalName>']))

  elif arguments['user']:
    # user info
    print(printuser(getuser()))
  
  elif arguments['-v']:
    # version y'all
    print(version)
  
  else:
    print(printargs(arguments))