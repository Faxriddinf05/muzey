from sqladmin import ModelView
from models.tickets import TicketsM

class TicketsAd(ModelView, model=TicketsM):
    column_list = ["id", "event_id", "exhibition_id","user_id", "status", "price", "visit_date"]
    name_plural = "Билеты"
    name = "Chiptalar"
    column_labels = {
        "id": "ID",
        "event_id": "Событие_ид",
        "exhibition_id" : "Выставка_ид",
        "user_id": "Пользователь_ид",
        "status": "Статус",
        "price" : "Цена",
        "visit_date" : "Дата посещение"
    }