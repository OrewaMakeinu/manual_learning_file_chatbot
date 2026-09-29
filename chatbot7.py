#Thala for a reason.
#Combining all the knowlegde got up untill now.

from gtts import gTTS
import speech_recognition as sr
stop_condition=False
recognizer = sr.Recognizer()

while True:
    print("Starts the infinite loop.")
    if stop_condition:
        break
    with sr.Microphone() as source:
        print("Listening:.... ")
        audio = recognizer.listen(source)
    try:
        user_text = recognizer.recognize_google(audio).lower()
        print("You said:", user_text)
    except Exception:
        print("couldn't get what you said")
        continue

    if "how r u" in user_text:
        reply="I am fine,thank you for asking."
        print(reply)
        tts1 = gTTS(text=reply,lang="en")
        tts1.save("voice9.mp3")
    elif user_text=="are you hinata":
        reply="Yes, I am Hinata"
        tts2 = gTTS(text=reply,lang="en")
        tts2.save("voice10.mp3")
    else:
        print("can't accept your request.")
print("code successfull.")
