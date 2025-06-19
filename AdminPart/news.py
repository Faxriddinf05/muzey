from sqladmin import ModelView
from models.news import NewsM  # Предполагаемое имя модели

class NewsAd(ModelView, model=NewsM):
    column_list = ["id", "title", "content", "publication_date", "image", "video"]
    name_plural = "Новости"
    name = "Yangiliklar"
    column_labels = {
        "id": "ID",
        "title": "Название",
        "content" : "Контент",
        "publication_date": "Дата_издание",
        "image" : "Изображение",
        "video" : "Видео"
    }