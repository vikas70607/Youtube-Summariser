
import time
import pandas as pd
import openai
from pytube import YouTube
import assemblyai as aai
import os

def subtitle_generator(filepath):

    aai.settings.api_key = "1f6d91ba08a045d1882e3d57c5c88219"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(f"{filepath}")
    os.remove(filepath)
    return transcript.text


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    youtubeObject.download()

    dir_list = os.listdir('.')

    for file in dir_list:
        if (file.endswith('.mp4')):
            return file


openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

        model=model,

        messages=messages,

        temperature=0,

    )

    return response.choices[0].message["content"]


def model(link):
    x = Download(str(link))
    text = (subtitle_generator(f'{x}'))
    text = text + 'Summarise this in bullet points'
    ans = get_completion(text)
    return ans
