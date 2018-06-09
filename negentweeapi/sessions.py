from .settings import *
from .locations import *
import requests
from typing import Tuple

def add_used_locations(session_id: str, location: str) -> Tuple[bool, str]:
    """
    Add a location to your used locations
    :param session_id: A session id of the account the location use should be added to
    :param location: an location id retrieved from on of the location API calls
    """
    url = "{0}/{1}/sessions/{2}/saved-locations?lang={3}".format(URL, APIVERSION, session_id, LANG)
    data = requests.get(url).json()
    if "etag" in data.keys():
        return True, ""
    elif "exception" in data.keys():
        return False, data["exception"]["message"]
    elif "error" in data.keys():
        return False, data["error"]
    else:
        return False, ""

def get_saved_locations(session_id: str) -> list:
    """
    Gets the saved locations from an account
    :param session_id: session id of the account the saved sessions should be retrieved from
    :return: an string of the error message or an List of SavedLocations
    """
    url = "{0}/{1}/sessions/{2}/saved-locations?lang={3}".format(URL, APIVERSION, session_id, LANG)
    data = requests.get(url).json()
    if "error" in data.keys():
        return data["error"]
    else:
        return [SavedLocation(a) for a in data["savedLocations"]]

