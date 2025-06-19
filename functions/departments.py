from models.departments import DepartmentsM

def create_otdel(form, db):
    new_departament = DepartmentsM(
        name=form.name,
        description=form.description
    )
    db.add(new_departament)
    db.commit()
    return "Новый отдел добавлен"

def update_otdel(ident, form, db):
    db.query(DepartmentsM).filter(DepartmentsM.id == ident).update({
        DepartmentsM.name: form.name,
        DepartmentsM.description: form.description
    })
    db.commit()
    return "Отдел изменён"

def delete_otdel(ident: int, db):
    db.query(DepartmentsM).filter(DepartmentsM.id == ident).delete()
    db.commit()
    return "Отдел удалён"