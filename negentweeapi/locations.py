from .settings import *
import requests
class Location:
    def __init__(self, d):
        self.__dict__ = d


class LatLong:
    def __init__(self, lat: float, long: float) -> object:
        self.lat = lat
        self.long = long

    def __repr__(self):
        return "{0},{1}".format(self.lat, self.long)


class SavedLocation:
    """
        This Object is a savedLocation retrieved from the getSavedLocations call
        A valid SavedLocation looks like this:
        {
            "id": -> str,
            "title": -> str,
            "icon": -> str,
            "hash": -> str,
            "location": {
                "id": -> str,
                "type": -> str,
                "stopType": -> str,
                "name": -> str,
                "place": {
                    "name": -> str,
                    "regionCode": -> str,
                    "regionName": -> str,
                    "showRegion": -> bool,
                    "countryCode": -> str,
                    "countryName": -> str,
                    "showCountry": -> bool
                },
                "latLong": {
                    "lat": -> double,
                    "long": -> double
                },
                "urls": {
                    "nl-NL": -> str,
                    "en-GB": -> str
                }
            }
        }
    """

    def __init__(self, d):
        self.__dict__ = d



def get_closest_location(lat_long: LatLong) -> Location:
    url = "{0}/{1}/locations?lang={2}&latlong={3}&type=address&rows=1".format(URL, APIVERSION, LANG, lat_long)
    print(url)