#function to accept audio input from user#

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        
        try:
            said=r.recognize_google(audio)
            print(said)
            
        except Exception as e:
            print("Exception: "+str(e))
            
    return said
#get_audio()


#function to convert text_to_speech#

def speak(text):
    tts=gTTS(text=text,lang="en-in")
    filename="voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



#Voice_assistant skills#

time.sleep(2)
speak("Hi Rohit what can i do for you?")
while True:
        query = get_audio().lower()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open youtube' in query:
            speak("Please hold on, i am opening youtube")
            webbrowser.open("https://www.youtube.com/")
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        
        elif 'notepad' in query:
            speak('Done for you sir.')            
            os.system('notepad')
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
            
        elif "where is" in query:
            query=query.replace("where is","")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
            
            
        elif 'wiki' in query:
            speak(wikiquotes.random_quote("gandhi", "english"))
            
        elif 'news' in query:
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            
        elif "country" in query:
            query=query.split(" ")
            name=CountryInfo(query[1])
            speak(name.capital())
            
            
            
        elif "covid" in query:
            name=Covid()
            a=str(name.get_total_active_cases())
            b=str(name.get_total_confirmed_cases())
            c=str(name.get_total_recovered())
            d=str(name.get_total_deaths())
            speak("The active cases are {}. The total confirmed cases are {}. The total recovered patients are {}. The total number of deaths are {}".format(a,b,c,d))
                
            
            
                    
        elif 'bye' in query:
            speak('see you later sir.Have a nice day')
    
        else:
            break
