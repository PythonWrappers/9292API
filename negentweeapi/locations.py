from .settings import *
import requests
from typing import Tuple, List


class Location:
    def __init__(self, d: dict) -> None:
        self.__dict__ = d


class LocationType:
    poi = 'poi'
    address = 'address'


class LocationStreet(Location):
    """
    This Object
    {
        'id': ->str,
        'name': -> str, 
        'place': {
            'showCountry': -> bool, 
            'name': -> str, 
            'regionName': -> str, 
            'regionCode': -> str, 
            'showRegion': -> bool, 
            'countryName': -> str, 
            'countryCode': 'NL'
        }, 
        'type': -> str, 
        'houseNr': -> str, 
        'latLong': {
            'long': -> float, 
            'lat': -> float}
        }

    """

    def __init__(self, d: dict) -> None:
        super().__init__(d)


class LatLong:
    def __init__(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long

    def __repr__(self):
        return "{0},{1}".format(self.lat, self.long)


def get_locations(query: str, type: str = None) -> List[Location]:
    """
    Request data about certain locations. This is done by querying the data. For example
        Bankstraat 1
        1234 AB
        Utrecht
        RTD

    :param query: the query which will be used to search for locations
    :param type: the type of the locations that need to be found. Default is all
    :return: A list of Locations or an error message
    """
    url = "{0}/{1}/Locations?query={3}".format(URL, APIVERSION, LANG, query)
    print(url)
    if type:
        url = "{0}&type={1}".format(url, type)
    data = requests.get(url, headers=HEADERS).json()
    print(data)
    if "locations" in data.keys():
        return [Location(a) for a in data["locations"]]
    else:
        if __name__ == '__main__':
            return data["exception"]["message"]


