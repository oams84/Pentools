# Website IP and Ports scan


In this code, we have a Python script that allows us to retrieve the IP addresses associated with a given website and scan for open ports on those IP addresses. This can be useful for network administrators or security professionals who want to assess the security of a website or network..



## Table of Contents

- [Website IP and Ports scan](#website-ip-and-ports-scan)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

**Linux**

- Copy the link  ***https://github.com/oams84/Pentools.git***
  
- Open terminal in Linux 
  
- use Git clone and past the link 


**Windows**

- Click https://github.com/oams84/Pentools.git
- Install the zip file and extract it 
- modify the oamscanner.py (change website name and modify ports numbers as need.)
- start the powershell and CD to the folder 
- run python oamscanner.py




## Usage

- cd to the folder 

- run Nano oamscanner.py

- change website name and modify ports numbers as need.

- use the ctrl + x to save the file

- use chmod + oamscanner.py to change it to exe file

- use ./oamscanner.py


```python
import socket

def get_ip_addresses(url):
    try:
        ip_addresses = socket.gethostbyname_ex(url)[2]
        return ip_addresses
    except socket.gaierror:
        return []

def scan_ports(ip_address):
    open_ports = []
    common_ports = [21, 22, 80, 443, 3389, 8080, 8443, 8888]  # Add more ports as needed

    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    websites = ["bjs.com"]  # Add more websites as needed

    for website_url in websites:
        ip_addresses = get_ip_addresses(website_url)

        if ip_addresses:
            print(f"The IP addresses of {website_url} are: {ip_addresses}")

            for ip_address in ip_addresses:
                open_ports = scan_ports(ip_address)

                if open_ports:
                    print(f"The open ports on {ip_address} are: {open_ports}")
                else:
                    print(f"No open ports found on {ip_address}")
        else:
            print(f"Failed to retrieve the IP addresses of {website_url}")



```


## License

MIT License

