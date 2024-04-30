import requests
from random import randint

# LONGITUDE FIRST FOLLOWED BY LATITUDE (ONLY HERE).

OP_RG_ENDPOINT = "http://api.openweathermap.org/geo/1.0/reverse?"
API_KEY = "96c7f5e55e99751c05d3117b2e078fb1"

MIN_LON = -180
MAX_LON = 180
MIN_LAT = -90
MAX_LAT = 90


def space_filter():
    """Returns pseudo-random 12-digit number based on a set of random coordinates."""
    lon_whole = str(randint(MIN_LON, MAX_LON))
    lat_whole = str(randint(MIN_LAT, MAX_LAT))
    lon_decimal = ""
    lat_decimal = ""

    if lon_whole == str(-180) or lon_whole == str(180):
        lon_decimal = "000000"
    elif lat_whole == str(-90) or lat_whole == str(90):
        lat_decimal = "000000"
    else:
        for _ in range(6):
            n_1 = str(randint(0, 9))
            n_2 = str(randint(0, 9))
            lon_decimal += n_1
            lat_decimal += n_2

    longitude = float(lon_whole + "." + lon_decimal)
    latitude = float(lat_whole + "." + lat_decimal)

    # noinspection SpellCheckingInspection
    parameters = {
        "lat": latitude,
        "lon": longitude,
        "limit": 1,
        "appid": API_KEY,
    }

    response = requests.get(OP_RG_ENDPOINT, params=parameters)

    # print(response.status_code)
    response.raise_for_status()

    geolocation_data = response.json()

    # print(f"{latitude}, {longitude}")  # CAN BE RETURNED.
    # print(geolocation_data)  # CAN BE RETURNED.

    if not geolocation_data:
        space = longitude * latitude
        semi_space = "{:.12f}".format(space)

        # print(f"No location so space, for now, is: {semi_space}.\n\n")  # CAN BE RETURNED.
    else:
        location = geolocation_data[0]["name"]
        quantity = len(location)
        space = quantity * (longitude * latitude)
        semi_space = "{:.12f}".format(space)

        # print(location)  # CAN BE RETURNED.
        # print(quantity)  # CAN BE RETURNED.
        # print(f"Result of the multiplication of coordinates "  # CAN BE RETURNED.
        #       f"times de characters in the location's name: {semi_space}.\n\n")  # CAN BE RETURNED.

    final_space = semi_space.split(".")[1]

    # print(f"This is the result of the space module: {final_space}.")  # CAN BE RETURNED.
    return final_space
