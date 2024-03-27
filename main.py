import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup 
import datetime
engine = pyttsx3.init("sapi5")#by this engine in this project is defined
voices = engine.getProperty("voices")
engine.setProperty("voice" ,voices[0].id)#this is the voice that exist in our sytem as default adn from them we are using the 0th index voice
engine.setProperty("rate" , 170)
    

#this is the function for speak command 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 #this is the function for take the user input    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
            print ("listening.....")
            r.pause_threshold =1 # this is the 1 sec pause that the systen will take after listening 
            r.energy_threshold =300   #it means that engine will cath the voice with frequency of 300 
            audio = r.listen(source,0,4)
    
    try:
        print("understanding.....")
        query =r.recognize_google(audio, language ='en-in')
        #query is been created here 
        print(f"you said: {query}\n") 
    except Exception as e:
        print("say that again")
        return "none"
    return query
#these are the communication that will happen as we stated 
if __name__ == "__main__":#main function start here 
    while True:
        query = takeCommand().lower()# it convert the qurey in lower case
        if"wake up" in query: #if we say this then the system will wake up and will start the "greetME" file method 
            from greetMe import greetMe
            greetMe()       
            
            while True :
                query = takeCommand().lower()# using this the syatem will listen but will not responde
                if"sleep"   in query:
                    speak ("OK sir , you can call me anytime")
                    break
            #this is the talk that the program is going to do with us  we can add as many conversation as we want      
                elif"hello" in query:
                    speak("hello sir, how are you")
                elif"i am fine " in query:
                    speak("that's great sir")
                elif"how are you" in query:
                    speak("i am great too sir")
                elif"thank" in query:
                    speak("welcome sir")
                
                #here start the searchine from the internet code so that engine can open websites or google 
                elif "open" in query:
                    from Dictapp import openappweb  
                    openappweb(query)
                elif"close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                         
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif"youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif"wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
               #this one is not working     
                elif "temerature" in query:
                    search ="temeprature in delhi"
                    url =f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ ="BNeawe").text
                    speak(f"curent{search} is {temp}")
              #this is properly working  for weather       
                elif "weather" in query:
                    search ="temeprature in delhi"
                    url =f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ ="BNeawe").text
                    speak(f"curent{search} is {temp}")
                #this part is used to make engine speak
                elif"the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif"finally sleep" in query:
                    speak("going to sleep,sir")
                    exit()