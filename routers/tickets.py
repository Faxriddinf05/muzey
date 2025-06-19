from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.tickets import TicketsM
from schemas.tickets import TicketS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.tickets import create_bilet, update_bilet, delete_bilet

bilet_router = APIRouter()


@bilet_router.get('/get_tickets')
def smotret_bilety(db: Session = Depends(database)):
    return db.query(TicketsM).all()

@bilet_router.post('/post_tickets')
def dobavit_bilet(form: TicketS, db: Session = Depends(database)):
    return create_bilet(form, db)

@bilet_router.put('/put_tickets')
def izmenit_bilet(ident: int, form: TicketS, db: Session = Depends(database)):
    return update_bilet(ident, form, db)

@bilet_router.delete('/delete_tickets')
def udalit_bilet(ident: int, db: Session = Depends(database)):
    return delete_bilet(ident, db)