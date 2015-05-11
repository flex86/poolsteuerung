from app import App

conf = {'sensors':[{'temp':[{'name':'Temperatur1','address':'C:\Projekte\privat\Python\Poolsteuerung\w1.slave'}]}]}


x = App(conf)

x.run()

