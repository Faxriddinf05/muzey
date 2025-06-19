from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.locations import LocationsM
from schemas.locations import LocationS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.locations import create_mesto, update_mesto, delete_mesto

mesto_router = APIRouter()


@mesto_router.get('/get_locations')
def smotret_mesta(db: Session = Depends(database)):
    return db.query(LocationsM).all()

@mesto_router.post('/post_locations')
def dobavit_mesto(form: LocationS, db: Session = Depends(database)):
    return create_mesto(form, db)

@mesto_router.put('/put_locations')
def izmenit_mesto(ident: int, form: LocationS, db: Session = Depends(database)):
    return update_mesto(ident, form, db)

@mesto_router.delete('/delete_locations')
def udalit_mesto(ident: int, db: Session = Depends(database)):
    return delete_mesto(ident, db)