import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ssl

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Merlin, Sir, Madam. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            webbrowser.open("https://www.google.com/")

        elif "open stack overflow" in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif "play music" in query:
            music_dir = "./Music"
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in the specified directory.")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "D:\ASSIGNMENT SET 1\PATTERN1.exe"
            os.startfile(codePath)


        elif "bye" in query:
            speak("Goodbye, Sir,Madam! Have a nice day😊")
            break

        else:
            speak("No query matched. Please try again.")
