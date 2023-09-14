import whois
import shodan
import requests
import sys
import argparse
import dns.resolver
import socket

argparse = argparse.ArgumentParser(description="This is a basic info gathering tool.", usage="python3 info_gathering.py -d DOMAIN [-o output]")
argparse.add_argument("-d","--domain", help="Enter the domain name for footprinting.",required=True)
argparse.add_argument("-o","--output", help="Enter the address of file to write output to. Saves the output in the file.")

args = argparse.parse_args()
domain = args.domain
output = args.output

#WHOIS Module
whois_result = 'WHOIS data: \n'
try:
	print("")
	print("[+] Getting WHOIS info...")
	py = whois.query(domain)
	print("[+] WHOIS info found.")
	print("")
	whois_result += "Name: {}".format(py.name) + '\n'
	whois_result += "Registrar: {}".format(py.registrar)  + '\n'
	whois_result += "Name Servers: {}".format(py.name_servers) + '\n'
	whois_result += "Creation Date: {}".format(py.creation_date) + '\n'
	whois_result += "Expiration Date: {}".format(py.expiration_date) + '\n'
	whois_result += "Last Updated: {}".format(py.last_updated) + '\n\n'
except:
	pass
print(whois_result)

#DNS Module
dns_data = 'DNS data: \n' #Stores the DNS result
print("[+] Getting DNS info...")
print("[+] DNS info found.")
print()
try:
	for a in dns.resolver.resolve(domain, 'A'):
		dns_data += "[+] A record: {}".format(a.to_text()) + '\n'
	dns_data += '\n'
except:
	dns_data += "[-] No A record found!" + '\n\n'
try:
	for aaaa in dns.resolver.resolve(domain, 'AAAA'):
		dns_data += "[+] AAAA record: {}".format(aaaa.to_text()) + '\n'
	dns_data += '\n'
except:
	dns_data += "[-] No AAAA record found!" + '\n\n'
try:
	for ns in dns.resolver.resolve(domain, 'NS'):
		dns_data += "[+] NS record: {}".format(ns.to_text()) + '\n'
	dns_data += '\n'
except:
	dns_data += "[-] No NS record found!" + '\n\n'
try:
	for mx in dns.resolver.resolve(domain, 'MX'):
		dns_data += "[+] MX record: {}".format(mx.to_text()) + '\n'
	dns_data += '\n'
except:
	dns_data += "[-] No MX record found!" + '\n\n'
try:
	for cname in dns.resolver.resolve(domain, 'CNAME'):
		dns_data += "[+] CNAME record: {}".format(cname.to_text()) + '\n'
	dns_data += '\n'
except: 
	dns_data += "[-] No CNAME record found!" + '\n\n'
try:
	for txt in dns.resolver.resolve(domain, 'TXT'):
		dns_data += "[+] TXT record: {}".format(txt.to_text()) + '\n'
	dns_data += '\n'
except: 
	dns_data += "[-] No TXT record found!" + '\n\n'
print(dns_data)

#Geolocation module
georesult = 'Geolocation_data: \n'
print("[+] Getting Geolocation info...")
try:
	response = requests.request('GET', "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
	print("[+] Geolocation info found!")
	georesult += "[+] Country: {}".format(response['country_name']) + '\n'
	georesult += "[+] Latitude: {}".format(response['latitude']) + '\n'
	georesult += "[+] Longitude: {}".format(response['longitude']) + '\n'
	georesult += "[+] City: {}".format(response['city']) + '\n'
	georesult += "[+] State: {}".format(response['state']) + '\n'
except:
	georesult += "Error in fetching geolocation data!!!" + '\n'
georesult += '\n'
print()
print(georesult)

#Saving the data
if(output):
	with open(output, 'w') as file:
		file.write(whois_result)
		file.write(dns_data)
		file.write(georesult)

