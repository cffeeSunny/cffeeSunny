def find_first_occurrence(haystack: str, needle: str) -> int | bool:
    # TODO implement
    list_haystack = list(haystack)
    for char in list_haystack:
        if char == needle:
            return list_haystack.index(needle)

        elif not (needle in list_haystack):
           return False
    pass
