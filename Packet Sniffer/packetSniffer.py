from socket import *
from struct import *

def ethernet_frakme(data):
    dest_mac, src_mac, eth_proto = unpack('! 6s 6s H', data[:14])
    return {
        'dest_mac': dest_mac.hex(),
        'src_mac': src_mac.hex(),
        'eth_proto': eth_proto
    }