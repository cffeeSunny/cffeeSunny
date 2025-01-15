def compute_pad(message: str) -> str:
    binary_message = ''.join(format(ord(x), '08b') for x in message)
    n = 0
    result = ""
    for i in binary_message:
        n += 1
    m_last_block = pow(n, 1, 128)
    length_m = pow(len(message), 1, (2 ** 8))
    bin_length_m = bin(length_m)[2:]
    c = 8 - len(bin_length_m)
    if c != 0:
        bin_length_m = "0" * c + bin_length_m
    else:
        bin_length_m = bin_length_m
    padding_length = 128 - 8 - 1 - m_last_block
    if padding_length == 0:
        result = "1" + "0" * 127 + bin_length_m
    else:
        result = "1" + "0" * padding_length + bin_length_m
    if len(result) == 9:
        result = "1" + "0" * 127 + bin_length_m

    return result
    pass