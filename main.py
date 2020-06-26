#Steven 06/25/2020 simple chatbot 
#pip install pyttsx3
#pip install SpeechRecognition
#pip install pywin32
#pip install PyAudio
#pip install chatterbot
#pip install chatterbot-corpus
#pip install PyYaml

import pyttsx3
import speech_recognition as sr
from chatbot import createBot,getResponse

def speak(text):
	engine = pyttsx3.init()
	engine.setProperty('rate',150)
	engine.setProperty('voice','en+m7')
	engine.say(text)
	engine.runAndWait()	

def get_voice():
	r=sr.Recognizer()
	print("Listening.....")
	with sr.Microphone() as source:
		audio = r.listen(source)
		said=""
		#print("loading.....")
		try:
			said = r.recognize_google(audio)
		except:
			pass
	
	return said.lower()

def get_data(text):
	text = text.lower()	
	for word in text.split():
		#print(word)
  		pass
	print('Get your voice:',text)

def mainloop(BYE):
	while True:
		text = get_voice()
		if text != '':
			print('your said:',text)
			speak(text)

			if text.count(BYE) > 0:
				break
		else:
			continue

def mainloopBot(BYE,chatbot):
	while True:
		text = get_voice()

		if text != '':
			if text.count(BYE) > 0:
				break

			print('your said:',text)
			response = chatbot.get_response(text)
			print('response:',response)
			speak(response)
		else:
			continue
  
def main():
	chatbot = createBot()

	speak("Hi, I am your voice assistant. Made by StevenHuang")
	speak("Please say 'Hello' to wake me up")
	speak("Please say 'Goodbye' to make me sleep")

	WAKE = "hello"
	BYE = "bye"

	text = get_voice()
	if text.count(WAKE) > 0:
		speak("I am ready")
		#mainloop(BYE)
		mainloopBot(BYE,chatbot)
	else:
		speak(text)
	
	speak("Good bye!")
 
if __name__=='__main__':
    main()
    