#wrap file for sipfullproxy.py
import socketserver
import socket
import sys
from libs.sipfullproxy import UDPHandler as sipHandler
import libs.sipfullproxy as proxy
from libs.SIPCodeInjector import replaceCode
import libs.myLogger

class Wrapper:

    def __init__(self,host,port, codeNames : dict, filename : str):
        self.serverData = (host,port)
        proxy.logs = self.log = libs.myLogger.myLogger(filename)
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        if ipaddress == "127.0.0.1":
            ipaddress = sys.argv[1]
        print(ipaddress)
        self.ip = ipaddress
        proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (self.ip,self.serverData[1])
        proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (self.ip,self.serverData[1])
        for code, text in codeNames.items():
            replaceCode(code,text)

    def start(self):
        server = socketserver.UDPServer(self.serverData,sipHandler)
        server.serve_forever()

