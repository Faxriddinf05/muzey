from models.locations import LocationsM

def create_mesto(form, db):
    new_mesto = LocationsM(
        name=form.name,
        address = form.address
    )
    db.add(new_mesto)
    db.commit()
    return "Место добавлено"

def update_mesto(ident, form, db):
    db.query(LocationsM).filter(LocationsM.id == ident).update({
        LocationsM.name: form.name,
        LocationsM.address:form.address
    })
    db.commit()
    return "Место изменено"

def delete_mesto(ident: int, db):
    db.query(LocationsM).filter(LocationsM.id == ident).delete()
    db.commit()
    return "Место удалено"