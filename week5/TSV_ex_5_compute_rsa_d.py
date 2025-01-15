def compute_d(p:int, q:int, e:int) -> int:
    phiN = (p - 1) * (q - 1)
    for i in range (2,p):
        if p % i == 0:
            raise ValueError ("p and q need to be prime")

    for i in range (2,q):
        if q % i == 0:
            raise ValueError ("q and p need to be prime")
    if p % q == 0 or q % p == 0:
        raise ValueError ("p and q need to be prime")
    if phiN % e == 0 or e % phiN == 0:
        raise ValueError ("e and phi(N) need to be coprime.")
    d = pow(e,-1,phiN)
    return d

