import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests



#creating recognizer class
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0bf8ef69787d4bc982836b4106650038"

def speak(text):
    engine.say(text)
    engine.runAndWait() # to stay for the output otherwise it will exit instant

#function for command
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linked in" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open you tube" in c.lower():
        webbrowser.open("https://youtube.com")
        #for playing song on youtube
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]       
        link = music_library.music[song]
        webbrowser.open(link)
        #for news article
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0bf8ef69787d4bc982836b4106650038")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])
            
            #Print the headlines
            for article in articles:
                speak(article['title'])
    
if __name__ == "__main__":
     speak("Initializing zarvis....")
     while True:
        #Listen for the wake word "Zarvis"
        #obtain audio from microphone
        r = sr.Recognizer()
         #timeout-> max no of sec within you have to speak something
            
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            print("recognizing...")
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))