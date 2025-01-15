import math

print(365*364)
def compute_birthday_paradox(n: int) -> float:
    if n < 2:
        raise ValueError("n too small")
    elif n > 120:
        raise ValueError('n too large')
    else:
        b=float(float(math.factorial(365)/(math.factorial(365-n))/pow(365,n)))
        result = (1.0-b)
        return (round(result,4))
    pass
