from gtts import gTTS
from google import genai
import speech_recognition as sr
import pygame
import time

recognizer=sr.Recognizer()
client=genai.Client(api_key="")
pygame.mixer.init()
timestamp=time.time()
print(timestamp)
stop_condition=False
while True:
    print("Starts the infinite loop")
    if stop_condition:
        break
    with sr.Microphone() as source:
        print("Listening:....")
        audio=recognizer.listen(source)
    try:
        user_text=recognizer.recognize_google(audio).lower()
        print("You said: ",user_text)
    except Exception:
        print("can't get what you said")
        continue
    if user_text=="exit":
        print("GoodBye")
        break

    bot_reply=client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_text
    ).text
    tts1=gTTS(text=bot_reply,lang="en")
    tts1.save("voice13.mp3") 
    pygame.mixer.music.load("voice13.mp3")
    pygame.mixer.music.play("voice13.mp3")
    print("saved successfull")
print("code successful")

