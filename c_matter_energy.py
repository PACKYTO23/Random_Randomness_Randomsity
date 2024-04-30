import requests

# THE INTERNATIONAL SPACE STATION AS IT BEING AN ENORMOUS HUMAN-MADE OBJECT WITH DETECTABLE COORDINATES.

ISS_NOW = "http://api.open-notify.org/iss-now.json"
OP_RG_ENDPOINT = "http://api.openweathermap.org/geo/1.0/reverse?"
API_KEY = "96c7f5e55e99751c05d3117b2e078fb1"


def matter_energy_filter():
    """Returns pseudo-random 12-digit number based on the ISS location (coordinates) at the time of the request."""
    response = requests.get(url=ISS_NOW)

    # print(response.status_code)
    response.raise_for_status()

    data = response.json()
    iss_location = data["iss_position"]
    iss_longitude = float(iss_location["longitude"])
    iss_latitude = float(iss_location["latitude"])

    # print(f"{iss_longitude}, {iss_latitude}")  # CAN BE RETURNED.

    # noinspection SpellCheckingInspection
    parameters = {
        "lat": iss_latitude,
        "lon": iss_longitude,
        "limit": 1,
        "appid": API_KEY,
    }

    response = requests.get(OP_RG_ENDPOINT, params=parameters)

    # print(response.status_code)
    response.raise_for_status()

    below_iss_data = response.json()

    if not below_iss_data:
        matter_energy = (iss_longitude ** 2) * (iss_latitude ** 2)
        semi_matter_energy = "{:.12f}".format(matter_energy)

        # print(f"No location so space below iss, for now, is: {semi_matter_energy}.\n\n")  # CAN BE RETURNED.
    else:
        location_below = below_iss_data[0]["name"]
        quantity = len(location_below)
        matter_energy = quantity * ((iss_longitude ** 2) * (iss_latitude ** 2))
        semi_matter_energy = "{:.12f}".format(matter_energy)

        # print(f"{location_below}, {quantity}")  # CAN BE RETURNED.
        # print(f"Result of the multiplication of coordinates "  # CAN BE RETURNED.
        #       f"times de characters in the location's name: {semi_matter_energy}.\n\n")  # CAN BE RETURNED.

    final_matter_energy = semi_matter_energy.split(".")[1]

    # print(f"This is the result of the matter and energy module: {final_matter_energy}.")  # CAN BE RETURNED.
    return final_matter_energy
