def unique_IPs(ip_list: list[str]) -> list[str]:
    a=[]
    for element in ip_list:
        if not (element in a):
            a.append(element)
    return a
    pass
