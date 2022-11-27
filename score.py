import pandas as pd
import requests
import os
from utils import process_data
import random
def get_video(link, filename):
    veideo_link = link
    veideo_name = "app/data/video/"
    if not os.path.isdir(veideo_name):
        os.makedirs(veideo_name)
    veideo_name += f"{filename}.mp4"
    with open(veideo_name, "wb") as f:
        # write bytes to file
        f.write(requests.get(veideo_link).content)
    return veideo_name




def score_data(df):
    angry = sum(df.angry)
    disgust = sum(df.disgust)
    fear = sum(df.fear)
    happy = sum(df.happy)
    sad = sum(df.sad)
    surprise = sum(df.surprise)
    neutral = sum(df.neutral)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotions_values = [angry, disgust, fear, happy, sad, surprise, neutral]
    emotions_values = [round((x/sum(emotions_values))*100, 2) for x in emotions_values]
    score_json = dict(zip(emotions, emotions_values))
    return score_json



