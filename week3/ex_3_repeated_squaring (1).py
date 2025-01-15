
def fast_power(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def main() -> None:
    assert fast_power(3, 16, 49) == 25
    assert fast_power(586561983649063, 982471150907619, 700106762604573) == 482959092846448
    print("All tests passed.")


if __name__ == "__main__":
    main()
