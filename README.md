You don't need sudo, Nmap, or struggling to find the IP address for any website This Python code is a simple script that performs two main tasks for you: it retrieves the IP addresses associated with a given list of websites and then scans for open ports on those IP addresses. Here's a breakdown of the code:

get_ip_addresses(url) function:

Uses the socket.gethostbyname_ex(url) function to get a list of IP addresses associated with the specified URL.
Returns the list of IP addresses if successful, or an empty list if an exception (socket.gaierror) occurs.
scan_ports(ip_address) function:

Defines a list of common ports (common_ports) that the script will check for openness (21, 22, 80, and 443) and you can add more ports as you need.
Iterates through the common ports and attempts to establish a connection to each port using socket.connect_ex().
If the connection attempt is successful (result is 0), it adds the port to the list of open ports (open_ports).
Closes the socket after each connection attempt.
Returns the list of open ports.
Main part of the script:

Defines a list of websites (websites) to be processed. Note that there is a typo in the list; "example,com" should be "example.com."
Iterates through each website in the list.
Calls get_ip_addresses() to retrieve the IP addresses associated with the website.
If IP addresses are obtained, it prints the IP addresses.
Iterates through each IP address obtained and calls scan_ports() to check for open ports.
Prints the open ports if any are found, or a message indicating no open ports.
If the script fails to retrieve IP addresses for a website, it prints an error message.
Notes:

The code uses the socket module, which is a standard library in Python, to perform DNS resolution and port scanning.
The timeout for port connection attempts is set to 1 second (sock.settimeout(1)), making the script responsive but less thorough.
You may need to adjust the common_ports list based on your specific needs or add more websites to the websites list. Additionally, fix the typo in the example website URL.
