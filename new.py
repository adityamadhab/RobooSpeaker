import pyttsx3

text_speech = pyttsx3.init()

print("Welcome to RoboSpeaker")
while True: 
    answer = input("Enter what you want you me to speak : ")
    if answer == "exit" :
        break
    text_speech.say(answer)
    text_speech.runAndWait()
