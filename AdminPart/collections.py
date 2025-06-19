from sqladmin import ModelView
from models.collections import CollectionsM

class CollectionsAd(ModelView, model=CollectionsM):
    column_list = ["id", "name", "description", "artist", "year", "department_id", "image", "inventory_num", "exhibition_id"]
    name_plural = "Коллекции"
    name = "Kolektsiyalar"
    column_labels = {
        "id": "ID",
        "name": "Название",
        "description": "Описание",
        "artist" : "Автор",
        "year" : "Дата",
        "department_id" : "отдел_ид",
        "image" : "изображение",
        "inventory_num" : "инвентарь_ид",
        "exhibition_id" : "выставка_ид"
    }