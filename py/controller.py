from dotenv import load_dotenv
load_dotenv(verbose=True)
import os
import requests
import logging
import json
from requests.auth import HTTPBasicAuth

def connect():
    """ This is the test call requests to ping server 
    """
    GOTIFY_URL = os.getenv("gotify_url")
    GOTIFY_USER = os.getenv("gotify_user")
    GOTIFY_PASS = os.getenv("gotify_password")

    

    logging.basicConfig(level=logging.INFO)
    res = requests.get(GOTIFY_URL + 'client', auth=(GOTIFY_USER, GOTIFY_PASS))

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

    json_obj = res.json()
    return json_obj


    # if(r.status_code == 404):
    #     logging.warning('Problem connecting to server. trying in %s', RETRY)

    # elif(r.status_code == 200):
    #     logging.info('Connected to server successfully')
    

resp = connect()

print(resp)
