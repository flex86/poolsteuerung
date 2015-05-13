from model.sensors.Sensor import Sensor
class W1Bus(object):
    path='C:/Projekte/privat/Python/Poolsteuerung/sys/bus/w1/devices/'
    #path='/sys/bus/w1/devices/'
    bus_master_template="w1_bus_master{}"
    w1_master_slave_count="w1_master_slave_count"
    w1_master_slaves="w1_master_slaves"
    w1_slave="w1_slave"

    def __init__(self, name):
        self.name=name
        self.slaves={}
        
    
    def getSensors(self):
        #path scannen mit bus_master_template
        #fuer jeden bus_master die slaves auslesen
        f=open(self.getMasterSlavesFileName())
        for line in f:
            self.slaves[line.strip()]=Sensor.factory('DS18B20',self.getSensorAddress(line.strip()),line.strip())

        return self.slaves

    def readSensorAdresses(self):
        file = open(self.getMasterSlavesFileName())

    def getMasterSlavesFileName(self):
        return self.path+self.getName()+'/'+self.w1_master_slaves

    def getName(self):
        return self.bus_master_template.format(self.name)

    def getSensorAddress(self,address):
        return self.path+address+'/'+self.w1_slave
        
        
