from models.shop_product import ProductM

def create_tovar(form, db):
    new_tovar = ProductM(
        title=form.title,
        description=form.description,
        price=form.price,
        image_url=form.image_url
    )
    db.add(new_tovar)
    db.commit()
    return "Товар добавлен"

def update_tovar(ident, form, db):
    db.query(ProductM).filter(ProductM.id == ident).update({
        ProductM.title: form.title,
        ProductM.description: form.description,
        ProductM.price: form.price,
        ProductM.image_url: form.image_url
    })
    db.commit()
    return "Товар изменён"

def delete_tovar(ident: int, db):
    db.query(ProductM).filter(ProductM.id == ident).delete()
    db.commit()
    return "Товар удалён"