def reverse_words(s: str) -> str:
    a = s.split()
    a.reverse()
    c=a[-1]

    b = ""
    for element in a:
        if element != c :
            b+=element +" "
        else:
            b+=element

    return  b


