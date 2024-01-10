# Projeto Lua - Assistente Virtual 🌟

O Projeto Lua é um assistente virtual desenvolvido por [Sergio Neto](https://github.com/sergioneto14) para interação entre usuário e máquina, trazendo funcionalidades de reconhecimento de voz, consulta a APIs de terceiros e interações com o usuário.

## Descrição

O assistente Lua utiliza a API do Chat GPT para realizar interações inteligentes com os usuários. A parte central do código reside no arquivo `index.py`, que é responsável por estabelecer a conexão com a API do Chat GPT. Além disso, o arquivo `comando.py` define várias funcionalidades do assistente, como busca na Wikipedia, reprodução de músicas via PyWhatKit, exibição de imagens e muito mais.

## Funcionalidades Principais

### Reconhecimento de Voz 🗣️

O assistente utiliza a biblioteca `speech_recognition` para capturar e processar comandos de voz, permitindo uma interação mais natural com o usuário. O reconhecimento é feito em PT-BR, mas o código irá reconhecer o idioma em que sua máquina estiver conectada.

### Funcionalidades de Busca e Entretenimento 🔍🎵

- **Pesquisa na Wikipedia:** Lua é capaz de procurar informações na Wikipedia sobre vários tópicos.
- **Reprodução de Música:** Basta dizer "Lua, toque" seguido do nome da música e o assistente reproduzirá a música via PyWhatKit.
- **Navegação no YouTube:** Lua pode abrir vídeos específicos no YouTube conforme as solicitações do usuário.

### Integração com o Chat GPT 💬

Através do arquivo `index.py`, Lua se conecta ao Chat GPT para oferecer respostas inteligentes e variadas aos usuários.

## Como Utilizar

Para utilizar o assistente Lua, é necessário ter as bibliotecas especificadas no arquivo `comando.py` instaladas. Depois, basta rodar o arquivo principal `comando.py` para iniciar a interação com o assistente.

### Exemplo de Uso:

```python
python comando.py
```
