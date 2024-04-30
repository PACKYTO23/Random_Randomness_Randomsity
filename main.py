import datetime
from b_space import space_filter
from a_time import time_filter
from c_matter_energy import matter_energy_filter
from d_user import user_filter
from e_random import random_filter

time_selected = time_filter()

random_list = random_filter()
space = int(space_filter())
time = int(time_selected[1])
matter_energy = int(matter_energy_filter())
user = int(user_filter())
rand_even_odd = random_list[0]
operations = random_list[1]


def random_randomness_randomsity():
    """Returns pseudo-random 9-digit number after the decimal point (0.0-1.0)."""
    if operations == "minus-plus":
        random_digits = (str(abs((space - time + matter_energy - user) * rand_even_odd)))[::-1]
        random_final = random_digits + random_digits
        print(float("0." + random_final[1:13]))
    elif operations == "plus-minus":
        random_digits = (str(abs((space + time - matter_energy + user) * rand_even_odd)))[::-1]
        random_final = random_digits + random_digits
        print(float("0." + random_final[1:13]))


random_randomness_randomsity()

now = str(datetime.datetime.now())
clock = now.split(" ")[1]
time_alpha = float(time_selected[0].split(":")[2])
time_delta = float(clock.split(":")[2])
final_process_time = "{:.12f}".format(time_delta - time_alpha)

print(f"\n\n{time_selected[0]}  |  Request.\n------------------------------\n{clock}  |  Execution."
      f"\n-----------------------------------------\n{final_process_time} seconds for random number.")
