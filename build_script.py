import requests
import os
import sys

print(sys.argv[1])

#for var in os.environ:
#  print(var, os.environ[var])

r=requests.get("http://www.example.com/", headers={"X-Security-Header":f"sys.argv[1]"})
