import pyaudio
import os
import time
from gtts import gTTS
import playsound
import speech_recognition as sr
import sounddevice
import random

def speak(text):

	r1 = random.randint(1,10000000)
	r2 = random.randint(1,10000000)
	filename = str(r2)+"audio"+str(r1)+".mp3"
	tts = gTTS(text = text , lang = "en")
	tts.save(filename)
	

	playsound.playsound(filename)
	os.remove(filename)

def get_audio():
	r = sr.Recognizer()
	r.energy_threshold = 2200
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception" + str(e))

	return said		
			


speak("whats app")	
x = get_audio()
speak(x)
