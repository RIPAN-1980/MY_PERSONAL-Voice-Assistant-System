
import speech_recognition as sr 
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai



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


def gemini_model_response(user_input):
    GEMIMI_API_KEY = "AIzaSyCkYYqV8KMzbC8Rnw2ygR6qkLV6Nmf7j-8"
    genai.configure(api_key= GEMIMI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Answer the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result =  response.text

    return result


#Continue Conversation Using Loops:

while True:
    query = takeCommand().lower()
    print(query)
    # speak(query)

    if "your name" in query:
        speak("my name is Zeni")
        logging.info("User asked for name ")

    elif "how are you" in query:
        speak("I am fine, tell me what can I do for you?")

    elif "introduce" in query:
        speak("i am a Python-based voice assistant system that can interact with the users through speech recognition and i can help in some activity as i have been trained.")
        logging.info("User asked for introduction")

# Asking for time:

    elif "time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S:")
        speak(f"The Curent time is {strtime}")
        logging.info("User asked for time")

# Open Google:

    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")   

# Open Youtube:

    elif "open youtube" in query:
        speak("ok sir. please type here what do you want to watch")
        webbrowser.open("youtube.com")
        logging.info("User requested to open YouTube.")

# Open Github:

    elif "open github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")

# Open facebook:

    elif "open facebook" in query:
        speak("Opening Facebook")
        webbrowser.open("facebook.com")
        logging.info("User requested to open Facebook")

# Open Calendar:

    elif "open calendar" in query or "calendar" in query:
        speak("Opening Windows Calendar")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open Calendar.")

# Open Gmail:

    elif "open gmail" in query:
        speak("Opening Gmail")
        webbrowser.open("gmail.com")
        logging.info("User requested to open Gmail")

# Open Calculator:

    elif"open calculator" in query:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open Calculator")

# Open Notepad:

    elif"open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad")

# Open Command Prompt:

    elif"open command prompt" in query:
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
        logging.info("User requested to open Command Prompt")

# Wikipedia Search:

    elif"wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        logging.info("User searched information from Wikipedia")

# Play Music:

    elif "play music" in query:
        music_dir = "E:\Backup 2020\Video"
        songs = os.listdir(music_dir)
        print(songs)
        random_song = random.choice(songs)
        os.startfile(os.path.join(music_dir, random_song))
        speak("Playing Music")
        logging.info("User requested to play music")

# Exit Command:

    elif "exit" in query:
        speak("Thank you Sir, Have a good time. I allways ready to help you.")
        logging.info("User exided the program")
        exit()

    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("User asked for ai based question")


## Activateing Gemini API Model:

# GEMIMI_API_KEY = "AIzaSyCkYYqV8KMzbC8Rnw2ygR6qkLV6Nmf7j-8"
    
# genai.configure(api_key= Gemini_API_KEY)

# model = genai.GenerativeModel("gemini-2.5-flash")

# user_input = "What is python?"
# response = model.generate_content(user_input)
# print(response)
