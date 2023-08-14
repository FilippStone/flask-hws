from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

engine = create_engine("sqlite:///shop.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)


Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    status: str


class OrderUpdate(BaseModel):
    user_id: int = None
    product_id: int = None
    status: str = None


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    return {"error": "User not found"}


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == user_id).update(user.dict(exclude_unset=True))
    db.commit()
    updated_user = db.query(User).filter(User.id == user_id).first()
    if updated_user:
        return updated_user
    return {"error": "User not found"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted"}


@app.post("/orders")
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@app.get("/orders/{order_id}")
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        return order
    return {"error": "Order not found"}


@app.put("/orders/{order_id}")
async def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db.query(Order).filter(Order.id == order_id).update(order.dict(exclude_unset=True))
    db.commit()
    updated_order = db.query(Order).filter(Order.id == order_id).first()
    if updated_order:
        return updated_order
    return {"error": "Order not found"}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    db.query(Order).filter(Order.id == order_id).delete()
    db.commit()
    return {"message": "Order deleted"}


@app.post("/products")
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.get("/products/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    return {"error": "Product not found"}


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == product_id).update(product.dict(exclude_unset=True))
    db.commit()
    updated_product = db.query(Product).filter(Product.id == product_id).first()
    if updated_product:
        return updated_product
    return {"error": "Product not found"}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
    return {"message": "Product deleted"}
