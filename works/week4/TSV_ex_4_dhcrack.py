def crack_dh_exchange(p: int, g: int, A: int, B: int) -> int:
    a=0
    while pow(g,a,p) != A:
        a += 1
    return pow(B,a,p)

    pass
