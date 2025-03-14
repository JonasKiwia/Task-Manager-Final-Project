from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database in the current directory
engine = create_engine('sqlite:///taskmaster.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Import models to make them available from models module
from models.project import Project
from models.task import Task