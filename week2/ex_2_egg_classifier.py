def egg_classifier(weight: int, is_white: bool, living_conditions: str) -> str:
    if weight <= 0:
        return "Error"
    elif weight < 53:
        size = "S"
    elif weight < 63:
        size = "M"
    elif weight < 73:
        size = "L"
    elif weight >= 73:
        size = "XL"
    if is_white == True:
        color = "white"
    elif is_white == False:
        color = "brown"
    return f"Size: {size}; Color: {color}; Living Conditions: {living_conditions} "
    pass
