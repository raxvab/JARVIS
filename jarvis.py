import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('I am listening, Sir')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('hello jarvis', '')
                #print(command)

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print('\nInput'+command+'\n')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        print('playing'+song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'on a date' in command:
        talk('You have a girlfriend stop kidding.')
        print('You have a girlfriend stop kidding.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        var = pyjokes.get_joke()
        print(var)
    elif 'go rest now' in command:
        talk('It was a nice time talking to you goodbye sir.')
        print('It was a nice time talking to you goodbye sir.')
        return 0
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
    if run_jarvis() == 0:
        exit()
