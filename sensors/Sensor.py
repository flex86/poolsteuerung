class Sensor(object):
    
    def __init__(self,address,name):
        self.address=address
        self.name=name

    def getValue(self):
        return 0.1
    
