def slaac_reversion(ipv6_address: str) -> str:
    ip6 = ipv6_address.replace(":","")
    ip6 = ip6.replace("fffe","")
    ip6_doubles = []
    for i in range (0,len(ip6),2):
        ip6_doubles.append(ip6[i:i+2])
    ip6_doubles = ip6_doubles[-6::]
    ip4_bytes = []
    for element in ip6_doubles:
        byte_int = int(element, 16)
        ip4_bytes.append(f"{byte_int:08b}")
    first_el = ip4_bytes[0]
    flip_bit = 1 - int(first_el [6])
    flipped_el = first_el[:6] + str(flip_bit) + first_el[7:]
    ip4_bytes_flip = []
    ip4_bytes_flip.append(flipped_el)
    for element in range (1,len(ip4_bytes)):
        ip4_bytes_flip.append(ip4_bytes[element])
    result = ""
    for element in ip4_bytes_flip:
        element_int = int(element, 2)
        result += f"{element_int:02X}".upper() + ":"
    result = result[:-1]
    return (result)

    pass
