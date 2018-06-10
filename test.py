import negentweeapi

negentweeapi.get_travel_advice("station-utrecht-centraal", "station-amsterdam-centraal",
                               requestType=negentweeapi.RequestTypes.LatestDeparture,
                               ExcludedTravelModes=[negentweeapi.ExcludedTravelModus.Tram,
                                                    negentweeapi.ExcludedTravelModus.Bus])
