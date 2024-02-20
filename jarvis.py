import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__== "__main__":
     speak("mahnoor is a good girl")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("good morning")
    elif hour>=12 and hour<18:
         speak("good evening")
         speak("i am jarvis how may i help you?")
    else:
        speak("Good Night!")
"""def takeCommand():
             r=sr.Recognizer()
             with sr.Microphone() as source:
                 print("Listening...")
                 r.pause_threshold=2
                 audio=r.listen(source)

             try:
                print("Recognizing...")     
                query= r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")   
             except Exception as e:
                 print("say that again please...")
                 return "None"       
             return query"""   
 

      
if __name__== "__main__":
       wishMe()
       
       
