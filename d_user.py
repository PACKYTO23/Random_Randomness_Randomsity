import requests

# THROUGH THE USER'S IP ADDRESS THE LAST FACTOR OF THE GENERATOR WILL BE PRODUCED.

IP_ADDRESS = "https://api64.ipify.org?format=json"


def user_filter():
    """Returns pseudo-random 12-digit number based on the tip address of user who made the request."""
    response = requests.get(url=IP_ADDRESS)

    # print(ip_response.status_code)
    response.raise_for_status()

    ip_data = response.json()
    ip_address = ip_data["ip"]

    # print(ip_address)  # CAN BE RETURNED.

    user = ip_address.split(":")
    quantity = len(user)

    # print(f"{user}, {quantity}")  # CAN BE RETURNED.

    sum_user = ""

    for _ in user:
        sum_user += _

    # print(sum_user)  # CAN BE RETURNED.

    sum_digits = ""

    for _ in sum_user:
        if _.isdigit() is True:
            sum_digits += _

    # print(sum_digits)  # CAN BE RETURNED.

    semi_user = str(quantity * int(sum_digits))

    # print(f"{semi_user}\n\n")  # CAN BE RETURNED.

    final_user = semi_user[0:12]

    # user_response = requests.get(f"https://ipapi.co/{ip_address}/json/")  USER'S LOCATION DATA VIA IP ADDRESS---------

    # print(user_response.status_code)
    # user_response.raise_for_status()

    # user_data = user_response.json()

    # print(user_data)  USER'S LOCATION DATA VIA IP ADDRESS-------------------------------------------------------------

    # print(f"This is the result of the user module: {final_user}.")
    return final_user
