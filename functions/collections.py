from models.collections import CollectionsM

def create_eksponat(form, db):
    new_eksponati = CollectionsM(
        title=form.title,
        description = form.description,
        artist = form.artist,
        year = form.year,
        department_id = form.department_id,
        image = form.image,
        inventory_num = form.inventory_num,
        exhibition_id = form.exhibition_id
    )
    db.add(new_eksponati)
    db.commit()
    return "Экспонат добавлен"

def update_eksponat(ident, form, db):
    db.query(CollectionsM).filter(CollectionsM.id == ident).update({
        CollectionsM.title : form.title,
        CollectionsM.description : form.description,
        CollectionsM.artist : form.artist,
        CollectionsM.year : form.year,
        CollectionsM.department_id : form.department_id,
        CollectionsM.image : form.image,
        CollectionsM.inventory_num : form.inventory_num,
        CollectionsM.exhibition_id : form.exhibition_id
    })
    db.commit()
    return "Экспонат изменён"

def delete_eksponat(ident:int, db):
    db.query(CollectionsM).filter(CollectionsM.id == ident).delete()
    db.commit()
    return "Экспонат удалён"
