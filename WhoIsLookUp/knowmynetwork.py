import socket
import psutil

def get_network_info():
    network_info = {}

    # Get hostname
    hostname = socket.gethostname()
    network_info['Hostname'] = hostname

    # Get local IP address
    local_ip = socket.gethostbyname(hostname)
    network_info['Local IP'] = local_ip

    # Get all network interfaces and their IP addresses
    interfaces = psutil.net_if_addrs()
    network_info['Interfaces'] = {}

    for interface, addrs in interfaces.items():
        network_info['Interfaces'][interface] = []
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                network_info['Interfaces'][interface].append({
                    'IP Address': addr.address,
                    'Netmask': addr.netmask,
                    'Broadcast IP': addr.broadcast
                })
            elif addr.family == socket.AF_INET6:  # IPv6
                network_info['Interfaces'][interface].append({
                    'IPv6 Address': addr.address,
                    'Netmask': addr.netmask,
                    'Broadcast IP': addr.broadcast
                })
            elif addr.family == psutil.AF_LINK:  # MAC address
                network_info['Interfaces'][interface].append({
                    'MAC Address': addr.address
                })

    # Get default gateways
    gateways = psutil.net_if_stats()
    network_info['Gateways'] = gateways

    return network_info

def print_network_info():
    network_info = get_network_info()

    print(f"Hostname: {network_info['Hostname']}")
    print(f"Local IP: {network_info['Local IP']}\n")

    for interface, addrs in network_info['Interfaces'].items():
        print(f"Interface: {interface}")
        for addr in addrs:
            if 'IP Address' in addr:
                print(f"  IP Address: {addr['IP Address']}")
            if 'Netmask' in addr:
                print(f"  Netmask: {addr['Netmask']}")
            if 'Broadcast IP' in addr:
                print(f"  Broadcast IP: {addr['Broadcast IP']}")
            if 'IPv6 Address' in addr:
                print(f"  IPv6 Address: {addr['IPv6 Address']}")
            if 'MAC Address' in addr:
                print(f"  MAC Address: {addr['MAC Address']}")
        print()

    print("Default Gateways:")
    for gateway, stats in network_info['Gateways'].items():
        print(f"  {gateway}: {'Up' if stats.isup else 'Down'}")

if __name__ == "__main__":
    print_network_info()
