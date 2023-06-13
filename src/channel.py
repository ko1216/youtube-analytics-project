import json

from src.yt_request_func import printj, youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API
        """
        self._channel_id = channel_id

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self):
        return Channel.get_info(self)['items'][0]['snippet']['title']

    @property
    def info(self):
        return Channel.get_info(self)['items'][0]['snippet']['description']

    @property
    def url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def subscribers(self):
        return Channel.get_info(self)['items'][0]['statistics']['subscriberCount']

    @property
    def video_count(self):
        return Channel.get_info(self)['items'][0]['statistics']['videoCount']

    @property
    def views(self):
        return Channel.get_info(self)['items'][0]['statistics']['viewCount']

    def get_info(self) -> None:
        """
        Выводит в консоль информацию о канале
        """
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        printj(Channel.get_info(self))

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return youtube

    def to_json(self, filename):
        """
        Возвращает атрибуты экземпляра в формате json и записывает их в файл
        """
        data = {'channel_id': self.channel_id,
                'title': self.title,
                'info': self.info,
                'url': self.url,
                'subscribers': self.subscribers,
                'video_count': self.video_count,
                'views': self.views}
        with open(filename, 'w') as f:
            json.dump(data, f)
