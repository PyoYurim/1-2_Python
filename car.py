from datetime import datetime
from datetime import *

class Car:
    def __init__(self, number):
        self.number = number
        self.intime = datetime.now()
        self.outtime = None

    def out(self):
        self.outtime = datetime.now()

    #def gettime(self):
        #if self.outtime :
            #return (self.outtime - self.intime).seconds // 3600
        #else:
            #return (datetime.now() - self.intime).seconds // 3600
    def gettime(self):
        if self.outtime:
            outtime = self.outtime
        else:
            outtime = datetime.now()

        return (outtime - self.intime).seconds #// 3600

    def calprice(self):
        return self.gettime() * 2000
