def celsius_to_fahrenheit_ice(celsius: int) -> str:
    temp = round(celsius * 1.8 + 32,2)
    if temp <= 32:
        return f"H2O is solid at {temp}f"
    elif temp >= 212:
        return f"H2O is gas at {temp}f"
    else:
        return f"H2O is liquid at {temp}f"
    pass