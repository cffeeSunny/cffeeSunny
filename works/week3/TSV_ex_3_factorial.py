def factorial(n: int) -> int:
    acc=1
    while n>=2:
        acc= acc*n
        n=n-1
    return acc
    pass