def fast_power(base: int, exponent: int, modulus: int) -> int:
    while exponent % 2 = 0:
        base = base**2
        exponent = exponent // 2
    return base**exponent % modulus

    pass
