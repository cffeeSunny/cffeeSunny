def compute_d(p:int, q:int, e:int) -> int:
    if (p % q == 0) or (q % p == 0):
        raise ValueError ("p and q need to be prime")
    phiN = (p-1)*(q-1)
    if (phiN % e == 0) or ( e % phiN == 0):
        raise ValueError ("e and phi(N) need to be coprime.")
    d = 0
    while not d*e == pow(1,1,phiN):
        d+=1
    return d

