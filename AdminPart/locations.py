from sqladmin import ModelView
from models.locations import LocationsM  # Предполагаемое имя модели

class LocationAd(ModelView, model=LocationsM):
    column_list = ["id", "name", "address"]
    name_plural = "Места"
    name = "Joylar"
    column_labels = {
        "id": "ID",
        "name": "Название",
        "address": "Адрес"
    }