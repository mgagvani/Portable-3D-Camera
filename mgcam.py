#!/usr/bin/env python3

import RPi.GPIO as GPIO
import subprocess
import threading
import time
import glob
import os

GPIO.setmode(GPIO.BCM) # use GPIO numbering
GPIO.setwarnings(False)
INT = 26 

GPIO.setup(INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def disp():
#    dispproc=subprocess.Popen(r"/usr/bin/gst-launch-1.0 -vvv -e v4l2src ! videoscale ! video/x-raw,width=656,height=192 !  autovideosink", shell=True)
    dispproc=subprocess.Popen([r"/usr/bin/gst-launch-1.0", r"-vvv", r"-e", r"v4l2src", "!", r"videoscale", "!", r"video/x-raw,width=656,height=192", "!",  r"autovideosink"],stdout=subprocess.PIPE)
    print("Started display pipeline")
    time.sleep(0.5)
    raiseproc=subprocess.run(r"/home/pi/zed/raise.sh", shell=True)
    print("Moved window")
    return dispproc

def rec():
    newfilename=genfilename()
    recproc=subprocess.Popen([r"/usr/bin/gst-launch-1.0", r"-vvv", r"-e", r"v4l2src", r"!", "tee", "name=t", "t.", "!", "queue", "!", r"videoscale", "!", r"textoverlay", r"text=\"Rec\"", r"valignment=bottom", r"halignment=left",  r"!", r"video/x-raw,width=656,height=192", "!",  r"autovideosink", r"t.", r"!", r"queue",  r"!",  r"videoscale",  r"!",  r"video/x-raw,width=1920,height=544,framerate=30/1",  r"!",  r"omxh264enc",  r"control-rate=1",  r"target-bitrate=3000000",  r"!",  r"h264parse",  r"!",  r"matroskamux",  r"!",  r"filesink",   r"location=", newfilename  ],stdout=subprocess.PIPE)
    print("Started rec pipeline")
    time.sleep(0.5)
    raiseproc=subprocess.run(r"/home/pi/zed/raise.sh", shell=True)
    print("Moved window")
    return recproc

def movefile():
    pathlist=glob.glob("/home/pi/zed/out[0-9]*.mkv")
    filelist=[name.split('/')[-1] for name in pathlist]
    maxnum=max([int(name[3:7]) for name in filelist])
    nextnum = maxnum+1
    newfilename="/home/pi/zed/out{:04d}.mkv".format(nextnum)
    try:
      os.rename("/home/pi/zed/out.mkv", newfilename)
      #copyproc=subprocess.check_call(['sudo','/bin/mv','/home/pi/zed/out.mkv',newfilename])
    except:
      print("Failed to move file")

def genfilename():
    pathlist=glob.glob("/home/pi/zed/out[0-9]*.mkv")
    filelist=[name.split('/')[-1] for name in pathlist]
    maxnum=max([int(name[3:7]) for name in filelist])
    nextnum = maxnum+1
    newfilename="/home/pi/zed/out{:04d}.mkv".format(nextnum)
    return newfilename


def main():
  isrecording = False
  disproc = disp()
  isdisplaying = True
  while True :
  # set an interrupt on a falling edge and wait for it to happen
    t0 = t1 = 0  
    GPIO.wait_for_edge(INT, GPIO.FALLING)
    time.sleep(0.2)   # Wait  to check for spurious input
    if( GPIO.input(INT) == 0 ) :
      t0 = time.time()
      t1 = t0
      #print(t0)
    GPIO.wait_for_edge(INT, GPIO.RISING)
    time.sleep(0.2)   # Wait to check for spurious input
    if( GPIO.input(INT) == 1 ) :
      t1 = time.time()
     #print(t1)
    if (t1- t0 < 1.0 and t1-t0 > 0):
        if not isrecording:
          if isdisplaying:
            disproc.terminate()
            time.sleep(0.5)
            recproc=rec()
            isrecording = True
            isdisplaying = False
        else:
          recproc.terminate()
          isrecording = False
          #rename the file, not working when running from /etc/xdg/lxsession/LXDE-pi/autostart
          #movefile()
          time.sleep(0.5)
          disproc = disp()
          isdisplaying = True
    elif (t1-t0 > 2.0 and t1-t0 < 5.0):
        # graceful shutdown
        shutproc = subprocess.check_call(['/usr/bin/sudo', 'shutdown', 'now'])



    #GPIO.add_event_detect(INT, GPIO.FALLING, callback=cb)
    #working=input("Press y to continue")

if __name__ == '__main__':
    main()
