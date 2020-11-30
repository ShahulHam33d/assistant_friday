import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newvoicerate=145#to set 135 words per minute
engine.setProperty("rate",newvoicerate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("good morning boss")

    elif hour>=12 and hour <18:
        speak("goodafternoon boss")
    else:
        speak("goodevening boss")

    speak("i am friday. how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        sr.pause_threshold = 1
        #r.energy_threshold=3500
        #r.adjust_for_ambient_noise(source,duration=0)
        audio = r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio)
        print(f"user said: {query}\n")


    except Exception as e:
        print("say that again please...")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if "hello friday" in query:
            speak("hello sir")

        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "stackover flow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir="D:\\music\\Hindi songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%m:%S")
            speak(f"sir, the time is:{time}\n")

        elif "thank you" in query:
            speak("your welcome")





