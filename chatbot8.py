from gtts import gTTS
import speech_recognition as sr
from google import genai

stop_condition=False
recognizer=sr.Recognizer()
client=genai.Client(api_key=)

while True:
    print("starts the infinite loop")
    if stop_condition:
        break
    with sr.Microphone() as source:
        print("Listening:......")
        audio = recognizer.listen(source)
    try:
        user_text = recognizer.recognize_google(audio).lower()
        print("You said: ", user_text)
    except Exception:
        print("can't get what you said")
        continue
    bot_reply=client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_text
    ).text
    tts=gTTS(text=bot_reply,lang="en")
    tts.save("voice11.mp3")
    if user_text=="exit":
        print("Goodbye!")
        stop_condition=True
        break

    
print("code successfull")

# from google import genai
# client=genai.Client(api_key="")
# for model in client.models.list():
#     print(model.name)
