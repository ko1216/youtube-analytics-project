import json

from src.yt_request_func import printj, youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API
        """
        self._channel_id = channel_id

        info = Channel.get_info(self)
        self.title = info['items'][0]['snippet']['title']
        self.description = info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self._channel_id}'
        self.subscribers = info['items'][0]['statistics']['subscriberCount']
        self.video_count = info['items'][0]['statistics']['videoCount']
        self.views = info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'Имя канала: {self.title}, ссылка на канал: {self.url}'

    def __add__(self, other_channel):
        return int(self.subscribers) + int(other_channel.subscribers)

    def __sub__(self, other_channel):
        return int(self.subscribers) - int(other_channel.subscribers)

    def __lt__(self, other):
        return int(self.subscribers) < int(other.subscribers)

    def __gt__(self, other):
        return int(self.subscribers) > int(other.subscribers)

    def __le__(self, other):
        return int(self.subscribers) <= int(other.subscribers)

    def __ge__(self, other):
        return int(self.subscribers) >= int(other.subscribers)

    def __eq__(self, other):
        return int(self.subscribers) == int(other.subscribers)

    @property
    def channel_id(self):
        return self._channel_id

    def get_info(self) -> dict:
        """
        Возвращает записанную информацию о канале в формате dict
        """
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
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
        data = {'channel_id': self._channel_id,
                'title': self.title,
                'info': self.description,
                'url': self.url,
                'subscribers': self.subscribers,
                'video_count': self.video_count,
                'views': self.views}
        with open(filename, 'w') as f:
            json.dump(data, f)
