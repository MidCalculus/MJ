

import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


DEV_KEY_ = "AIzaSyAHIonSsN8_6cptdG00RW25fudECPI4CjU"
YTB_API_SERV_NAME = "youtube"
YTB_API_VER = "v3"


youtube = build(YTB_API_SERV_NAME, YTB_API_VER, developerKey=DEV_KEY_)


search_resp = youtube.search().list(
    q="minecraft", 
    order="relevance",
    type="video",
    videoDuration="long",
    maxResults=10,
    part="snippet"
).execute()


print(search_resp)


vids = []
titles = []
channels = []
publishTime = []
description = []
channelId = []

for item in search_resp['items']:
    vids.append(item['id']['videoId'])
    titles.append(item['snippet']['title'])
    channels.append(item['snippet']['channelTitle'])
    publishTime.append(item['snippet']['publishedAt'])
    description.append(item['snippet']['description'])
    channelId.append(item['snippet']['channelId'])
df = pd.DataFrame([vids, titles, channels, publishTime, description, channelId]).T
df.columns = ["Video ID", "Titles", "Channel Name", "publishTime", "description", "channelId"]


print(df)