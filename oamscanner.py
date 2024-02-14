import socket
import concurrent.futures

def get_ip_addresses(url):
    try:
        ip_addresses = socket.gethostbyname_ex(url)[2]
        return ip_addresses
    except socket.gaierror:
        return []

def scan_ports(ip_address):
    open_ports = []
    common_ports = [21, 22, 80, 443]  # Add more ports as needed

    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)

    return open_ports

websites = ["example.com"]  # Add more websites as needed

with concurrent.futures.ThreadPoolExecutor() as executor:
    for website_url in websites:
        ip_addresses = get_ip_addresses(website_url)

        if ip_addresses:
            print(f"The IP addresses of {website_url} are: {ip_addresses}")

            results = executor.map(scan_ports, ip_addresses)

            for ip_address, open_ports in zip(ip_addresses, results):
                if open_ports:
                    print(f"The open ports on {ip_address} are: {open_ports}")
                else:
                    print(f"No open ports found on {ip_address}")
        else:
            print(f"Failed to retrieve the IP addresses of {website_url}")
