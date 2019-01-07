def reverse(x : int):
    int_to_str = str(x)
    if not int_to_str[0].isdigit():
        int_to_str = int_to_str[1:]
        int_to_str = int_to_str[::-1]
        if int(int_to_str) * -1 > -2**31 and int(int_to_str) * -1 < 2**31 - 1:
            return int(int_to_str) * -1
        else:
            return 0
    else:
        int_to_str = int_to_str[::-1]
        reversed_int = int(int_to_str)
        if reversed_int > -2**31 and reversed_int < 2**31 - 1:
            return reversed_int
        else:
            return 0
