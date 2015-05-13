import time
import re
class Sensor(object):
    type=0
    def factory(type,address,name):
        if type == "DS18B20":return DS18B20(address,name)
        assert 0, "Bad sensor creation: " + type
    def __init__(self,address,name):
        self.address=address
        self.name=name
        
    
    def getValue(self):
        return 0.1
    def getType(self):
        return self.type

class DS18B20(Sensor):
    type='DS18B20'
    
    def getValue(self):
        value = "U"
        try:
            f = open(self.address, "r")
            line = f.readline()
            if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
                line = f.readline()
                m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
                if m:
                    value = str(float(m.group(2)) / 1000.0)
            f.close()
        except IOError as e:
            print(time.strftime("%x %X"), "Error reading", self.address, ": ", e)
        return value
    
