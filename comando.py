'''
    coding: utf-8

    created by: Sergio Neto
    last update: 19/03/2023

    references: https://www.youtube.com/watch?v=36RIoJeV95M
'''

# imports from python
import webbrowser
import locale

# needed libs you'll install
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

# module that imports data from chat gpt api
from index import busca, image

# setting the audio recognizer from your mic, the machine speaker and the command string
audio = sr.Recognizer()
assistant = pyttsx3.init()
language = locale.getdefaultlocale()[0]
command = ''

def executa_command(language: str):
    '''
    This function creates an interaction between user and local machine.
    It is only triggered by calling its name, Lua.

    It captures the speech and translate it to string format, and by keywords a response is chosen.

    The only parameter is a auto-defined language, captured by the system own language.

    In case of an error, a general exception is printed to the user knowledge.
    '''
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            sound = audio.listen(source)
            command = audio.recognize_google(sound, language=language)
            command = command.lower()
            if 'lua' in command:
                command = command.replace('lua', '')
                assistant.say(command)
                assistant.runAndWait()

            return command
    
    except Exception as e:
        print('There is something wrong, ', e)

def command_user(language: str):
    '''
    The user response is done by this function.
    Note that this is a test with brazilian portuguese terms.

    We have some options to create the response:
    The first conditional form searches in wikipedia about the response.
    The second opens a vídeo to play the exact song asked. The third part also opens a youtube browser instance, but with an open exploration.
    Finally, we have two chat gpt calls: the first to an image and the second for all questions.

    The parameters is a auto-defined language parameter.
    '''
    command = executa_command(language)
    if 'procure por' in command:
        procurar = command.replace('procure por', '')
        wikipedia.set_lang(str(language)[0:2])
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        assistant.say(resultado)
        assistant.runAndWait()

    elif 'toque' in command:
        musica = command.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        assistant.say('Tocando música')
        assistant.runAndWait()

    elif 'no youtube' in command:
        musica = command.replace('no youtube','')
        resultado = pywhatkit.playonyt(musica)
        assistant.say('Esse é o seu resultado')
        assistant.runAndWait()

    elif ('imagem' in command or 'retrato' in command):
        imagem = image(command)
        webbrowser.open(imagem)
        assistant.say('Mostrando Imagem')
        assistant.runAndWait()

    else:
        resultado = busca(command)
        assistant.say(resultado)
        assistant.runAndWait()

command_user(language)

