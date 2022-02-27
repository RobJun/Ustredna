
import sys
from datetime import datetime as dt

class myLogger:
    calls = {}
    def __init__(self,filename : str = None):
        if filename is None:
            return 
        self.filename = filename
        try:
            file = open(filename, "w")
        except:
            print("--> Problem with file creation <--")
            sys.exit(1)
        file.write(">> Logging\n")
        file.close()
    
    def writeTofile(self, text : str, callID : str = None):
        date_time =  dt.now().strftime("%m/%d/%Y, %H:%M:%S")
        if callID is None:
            string = date_time + " >> [ " + text + " ]\n"
        else:
            string = date_time +" >> "+ callID +" >> [ " + text + " ]\n"
        file = open(self.filename,"a")
        file.write(string)
        file.close()

