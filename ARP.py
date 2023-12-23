"""
ARP Scanner
"""
from scapy.all import Ether, ARP, srp

def inputIPAddr():
    ip_range = input("[*] Enter IP Range to scan: ")
    bitmask = input("[*] Enter Bitmask for the subnet (ex. /24): ")

    bitmask.replace("/", "")
    return ip_range,bitmask



def arpScan(text=""):

    # if text != "":
    #     ip_range = text
    #     bitmask = "24"
    # else:
    
    ip_range, bitmask = inputIPAddr()

    broadcase = "ff:ff:ff:ff:ff:ff"
    ether_layer = Ether(dst=broadcase)


    # print(bitmask)

    ip_range = f"{ip_range}/{bitmask}"
    arp_layer = ARP(pdst=ip_range)

    packet = ether_layer / arp_layer

    ans, unans = srp(packet, iface="eth0", timeout=2)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print(f"IP: {ip} MAC: {mac}")

