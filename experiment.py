import requests

json = {
    "link": "https://static.videezy.com/system/resources/previews/000/009/169/original/Young_hispanic_woman_upset_angry_emotional_2.mp4",
    "user": "test_user"
}

#cloud
# r = requests.post("https://emot-api.azurewebsites.net/score", json=json)
#local
r = requests.post("http://127.0.0.1:5000/score", json=json)
print(r.json())
import pandas as pd
df = pd.DataFrame(r.json(), index=[0])
print(df)

