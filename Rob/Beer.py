# -*- coding: utf-8 -*-

from time import sleep
import pyttsx
engine = pyttsx.init()

for x in range(100):
    y = str(99-x)
    z = str(98 - x)

    engine.say(y + " bottles of beer on the wall, " + y + " bottles of beer, now you’ve drunk one, there’s " + z + " bottles of beer. \n ")
    sleep(1)
engine.runAndWait()