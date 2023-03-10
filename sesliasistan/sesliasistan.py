import speech_recognition as sr
from datetime import datetime 
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):

   with sr.Microphone() as source:
        if ask:
            speak(ask)

        audio = r.listen(source)
        voice = ''
        try:
           voice = r.recognize_google(audio , language = 'tr-TR')
        except sr.UnknownValueError:
            speak("Anlayamadım. Lütfen tekrar eder misin?")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")    
        return voice

def response(voice):
    if "Nasılsın." in voice:
        speak("İyiyim. Sen nasılsın?")
    if "Saat kaç?" in voice:
        speak(datetime.now().strftime("%H:%M:%S"))
    if "Arama yap." in voice:
        search = record("Ne aramak istiyorsun?")
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım.")
    if "Tamamdır.." in voice:
        speak("Görüşürüz. Kendine iyi bak..")
        exit()
    

def speak(string):
   tts =  gTTS(string,lang='tr-TR')
   rand = random.randint(1,1000)
   file = 'audio-'+str(rand)+'.mp3'
   tts.save(file)
   playsound(file)
   os.remove(file)


speak("Nasıl yardımcı olabilirim ?")
time.sleep(1)
while 1:
   voice = record()
   print(voice)
   response(voice)
