import requests
import os

GOTIFY_URL = os.getenv("gotify_url")
GOTIFY_USER = os.getenv("gotify_user")
GOTIFY_password = os.getenv("gotify_password")

r = requests.get(GOTIFY_URL)

print(r.text)

""" controller will do the following 
    1. ping server and check its live else it will log error and retry n times
    2. it will check if its app token or else it will request it """
    
    
