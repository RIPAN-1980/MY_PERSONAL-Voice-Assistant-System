
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

#speak("Helo, This is Ripan Deb Nath. How can I help you?")


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
    
# Create Greetings:

def greeting():
    hour = (datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir. How are you? Zeni is here to assist you. Please tell How can I help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. How are you? Zeni is here to assist you. Please tell How can I help you?")
    else:
        speak("Good Evening Sir. How are you? Zeni is here to assist you. Please tell How can I help you?")  

greeting()    


#Continue Conversation Using Loops:

while True:
    query = takeCommand().lower()
    print(query)
    speak(query)

    if "your name" in query:
        speak("my name is Zeni")
        logging.info("User asked for name ")
    elif "how are you" in query:
        speak("I am fine, tell me what can I do for you?")
    elif "introduce" in query:
        speak("i am a Python-based voice assistant system that can interact with the users through speech recognition and i can help in some activity as i have been trained.")
    elif "time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S:")
        speak(f"The Curent time is {strtime}")
    elif "exit" in query:
        speak("Thank you Sir, Have a good time. I allways ready to help you.")
        logging.info("User exided the program")
        exit()
    else:
        speak("Sorry I Don't have any idea about it")
        logging.info("User asked for uslearned command")
    
