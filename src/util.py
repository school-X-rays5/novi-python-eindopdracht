def str_int_safe(convert: str):
    if convert is None:
        return 0

    convert = convert.lower()

    if convert == "" or convert == "nan":
        return 0
    else:
        return int(convert)
