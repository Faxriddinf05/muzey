from models.users import UsersM
from routers.login import get_password_hash
from fastapi import HTTPException


def create_polzovatel(form, db, current_user):
    a = db.query(UsersM).filter(UsersM.username == form.username).first()
    if a:
        raise HTTPException(400, "Bunday Username mavjud !")

    new_polzovatel = UsersM(
        name=form.name,
        username = form.username,
        password=get_password_hash(form.password),
        email=form.email,
        role= 'staff'    # staff(hodim) == user desa ham bo'ladi
    )
    db.add(new_polzovatel)
    db.commit()
    return "Пользователь добавлен"


def create_admin(form, db, current_user):
    if current_user.role != "admin":
        raise HTTPException(400, "Sizga ruxsat yo'q !")

    a = db.query(UsersM).filter(UsersM.username == form.username).first()
    if a:
        raise HTTPException(400, "Bunday Username mavjud ! ")

    new_admin = UsersM(
        name=form.name,
        username=form.username,
        password=get_password_hash(form.password),
        email=form.email,
        role='admin'
    )
    db.commit()
    return "Admin qo'shildi !"


def update_polzovatel(ident:int, form, db, current_user):
    db.query(UsersM).filter(UsersM.id == ident).update({

        UsersM.name: form.name,
        UsersM.username: form.username,
        UsersM.password: get_password_hash(form.password),
        UsersM.email: form.email,

    })
    db.commit()
    return "Пользователь изменён"




def delete_polzovatel(ident, db, form, current_user):
    if current_user.role != "admin":
        raise HTTPException(400, "Sizga ruxsat yo'q !")

    a = db.query(UsersM).filter(UsersM.username == form.username).first()
    if a:
        raise HTTPException(400, "Bunday Username mavjud !")


    db.query(UsersM).filter(UsersM.id == ident).delete()
    db.commit()
    return "Foydalanuvchi o'chirildi !"




def hash_old_user(ident, form, db):
    db.query(UsersM).filter(UsersM.id == ident).update({
        UsersM.name : form.name,
        UsersM.username : form.username,
        UsersM.password : get_password_hash(form.password)
    })
    db.commit()
    return "Parol inshaalloh shifrlandi "