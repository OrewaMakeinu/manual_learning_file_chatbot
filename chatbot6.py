#The basic syntax of the speech recognition library.
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening:....... ")
    audio = recognizer.listen(source)

try:
    user_text = recognizer.recognize_google(audio)
    print("You said:",user_text)
except:
    print("couldn't get what you said")