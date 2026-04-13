import os
import pyttsx3
def falar(texto):
    motor = pyttsx3.init()
    motor.say(texto) 
    motor.runAndWait()
falar("Oi")

motor = pyttsx3.init()
motor.s
