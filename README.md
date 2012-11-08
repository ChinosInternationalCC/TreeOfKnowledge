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

###Record

###Playback
