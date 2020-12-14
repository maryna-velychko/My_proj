from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import exc

Base = declarative_base()


class Costumer(Base):
    __tablename__ = 'costumer'
    id = Column(Integer, primary_key=True)
    name_costumer = Column(String(100))
    email = Column(String(100))
    costumer_product = relationship('CostumerProduct')

    def __repr__(self):
        return "<Costumer(id='{}', name='{}', email={}>" \
            .format(self.id, self.name_costumer, self.email)


class Firm(Base):
    __tablename__ = 'firm'
    name_firm = Column(String(30), primary_key=True)
    address = Column(String(30))
    firm_product = relationship("FirmProduct")
    def __repr__(self):
        return "<Firm(name_firm='{}', address='{}'" \
            .format(self.name_firm, self.address)


class Product(Base):
    __tablename__ = 'product'
    article = Column(Integer, primary_key=True)
    name_product = Column(String(30))
    price = Column(Float)
    costumer_product = relationship("CostumerProduct")
    firm_product = relationship("FirmProduct")
    def __repr__(self):
        return "<Firm(article='{}', name_product='{}', price='{}'" \
            .format(self.article, self.name_product, self.price)


class CostumerProduct(Base):
    __tablename__ = 'costumer_product'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, ForeignKey('costumer.id'), primary_key=True)
    article = Column(Integer, ForeignKey('product.article'), primary_key=True)
    def __repr__(self):
        return "<CostumerProduct(id='{}', article='{}'" \
            .format(self.id, self.article)


class FirmProduct(Base):
    __tablename__ = 'costumer_product'
    __table_args__ = {'extend_existing': True}
    name_firm = Column(String(100), ForeignKey('firm.name_firm'), primary_key=True)
    article = Column(Integer, ForeignKey('product.article'), primary_key=True)

    def __repr__(self):
        return "<CostumerProduct(name_firm='{}', article='{}'" \
            .format(self.name_firm, self.article)


def create(s, table, parameter_1, parameter_2):
    try:
        arg = None
        if table == 1:
            arg = Costumer(name_costumer=parameter_1, email=parameter_2)
        elif table == 2:
            arg = Firm(name_firm=parameter_1, address=parameter_2)
        elif table == 3:
            arg = Product(name_product=parameter_1, price=parameter_2)
        elif table == 4:
            arg = CostumerProduct(id=parameter_1, article=parameter_2)
        elif table == 5:
            arg = FirmProduct(name_firm=parameter_1, article=parameter_2)
        s.add(arg)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        print("Error")


def edit(s, table, param1, param2, param3):
        x = None
        if table == 1:
            x = s.query(Costumer).get(param3)
            x.name_costumer = param1
            x.email = param2
        elif table == 2:
            x = s.query(Firm).get(param3)
            x.name_firm = param1
            x.address = param2
        elif table == 3:
            x = s.query(Product).get(param3)
            x.name_product = param1
            x.price = param2
        elif table == 4:
            x = s.query(CostumerProduct).get(param3)
            x.id = param1
            x.article = param2
        elif table == 5:
            x = s.query(FirmProduct).get(param3)
            x.name_firm = param1
            x.article = param2
        s.add(x)
        s.commit()
        print("Error")


def delete(s, table, param):
    try:
        x = None
        if table == 1:
            x = s.query(Costumer).get(param)
        elif table == 2:
            x = s.query(Firm).get(param)
        elif table == 3:
            x = s.query(Product).get(param)
        elif table == 4:
            x = s.query(CostumerProduct).get(param)
        elif table == 5:
            x = s.query(FirmProduct).get(param)
        s.delete(x)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        print("Error")


def print_table(s, table):
    if table == 1:
        for cost in s.query(Costumer).all():
            print(cost)
    elif table == 2:
        for firm in s.query(Firm).all():
            print(firm)
    elif table == 3:
        for prod in s.query(Product).all():
            print(prod)
    elif table == 4:
        for cost_prod in s.query(CostumerProduct).all():
            print(cost_prod)
    elif table == 5:
        for cost_firm in s.query(FirmProduct).all():
            print(cost_firm)
