from datetime import datetime
from typing import List
from .settings import *
import requests


class RequestTypes:
    Departure = 0
    Arrival = 1
    EarliestDeparture = 2
    LatestDeparture = 3
    EarliestArrival = 4
    LatestArrival = 5


class ExcludedTravelModus:
    Bus = 0
    Train = 1
    Tram = 2
    Subway = 3
    Ferry = 4
    Walk = 5


def get_travel_advice(
        fromid: str,
        toid: str,
        viaid: str = None,
        date_time: datetime = datetime.now(),
        requestType: int = RequestTypes.Departure,
        english: bool = False,
        fiveminutetransfertime: bool = False,
        ExcludedTravelModes: List[int] = None):
    url = "{0}/{1}/Journeys?FromId={2}&ToId={3}&DateTime={4}&Language={5}&InterchangeTime={6}&Requesttype={7}".format(
        URL,
        APIVERSION,
        fromid,
        toid,
        date_time.strftime("%Y-%m-%d,%H:%M"),
        1 if english else 0,
        1 if fiveminutetransfertime else 0,
        requestType
    )
    if viaid:
        url = "{0}&ViaId={1}".format(url, viaid)
    if ExcludedTravelModes:
        for excluded in ExcludedTravelModes:
            url = "{0}&ExcludedTravelModes={1}".format(url, excluded)
    print(url)
    print(requests.get(url=url, headers=HEADERS).json())
