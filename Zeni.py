
import speech_recognition as sr 
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess


# Logging configuration 

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

# ACTIVATE VOICE PROPERTY (PYTTSX3)

engine = pyttsx3.init("sapi5") 
voices  = engine.getProperty("voices") 
#voice = voices 
#print(voice) 
#print(voice[2].id) 
engine.setProperty('voice' , voices[2].id)
engine.setProperty('rate', 170) 


# Creating Speak Function

def speak(text):
    """ this function converts text to voice
        Args:
            text
        returns:
            voice
    """

    engine.say(text)
    engine.runAndWait()

speak("Helo, This is Ripan Deb Nath. How can I help you?")


# Recognizing user spech to Text:

def takeCommand():
    """This function can take command from users & can recognize

    Returns:
        text as query
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeninh.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        # Exception Hendeling
        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")                               

        except Exception as e:
            logging. info(e)
            print(" Please Speak Again....")
            return "None"
        
        return query
    
query = takeCommand()
print(query)


