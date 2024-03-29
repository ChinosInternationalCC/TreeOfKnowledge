import os
import random
import sys
import serial

from pyglet.gl import *
import pyglet
from pyglet.window import key

#config
messagePath = "messages/"

#load the static sounds
soundA = pyglet.resource.media("messages/lucas.mp3", streaming=False)
soundB = pyglet.resource.media("messages/lucas.mp3", streaming=False)
soundC = pyglet.resource.media("messages/lucas.mp3", streaming=False)
soundD = pyglet.resource.media("messages/lucas.mp3", streaming=False)
soundE = pyglet.resource.media("messages/lucas.mp3", streaming=False)
soundF = pyglet.resource.media("messages/lucas.mp3", streaming=False)

#start the serial communication
ser = serial.Serial(3, 9600, timeout=1)
print "Conn established"


def playRandomMessage():
    fileName = random.choice(os.listdir(messagePath))
    fileName = os.path.join(messagePath, fileName)
    randomSound = pyglet.resource.media(fileName, streaming=False)
    randomSound.play()
#data = ser.read(1).__repr__()
soundA.play()
#the cyclic function called by the pyglet engine
def update(dt):
    #data = ser.read(1).__repr__()
    data = "Z"
    if data:
        #print "Received: %s." % data
        if 'A' in data:
            #playRandomMessage()
            soundA.play()
            print "A event"
                
        if 'B' in data:
            soundB.play()
            print "B event"
                
        if 'C' in data:
            soundC.play()
            print "C event"
        
        if 'D' in data:
            soundD.play()
            print "D event"
        
        if 'E' in data:
            soundE.play()
            print "E event"
        
        if 'F' in data:
            soundF.play()
            print "F event"
            
        if 'G' in data:
            print "G event"
            
        if 'H' in data:
            print "H event"

pyglet.clock.schedule_interval(update, 1/10.)


if __name__ == '__main__':
    pyglet.app.run()
