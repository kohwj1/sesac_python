from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE = 'database/db/mycrm.db'

engine = create_engine(f'sqlite:///{DATABASE}', echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    Id = Column(String, primary_key=True)
    Name = Column(String)
    Gender = Column(String)
    Age = Column(Integer)
    Birthdate = Column(String)
    Address = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    Id = Column(String, primary_key=True)
    OrderAt = Column(DateTime)
    StoreId = Column(String)
    UserId = Column(String)

class Store(Base):
    __tablename__ = 'stores'
    Id = Column(String, primary_key=True)
    Name = Column(String)
    Type = Column(String)
    Address = Column(String)

class Item(Base):
    __tablename__ = 'items'
    Id = Column(String, primary_key=True)
    Name = Column(String)
    Type = Column(String)
    UnitPrice = Column(Integer)

class OrderItem(Base):
    __tablename__ = 'orderitems'
    Id = Column(String, primary_key=True)
    OrderId = Column(String)
    ItemId = Column(String)

