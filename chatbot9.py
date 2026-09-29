from google import genai
from gtts import gTTS
import speech_recognition as sr

stop_condition=False
recognizer=sr.Recognizer()
client=genai.Client(api_key=)

while True:
    print("starts the infinite loop")
    if stop_condition:
        break
    with sr.Microphone() as source:
        print("Listening:....")
        audio=recognizer.listen(source)
    try:
        user_text=recognizer.recognize_google(audio).lower()
        print("You said: ", user_text)
    except Exception:
        print("can't hear you.")
        continue
    bot_reply=client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_text
    )
    tts=gTTS(text=bot_reply,lang="ja")
    tts.save("voice12.mp3")
    if user_text=="exit":
        print("Goodbye")
        stop_condition=True
        break
print("Code Successfull")


    