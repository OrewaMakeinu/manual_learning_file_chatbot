from gtts import gTTS
from google import genai
import pygame
import speech_recognition as sr
import time

recognizer=sr.Recognizer()
client=genai.Client(api_key=" ")
pygame.mixer.init()

while True:
    print("Starts the infinite loop")

    with sr.Microphone() as source:
        print("Listening:......")
        audio = recognizer.listen(source)
    try:
        user_text = recognizer.recognize_google(audio).lower()
        print("You said: ",user_text)
    except Exception:
        print("Can't get what you said")
        continue
    if user_text=="exit":
        print("GoodBye")
        break
    bot_reply=client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_text
    ).text
    tts=gTTS(text=bot_reply,lang="en")
    tts.save("voice12.mp3")
    pygame.mixer.music.load("voice12.mp3")
    pygame.mixer.music.play("voice12.mp3")
    print("saved successful")
print("code successfull")