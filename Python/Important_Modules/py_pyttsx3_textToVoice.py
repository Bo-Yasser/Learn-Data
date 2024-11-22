

import pyttsx3

engine = pyttsx3.init()
say = input("Write Any Thing: ")
engine.say(say)
engine.runAndWait()
