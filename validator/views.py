from django.http import JsonResponse
from .constants import VALIDATOR_URL, REFERER_URL
import requests


def get_response(email):
    email.replace('@', '%')
    res = requests.get(url=VALIDATOR_URL + email, data=REFERER_URL)
    return res


def check_if_email_hacked(request, email):
    response = get_response(email)
    if response.status_code == 404:
        return JsonResponse({
            'status': 'safe',
            'breaches': 0
        })
    else:
        return response.json()
