import string
print (list(string.ascii_letters))
def replacement_cipher(key_dict: dict[str, str], cipher_text: str) -> str:
    import string
    allowed_list=list(string.ascii_uppercase)
    cipher_list=list(cipher_text)
    acc=""
    for element in cipher_list:
        if element not in allowed_list:
            if element in key_dict.keys():
                acc+=key_dict[element]
            else:
                acc+=element
        else:
            acc+=key_dict[element]
    return acc

    pass



