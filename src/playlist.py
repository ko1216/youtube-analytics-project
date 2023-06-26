import datetime

import isodate

from src.yt_request_func import youtube


class PlayList:
    def __init__(self, pl_video_id):
        self.pl_video_id = pl_video_id

        info = PlayList.get_info(self)
        self.title = (info[0]['items'][0]['snippet']['title']).split('.')[0]
        self.url = f'https://www.youtube.com/playlist?list={self.pl_video_id}'

    def get_video_list(self):
        playlist_videos = youtube.playlistItems().list(playlistId=self.pl_video_id, part='contentDetails',
                                                       maxResults=50,).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def get_info(self):
        videos_info = []

        for video_id in self.get_video_list():

            video_info = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
            videos_info.append(video_info)
        return videos_info

    @property
    def total_duration(self):
        total_duration = datetime.timedelta(0)

        video_ids = self.get_video_list()

        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        video_info = PlayList.get_info(self)

        like_counter = 0

        for x in range(len(video_info)):
            if int(video_info[x]['items'][0]['statistics']['likeCount']) >= like_counter:
                favorite_video = f"https://youtu.be/{video_info[x]['items'][0]['id']}"

        return favorite_video
