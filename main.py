from fastapi import FastAPI
from sqladmin import Admin
from AdminPart.collections import CollectionsAd
from AdminPart.departments import DepartmentAd
from AdminPart.events import EventAd
from AdminPart.exhibitions import ExhibitionAd
from AdminPart.locations import LocationAd
from AdminPart.news import NewsAd
from AdminPart.shop_product import ProductAd
from AdminPart.tickets import TicketsAd
from routers.login import login_router, SECRET_KEY
from routers.collections import eksponat_router
from routers.departments import departament_router
from routers.events import event_router
from routers.exhibitions import vystavka_router
from routers.locations import mesto_router
from routers.news import novost_router
from routers.shop_product import tovar_router
from routers.tickets import bilet_router
from routers.users import polzovatel_router
from starlette.middleware.sessions import SessionMiddleware
from db import engine




app = FastAPI(docs_url='/')


admin = Admin(app, engine)

admin.add_model_view(CollectionsAd)
admin.add_model_view(DepartmentAd)
admin.add_model_view(EventAd)
admin.add_model_view(ExhibitionAd)
admin.add_model_view(LocationAd)
admin.add_model_view(NewsAd)
admin.add_model_view(ProductAd)
admin.add_model_view(TicketsAd)


app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


app.include_router(eksponat_router, tags=['Collections'])
app.include_router(departament_router, tags=['Departments'])
app.include_router(event_router, tags=['Events'])
app.include_router(vystavka_router, tags=['Exhibitions'])
app.include_router(mesto_router, tags=['Locations'])
app.include_router(novost_router, tags=['News'])
app.include_router(bilet_router, tags=['Tickets'])
app.include_router(tovar_router, tags=['Product'])
app.include_router(polzovatel_router, tags=['Profil'])
app.include_router(login_router)