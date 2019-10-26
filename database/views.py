from django.shortcuts import render
from .handler import *


def kickoff_database_tasks(email, res):
    response_json = res.json()
    is_email_stored = add_email(email)
    is_hack_stored = add_hack(response_json['Breaches'])
    is
