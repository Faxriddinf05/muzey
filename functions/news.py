from models.news import NewsM

def create_novost(form, db):
    new_novost = NewsM(
        title=form.title,
        content=form.content,
        publication_date=form.publication_date,
        image=form.image,
        video=form.video
    )
    db.add(new_novost)
    db.commit()
    return "Новость добавлена"

def update_novost(ident, form, db):
    db.query(NewsM).filter(NewsM.id == ident).update({
        NewsM.title: form.title,
        NewsM.content: form.content,
        NewsM.publication_date: form.publication_date,
        NewsM.image: form.image,
        NewsM.video: form.video
    })
    db.commit()
    return "Новость изменена"

def delete_novost(ident: int, db):
    db.query(NewsM).filter(NewsM.id == ident).delete()
    db.commit()
    return "Новость удалена"