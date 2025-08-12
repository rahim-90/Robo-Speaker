import pyttsx3 as py

if __name__ == '__main__':
    print("Welcome to Robo Speaker Created by Rahim")

    while True: 
        a = input("Enter what you want to speak: ")
        if a == "q":
            break
        b = py.init()
        b.say(a)
        b.runAndWait()