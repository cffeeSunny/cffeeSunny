
def fast_power(base: int, exponent: int, modulus: int) -> int:
    a=base
    if exponent == 0:
        return 1

    else:
        if exponent % 2 == 0:
            while exponent > 0 and exponent != 1:
                base = (base**2) % modulus
                exponent = exponent//2
            return base % modulus
        else:
            while (exponent - 1) > 0 and (exponent-1) != 1:
                base = (base**2) % modulus
                exponent = exponent//2
            return (a*base) % modulus
    pass
