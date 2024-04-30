import datetime

# ALL THE DIVISIONS OF THE DATETIME CONSTANT AND THE NOW MODULE ARE FOR RETURNING VARIABLES OF AN EXACT AND UNIQUE TIME.


def time_filter():
    """Returns pseudo-random 12-digit number based on the date and time of the request."""
    now = str(datetime.datetime.now())
    date = now.split(" ")[0]
    clock = now.split(" ")[1]
    date_y_m_d = date.split("-")
    clock_h_m_s = clock.split(":")
    clock_s_ms = clock_h_m_s[2].split(".")

    # print(date_y_m_d)  # CAN BE RETURNED.
    # print(clock_h_m_s)  # CAN BE RETURNED.
    # print(clock_s_ms)  # CAN BE RETURNED.

    year = date_y_m_d[0]
    month = date_y_m_d[1]
    day = date_y_m_d[2]
    hour = clock_h_m_s[0]
    minute = clock_h_m_s[1]
    second = clock_s_ms[0]
    microsecond = clock_s_ms[1]

    # print(f"{year}, {month}, {day}, {hour}, {minute}, {second}, {microsecond}")  # CAN BE RETURNED.

    time = year + month + day + hour + minute + second + microsecond

    # print(time)  # CAN BE RETURNED.

    quantity = 0

    for _ in time:
        number = int(_)
        quantity += number

    # print(quantity)  # CAN BE RETURNED.

    r_time = time[::-1]

    # print(r_time)  # CAN BE RETURNED.

    semi_time = str(quantity * int(r_time))

    # print(f"{semi_time}\n\n")  # CAN BE RETURNED.

    final_time = semi_time[0:12]
    time_list = [clock, final_time]

    # print(f"This is the result of the time module: {final_time}.")  # CAN BE RETURNED.
    return time_list
