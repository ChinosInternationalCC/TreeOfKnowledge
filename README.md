The Tree Of Knowledge Of Good And Evil
===============
##Description
The instalation has 2 parts: one part where people can "leave" their knowledge by leaving a message 
that is recorded usign a microphone and the part where people can receive the knowledge from the tree by touching 
the apples that hang in the tree and listening the message or some other sounds on the headphones.

The recording instalation consists from the head of a goat that has a microphone fitted near the ear.
In order to leave the message you have to push a button with backlight illumination, when you finish your message the 
light will turn off indicating that the recording of the message was finished. The sesning of the button and control of 
the light are done by an arduino that is connected to a computer that records the sounds.

The playback instalation consists from a tree with more apples. Using banana connectors and wires the apples are connected 
to an arduino board and they will act as capacitive sensors. The software from the arduino board will detect when an
apple is touched and will sent the event via the serial port to a computer that will play a message or a sound.
To the computer are connected more headphones. The messages folders from the recording and playback instalation are synchronized
via ethernet.

##Software

For each part of the installation there are 2 software applications one that runs on the arduino board and the other one
written in Python that runs on the PC.

For the arduino aplications is used [arduino 1.0.1](http://arduino.cc/en/Main/Software) and [arduino uno](http://www.arduino.cc/en/Main/arduinoBoardUno) boards.
The arduino application that detects the touching of apples uses the [cap sense library](http://arduino.cc/playground/Main/CapacitiveSensor?from=Main.CapSense).

For the Python applictions is used [Python 2.7.3](http://www.python.org/download/releases/2.7.3/) with the following libraries: 
- [PySerial](http://pypi.python.org/pypi/pyserial) for the serial communication, 
- [PyGlet](http://www.pyglet.org/download.html) for the audio playback
- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) for the sound recording

Download and install all this dependecies in order to get started.

###Record
The arduino application is reading the state of the pushbutton connected to a digitial input pin and sends the state of the
button via the serial port to the python application that runs on the PC.
When the button is pressed, the arduino application turns on the 12V bulb that illuminates the button using a relay. The
illumination is turned off when the turn off event is received from the python application via the serial port.

The python application waits for the start recording event received via the serial port from the arduino board. When this
event is received the recording is started. The recording ends when a period of silence is detected. There is a THRESHOLD
to configure the "level" of silence. When the recording ends the appropiate event is sent via the serial port in order to
turn off the push button illumination.

###Playback

The arduino application detects when an apple is touched using the cap sense library and sends the event via the serial port
to the python application that runs on the computer. Each apple has asociated a unique id.
When 3 apples are touched in the same time a "god mode" event is sent through the serial port.

The python application receives the apples events and plays the sound that associated with each event. One apple is a "special"
apple that plays the message recorded by the recording instalation. The message that is played each time is selected randomly.
For the "god mode" event will be played a message from god sounds, while the sounds associated to the other apples are samples
that can be used to creat musical compositions.

##Hardware

- 2 x Arduino Uno Board
- 2 x USB cables to conect the arduino boards to the computers
- 2 x computers connected through ethernet
- headphones
- protoboards
- wires
- 4 x banana connectors
- 1 x pushbutton with illumination
- 1 x 100kohm pulldown resistor for the button
- 4 x 10Mohms resistors for apples
- 1 x 100pF capacitor for the apples
- 12V power supply for the illumination bulb
- 1 x connector for the power supply

##Soundcloud

Take a look on the [Tree_of_knowledge](http://soundcloud.com/tree_of_knowledge) soundcloud page for some sound samples.