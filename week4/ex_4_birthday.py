import math

def compute_birthday_paradox(n: int) -> float:
    if n < 2:
        raise ValueError("n too small")
    elif n > 120:
        raise ValueError('n too large')
    else:
        b=float(float(math.factorial(365)/(math.factorial(365-n))/pow(365,n)))
        result = 100 * (1.0-b)
        round(result,4)
        return (result)
    pass
