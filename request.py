"""
Python: Using requests
"""
import requests


if __name__ == '__main__':
    URL = "http://maps.googleapis.com/maps/appi/geocode/json"
    location = "Bagmane World Technology Center"
    PARAMS = {'address':location}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    print("Latitude {}\nLongitude  {}\n Formatted Address {}"
          .format(latitude, longitude, formatted_address))
