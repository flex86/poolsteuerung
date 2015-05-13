#!/usr/bin/env python
import datetime, threading, time
from app import App

next_call = time.time()

conf = {'sensors':[{'temp':[{'name':'Temperatur1','address':'C:\Projekte\privat\Python\Poolsteuerung\w1.slave'}]}]}
x = App(conf)
##def mainloop():
##    global next_call
##    print (datetime.datetime.now())
##    x.run()
##    next_call = next_call+3
##    try:
##        threading.Timer( next_call - time.time(), mainloop).start()
##    except(KeyboardInterrupt):
##        print('Wird beendet...')

##def do_every (interval, worker_func, iterations = 0):
##  if iterations != 1:
##    threading.Timer (
##      interval,
##      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
##    ).start ()
##
##  worker_func ()
##
##do_every(5,x.run())
x.run()
