import dpkt
import struct
def packet_analyser(filepath:str):
    res = []
    with open(filepath, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        for timestamp, packet in pcap:
           res_dict={}

           frame = dpkt.ethernet.Ethernet(packet)
           ip = frame.data
           sip= ip.src
           dip = ip.dst
           smac = frame.src
           dmac = frame.dst
           if ip.p == dpkt.ip.IP_PROTO_UDP :
               protocol = "UDP"
           if isinstance(ip.data, dpkt.tcp.TCP):
               protocol= "TCP"
           port = ip.data
           sport = port.sport
           dport = port.dport

           res_dict["dmac"] = dmac
           res_dict["smac"] = smac
           res_dict["sip"] = sip
           res_dict["dip"] = dip
           res_dict["dport"] = dport
           res_dict["sport"] = sport
           res_dict["timestamp"] = timestamp
           res_dict["segment_type"] = protocol
           res.append(res_dict)
    return res


