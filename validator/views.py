from django.shortcuts import render
from .constants import VALIDATOR_URL
import requests


def check_if_email_hacked(request, email):
    res = requests.get(VALIDATOR_URL + email)
    response = res.json()
