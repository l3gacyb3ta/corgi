# corgi
A new thing for doggo.ninja  
This is a cli for doggo.ninja, it should be pretty helpful and useful.  
## Install
To install:  
```pip install corgi-cli```
## Refrence:
```
Usage:
    corgi
    corgi ls
    corgi user
    corgi upload [-d | --dir] <path>
    corgi delete [--all] [<originalName>]
    corgi -v

Options:
    <path>  Optional path argument.
    <originalName>  The original name of the file to be manipulated.
```
## Examples:
Upload ```file.txt```:  
```corgi upload file.txt```  
  
Upload every file from a directory:  
```corgi upload --dir directory```  
  
Get user info:  
```corgi user```  
  
Delete ```file.txt``` from doggo.ninja:  
```corgi delete file.txt```  
  
Delete _every_ file from doggo.ninja:  
```corgi delete --all```
