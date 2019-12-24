import sys
import time

import requests
from apiclient.discovery import build

YOUTUBE_IN_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&pageToken={pageToken}&videoId={videoId}&key={key}'
YOUTUBE_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&videoId={videoId}&key={key}'
key = 'AIzaSyAjt9YVfkwsBGaFYem8W0SI7gwY6o7uebM'


def commentExtract(videoId, count=100):
    page_info = requests.get(YOUTUBE_LINK.format(videoId=videoId, key=key))
    while page_info.status_code != 200:
        if page_info.status_code != 429:
            # print ("Comments disabled")
            sys.exit()

        time.sleep(20)
        page_info = requests.get(YOUTUBE_LINK.format(videoId=videoId, key=key))

    page_info = page_info.json()

    comments = []
    co = 0;
    for i in range(len(page_info['items'])):
        comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
        co += 1
        if co == count:
            return comments

    # INFINTE SCROLLING
    while 'nextPageToken' in page_info:
        temp = page_info
        page_info = requests.get(YOUTUBE_IN_LINK.format(videoId=videoId, key=key, pageToken=page_info['nextPageToken']))

        while page_info.status_code != 200:
            time.sleep(20)
            page_info = requests.get(YOUTUBE_IN_LINK.format(videoId=videoId, key=key, pageToken=temp['nextPageToken']))
        page_info = page_info.json()

        for i in range(len(page_info['items'])):
            comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
            co += 1
            if co == count:
                return comments

    return comments


def retrieveVideos(keyword):
    try:
        youtube = build('youtube', 'v3', developerKey=key)
        request = youtube.search().list(q=keyword, part='snippet', type='video', maxResults=10, order='relevance',
                                        regionCode='SA')
        videoList = request.execute()

        comments = []
        for item in videoList['items']:
            video = item['id']['videoId']
            comment = commentExtract(video)
            comments.extend(comment)

        return comments

    except:
        pass