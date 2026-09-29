#Final Part of Phase1 Learning of my chatbot journey , i made a simple text to speech code by myself.
from gtts import gTTS

line1 = "Hello,What can i do for you today?"
line2 = "sorry, didn't know what you mean?"
tts1= gTTS(text=line1+line2,lang="en")
#tts2 = gTTS(text=line2,lang="en")
stop_condition=False

while True:
    print("Infinte loop begins")
    user_Text = input("text: ")
    if user_Text == "hi":
        tts1.save("voice4.mp3")
    elif user_Text == "bye":
        stop_condition=True
        if stop_condition==True:
            tts1.save("voice5.mp3")
            print("Loading")
            break
    else:
        tts1.save("voice5.mp3")

print("Code Successfull!")

        

 
