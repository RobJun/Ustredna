#wrap file for sipfullproxy.py
import socketserver
import socket
import sys
#from sipfullproxy import UDPHandler as sipHandler
#import sipfullproxy as proxy
#from SIPCodeInjector import replaceCode
from libs import sipfullproxy
from libs import SIPCodeInjector 
from libs import myLogger
#import myLogger

class Wrapper:

    def __init__(self,host,port, codeNames : dict, filename : str):
        self.serverData = (host,port)
        sipfullproxy.logs = self.log = myLogger.myLogger(filename)
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        if ipaddress == "127.0.0.1":
            ipaddress = sys.argv[1]
        print(ipaddress)
        self.ip = ipaddress
        sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (self.ip,self.serverData[1])
        sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (self.ip,self.serverData[1])
        for code, text in codeNames.items():
            SIPCodeInjector.replaceCode(code,text)

    def start(self):
        server = socketserver.UDPServer(self.serverData,sipfullproxy.UDPHandler)
        server.serve_forever()

