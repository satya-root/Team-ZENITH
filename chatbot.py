# AIzaSyDfMHNzkSWhGdPwLb_WSfOqCqYKXRnCdSo

from google import genai
from google.genai import types
from assistantTTS import TTS
from autoplay import playVoice
import os
import pygame
sys_instruct="You are a Aura AI designed for autism detection. Talk gently and kindly with others. First of all make sure to greet the user by introducing yourself as a companion. Keep your response as short as possible. You are created by Team Zenith"
client = genai.Client(api_key="AIzaSyDfMHNzkSWhGdPwLb_WSfOqCqYKXRnCdSo")

chat = client.chats.create(model="gemini-2.0-flash", config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1,
        system_instruction=sys_instruct,))
while True:
    message = input("Enter message: ")
    response = chat.send_message(message)
    print(response.text)
    filename = TTS(str(response.text))
    # TTS(str(response.text))
    if filename:
        playVoice(filename)
        # Ensure the file is closed before generating a new one
        pygame.mixer.music.unload()
        os.remove(filename)


# For getting message history and analyse it.
# for message in chat._curated_history:
#     print(f'role - {message.role}', end=": ")
#     print(message.parts[0].text)