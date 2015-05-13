from manager.SensorManager import SensorManager
import queue
import threading
class App(object):
    
    def __init__(self,config):
        self.config=config
        self.sensormanager=SensorManager()
        self.db=""
        self.data_queue=queue.Queue()
       
        
        #sensoren registrieren
        #self.sensors={'temp':[DS18B20('C:\Projekte\privat\Python\Poolsteuerung\w1.slave','Temperatur1')]}
        #for sensorclass in config['sensors']:
           # for sensor in sensorclass:
                #self.sensors['temp'].append()
        #datenbankconnection initialisieren
    def run(self):
        self.sensormanager.discoverSensors()
       
        t1 = threading.Thread(target=self.getSensorData,args=[self.data_queue])
        
        t1.start()
        t2 = threading.Thread(target=self.saveSensorData,args=[self.data_queue])
       
        t2.start()
        
        
        #t1.join()
        #t2.join()
        
        #print(self.data_queue)
       
    def getSensorData(self,queue):
        for name,sensor in self.sensormanager.sensors['temp'].items():
            queue.put({'address':sensor.address,'value':sensor.getValue()})
            print("Put data in queue")

    def saveSensorData(self,queue):
        while not queue.empty():
            print("get data from queue")
            print(queue.get())
        
