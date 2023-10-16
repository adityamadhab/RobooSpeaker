from gtts import gTTS
import os

if __name__ == '__main__':
    print("Welcome to RoBoSpeaker")
    while True:
        x = input("Enter what you want me to speak :  ")
        language = 'en'
        command = gTTS(text=x, lang=language, slow=False)
        command.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")
