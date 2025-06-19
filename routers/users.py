from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users import UserS
from models.users import UsersM
from db import database
from routers.login import get_current_user
from functions.users import create_polzovatel, update_polzovatel, delete_polzovatel, create_admin, hash_old_user

polzovatel_router = APIRouter()


@polzovatel_router.get('/get_users')
def smotret_polzovateli(db: Session = Depends(database)):
    return db.query(UsersM).all()



@polzovatel_router.post('/post_users')
def dobavit_polzovatel(form:UserS, db:Session = Depends(database), current_user: UsersM = Depends(get_current_user)):
    try:
        return create_polzovatel(form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))



@polzovatel_router.post('/post_admin')
def dobavit_admin(form:UserS, db:Session = Depends(database), current_user:UsersM = Depends(get_current_user)):
    try:
        return create_admin(form, db, current_user)
    except Exception as e:
        raise HTTPException (400, str(e))




@polzovatel_router.put('/put_users')
def izmenit_polzovatel(ident: int, form: UserS, db: Session = Depends(database), current_user:UsersM=Depends(get_current_user)):
    return update_polzovatel(ident, form, db, current_user)





@polzovatel_router.delete('/delete_users')
def udalit_polzovatel(ident: int, db: Session = Depends(database), current_user:UsersM=Depends(get_current_user)):
    return delete_polzovatel(ident, db, current_user)



@polzovatel_router.put('/hash_password')
def shifr_parol(ident:int, form:UserS, db:Session=Depends(database)):
    return hash_old_user(ident, form, db)