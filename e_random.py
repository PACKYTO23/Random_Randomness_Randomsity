import datetime
from random import randint

# SET OF OPERATIONS DEPENDING ON THE LAST (OF 6) MICROSECONDS GIVEN BY THE DATETIME MODULE.


def random_filter():
    """Returns pseudo-random 1-digit number and operation order based on the time of the request."""
    now = str(datetime.datetime.now())

    # random = now.split(".")[1]
    semi_random = int(now.split(".")[1][5])

    # print(f"{random}, {semi_random}")  # CAN BE RETURNED.

    rand_if_even = randint(2, 9)
    rand_if_odd = randint(2, 9)

    # print(f"{rand_if_even}, {rand_if_odd}\n\n")  # CAN BE RETURNED.

    if semi_random % 2 == 0:
        final_random = [rand_if_even, "minus-plus"]

        # print(f"This is the result of the random module: {final_random}.")  # CAN BE RETURNED.
        return final_random
    else:
        final_random = [rand_if_odd, "plus-minus"]
        # print(f"This is the result of the random module: {final_random}.")  # CAN BE RETURNED.
        return final_random
