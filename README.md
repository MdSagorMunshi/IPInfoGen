# IPInfoGen

![IPInfoGen Logo](ipinfogen_logo.png)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=MdSagorMunshi.IPInfoGen)](https://github.com/MdSagorMunshi/IPInfoGen)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/MdSagorMunshi/IPInfoGen)



IPInfoGen is a Python script that provides information about a given IP address. It collects and displays various details, including basic information, DNS information, geolocation, Whois lookup, reverse DNS, and open ports.

## Features

- Retrieve basic information using the ipinfo.io API.
- Fetch DNS information, including domain name and aliases.
- Obtain geolocation information using the ipinfo.io API.
- Perform a Whois lookup to get details like ASN, registrar, country, registration date, and IP range.
- Fetch reverse DNS information (domain name) for a given IP address.
- Scan common ports to check for open ports on the specified IP address.
 
## Requirements
- Python
- pip modules ```` pip install -r requirements.txt ````

## Instalation

- Linux/Debian
````
git clone https://github.com/MdSagorMunshi/IPInfoGen.git 
cd IPInfoGen
sudo python3 setup.py install
````
- Windows
````
git clone https://github.com/MdSagorMunshi/IPInfoGen.git 
cd IPInfoGen
python3 setup.py install
````
- Termux
````
git clone https://github.com/MdSagorMunshi/IPInfoGen.git 
cd IPInfoGen
python setup.py install
````
## Usage

Type on your Terminal: ````IPInfoGen````

- Follow the on-screen instructions to enter the target IP address.

## Uninstall

````
cd /path/IPInfoGen/ **/home/ryan/Desktop/IPInfoGen
python setup.py uninstall
````
- Note: Use sudo in Linux/Debian.
- Example: sudo python setup.py uninstall


## Dependencies

- `requests`: For making HTTP requests to the ipinfo.io API.
- `whois`: For performing Whois lookups.
- `dns`: For additional DNS information.
- `ipwhois`: For retrieving detailed IP information.

## Disclaimer

This script is intended for educational and informational purposes only. Ensure that you have the right to perform such activities on the target IP address, and be aware of legal considerations.
## Author

**Md Sagor Munshi**

- GitHub: [@MdSagorMunshi](https://github.com/MdSagorMunshi)
- X: [RYAN SHELBY](https://www.linkedin.com//)
- Email: ryanshelby@tuta.io

