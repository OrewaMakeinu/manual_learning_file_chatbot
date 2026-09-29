#Abasic text to text Answer syntax of a chatbot.
from gtts import gTTS

stop_condition=False
text=[]
while True:
    print("infinte loop begins")
    user_text = input("text: ")
    if user_text == "Hi":
        print("Hello, Nice to meet you.")
    elif user_text == "how are you?":
        print("Thankyou for asking, I am totally fine. How about you?")
    elif user_text == "bye":
        stop_condition=True
        if stop_condition==True:
            break
    else:
        print("sorry didn't get what you mean?")
print("Code Fails***")

