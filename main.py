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
import time
import wikipedia
import datetime 
import pyjokes
import wikiquotes


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

	elif 'the time' in command:
	        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
	        talk_to_me(f"The time is {strTime}")


	#elif 'wikipedia' in command:                                    #12345678
	elif re.search("tell me about|i want to know about",command):        
	        #command = command.replace("wikipedia", "")
	        #command = command.split(" ")[-1]
	        print("inside")
	        command = re.findall("tell me about|i want to know about ([a-zA-Z0-9])",command)
	        #print(command)
	        if len(command) > 1:
	        	command = " ".join(command)
	        #	print(command)
	        results = wikipedia.summary(command, sentences=2)
	        talk_to_me("According to Wikipedia" + results)
	        #print(results)
	        #talk_to_me(results)
	      
	elif 'joke' in command:
	        talk_to_me(pyjokes.get_joke())
	        
	        
	elif "where is" in command:                                  #12345678
	    command=command.replace("where is","")
	    location = command
	    talk_to_me("User asked to Locate"+location)

	    webbrowser.open("https://www.google.nl/maps/place/" + location + "")
	    
	    
	    
	elif 'qoute from ' in command:                   #command syntax : quote from <name of a famous person >
		command = command.replace("qoute from","")
	    talk_to_me(wikiquotes.random_quote(command, "english"))
	    
	elif 'news' in command:
	    webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
	    
	elif "country" in command:                      #command syntax : country <country name> 
	    command=command.split(" ")
	    name=CountryInfo(command[1])
	    talk_to_me(name.capital())                	

	elif("open website" in command):                 #command syntax : open website <website name>
		command = command.split(" ")
		webbrowser.open(url.format(command[2]))
		

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



	elif re.search(".*active|recovered|deaths|confirmed.*",command):
		type_c = re.findall(".*(active|recovered|deaths|confirmed).*",command)

		command = command.split(" ")
		if command[-1] == "world":

	 		x = covid.get_total_active_cases()
		else:

	 		x = covid.get_status_by_country_name(command[-1])
	 		x = x[type_c[0]]

		if type_c[0] == "deaths":
			talk_to_me(f"The  number of {type_c[0]} due to covid 19  in {command[-1]} are {x} ")
		else:
			talk_to_me(f"The  number of {type_c[0]} covid-19 cases in {command[-1]} are {x} ")

	
	else:	
				driver = webdriver.Chrome()
				driver.get("https://www.google.com/search?q="+ command)	

		

	

talk_to_me("I am Ready")

while(True):
	assistant(get_audio())

			



		











