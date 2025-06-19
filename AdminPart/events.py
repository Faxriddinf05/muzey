from sqladmin import ModelView
from models.events import EventsM  # Предполагаемое имя модели

class EventAd(ModelView, model=EventsM):
    column_list = ["id", "title", "description", "date", "location_id", "price"]
    name_plural = "События"
    name = "Tadbirlar"
    column_labels = {
        "id": "ID",
        "title": "Заголовок",
        "description" : "Описание",
        "date": "Дата",
        "location_id" : "Локация_ид",
        "price" : "Цена"
    }