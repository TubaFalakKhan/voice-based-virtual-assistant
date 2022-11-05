import speech_recognition as sr  
from PyQt5.QtWidgets import *
import front
import bot
import pyttsx3
import sys
import datetime
from features import searchanythingongoogle
import re

#below is for initializing package pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#printing current volume level
print (volume)
voices = engine.getProperty('voices')
#in below line we are setting the voice of assistant as female
engine.setProperty('voice', voices[1].id)                  
# get audio from the microphone                                                             
r = sr.Recognizer()                                                                                   
 
# try:
#     print("You said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

def startup():
    engine.say("Initializing Jarvis")
    engine.say("Checking the internet connection")
    engine.say("Wait a moment Mam")
    engine.say("All systems have been activated")

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        engine.say("Good Morning")
    elif 12 < hour < 18:
        engine.say("Good afternoon")
    else:
        engine.say("Good evening")
    # c_time = obj.tell_time()
    # engine.say(f"Currently it is {c_time}")
    engine.say("I am Jarvis. Online and ready Mam. Please tell me how may I help you")

class MainThread(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = front.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_15.clicked.connect(self.TaskExecution)
        self.ui.pushButton_11.clicked.connect(self.bot_window)
        self.ui.pushButton_9.clicked.connect(self.usr_win)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def usr_win(self):
        engine.say("This Feature is not available yet")

    def bot_window(self):
        self.jar = front.Sub_Window()
        self.jar.show()
        engine.say("After Making Change I Recommand you to restart Me")

    def TaskExecution(self):
        self.ui.label_2.setText("Listening...")
        if True:
            with sr.Microphone() as source:                                                                       
                print("Speak:")                                                                                   
                audio = r.listen(source)
                command = r.recognize_google(audio, language='en-in').lower()
            
                self.ui.textEdit.append("you:" + command)
                if re.search("search for",command):
                    searchanythingongoogle.google_search(command)
                    self.ui.textEdit.append("jarvis: "+res)
                ints = bot.predict_class(command)
                res = bot.get_response(ints, bot.intents)
                print(res)
                engine.say(res)
                engine.runAndWait()
                self.ui.textEdit.append("jarvis: "+res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = MainThread()
    jarvis.show()
    startup()
    wish()
    engine.runAndWait()
    exit(app.exec_())

  