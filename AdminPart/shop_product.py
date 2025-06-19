from sqladmin import ModelView
from models.shop_product import ProductM

class ProductAd(ModelView, model=ProductM):
    column_list = ["id", "title", "description","price", "image_url"]  # Убрал amount, если его нет
    name_plural = "Продукты"
    name = "Mahsulotlar"
    column_labels = {
        "id": "ID",
        "title": "Название",
        "description" : "Описание",
        "price": "Цена",
        "image_url": "Изображение_ссылка"
    }