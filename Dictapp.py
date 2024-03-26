import os
import  pyautogui#buy this we can press any key in keyboard with python
import  webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")#by this engine in this project is defined
voices = engine.getProperty("voices")
engine.setProperty("voice" ,voices[0].id)#this is the voice that exist in our sytem as default adn from them we are using the 0th index voice
engine.setProperty("rate" , 170)
    

#this is the function for speak command 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dictapp = { "commandpromt" : "cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("launching sir")
    if ".com" in query or".co.in" in query or ".org" in query:#if any web has to be opened then this logic will go on
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
        
    else:
        keys = list(dictapp.keys())#if any web app that is in system has to be open then this ogic will be executed 
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")# there should be space in commands as start winword would work instead of startwinword 
    
def closeappweb(query):
    speak("closing,sir")
    if"one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
        
    elif"2 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
        
    elif"3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
        
    elif"4 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
        
    elif"5 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs are closed")
        
    else:
        #it is for opening the appin our pc
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im{dictapp[app]}.exe")
    
       
        