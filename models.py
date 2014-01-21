#Author: Ian Auld
#Date: '1/15/14'
#PyVer: 3.3
#Title: 'Flask_Inventory_Manager'
#Description:


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.sqlalchemy import SQLAlchemy


Base = declarative_base()
db = SQLAlchemy()


class Shelf(Base):
    __tablename__ = 'shelf'
    shelf_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)


class Item(db.Model):
    __tablename__ = 'item'
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String(50), nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self, sku, title):
        self.sku = sku
        self.title = title

class Bin(Base):
    __tablename__ = 'bin'
    bin_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    shelf_id = Column(Integer, ForeignKey('shelf.shelf_id'))


class BinItem(Base):
    __tablename__ = 'bin_item'
    bin_id = Column(Integer, ForeignKey('bin.bin_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.item_id'), primary_key=True)
    qty = Column(Integer, nullable=False)


