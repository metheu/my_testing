from dotenv import load_dotenv
load_dotenv(verbose=True)
import os
import requests
import logging
import json
from requests.auth import HTTPBasicAuth

GOTIFY_URL = os.getenv("gotify_url")
GOTIFY_USER = os.getenv("gotify_user")
GOTIFY_PASS = os.getenv("gotify_password")


def get_number_of_clients():
    """ This is the test call requests to get number of clients 
    """
    numb_of_clients = 0

    res = requests.get(GOTIFY_URL + 'client', headers={'Content-Type': 'application/json'}, auth=(GOTIFY_USER, GOTIFY_PASS))

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    
    res_j = res.json()
    for res_js in res_j:
        numb_of_clients += 1

    print(numb_of_clients)


def create_application(name, desc):

    payload = {"description": desc, "name": name}
   
    res = requests.post(GOTIFY_URL + 'application', headers={'Content-Type': 'application/json'}, json=payload, auth=(GOTIFY_USER, GOTIFY_PASS))

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return logging.exception ("Error: " + str(e))
    
    resj = res.json()

    ## write this to db..

create_application('matt', 'bbb')
