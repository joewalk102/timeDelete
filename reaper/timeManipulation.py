

def string_to_seconds(time_arg):
    """
    Changes time string argument into seconds

    :param time_arg: String to interpret
    :type time_arg: str

    :return: time in seconds
    :rtype: int
    """
    if isinstance(time_arg, str):
        # setting up variables needed
        time_len = len(time_arg)
        time_type = str(time_arg[time_len - 1]).lower()
        time_digits = ""
        # Separating digits from time designation and making sure they are numbers
        for i in range(0, time_len - 1):
            if '0' <= str(time_arg[i]) and str(time_arg) <= '9':
                time_digits += str(time_arg[i])
            else:
                # Does not support decimals or any other digits. Only whole numbers followed by supported time
                # designations as shown below (s, m, h, d)
                raise NotImplementedError
        time_digits = int(time_digits)
        # Determining multiplier for minute, hour, day or returning seconds
        if time_type == 's':
            return int(time_digits)
        if time_type == 'm':
            # 60 seconds in a minute
            return int(time_digits * 60)
        if time_type == 'h':
            # 3600 seconds in an hour
            return int(time_digits * 60 * 60)
        if time_type == 'd':
            # 86400 seconds in a day
            return int(time_digits * 60 * 60 * 24)
        raise NotImplementedError
    else:
        raise TypeError