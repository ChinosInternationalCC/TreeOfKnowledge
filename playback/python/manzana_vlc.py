import os
import random
import sys
import serial
import time
from os import listdir
from os.path import isfile, join

from pyglet.gl import *
import pyglet
from pyglet.window import key
from multiprocessing import Process, Queue
from subprocess import call
import subprocess

#config
messagePath = "messages/"
NoOfSets = 4

SetCount = 0

#start the serial communication
ser = serial.Serial(10, 9600, timeout=1)
print "Conn established"

def GetFileNames(i):
    mypath = os.path.dirname(os.path.abspath(__file__))+"\\set"+str(i)
    onlyFiles = [ "set"+str(i)+"/"+f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyFiles

def playRandomMessage():
    fileName = random.choice(os.listdir(messagePath))
    fileName = os.path.join(messagePath, fileName)
    subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", fileName])



startTime = time.time()
PathsList = GetFileNames(1)
print PathsList[0]

#the cyclic function called by the pyglet engine
while 1:
    if ((startTime-time.time())>1800):
        if (SetCount < (NoOfSets - 1)):
            SetCount = SetCount + 1
        else:
            SetCount = 0
        startTime = time.time()
        PathsList = GetFileNames(SetCount)
        print "New Set "+str(SetCount)
    data = ser.read(1).__repr__()
    if data:
        #print "Received: %s." % data
        if 'A' in data:
            
            print "A event"

        if 'B' in data:
			playRandomMessage()
            #subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[0]])
            print "B event"

        if 'C' in data:
            subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[1]])
            print "C event"
        
        if 'D' in data:
            subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[2]])
            print "D event"
        
        if 'E' in data:
            subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[3]])
            print "E event"
        
        if 'F' in data:
            subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[4]])
            print "F event"
            
        if 'G' in data:
            subprocess.Popen(["c:/Program Files/VideoLAN/VLC/vlc.exe", PathsList[5]])
            print "G event"
            
        if 'X' in data:
            print "X event"

