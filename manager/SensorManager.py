from model.W1Bus import W1Bus
class SensorManager(object):

    def discoverSensors(self):
        #Temperatursensoren
        #1WireBus
        self.w1bus = W1Bus(1)
        self.sensors={}
        self.sensors['temp']=self.w1bus.getSensors()
            
