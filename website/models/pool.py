from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from ..db import Base


class Pool(Base, UserMixin):
    __tablename__ = 'pools'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    amount = Column(Integer)
    count = Column(Integer)

    def __repr__(self):
        return '<Pool(name="{}", number="{}", amount="{}", count="{}")>'. \
            format(self.name, self.number, self.amount, self.count)
