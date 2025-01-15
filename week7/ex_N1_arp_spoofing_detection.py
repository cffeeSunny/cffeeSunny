def detect_arp_spoofing(table: list[str]) -> set[str]:
    ip_mac_dict = {}
    poisoned_ips = set()
    for element in table:
        ip,mac = element.split(' is at ')
        mac = mac.lower().replace(":","").zfill(12)
        if ip in ip_mac_dict and ip_mac_dict[ip] != mac:
            poisoned_ips.add(ip)
        else:
            ip_mac_dict[ip] = mac
    return poisoned_ips


    pass
