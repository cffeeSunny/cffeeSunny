def crack_dh_exchange(p: int, g: int, A: int, B: int) -> int:
    e = 2
    E = pow(g,e,p)
    return pow(B,e,p)

    pass
