# Voice Assistant GENNADIY v2.0 beta

import speech_recognition as sr 
from brain import Assistant

assist = Assistant()

# obtain audio from the microphone
m = sr.Microphone(device_index=1)

# hello user
assist.speak("Привет Юджин! Гена на связи!")

# execute commands
while True:
    assist.execute(m)