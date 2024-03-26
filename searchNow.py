import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

query = takeCommand().lower()
engine = pyttsx3.init("sapi5")#by this engine in this project is defined
voices = engine.getProperty("voices")
engine.setProperty("voice" ,voices[0].id)#this is the voice that exist in our sytem as default adn from them we are using the 0th index voice
engine.setProperty("rate" , 170)


#this is the function for speak command 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def searchGoogle(query):
    if"google" in query:
        import wikipedia as googleScrap
        query = query.replace("google" ,"")
        query = query.replace("google search " ,"")
        query = query.replace("jarvis" ,"")
        speak("this is what is found in google")
        
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
            
        except:
            speak ("NO speakable output available ")
            
def searchYoutube(query):
    if "youtube" in query:
        speak("this is what i found in you tube search!")
        query = query.replace("youtube search" ,"")
        query = query.replace("youtube" ,"")
        query = query.replace("jarvis" ,"")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done, sir")  
        
def searchWikipedia(query):
    if"wikipedia" in query:
        speak("searching from wikipedia.....")  
        query =query.replace("wikipedia","") 
        query =query.replace("jarvis","") 
        query =query.replace("search wikipedia","") 
        results = wikipedia.summary(query,sentences =2 ) #wikipedia summary is initialised as the rsult
        speak ("accordiing to wikipedia ..")
        print(results)
        speak(results)                       

