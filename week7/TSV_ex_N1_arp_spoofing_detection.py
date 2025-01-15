#
def detect_arp_spoofing(table: list[str]) -> set[str]:
    ip_mac_dict = {}
    poisoned_ips = set()
    for element in table:
        ip,mac = element.split(' is at ')
        for mac1 in mac.split(':'):
            formatted_mac = ':'.join(f"{int(mac1, 16):02x}")
        if ip in ip_mac_dict and ip_mac_dict[ip] != formatted_mac:
            poisoned_ips.add(ip)
        else:
            ip_mac_dict[ip] = formatted_mac
    return poisoned_ips


    pass
