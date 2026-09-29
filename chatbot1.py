from gtts import gTTS

line = "Morning Everyone."

tts = gTTS(text=line, lang="en")

tts.save("voice1.mp3")

print("Saved Successfully")

