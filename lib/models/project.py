from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from models import Base, session

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String())
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship
    tasks = relationship('Task', back_populates='project', cascade='all, delete-orphan')
    
    # Property methods for constraints
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name or len(name) < 1:
            raise ValueError("Project name cannot be empty")
        self._name = name
    
    # ORM methods
    @classmethod
    def create(cls, name, description=""):
        project = cls(name=name, description=description)
        session.add(project)
        session.commit()
        return project
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(_name=name).first()
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    def __repr__(self):
        return f"<Project {self.id}: {self.name}>"