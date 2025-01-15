def gcd_output(x: int, y: int) -> list[str]:
    rest = x % y
    result = []
    while rest != 0 and rest != 1:
        factor = x/y
        result.append(f"{x} = {factor}*{y} + {rest}")
        x=y
        y=rest
        rest = x % y
    return result
