def rec_factorial(x: int) -> int:
    if x==0:
        return 1
    elif x==1:
        return 1
    elif x>1:
        return x * rec_factorial(x-1)
    pass
