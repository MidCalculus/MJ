import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEV_KEY_ = "AIzaSyAHIonSsN8_6cptdG00RW25fudECPI4CjU"
YTB_API_SERV_NAME = "youtube"
YTB_API_VER = "v3"
youtube = build(YTB_API_SERV_NAME, YTB_API_VER, developerKey = DEV_KEY_)

search_bar = youtube.search().list(
    q ="life hacks",
    order="relevance",
    type = "video",
    videoDuration = "long",
    maxResults = 100,
    part = "snippet"
).execute()

# print(search_bar)

vids = []
titles = []
channels = []

for item in search_bar['items']:
    vids.append(item['id']['videoId'])
    titles.append(item['snippet']['title'])
    channels.append(item['snippet']['channelTitle'])

df = pd.DataFrame([vids, titles, channels]).T
df.columns = ["Video ID", "Titles", "Channel Name"]

sns.countplot(x=df["Channel Name"])
# plt.show()

sns.boxenplot(data=df, x="Channel Name")
plt.show()
