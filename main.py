from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"], allow_methods=["*"])

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


@app.get("/greet/")

def greet():
    return "Aloha!" 

products = [
    Product(id=1,name="phone", description="low", price=99,quantity=10),
    Product(id=2,name="laptop", description="mid", price=299,quantity=10),
    Product(id=3,name="desktop", description="high", price=999,quantity=10)
]


def init_db():
    db=session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for p in products:
            db.add(database_models.Product(**p.model_dump()))
        db.commit()

init_db()


@app.get("/products/")
def get_products(db : Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_products_id(id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first();
    if db_product:
        return db_product
    return "No product found"


@app.post("/products/")
def add_products(p:Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**p.model_dump()))
    db.commit() 
    return "successfully added"


@app.put("/products/{id}")
def replace_products(id : int , p:Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first();
    if db_product:
        db_product.name=p.name
        db_product.description=p.description
        db_product.price=p.price
        db_product.quantity=p.quantity
        db.commit()
        return "Updated Successfully"
    return "Not Found"


@app.delete("/products/{id}")
def delete_products(id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first();
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Deleted Successfully"
    return "Not Found"