from sensors.temp.DS18B20 import *
import time
class App(object):
    
    def __init__(self,config):
        self.config=config

       
        
        #sensoren registrieren
        self.sensors={'temp':[DS18B20('C:\Projekte\privat\Python\Test\w1.slave','Temperatur1')]}
        #for sensorclass in config['sensors']:
           # for sensor in sensorclass:
                #self.sensors['temp'].append()
        #datenbankconnection initialisieren
    def run(self):
        while True:
            for sensor in self.sensors['temp']:
                print(sensor.getValue())
            time.sleep(2)
