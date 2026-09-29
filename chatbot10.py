from gtts import gTTS
import speech_recognition as sr
from google import genai
import pygame
import time

recognizer=sr.Recognizer()
client=genai.Client(api_key=)
pygame.mixer.init()


while True:
    print("starts the infinite loop")
    
    with sr.Microphone() as source:
        print("Listening:......")
        audio = recognizer.listen(source)
    try:
        user_text = recognizer.recognize_google(audio).lower()
        print("You said: ", user_text)
    except Exception:
        print("can't get what you said")
        continue
    if user_text=="exit":
                print("Goodbye!")
                break
    
    bot_reply=client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_text
    ).text
    tts=gTTS(text=bot_reply,lang="en")
    tts.save("voice11.mp3")
    pygame.mixer.music.load("voice11.mp3")
    pygame.mixer.music.play("voice11.mp3")
    print("saved successfull")
    
print("code successfull")

# from google import genai
# client=genai.Client(api_key="")
# for model in client.models.list():
#     print(model.name)
