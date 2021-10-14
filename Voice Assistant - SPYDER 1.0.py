#Import all required libraries
import speech_recognition as sr  #performing speech recognition
import pyttsx3  #Text to Speech library
import datetime  #showing Date and Time.
from datetime import date
import time
import wikipedia #to get information from Wikipedia or to perform Wikipedia search
import webbrowser #to extract data from the web.
#webbrowser.open('https://www.python.org')
import os #provides the function to interact with operating system
import subprocess #to process various system commands like to log off or to restart your PC.
from ecapture import ecapture as ec #to capture images from webcam.
import wolframalpha #to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology.
import json
import requests #to send all types of HTTP request. Its accepts URL as parameters and gives access to the given URL’S.
import pyjokes #Jokes
from bs4 import BeautifulSoup #to scrape information from web pages
import shutil #offers a number of high-level operations on files and collections of files
import winshell
import pyowm #OpenWeatherMap Web API
import pyautogui #control mouse & Keyboard
import ctypes

engine = pyttsx3.init('sapi5')
#Sapi5 is a Microsoft Text to speech engine used for voice recognition
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def userName():
    #speak("What should i call you sir")
    #user_name = takeCommand()
    user_name = "Subhajit"
    speak("Welcome Mister")
    speak(user_name)
    print("Welcome Mr.", user_name)
    speak("How can i Help you, Sir")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Pardon me, please say that again")
        return "None"
    return query
print("Loading your AI personal assistant...")
speak("Loading your AI personal assistant")
asst_name = ("SPYDER 1 point 0")
speak("I am your Assistant")
speak(asst_name)
print("I am your Assistant, SPYDER 1.0")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    # This Function will clean any command before execution of this
    clear()
    wishMe()
    userName()
    while True:
        query = takeCommand().lower()
        # All the commands said by user will be stored here in 'query' and will be
        # converted to lower case for easily recognition of command
        if 'wikipedia' in query:
            speak("About what's topic ?")
            topic_name = takeCommand()
            speak('Searching Wikipedia...')
            query = topic_name
            results = wikipedia.summary(query, sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'search' in query:
            query = query.replace("search", "")
            statement = "https://www.google.com/search?q="+query
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(statement)
            time.sleep(5)
        elif 'news' in query:
            newsURL= "https://timesofindia.indiatimes.com/home/headlines"
            news = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(newsURL)
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif "weather" in query:
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            city_name = takeCommand()
            API_KEY = "My API_KEY"
            # upadting the URL
            URL = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=metric"
            # HTTP request
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                # getting the main dict block
                main = data['main']
                # getting temperature
                temperature = main['temp']
                # getting the humidity
                humidity = main['humidity']
                # weather report
                report = data['weather']
                print(f"{city_name:-^30}")
                print(f"Temperature: {temperature}°C")
                speak(f"the temparature at {city_name} is {temperature}°C")
                print(f"Humidity: {humidity}%")
                speak(f"and the humidity at {city_name} is {humidity}%")
                print(f"Weather Report: {report[0]['description']}")
                speak(f"and the overall weather condition at {city_name} is {report[0]['description']}")
            else:
                # showing the error message
                print("Error in the HTTP request")
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "My APP_ID"
            client = wolframalpha.Client('My APP_ID')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'find my location' in query:
            app_id = "My APP_ID"
            client = wolframalpha.Client('My APP_ID')
            res = client.query(query)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif "calculate" in query:
            app_id = "My APP_ID"
            client = wolframalpha.Client('My APP_ID')
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "today's date" in query or "date" in query:
            today = date.today()
            speak("Today's date")
            speak(today)
            print("Today's date:", today.strftime("%b %d, %Y"))
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print("The time is ", strTime)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("youtube.com")
            time.sleep(5)
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("google.com")
            time.sleep(5)
        elif 'open github' in query:
            speak("Here you go to Github\n")
            search_URL="https://github.com/Subhajit419"
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(search_URL)
        elif 'open gmail' in query:
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open google chrome' in query or 'open googlechrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome"
            os.startfile(codePath)
        elif 'open settings' in query or 'settings' in query:
            pyautogui.hotkey("win", "i")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            cond = takeCommand()
            if "yes" in cond or "fine" in cond:
                speak("Ok, Sir")
            else:
                speak("What can I do for you ?")
        elif "what's your name" in query or "What is your name" in query:
            speak("You can call me")
            speak(asst_name)
            print("You can call me", asst_name)
        elif "spyder" in query or "spider" in query:
            wishMe()
            speak("SPYDER 1 point o in your service Sir")
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am SPYDER version 1 point O your personal assistant. I am programmed to perform minor tasks like'
                  'opening youtube,google, github, gmail, predict time, take photo, screenshot, search wikipedia,'
                  'predict weather in different cities, get top headline news from times of india and you can ask me '
                  'computational or geographical questions too!')
        elif "goodbye" in query or "okbye" in query or "stop" in query or "exit" in query or "ok bye" in query or "good bye" in query:
            speak('your personal assistant SPYDER is shutting down,Good bye')
            print('your personal assistant SPYDER is shutting down,Good bye')
            break
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Subhajit Paul.")
        elif 'joke' in query:
            speak(pyjokes.get_joke(language="en", category="all"))
            print(pyjokes.get_joke(language="en", category="all"))

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, False, "img.jpg")
        elif "screenshot" in query or "take a screenshot" in query:
            #pyautogui.screenshot(r"F:\Subhajit Paul\Pictures\screenshot1.png")
            pyautogui.hotkey("win", "prtsc")

        elif 'empty recycle bin' in query or 'recyclebin' in query or 'recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")
        elif "refresh" in query:
            pyautogui.click(button='right')
            pyautogui.press('down', presses=3)
            pyautogui.press('enter')

        elif "restart" in query:
            speak("Ok, your laptop is ready to restart")
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "hybernet" in query:
            speak("Ok, your laptop is going to be in hibernate mode")
            subprocess.call(["shutdown", "/h"])
        elif "logoff" in query or "signout" in query or "shutdown" in query:
            speak("Ok , your laptop will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif "sleep" in query:
            speak("Ok, your laptop is going to be in sleep mode")
            pyautogui.hotkey("alt", "f4")
            pyautogui.press('up')
            pyautogui.press('enter')
        elif "lock" in query or "lock my laptop" in query:
            speak("Ok, your laptop is going to be locked")
            ctypes.windll.user32.LockWorkStation()


