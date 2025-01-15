def generate_keys(p: int, g: int, x: int) -> tuple:
    for i in range (2,p):
        if p % i == 0:
            raise ValueError ('Invalid prime!')
    if p <= x:
        raise ValueError('Invalid prime!')
    if p % g == 0:
        raise ValueError('Invalid generator!')
    else:
        return ((p,g,x),(p,g,pow(g,x,p)))
