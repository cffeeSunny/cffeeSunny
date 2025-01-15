import string
from itertools import cycle
from string import ascii_letters, ascii_lowercase

print(ascii_lowercase)

def vigenere_encrypt (message: str, key: str) -> str:
    num_to_let = list(ascii_lowercase)
    let_to_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    message.lower()
    key.lower()
    message1 = list(message)
    key1 = list(key)
    m_num = 0
    k_num = 0
    result = []
    for m, k in zip(message1, cycle(key1)):
        m_num = let_to_num[m]
        k_num = let_to_num[k]
        secret_num = (m_num + k_num) % 26
        secret_let = num_to_let[secret_num]
        result.append(secret_let)
    return ''.join(result)



