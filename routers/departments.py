from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.departments import DepartmentsM
from schemas.departments import DepartmentS
from routers.login import get_current_user
from models.users import UsersM
from db import database
from functions.departments import create_otdel, update_otdel, delete_otdel

departament_router = APIRouter()


@departament_router.get('/get_departments')
def smotret_otdeli(db: Session = Depends(database)):
    return db.query(DepartmentsM).all()

@departament_router.post('/post_departments')
def dobavit_otdel(form: DepartmentS, db: Session = Depends(database)):
    return create_otdel(form, db)

@departament_router.put('/put_departments')
def izmenit_otdel(ident: int, form: DepartmentS, db: Session = Depends(database)):
    return update_otdel(ident, form, db)

@departament_router.delete('/delete_departments/{ident}')
def udalit_otdel(ident: int, db: Session = Depends(database)):
    return delete_otdel(ident, db)