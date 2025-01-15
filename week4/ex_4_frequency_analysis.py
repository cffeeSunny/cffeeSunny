import collections
import string


def frequency_analysis(file_directory: str) -> dict[str, int]:
    frequency_dict = collections.defaultdict(set)
    allowed_letters = list(string.ascii_lowercase)
    with open (file_directory, 'r') as file:
        file_list = list(file.read())
        for element in file_list:
            if element not in allowed_letters:
                continue
            else:
                if element in frequency_dict.keys():
                    b= frequency_dict[element]
                    frequency_dict.update({element:(b+1)})
                else:
                    frequency_dict[element].add(1)
    return frequency_dict
    pass
