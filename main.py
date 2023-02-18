import requests
import keyboard
import clipboard
import pyautogui as pg
import openai as ai
from sys import exit

def generate_text(prompt):
    ai.api_key = "YOUR-API-KEY-HERE" 
    model_engine = "text-davinci-003"

    completion = ai.Completion.create( 
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )

def check_press():
    if keyboard.is_pressed("-"):
        prompt = clipboard.paste()
        print(prompt)
        print(generate_text(prompt))
        pg.hotkey('alt', 'tab')
        exit()

while True:
    check_press()
