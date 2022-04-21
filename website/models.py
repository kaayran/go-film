from sqlalchemy import Column, Integer, String

from website import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return '<User(email="{}", name="{}")>'.format(self.email, self.name)
