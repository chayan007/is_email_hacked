from django.shortcuts import render
from .constants import VALIDATOR_URL, REFERER_URL
import requests


def check_if_email_hacked(request, email):
    email.replace('@', '%')
    res = requests.get(url=VALIDATOR_URL + email, data=REFERER_URL)
    response = res.json()
    return response


