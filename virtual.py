import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import uuid
import time
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("jhony jhony yes papa!")
        audio = r.listen(source,phrase_time_limit=5)
    data=""
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you speak louder")
    except sr.RequestError as e:
        print("Microphone is not working")
    return data
    '''tts=gTTS(data)
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
listen()'''
def respond(String):
    tts=gTTS(text=String)
    tts.save("Speech.mp3")
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def virtual_assistant(data):
    if 'how are you' in data:
        listening=True
        respond("I am good thank you")
    elif "time" in data:
        listening=True
        respond(time.ctime())
    elif "you thinking" in data:
        listening=True
        respond("Yes about the weekend plan")
    elif "open google" in data.lower():
        listening=True
        url='https://www.google.com/'
        webbrowser.open(url)
        respond("Success")
    elif "stop talking" in data:
        listening=False
        repond("Okay take care")
    try:
        return listening
    except:
        print("Stopped")
respond("Hey codegnan this is your assistant")
listening=True
while listening==True:
    data=listen()
    listening=virtual_assistant(data)
    
         
        

