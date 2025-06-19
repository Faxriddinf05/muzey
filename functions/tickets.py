from models.tickets import TicketsM

def create_bilet(form, db):
    new_bilet = TicketsM(
        event_id=form.event_id,
        exhibition_id=form.exhibition_id,
        user_id=form.user_id,
        status=form.status,
        price=form.price,
        visit_date=form.visit_date
    )
    db.add(new_bilet)
    db.commit()
    return "Билет добавлен"

def update_bilet(ident, form, db):
    db.query(TicketsM).filter(TicketsM.id == ident).update({
        TicketsM.event_id: form.event_id,
        TicketsM.exhibition_id: form.exhibition_id,
        TicketsM.user_id: form.user_id,
        TicketsM.status: form.status,
        TicketsM.price: form.price,
        TicketsM.visit_date: form.visit_date
    })
    db.commit()
    return "Билет изменён"

def delete_bilet(ident: int, db):
    db.query(TicketsM).filter(TicketsM.id == ident).delete()
    db.commit()
    return "Билет удалён"