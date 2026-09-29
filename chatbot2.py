from gtts import gTTS

line = "OHAYO minna"

tts = gTTS(text=line , lang="ja")

tts.save("voice2.mp3")

print("saved successfully")