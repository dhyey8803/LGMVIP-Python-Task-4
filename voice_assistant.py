# Voice Assistant:

import speech_recognition as sr
import pyttsx3
import pywhatkit
import subprocess
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)       # 0 for male, and 1 for female
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print('Clearing the background noise, please wait...')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Say something...')
        speak('Say something...')
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print('You said: ', command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""

    except sr.RequestError:
        speak("Sorry, the service is not available.")
        return ""

def execute_command(command):
    if 'hello' in command or 'hey' in command:
        speak("Hello! I'm fine! What about you!")

    elif 'year' in command:
        year = datetime.datetime.now().strftime('%Y')
        print(year)
        speak("It's: " + year)

    elif 'month' in command:
        month = datetime.datetime.now().strftime('%B')
        print(month)
        speak("It's: " + month)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%x')
        print(date)
        speak("The date is: " + date)

    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A')
        print(day)
        speak("The day is: " + day)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        speak("The time is: " + time)

    elif 'chrome' in command or 'google' in command:
        speak(f'{command}...')
        program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.Popen([program])
        print("Chrome is running. Please close it to continue.")
        speak(" Chrome is running. Please close it to continue.")
        while True:
            proc = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE)
            result = proc.stdout.read().decode('utf-8')
            if "chrome.exe" not in result.lower():
                break
        print("Chrome closed, resuming assistant.")
        speak(" Chrome closed, resuming assistant.")

    elif 'play' in command or 'youtube' in command:
        speak(f'{command}...!')
        query = command.replace('play', '').replace('youtube', '')
        pywhatkit.playonyt(query)
        print("YouTube is running. Please close it to continue.")
        speak(" YouTube is running. Please close it to continue.")
        while True:
            proc = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE)
            result = proc.stdout.read().decode('utf-8')
            if "chrome.exe" not in result.lower():
                break
        print("YouTube closed, resuming assistant.")
        speak(" YouTube closed, resuming assistant.")

    elif 'search' in command:
        speak(f' {command}...')
        pywhatkit.search(command)
        print("Google is running. Please close it to continue.")
        speak(" Your search is running. Please close it to continue.")
        while True:
            proc = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE)
            result = proc.stdout.read().decode('utf-8')
            if "chrome.exe" not in result.lower():
                break
        print("Goggle closed, resuming assistant.")
        speak(" Your search closed, resuming assistant.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Have a nice day!")
        return False

    else:
        print('Say it again, it is not clear..!')
        speak('Say it again, it is not clear..!')

    return True

if __name__ == "__main__":
    speak('Hey WhatsApp')
    print("\nVoice assistant started. How can I help you?")
    speak("Voice assistant started. How can I help you?")

    running = True
    while running:
        command = listen_command()
        running = execute_command(command)