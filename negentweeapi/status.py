import requests
from .settings import *
from datetime import datetime
from typing import Tuple


def get_data_date_range() -> Tuple[datetime, datetime]:
    """
    Gets the current from/to date available in the 9292 API
    :return: a tuple from a from and to date
    """
    url = "{0}/{1}/status?lang={2}".format(URL, APIVERSION, LANG)
    data = requests.get(url).json()
    from_date = datetime.strptime(data["dateRange"]["from"], "%Y-%m-%d")
    to_date = datetime.strptime(data["dateRange"]["to"], "%Y-%m-%d")
    return from_date, to_date


def get_api_version() -> str:
    """
    Gets the current version of the 9292 API
    :return: A string which contains the current version of the 9292 API
    """
    url = "{0}/{1}/status?lang={2}".format(URL, APIVERSION, LANG)
    data = requests.get(url).json()
    return data["version"]
