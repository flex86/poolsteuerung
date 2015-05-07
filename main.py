from app import App
conf = {'sensors':[{'temp':[{'name':'Temperatur1','address':'C:\Projekte\privat\Python\Test\w1.slave'}]}]}


x = App(conf)

x.run()

