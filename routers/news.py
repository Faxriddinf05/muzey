from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.news import NewsM
from schemas.news import NewS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.news import create_novost, update_novost, delete_novost

novost_router = APIRouter()


@novost_router.get('/get_news')
def smotret_novosti(db: Session = Depends(database)):
    return db.query(NewsM).all()

@novost_router.post('/post_news')
def dobavit_novost(form: NewS, db: Session = Depends(database)):
    return create_novost(form, db)

@novost_router.put('/put_news')
def izmenit_novost(ident: int, form: NewS, db: Session = Depends(database)):
    return update_novost(ident, form, db)

@novost_router.delete('/delete_news')
def udalit_novost(ident: int, db: Session = Depends(database)):
    return delete_novost(ident, db)