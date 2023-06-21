from src.yt_request_func import youtube


class Video:
    def __init__(self, video_id: str):
        self._video_id = video_id

        info = Video.get_info(self)
        self.title = info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = info['items'][0]['statistics']['viewCount']
        self.like_count = info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title

    @property
    def video_id(self):
        return self._video_id

    def get_info(self):
        video_info = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=self.video_id).execute()
        return video_info


class PLVideo(Video):
    def __init__(self, video_id: str, pl_video_id: str):
        super().__init__(video_id)
        self._pl_video_id = pl_video_id

    @property
    def pl_video_id(self):
        return self._pl_video_id
