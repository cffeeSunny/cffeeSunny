def elgamal_decrypt(private_key: tuple[int, int, int], message: tuple[int, int]) -> int:
    p = private_key[0]
    q = private_key[1]
    x = private_key[2]
    C1 = message[0]
    C2 = message[1]
    K = pow (C1,x,p)
    Kmin = pow (K,(-1),1)
    M = pow ((C2*Kmin),1,p)
    return M
