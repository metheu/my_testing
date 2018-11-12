import requests
import os

GOTIFY_URL = os.getenv("gotify_url")
GOTIFY_USER = os.getenv("gotify_user")
GOTIFY_password = os.getenv("gotify_password")

r = requests.get(GOTIFY_URL)

print(r.text)