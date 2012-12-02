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
#ser = serial.Serial(11, 9600, timeout=1)
print "Conn established"


def playRandomMessage():
    fileName = random.choice(os.listdir(messagePath))
    fileName = os.path.join(messagePath, fileName)
    randomSound = pyglet.resource.media(fileName, streaming=False)
    randomSound.play()

soundA.play()
#the cyclic function called by the pyglet engine


#pyglet.clock.schedule_interval(update, 1/30.)

if __name__ == '__main__':
    pyglet.app.run()
