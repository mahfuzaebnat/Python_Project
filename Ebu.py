import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pywhatkit
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    
    elif hour>=19 and hour<22:
        speak("Good Evening!!")   

    else:
        speak("Good Night")  
    
    speak("I am Ebu. Please tell me how may I help you")  
    
    print("\nYou want search wikipedia,Please say 'Tell me about ... ...'" )   
    print("\nYou want open google brawser,Please say 'open google'" ) 
    print("\nYou want open google brawser,Please say 'open google'" )    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...\n")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'tell me about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'play music' in query:
            music_dir = query.replace('play music', '')
           
            pywhatkit.playonyt(music_dir)
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S ") 
            print("Now time is "+strTime)
            speak(f"Now time is {strTime}")
            