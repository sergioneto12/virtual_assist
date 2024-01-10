import os
import openai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def busca(words: str): 
    '''
    This function can create a response from voice command on the application.

    The setting parameters chosen were
    - model: text-davinci-003
    - max_tokens of 1024
    - n = 1
    - No stop
    - temperature of 0.5

    This assumes the text from speech recognition and returns the corresponding quest.

    The input is a phrase that is written from the speech recognition, on a string type.
    '''
    response = openai.Completion.create(
                                        model="text-davinci-003", 
                                        # prompt=input('Faça sua pergunta: '), 
                                        prompt=f'{words}',
                                        max_tokens=1024,
                                        n=1,
                                        stop=None,
                                        temperature=0.5
                                        )

    res = response.choices[0].text
    return res

def image(words: str):
    '''
    This function can create an image of DALL-E from voice command on the application.

    The setting parameters chosen were
    - n = 1
    - size of 1024x1024

    This assumes the text from speech recognition and returns the corresponding quest.

    The input is a phrase that is written from the speech recognition, on a string type.
    '''
    response = openai.Image.create(
    prompt=f'{words}',
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return image_url
    # print(image_url)
