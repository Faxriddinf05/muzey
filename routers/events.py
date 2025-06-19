from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.events import EventsM
from schemas.events import EventS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.events import create_sobitie, update_sobitie, delete_sobitie

event_router = APIRouter()


@event_router.get('/get_events')
def smotret_eventi(db: Session = Depends(database)):
    return db.query(EventsM).all()

@event_router.post('/post_events')
def dobavit_event(form: EventS, db: Session = Depends(database)):
    return create_sobitie(form, db)

@event_router.put('/put_events')
def izmenit_event(ident: int, form: EventS, db: Session = Depends(database)):
    return update_sobitie(ident, form, db)

@event_router.delete('/delete_events')
def udalit_event(ident: int, db: Session = Depends(database)):
    return delete_sobitie(ident, db)