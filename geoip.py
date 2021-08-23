#!/usr/bin/env python3

import sys
import json
import socket
import requests

UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"}

def main(host):

	host = socket.gethostbyname(host)

	url = "https://ipinfo.io/"+host+"/json"
	r = requests.get(url, headers=UA)
	
	if r.status_code != 200:
			print ("\nError {}\n".format(r.status_code))
	else:
		j = json.loads(r.text)

		ip = j['ip']
		country = j['country']
		city = j['city']
		region = j['region']
		geo = j['loc']
		isp = j['org']
		timezone = j['timezone']
		
		print ("""
GEOIP Version 0.1v

IP: {}
Pais: {}
Ciudad: {}
Region: {}
Geolocalizacion: {}
ISP: {}
Zona Horaria: {}
		""".format(ip, country, city, region, geo, isp, timezone))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print ("\nGeoIp 0.1v - 2021")
		print ("\n{} <ip/url>\n".format(sys.argv[0]))
	else:
		target = sys.argv[1]

		if target.startswith("http"):
			target = target.split('/')[2]

		main(target)

