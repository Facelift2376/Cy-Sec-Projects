# Footprinter

# Domain Information Finder

## Introduction

The Domain Information Finder is a simple Python script that allows you to retrieve information about a domain name. Whether you're a web developer, a security analyst, or just curious about a particular website, this tool provides you with valuable insights into the domain's registration details, DNS records, and more.

## Features

- Retrieve WHOIS information: Get registration details, such as domain owner, registrar, and registration date.
- Display DNS records: Find out the domain's IP address, mail servers, and other DNS-related information.
- Display Geolocation information

## Getting Started

### Prerequisites

Before you can use this script, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - `whois`
  - `dnspython`
  - `requests`
  - `sys`
  - `argparse`
  - `socket`

### Usage

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/sanghaibiraj/Footprinter.git
   ```

2. Navigate to the project directory:

    ```shell
    cd Footprinter
    ```

3. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

4. Run the script by providing a domain name as an argument:

   ```shell
   python info_gathering.py -d example.com -o file_address
   ```

   Replace `example.com` with the domain name you want to look up.
   Replace `file_address` with the address of the file where you want to store the data
   Providing the domain name is compulsory, you may/may not use the `-o or --output` to save the output

5. The script will provide you with information about the specified domain, including WHOIS details, DNS records, and geolocation information.

### Example Output
Here's an example of the output you can expect from the script:
    
    [+] Getting WHOIS info...
    [+] WHOIS info found.

    WHOIS data: 
    Name: google.com
    Registrar: MarkMonitor Inc.
    Name Servers: {'ns1.google.com', 'ns4.google.com', 'ns2.google.com', 'ns3.google.com'}
    Creation Date: 1997-09-15 04:00:00
    Expiration Date: 2028-09-13 07:00:00+00:00
    Last Updated: None


    [+] Getting DNS info...
    [+] DNS info found.

    DNS data: 
    [+] A record: 142.251.42.110

    [+] AAAA record: 2404:6800:4009:832::200e

    [+] NS record: ns1.google.com.
    [+] NS record: ns2.google.com.
    [+] NS record: ns3.google.com.
    [+] NS record: ns4.google.com.

    [+] MX record: 10 smtp.google.com.

    [-] No CNAME record found!

    [+] TXT record: "onetrust-domain-verification=de01ed21f2fa4d8781cbc3ffb89cf4ef"
    [+] TXT record: "google-site-verification=TV9-DBe4R80X4v0M4U_bd_J9cpOJM0nikft0jAgjmsQ"
    [+] TXT record: "docusign=1b0a6754-49b1-4db5-8540-d2c12664b289"
    [+] TXT record: "v=spf1 include:_spf.google.com ~all"
    [+] TXT record: "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
    [+] TXT record: "MS=E4A68B9AB2BB9670BCE15412F62916164C0B20BB"
    [+] TXT record: "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
    [+] TXT record: "apple-domain-verification=30afIBcvSuDV2PLX"
    [+] TXT record: "google-site-verification=wD8N7i1JTNTkezJ49swvWW48f8_9xveREV4oB-0Hf5o"
    [+] TXT record: "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
    [+] TXT record: "webexdomainverification.8YX6G=6e6922db-e3e6-4a36-904e-a805c28087fa"
    [+] TXT record: "atlassian-domain-verification=5YjTmWmjI92ewqkx2oXmBaD60Td9zWon9r6eakvHX6B77zzkFQto8PQ9QsKnbf4I"


    [+] Getting Geolocation info...
    [+] Geolocation info found!

    Geolocation_data: 
    [+] Country: United States
    [+] Latitude: 37.751
    [+] Longitude: -97.822
    [+] City: None
    [+] State: None


## Contributing

Contributions to this project are welcome! If you have ideas for improvements or new features, please submit an issue or a pull request.


## Acknowledgments

- Special thanks to the creators of the `whois` and `dnspython` libraries for making domain information retrieval easy.
- Inspired by the need for a simple tool to quickly gather domain information.


Happy domain hunting!

