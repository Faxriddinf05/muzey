from sqladmin import ModelView
from models.exhibitions import ExhibitionsM  # Предполагаемое имя модели

class ExhibitionAd(ModelView, model=ExhibitionsM):
    column_list = ["id", "title", "description","start_at", "end_at", "type", "department_id"]
    name_plural = "Выставки"
    name = "Ko'rgazmalar"
    column_labels = {
        "id": "ID",
        "title": "Название",
        "description" : "Описание",
        "start_at": "Начинается с",
        "end_at" : "Заканчивается с",
        "type" : "Тип",
        "department_id" : "Отдел_ид"
    }