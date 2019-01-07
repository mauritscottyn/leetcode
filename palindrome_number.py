def is_palindrom(x : int):
    int_to_str = str(x)
    int_reversed = int_to_str[::-1]
    if int_to_str == int_reversed:
        return True
    else:
        return False