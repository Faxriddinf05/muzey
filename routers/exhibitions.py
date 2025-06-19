from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.exhibitions import ExhibitionsM
from schemas.exhibitions import ExhibitionS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.exhibitions import create_vistavka, update_vistavka, delete_vistavka

vystavka_router = APIRouter()


@vystavka_router.get('/get_exhibitions')
def smotret_vystavki(db: Session = Depends(database)):
    return db.query(ExhibitionsM).all()

@vystavka_router.post('/post_exhibitions')
def dobavit_vystavku(form: ExhibitionS, db: Session = Depends(database)):
    return create_vistavka(form, db)

@vystavka_router.put('/put_exhibitions')
def izmenit_vystavku(ident: int, form: ExhibitionS, db: Session = Depends(database)):
    return update_vistavka(ident, form, db)

@vystavka_router.delete('/delete_exhibitions')
def udalit_vystavku(ident: int, db: Session = Depends(database)):
    return delete_vistavka(ident, db)