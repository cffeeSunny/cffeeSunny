
import itertools
import string
def vigenere_encrypt (message: str, key:str) -> str:
    message=message.lower()
    key=key.lower()

    return zip(message,itertools.cycle(key))


