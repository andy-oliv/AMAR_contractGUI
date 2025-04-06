import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Pyinstaller configuration to make the GUI .exe able to detect the .env variables
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(base_path, '.env')
load_dotenv(dotenv_path=env_path)

database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
