# corgi
A new thing for doggo.ninja  
This is a cli for doggo.ninja, it should be pretty helpful and useful.  
## Refrence:
```
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
```
## Examples:
Upload ```file.txt```:  
```python corgi.py upload file.txt```  
  
Upload every file from a directory:  
```python corgi.py upload --dir directory```  
  
Get user info:  
```python corgi.py user```  
  
Delete ```file.txt``` from doggo.ninja:  
```python corgi.py delete file.txt```  
  
Delete _every_ file from doggo.ninja:  
```python corgi.py delete --all```
