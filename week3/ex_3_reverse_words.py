def reverse_words(s: str) -> str:
    a = s.split()
    a.reverse()
    b=""
    for ele in a:
        b +=ele
    return b
