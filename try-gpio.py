#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import threading
import time

GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setwarnings(False)
INT = 26 

GPIO.setup(INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
  working = "y"
  while True and working == "y":

  # set an interrupt on a falling edge and wait for it to happen
    t0 = t1 = 0  
    GPIO.wait_for_edge(INT, GPIO.FALLING)
    #time.sleep(0.01)   # Wait  to check for spurious input
    #GPIO.wait_for_edge(INT, GPIO.FALLING)
    time.sleep(0.2)   # Wait  to check for spurious input
    if( GPIO.input(INT) == 0 ) :
      t0 = time.time()
      t1 = t0
      print(t0)
    GPIO.wait_for_edge(INT, GPIO.RISING)
    #time.sleep(0.01)   # Wait  to check for spurious input
    #GPIO.wait_for_edge(INT, GPIO.RISING)
    time.sleep(0.2)   # Wait to check for spurious input
    if( GPIO.input(INT) == 1 ) :
      t1 = time.time()
      print(t1)
    print(t1-t0)
    
    #GPIO.add_event_detect(INT, GPIO.FALLING, callback=cb)
    working=input("Press y to continue")

if __name__ == '__main__':
    main()
