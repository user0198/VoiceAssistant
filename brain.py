import speech_recognition as sr 
import pyttsx3
import datetime
import time
import webbrowser

from fuzzywuzzy import fuzz
from options import *

# assistant brain 
class Assistant(object):
    
    opt = Options()
    
    # init text-to-speech conversion lib
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    
    # get audio
    def __callback(self, recognizer, audio):
        try:
            __voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
            print("[log] Recognized: " + __voice)

            if __voice.startswith(self.opt.options["alias"]):
                # talk to assistant
                cmd = __voice

                for x in self.opt.options['alias']:
                    cmd = cmd.replace(x, "").strip()

                for x in self.opt.options['remove']:
                    cmd = cmd.replace(x, "").strip()
                
                cmd = self.__recognize_cmd(cmd)
                self.__execute_cmd(cmd['cmd'])

            else: print("[log] Not alias")

        except sr.UnknownValueError:
            print("[log] Voice is not recognized!")
        except sr.RequestError:
            print("[log] Unknown error!")

    # string matching
    def __recognize_cmd(self, cmd):
        __RC = {'cmd': '', 'percent': 0}
        for c,v in self.opt.options['cmds'].items():

            for x in v:
                tmp = fuzz.ratio(cmd, x)
                if tmp > __RC['percent']:
                    __RC['cmd'] = c
                    __RC['percent'] = tmp

        return __RC

    # convert cmd into an action
    def __execute_cmd(self, cmd):
        if cmd == "ctime":
            # current time
            now = datetime.datetime.now()
            self.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        elif cmd == "hello":
            self.speak("Привет привет")
        elif cmd == "name":
            self.speak("Меня зовут Геннадий. Но Вы можете меня называть как угодно")
        elif cmd == "fact":
            self.speak("Тараканы могут задержывать дыхание на 40 секунд!")
        elif cmd == "joke":
            self.speak("Пожар на складе огнетушителей собрал толпу любителей иронии!")
        elif cmd == "whatsup":
            self.speak("Лучше всех!") 
        elif cmd == "youtube":
            self.speak("Открываю")
            webbrowser.open_new("http://youtube.com")
        elif cmd == "google":
            self.speak("Открываю")
            webbrowser.open_new("http://google.com")
        elif cmd == "thankyou":
            self.speak("Всегда пожалуйста")
        elif cmd == "bye":
            self.speak("всего хорошего!")
            exit()   
        
        else:
            print("Cannot identify command!")
    
    # makes assistant speak
    def speak(self, what):
        print(what)
        self.engine.say(what)
        self.engine.runAndWait()
        self.engine.stop() 

    # execute assistant
    def execute(self, microphone):
        recognizer = sr.Recognizer()
        
        with microphone as source:
            print("Ready for your command!")
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=1)  # listen to background
            audio = recognizer.listen(source)
        
        # call recognition fucn
        self.__callback(recognizer, audio)