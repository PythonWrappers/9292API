from .settings import *
import requests
import json


def login(username: str, password: str) -> dict:
    """
    Tries to login to the 9292 API. Some function that available need a sessionID. This is because they are user
    specific.
    :param username: A string that contains the email account of a specific user
    :param password: A string that contains the password of the given email account
    :return: An dict which can contain two different keys:
            { 'error' : 'An error' },
            { 'sessionID' : 'An sessionID'}
    """
    url = "{0}/{1}/accounts/login?lang={2}".format(URL, APIVERSION, LANG)
    data = {
        "email": username,
        "password": password
    }
    return requests.post(url=url, data=json.dumps(data)).json()


def register(username: str, password: str) -> dict:
    """
        Tries to create a 9292 account through the API. Some function that available need a sessionID. This is because
        they are user specific.
        :param username: A string that contains the email account of a specific user
        :param password: A string that contains the password of the given email account
        :return: An dict which can contain two different keys:
                { 'error' : 'An error' },
                { 'sessionID' : 'An sessionID'}
    """
    url = "{0}/{1}/accounts/register?lang={2}".format(URL, APIVERSION, LANG)
    data = {
        "email": username,
        "password": password
    }
    return requests.post(url=url, data=json.dumps(data)).json()
