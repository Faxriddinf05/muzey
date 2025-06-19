from models.exhibitions import ExhibitionsM

def create_vistavka(form, db):
    new_vistavka = ExhibitionsM(
        title=form.title,
        description=form.description,
        start_at=form.start_at,
        end_at=form.end_at,
        type=form.type,
        department_id=form.department_id
    )
    db.add(new_vistavka)
    db.commit()
    return "Выставка добавлена"

def update_vistavka(ident, form, db):
    db.query(ExhibitionsM).filter(ExhibitionsM.id == ident).update({
        ExhibitionsM.title: form.title,
        ExhibitionsM.description: form.description,
        ExhibitionsM.start_at: form.start_at,
        ExhibitionsM.end_at: form.end_at,
        ExhibitionsM.type: form.type,
        ExhibitionsM.department_id: form.department_id
    })
    db.commit()
    return "Выставка изменена"

def delete_vistavka(ident: int, db):
    db.query(ExhibitionsM).filter(ExhibitionsM.id == ident).delete()
    db.commit()
    return "Выставка удалена"