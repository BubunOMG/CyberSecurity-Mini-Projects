import os
import nmap

# Ensure Nmap path is included
nmap_path = 'C:\\Program Files (x86)\\Nmap'  # Adjust the path to your Nmap installation
os.environ['PATH'] += os.pathsep + nmap_path

# Initialize PortScanner
nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC" 

print("Starting Nmap scan on target:", target)

# Perform the scan
nm.scan(target, arguments=options)

# Debug print to check if any hosts were scanned
print("Scan completed. Hosts found:", nm.all_hosts())

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))

print("Nmap scan finished.")
