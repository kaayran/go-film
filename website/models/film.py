from sqlalchemy import Column, Integer, String, Float

from ..db import Base


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    kinopoisk_id = Column(Integer)
    name_rus = Column(String)
    name_original = Column(String)
    url = Column(String)
    image = Column(String)
    rating_kinopoisk = Column(Float)
    rating_imdb = Column(Float)
    votes_kinopoisk = Column(Integer)
    votes_imdb = Column(Integer)
    user_id = Column(Integer)

    def __repr__(self):
        return '<Film(film_id="{}", name_eng="{}", rating_kinopoisk="{}">'. \
            format(self.kinopoisk_id, self.name_original, self.rating_kinopoisk)
