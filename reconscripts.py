#!/usr/bin/env python3

import sys
import argparse
import subprocess
import ipaddress

# ADD COMMAND LINE SWITCHES
# switches = argparse.ArgumentParser(description='Basic scripted recon tasks.')
# switches.add_argument('-a') # AUTOMATE ALL TESTS  --all
# switches.add_argument('-d') # DNS ENUMERATION     --dns               -D  --dns-off
# switches.add_argument('-e') # SMTP ENUMERATION    --smtp              -E  --smtp-off
# switches.add_argument('-f') # FTP ENUMERATION     --ftp               -F  --ftp-off
# switches.add_argument('-i') # input file          --input-file
# switches.add_argument('-m') # SNMP ENUMERATION    --snmp              -M  --snmp-off
# switches.add_argument('-n') # input network       --input-network
# switches.add_argument('-p') # PINGSWEEP           --ping-sweep        -P  --ping-sweep-off
# switches.add_argument('-s') # SSH ENUMERATION     --ssh               -S  --ssh-off
# switches.add_argument('-w') # HTTP ENUMERATION    --http              -W  --http-off
# switches.add_argument('--prompt') # Prompt to continue or quit (yes/no, default=no)

pos_ping = []
neg_ping = []

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


def pingsweep(net):
    """Ping a given network using Linux's native Ping tool."""
    print("Pinging %s addresses..." % net.num_addresses)
    for ip in net:
        ping = subprocess.call(['ping', '-c', '1', '-W', '2', str(ip)], stdout=subprocess.DEVNULL)
        if ping == 0:
            print("Ping from %s" % ip)
            pos_ping += []
        else:
            print("No ping from %s" % ip)
            neg_ping += []
    print("Ping response from %s hosts." % len(pos_ping))
    print("No ping response from %s hosts." % len(neg_ping))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You must provide a CIDR address as an argument (e.g. 10.0.0.0/24)")
    else:
        try:
            ipaddress.ip_network(sys.argv[1])
        except ValueError as e:
            print(e)
    net = ipaddress.ip_network(sys.argv[1])
    # Evaluate the options and execute the scripts appropriately
