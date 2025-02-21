import ipaddress


def find_smallest_cidr(ips: list[str]) -> str:
    int_ip_list = []
    for ip in ips:
        int_ip_list.append(int(ipaddress.IPv4Address(ip)))
    min_ip = min(int_ip_list)
    max_ip = max(int_ip_list)
    differing_bits = min_ip ^ max_ip
    mask = 32
    while differing_bits:
        differing_bits >>= 1
        mask -= 1
    base_network_address = ipaddress.IPv4Address(min_ip & ((1 << mask) - 1) << (32- mask))
    result = f"{base_network_address}/{mask}"
    return print (result)
    pass
