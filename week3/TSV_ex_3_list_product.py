
def list_product(lst: list) -> int:
    acc=1
    if lst == []:
        return 0
    for i in lst:
            acc*=i
    return acc
    pass
