from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.collections import CollectionsM
from schemas.collections import CollectionS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.collections import create_eksponat, update_eksponat, delete_eksponat

eksponat_router = APIRouter()


@eksponat_router.get('/get_collections')
def smotret_eksponati(db:Session=Depends(database)):
    return db.query(CollectionsM).all()

@eksponat_router.post('/post_collections')
def dobavit_eksponati(form:CollectionS, db:Session=Depends(database)):
    return create_eksponat(form, db)

@eksponat_router.put('put_collections')
def izmenit_eksponati(ident:int, form:CollectionS, db:Session=Depends(database)):
    return update_eksponat(ident, form, db)

@eksponat_router.delete('/delete_collections')
def udalit_eksponati(ident:int, db:Session=Depends(database)):
    return delete_eksponat(ident, db)