#!/usr/bin/env python3

import sys
import argparse
import subprocess
import ipaddress
import multiprocessing

# ADD COMMAND LINE SWITCHES
# switches = argparse.ArgumentParser(description='Basic scripted recon tasks.')
# switches.add_argument('-a') # AUTOMATE ALL TESTS  --all
# switches.add_argument('-d') # DNS ENUMERATION     --dns               -D  --dns-off
# switches.add_argument('-e') # SMTP ENUMERATION    --smtp              -E  --smtp-off
# switches.add_argument('-f') # FTP ENUMERATION     --ftp               -F  --ftp-off
# switches.add_argument('-i') # input file          --input-file
# switches.add_argument('-m') # SNMP ENUMERATION    --snmp              -M  --snmp-off
# switches.add_argument('-n') # input network       --input-network
# switches.add_argument('-p') # PING SWEEP          --ping-sweep        -P  --ping-sweep-off
# switches.add_argument('-s') # SSH ENUMERATION     --ssh               -S  --ssh-off
# switches.add_argument('-t') # SMB ENUMERATION     --smb               -T  --smb-off
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


def multi_proc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip,port))
    jobs.append(p)
    p.start()
    return


def sql_enum(ip, port):
    print("INFO: Detected MS-SQL on %s:%s" % (ip, port))
    print("INFO: Performing nmap mssql script scan for %s:%s" % (ip, port)
    MSSQLSCAN = "nmap -vv -sV -Pn -p %s --script=ms-sql-info,ms-sql-config,ms-sql-dump-hashes --script-args=mssql.instance-port=1433,smsql.username-sa,mssql.password-sa -oX results/exam/nmap/%s_mssql.xml %s" % (port, ip, ip)
    results = subprocess.check_output(MSSQLSCAN, shell=True)


def dns_enum(ip, port):
    print("INFO: Detected DNS on %s:%s" % (ip, port))
    if port.strip() == "53":
       SCRIPT = "./dnsrecon.py %s" % ip
       subprocess.call(SCRIPT, shell=True)
    return


def smtp_enum(ip, port):
    print("INFO: Detected smtp on %s:%s" % (ip, port))
    if port.strip() == "25":
       SCRIPT = "./smtprecon.py %s" % ip
       subprocess.call(SCRIPT, shell=True)
    else:
       print("WARNING: SMTP detected on non-standard port, smtprecon skipped (must run manually)")
    return


def ftp_enum(ip, port):
    print("INFO: Detected ftp on %s:%s" % (ip, port))
    SCRIPT = "./ftprecon.py %s %s" % (ip, port)
    subprocess.call(SCRIPT, shell=True)
    return


def snmp_enum(ip, port):
    print("INFO: Detected snmp on %s:%s" % (ip, port))
    SCRIPT = "./snmprecon.py %s" % ip
    subprocess.call(SCRIPT, shell=True)
    return


def ping_sweep(net):
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


def ssh_enum(ip, port):
    print("INFO: Detected SSH on %s:%s" % (ip, port))
    SCRIPT = "./sshrecon.py %s %s" % (ip_address, port)
    subprocess.call(SCRIPT, shell=True)
    return


def smb_enum(ip, port):
    print("INFO: Detected SMB on %s:%s" % (ip, port))
    if port.strip() == "445":
       SCRIPT = "./smbrecon.py %s 2>/dev/null" % ip
       subprocess.call(SCRIPT, shell=True)
    return


def http_enum(ip, port):
    print("INFO: Detected http on %s:%s" % (ip, port))
    print("INFO: Performing nmap web script scan for %s:%s" % (ip, port))
    HTTPSCAN = "nmap -sV -Pn -vv -p %s --script=http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,http-robots.txt -oN /root/scripts/recon_enum/results/exam/%s_http.nmap %s" % (port, ip_address, ip_address)
    results = subprocess.check_output(HTTPSCAN, shell=True)
    DIRBUST = "./dirbust.py http://%s:%s %s" % (ip_address, port, ip_address)  # execute the python script
    subprocess.call(DIRBUST, shell=True)
    # NIKTOSCAN = "nikto -host %s -p %s > %s._nikto" % (ip_address, port, ip_address)
    return


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
