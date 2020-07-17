import pyaudio
import os
import time
from gtts import gTTS
import playsound
import speech_recognition as sr
import sounddevice
import random
import sys
import smtplib
import webbrowser
from selenium import webdriver
import subprocess



chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
url = "https://www.{}.com"




def talk_to_me(text):

	r1 = random.randint(1,10000000)
	r2 = random.randint(1,10000000)
	filename = str(r2)+"audio"+str(r1)+".mp3"

	tts = gTTS(text = text , lang = "en-in")
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

	return said.lower()	
			

def assistant(command):
	if command in ["stop","terminate"]:
		talk_to_me("Ok")
		sys.exit()

	#if "google" in command:
	if command in ["browse the net","browse the internet"]:
		talk_to_me("What should i search for?")

		
		command = get_audio()
		while(True):
			if(command in ["backup","back up"]):
				talk_to_me("ok")
				break
			elif len(command) == 1:
				
				webbrowser.get("chrome").open(url.format(command))

			


			else:
				#webbrowser.get("chrome").open(command)
				if "new tab" in command:
					talk_to_me("ok")
					body = driver.findElement(By.cssSelector("body"))
					body.send_keys(Keys.CONTROL + 't')
				else:	
					talk_to_me(f"command recieved:{command}")
					driver = webdriver.Chrome()
					driver.get("https://www.google.com/search?q="+ command)
					

			talk_to_me("Ready for your next command")
			command = get_audio()		
		
			talk_to_me(f"command recieved:{command}")
		
	if command in ["open a program" , "execute a program"]:
		talk_to_me("Which one?")
		command = get_audio()
		if command == "notepad":
			subprocess.Popen("C:Windows\\system32\\notepad.exe")
		if command == "calculator":
			subprocess.Popen("C:Windows\\system32\\calc.exe")	
		if command == "sublime text":
			subprocess.Popen("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
		

	if "make a note" in command:
		talk_to_me("PLease give a suitable filename")
		command = get_audio()
		f_txt = command+".txt"
		talk_to_me("What should I write in it?")
		command = get_audio()
		with open(f_txt,"w") as obj:
			obj.write(command)
		talk_to_me("please check if it's  correct.")
		x = subprocess.Popen(["C:Windows\\system32\\notepad.exe",f_txt])
		command = get_audio()
		if "yes" in command:
			x.kill()




		

	

talk_to_me("I am Ready")

while(True):
	assistant(get_audio())

			



		












