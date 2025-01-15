def celsius_to_fahrenheit_ice(celsius: int) -> str:
    # TODO implement
    # make sure to round temperature to two decimal digit after calculation
    temp = celsius * 1.8 + 32
    if temp <= 32:
        return f"H2O is solid at {temp}f."
    elif temp >= 212:
        return f"H2O is gas at {temp}f."
    else:
        return f"H2O is liquid at {temp}f."
    pass