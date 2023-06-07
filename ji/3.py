import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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
    type="channel",
    maxResults=10,
    part="id"
).execute()

chn_id = search_resp['items'][0]['id']['channelId']

play_lists = youtube.playlists().list(
    channelId=chn_id,
    part="snippet",
    maxResults=20).execute()

ids= []
titles = []

for i in play_lists['items']:
    ids.append(i['id'])
    titles.append(i['snippet']['title'])

df = pd.DataFrame([ids, titles]).T
df.columns = ["Playlists", "Titles"]

dtcu = df['Playlists'][0]
pl_vids = youtube.playlistItems().list(
    playlistId = dtcu,
    maxResults = 50,
    part = 'snippet'
).execute()

vid_names = []
vid_ids = []
vid_date = []

for vid in pl_vids['items']:
    vid_names.append(vid['snippet']['title'])
    vid_ids.append(vid['snippet']['resourceId']['videoId'])
    vid_date.append(vid['snippet']['publishedAt'])

vdf = pd.DataFrame([vid_date, vid_ids, vid_names]).T
vdf.columns = ['Date', 'ID', 'Title']


#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________
#_____________________________________________________________________________________________________

views = []
likes = []
comments = []
titles = []
dates = []

for v in range(len(vdf)):
    req_vid_search = youtube.videos().list(
        part = 'snippet,contentDetails, statistics',
        id = vdf['ID'][v]
    )

vid_search_res = req_vid_search.execute()


if vid_search_res['items'] == []:
    views.append('-')
    likes.append('-')
    comments.append('-')
    titles.append('-')
    dates.append('-')

views.append(vid_search_res['items'][0]['statistics']['viewCount'])
likes.append(vid_search_res['items'][0]['statistics']['viewCount'])
comments.append(vid_search_res['items'][0]['statistics']['viewCount'])
titles.append(vid_search_res['items'][0]['statistics']['viewCount'])
dates.append(vid_search_res['items'][0]['statistics']['viewCount'])

ytbv_df = pd.DataFrame([dates, titles, views, likes, comments]).T
ytbv_df.columns = ['Date', 'Title', 'views', 'Likes', 'Comments']

print(ytbv_df)
ytbv_df.to_excel("Youtube_test_1.xlsx")

t_1 = np.array(ytbv_df["views"].astype("int64"))
t_2 = np.array(ytbv_df["views"].astype("int64"))

plt.plot(t_2, t_1, 'co')
plt.xlabel('Likes')
plt.ylabel('Views')
plt.show()


