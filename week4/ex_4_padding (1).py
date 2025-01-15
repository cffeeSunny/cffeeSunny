def compute_pad(message: str) -> str:
    result=""
    m_length_bites=message[-8:]
    m_length_mod_int=int.from_bytes(m_length_bites,'big')
    a=0
    while pow(a,1,(2**8)) != m_length_mod_int:
        a=a+1
    padding_length=128-a
    padded_string=(padding_length).rjust(result)
    return padded_string
    pass
