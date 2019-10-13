from django.http import JsonResponse, HttpResponse
from .constants import VALIDATOR_URL, REFERER_URL
import requests
import cfscrape


def get_response(email):
    session = requests.session()
    headers = {
        'user-agent': 'Mozilla/5.0',
        'accept-language': 'en-GB',
        'referrer': REFERER_URL
    }
    scraper = cfscrape.create_scraper(sess=session)
    return scraper.get(url=VALIDATOR_URL + email, headers=headers)
    #curl 'https://haveibeenpwned.com/unifiedsearch/sonicxxx7@gmail.com' -H 'user-agent: Mozilla/5.0' -H 'accept-language: en-GB' -H 'rerferrer: https://www.haveibeenpwned.com'


def check_if_email_hacked(request, email):
    response = get_response(email)
    if response.status_code == 404:
        return JsonResponse({
            'status': 'safe',
            'breaches': 0
        }, status=404)
    else:
        return HttpResponse(response)
