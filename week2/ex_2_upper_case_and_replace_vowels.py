def upper_case_and_replace_vowels(my_string: str) -> str:
    vowels = ['A', 'E', 'I','O','U','a', 'e', 'i', 'o', 'u']
    my_string = my_string.upper()
    my_list = list(my_string)
    final_list = []
    for char in my_list:
        if char in vowels:
            final_list.append('x')
            break
        else:
            final_list.append(char)
    final_string = ''.join(final_list)
    return final_string
pass
