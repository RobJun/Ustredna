
import sys
from datetime import datetime as dt

class myLogger:
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
    
    def writeTofile(self, text : str):
        date_time =  dt.now().strftime("%m/%d/%Y, %H:%M:%S")
        string = date_time + " >> " + text + "\n"
        file = open(self.filename,"a")
        file.write(string)
        file.close()

