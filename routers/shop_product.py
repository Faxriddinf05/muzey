from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.shop_product import ProductM
from schemas.shop_product import ProductS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.shop_product import create_tovar, update_tovar, delete_tovar

tovar_router = APIRouter()


@tovar_router.get('/get_shop_products')
def smotret_tovary(db: Session = Depends(database)):
    return db.query(ProductM).all()

@tovar_router.post('/post_shop_products')
def dobavit_tovar(form: ProductS, db: Session = Depends(database)):
    return create_tovar(form, db)

@tovar_router.put('/put_shop_products')
def izmenit_tovar(ident: int, form: ProductS, db: Session = Depends(database)):
    return update_tovar(ident, form, db)

@tovar_router.delete('/delete_shop_products')
def udalit_tovar(ident: int, db: Session = Depends(database)):
    return delete_tovar(ident, db)