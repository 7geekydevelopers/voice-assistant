import os
from gtts import gTTS
import playsound
import speech_recognition as sr
import random
import sys
import webbrowser
from selenium import webdriver
import subprocess
from covid import Covid
import regex as re





chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
url = "https://www.{}.com"

covid = Covid(source="worldometers")




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
			said = r.recognize_google(audio , language = "en-in")
			print(said)
		except Exception as e:
			print("Exception" + str(e))

	return said.lower()	
			

def assistant(command):
	if re.search(".*terminate|stop|bye|see you later|rest|deactivate.*",command):
		talk_to_me("Ok")
		sys.exit()

	elif("open website" in command):
		command = command.split(" ")
		webbrowser.get("chrome").open(url.format(command[2]))
		

	elif re.search(".*notepad.*",command):
		subprocess.Popen("C:Windows\\system32\\notepad.exe")
	elif re.search(".*calculator.*",command):
		subprocess.Popen("C:Windows\\system32\\calc.exe")	
	elif re.search(".*sublimetext.*",command):
		subprocess.Popen("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
		

	elif re.search(".*note.*",command):
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
		if re.search(".*yes|yep.*",command):
			x.kill()
		elif re.search(".*no|not|wrong.*",command):
			talk_to_me("Please make the necessary changes in it")



	elif re.search(".*active.*",command):
		x = covid.get_total_active_cases()
		talk_to_me(f"The  number of active covid-19 cases  are {x} ")

	elif re.search(".*confirmed.*",command):
		x = covid.get_total_confirmed_cases()
		talk_to_me(f"The  number of confirmed covid-19 cases are {x} ")	

	elif re.search(".*recovered|recoveries.*",command):
		x = covid.get_total_recovered()
		talk_to_me(f"The  number of recovered covid-19 cases  are {x} ")

	elif re.search(".*deaths.*",command):
		x = covid.get_total_deaths()
		talk_to_me(f"The  number of deaths due to  covid-19 are {x} ")

	else:	
				driver = webdriver.Chrome()
				driver.get("https://www.google.com/search?q="+ command)	

		

	

talk_to_me("I am Ready")

while(True):
	assistant(get_audio())

			







