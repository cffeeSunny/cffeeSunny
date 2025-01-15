import string
import collections
a="123"
n=9
for element in a:
    print(n)





def frequency_analysis(file_directory: str) -> dict[str, int]:
    frequency_dict = collections.defaultdict(int)
    allowed_letters = list(string.ascii_lowercase)
    for letter in allowed_letters:
        frequency_dict[letter] = 0
    with open (file_directory, 'r') as file:
        file_list = list(repr(file))
        for element in file_list:
            if element in allowed_letters:
                frequency_dict[element] += 1

    return dict(frequency_dict)
    pass
