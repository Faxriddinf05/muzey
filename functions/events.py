from models.events import EventsM

def create_sobitie(form, db):
    new_event = EventsM(
        title=form.title,
        description=form.description,
        date=form.date,
        location_id=form.location_id,
        price=form.price
    )
    db.add(new_event)
    db.commit()
    return "Событие добавлено"

def update_sobitie(ident, form, db):
    db.query(EventsM).filter(EventsM.id == ident).update({
        EventsM.title: form.title,
        EventsM.description: form.description,
        EventsM.date: form.date,
        EventsM.location_id: form.location_id,
        EventsM.price: form.price
    })
    db.commit()
    return "Событие изменено"

def delete_sobitie(ident: int, db):
    db.query(EventsM).filter(EventsM.id == ident).delete()
    db.commit()
    return "Событие удалено"