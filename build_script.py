import requests
import os

for var in os.environ:
  print(var, os.environ[var])

#r=requests.get("http://www.example.com/", headers={"X-Security-Header":""})
