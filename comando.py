'''
    coding: utf-8

    created by: Sergio Neto
    last update: 13/12/2023

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

# ...

class Assistant:
    def __init__(self, language=None):
        '''
        Inicializa a instância da classe Assistant.

        Parameters:
            language (str): O idioma a ser usado (padrão é None para o idioma padrão do sistema).
        '''
        self.audio = sr.Recognizer()
        self.assistant = pyttsx3.init()
        self.language = language or locale.getdefaultlocale()[0]

    def executa_command(self) -> str:
        '''
        Esta função cria uma interação entre o usuário e a máquina local.
        É acionada apenas chamando seu nome, Lua.
        Captura o áudio e o traduz para o formato de string. Uma resposta é escolhida com base em palavras-chave.
        Em caso de erro, uma exceção geral é impressa para o conhecimento do usuário.

        Returns:
            str: O comando reconhecido em formato de string.
        '''
        try:
            with sr.Microphone() as source:
                print('Ouvindo..')
                sound = self.audio.listen(source)
                command = self.audio.recognize_google(sound, language=self.language)
                command = command.lower()

                if 'lua' in command:
                    command = command.replace('lua', '')
                    self.assistant.say(command)
                    self.assistant.runAndWait()

                return command

        except sr.UnknownValueError:
            print('Não foi possível entender o áudio')
        except sr.RequestError as e:
            print(f'Erro na requisição ao Google: {e}')
        except Exception as e:
            print(f'Algo deu errado: {e}')
    
    def command_user(self, command: str):
        '''
        A resposta do usuário é feita por esta função.
        Esta é uma versão de teste com termos em português do Brasil.
        Algumas opções para criar a resposta incluem:
        - A primeira forma condicional pesquisa na Wikipedia sobre a resposta.
        - A segunda abre um vídeo para tocar a música exata solicitada.
        - A terceira também abre uma instância do navegador YouTube, mas com uma exploração aberta.
        - Finalmente, temos duas chamadas para o Chat GPT: a primeira para uma imagem e a segunda para todas as perguntas.

        Parameters:
            command (str): O comando fornecido pelo usuário.
        '''
        keywords_to_functions = {
            'procure por': self.search_wikipedia,
            'toque': self.play_music,
            'no youtube': self.play_youtube,
            'imagem': self.show_image,
            'retrato': self.show_image
        }

        for keyword, function in keywords_to_functions.items():
            if keyword in command:
                function(command)
                break
        else:
            self.default_response(command)

    def search_wikipedia(self, command: str):
        procurar = command.replace('procure por', '')
        wikipedia.set_lang(str(self.language)[0:2])
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        self.assistant.say(resultado)
        self.assistant.runAndWait()

    def play_music(self, command: str):
        musica = command.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        self.assistant.say('Tocando música')
        self.assistant.runAndWait()

    def play_youtube(self, command: str):
        musica = command.replace('no youtube', '')
        resultado = pywhatkit.playonyt(musica)
        self.assistant.say('Esse é o seu resultado')
        self.assistant.runAndWait()

    def show_image(self, command: str):
        imagem = image(command)
        webbrowser.open(imagem)
        self.assistant.say('Mostrando Imagem')
        self.assistant.runAndWait()

    def default_response(self, command: str):
        resultado = busca(command)
        self.assistant.say(resultado)
        self.assistant.runAndWait()

if __name__ == "__main__":
    assistant = Assistant()
    user_command = assistant.executa_command()
    assistant.command_user(user_command)
