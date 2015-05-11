
from manager.SensorManager import SensorManager
import time
class App(object):
    
    def __init__(self,config):
        self.config=config
        self.sensormanager=SensorManager()
        
       
        
        #sensoren registrieren
        #self.sensors={'temp':[DS18B20('C:\Projekte\privat\Python\Poolsteuerung\w1.slave','Temperatur1')]}
        #for sensorclass in config['sensors']:
           # for sensor in sensorclass:
                #self.sensors['temp'].append()
        #datenbankconnection initialisieren
    def run(self):
        self.sensormanager.discoverSensors()
        while True:
            for name,sensor in self.sensormanager.sensors['temp'].items():
                print(sensor.getValue())
            time.sleep(10)
