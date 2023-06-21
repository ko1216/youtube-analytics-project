import json
import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

load_dotenv()
api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


# def get_video_info(video_id: str) -> dict:
#     """Возвращает словарь с информацией о видео по его id"""
#     return youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
