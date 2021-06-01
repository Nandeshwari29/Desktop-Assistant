import ctypes
import os
import smtplib
import time
import webbrowser
import pyjokes as pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening ")
    speak("I am your Desktop Assistant. Please tell me how can I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('<enter-your-email-id>','<enter-the-password>')
    server.sendmail('<Enter-your-email-id>', to, content)
    server.close()

if __name__ == '__main__':
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia..")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                music_dir = '<Enter-the-path-of-your-music-directory>'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is{strTime}")

            elif 'open visual studio' in query:
                codePath = "<enter-the-path-of-your-application>"
                os.startfile(codePath)

            elif 'on youtube' in query:
                speak("Searching on Youtube")
                query = query.replace("play on youtube", "")
                webbrowser.open(query+"youtube.com")

            elif 'send email' in query:
                try:
                    speak("What should I say")
                    content = takeCommand()
                    to = "<Enter-receivers email>"
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend email has not been sent")

            elif 'joke' in query:
                speak(pyjokes.get_joke())


            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()


            elif "don't listen" in query or "stop listening" in query:
                speak("for how much seconds you want to stop Desktop Assistant from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)



            elif 'exit now' in query:
                    speak("Thank you sir!!! Hope you liked the services.")
                    exit()




