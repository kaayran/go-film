from sqlalchemy import Column, Integer, String

from ..db import Base


class Pool(Base):
    __tablename__ = 'pools'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    amount = Column(Integer)
    count = Column(Integer)
    user_id = Column(Integer)
    hash_link = Column(String)

    def __repr__(self):
        return '<Pool(name="{}", number="{}", amount="{}", count="{}", user_id="{}")>'. \
            format(self.name, self.number, self.amount, self.count, self.user_id)
