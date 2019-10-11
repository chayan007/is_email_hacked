from django.http import JsonResponse, HttpResponse
from .constants import VALIDATOR_URL, REFERER_URL
import requests


def get_response(email):
    headers = {
        'user-agent': 'Mozilla/5.0',
        'accept-language': 'en-GB',
        'referrer': REFERER_URL
    }
    return requests.get(url=VALIDATOR_URL + email, headers=headers)


def check_if_email_hacked(request, email):
    response = get_response(email)
    if response.status_code == 404:
        return JsonResponse({
            'status': 'safe',
            'breaches': 0
        }, status=404)
    else:
        return HttpResponse(response)
