import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(f"{os.environ.get("DATABASE_URL")}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

