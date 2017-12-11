#!/usr/bin/env python3

import sys
import subprocess
import ipaddress

# Check arguments
if len(sys.argv) != 2:
    print("You must provide a CIDR address as an argument (e.g. 10.0.0.0/24)")
else:
    try:
        ipaddress.ip_network(sys.argv[1])
    except ValueError as e:
        print(e)
    net = ipaddress.ip_address(sys.argv[1])
    pos_ping = []
    neg_ping = []
    print("Pinging %s addresses..." % net.num_addresses)
    for ip in net:
        ping = subprocess.call(['ping', '-c', '1', '-W', '2', str(ip)], stdout=subprocess.DEVNULL)
        if ping == 0:
            print("Ping from %s" % ip)
            pos_ping += [ip]
        else:
            print("No ping from %s" % ip)
            neg_ping += [ip]
    print("Ping response from %s hosts." % len(pos_ping))
    print("No ping response from %s hosts." % len(neg_ping))
