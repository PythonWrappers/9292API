import negentweeapi

login = negentweeapi.login("Hylcos@gmail.com", "gm3TzDe6kXnP")
successLogin = "error" not in login.keys()
if not successLogin:
    print("unvalid Login")
    exit()
else:
    session_id = login["sessionId"]
    for loc in negentweeapi.get_saved_locations(session_id):
        print(loc.id)
    print(negentweeapi.get_data_date_range())

help(negentweeapi)
print(negentweeapi.get_closest_location(negentweeapi.LatLong(52.0358874,5.0812099)))