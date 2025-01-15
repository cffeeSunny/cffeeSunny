def find_first_occurrence(haystack: str, needle: str) -> int | bool:
    if needle in haystack:
        return haystack.index(needle)
    elif not (needle in haystack):
           return False
    pass
