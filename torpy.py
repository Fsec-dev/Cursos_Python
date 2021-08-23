#!/usr/bin/env python3
import sys
import requests

# Sock5 (Tor)
def session_tor():
    session = requests.session()
    # Por defecto el sock de Tor en Linux se mantiene en el puerto 9050
    session.proxies = {'http':'socks5h://127.0.0.1:9050',
                       'https':'socks5h://127.0.0.1:9050'}
    return session

def consulta(host):
    session = session_tor()
    req = session.get(host)

    if req.ok:
        for header in req.headers:
            print(header + " :" + req.headers[header])
    else:
        print (str(req.status_code))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("USO: \n\n{} <host>\n".format(sys.argv[0]))
    else:
        consulta(sys.argv[1])
