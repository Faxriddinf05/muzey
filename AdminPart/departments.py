from sqladmin import ModelView
from models.departments import DepartmentsM  # Предполагаемое имя модели

class DepartmentAd(ModelView, model=DepartmentsM):
    column_list = ["id", "name", "description"]
    name_plural = "Отделы"
    name = "Bo'limlar"
    column_labels = {
        "id": "ID",
        "name": "Название",
        "description": "Описание"
    }