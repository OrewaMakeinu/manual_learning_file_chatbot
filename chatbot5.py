from gtts import gTTS

line1 = "mosi-mosh, Kyou wa nani o shimashou ka?"
line2 = "orewa hyuga hinata, yourashiku!"
line3 = "Summimasen, dou iu imi desu ka?"
tts1 = gTTS(text=line1,lang="ja")
tts2 = gTTS(text=line2,lang="ja")
tts3 = gTTS(text=line3,lang="ja")
stop_condition = False
while True:
    print("infinite loop begins.")
    user_text = input("text: ")
    if user_text=="Hi" or user_text=="hi":
        tts1.save("voice6.mp3")
    elif user_text=="Who are you?":
        tts2.save("voice7.mp3")
    elif user_text=="NAni desuka?":
        if stop_condition==True:
         

       print("Loading")
            break
    else:
        tts3.save("voice8.mp3")
print("code successfull")
