import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(os.environ['PS_URL'])
Session = sessionmaker(bind=engine)
