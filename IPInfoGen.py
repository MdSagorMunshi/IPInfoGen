#!/usr/bin/env python
import socket
import requests
import whois
import json
from dns import resolver
from ipwhois import IPWhois
from colorama import Fore, Style

# ASCII art for the logo
logo = r"""
._____________.___        _____        ________               
|   \______   \   | _____/ ____\____  /  _____/  ____   ____  
|   ||     ___/   |/    \   __\/  _ \/   \  ____/ __ \ /    \ 
|   ||    |   |   |   |  \  | (  <_> )    \_\  \  ___/|   |  \
|___||____|   |___|___|  /__|  \____/ \______  /\___  >___|  /
                       \/                    \/     \/     \/ 
"""

def print_logo():
    print(Fore.BLUE + Style.BRIGHT + logo + Style.RESET_ALL)

def get_basic_info(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()

        print("\nBasic Information:")
        print("IP Address:", data.get("ip"))
        print("Country:", data.get("country"))
        print("Region:", data.get("region"))
        print("City:", data.get("city"))

    except requests.RequestException as e:
        print(f"Error fetching basic information: {e}")

def get_dns_info(ip_address):
    try:
        domain_info = socket.gethostbyaddr(ip_address)

        print("\nDNS Information:")
        print("Domain Name:", domain_info[0])
        print("Aliases:", domain_info[1])

        # Additional DNS information using the 'dns' library
        resolver_obj = resolver.Resolver()
        answer = resolver_obj.query(domain_info[0], 'A')
        print("\nAdditional DNS Information:")
        for rdata in answer:
            print(f"IP Address (DNS): {rdata.address}")

    except socket.herror as e:
        print(f"Error fetching DNS information: {e}")

def get_geolocation(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()

        print("\nGeolocation:")
        print("Location:", data.get("loc"))
        print("Geographical Coordinates:", data.get("loc").split(','))

    except requests.RequestException as e:
        print(f"Error fetching geolocation information: {e}")

def get_whois_info(ip_address):
    try:
        obj = IPWhois(ip_address)
        results = obj.lookup_rdap()

        print("\nWhois Lookup:")
        print("ASN:", results.get("asn"))
        print("Registrar:", results.get("asn_registry"))
        print("Country:", results.get("asn_country_code"))
        print("Registration Date:", results.get("asn_date"))
        print("IP Range:", results.get("asn_cidr"))

    except Exception as e:
        print(f"Error fetching Whois information: {e}")

def get_reverse_dns(ip_address):
    try:
        domain_name, _, _ = socket.gethostbyaddr(ip_address)

        print("\nReverse DNS:")
        print("Domain Name:", domain_name)

    except socket.herror as e:
        print(f"Error fetching reverse DNS information: {e}")

def get_open_ports(ip_address):
    try:
        # Example: scanning common ports (adjust as needed)
        common_ports = [21, 22, 23, 25, 80, 443, 3389]
        open_ports = []

        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)

            sock.close()

        print("\nOpen Ports:")
        if open_ports:
            print("Open Ports:", open_ports)
        else:
            print("No open ports found.")

    except Exception as e:
        print(f"Error fetching open ports information: {e}")

def main():
    print_logo()
    ip_address = input("Enter the IP address: ")
    get_basic_info(ip_address)
    get_dns_info(ip_address)
    get_geolocation(ip_address)
    get_whois_info(ip_address)
    get_reverse_dns(ip_address)
    get_open_ports(ip_address)

if __name__ == "__main__":
    main()

