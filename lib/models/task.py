from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from models import Base, session

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String())
    priority = Column(Integer, default=1)  # 1=low, 2=medium, 3=high
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime)
    
    # Foreign key
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    
    # Relationship
    project = relationship('Project', back_populates='tasks')
    
    # Property methods for constraints
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not title or len(title) < 1:
            raise ValueError("Task title cannot be empty")
        self._title = title
    
    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, priority):
        if priority not in [1, 2, 3]:
            raise ValueError("Priority must be 1 (low), 2 (medium), or 3 (high)")
        self._priority = priority
    
    # ORM methods
    @classmethod
    def create(cls, title, project_id, description="", priority=1, due_date=None):
        task = cls(
            title=title,
            description=description,
            priority=priority,
            project_id=project_id,
            due_date=due_date
        )
        session.add(task)
        session.commit()
        return task
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_project(cls, project_id):
        return session.query(cls).filter_by(project_id=project_id).all()
    
    def mark_completed(self):
        self.completed = True
        session.commit()
    
    def mark_incomplete(self):
        self.completed = False
        session.commit()
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"<Task {self.id}: {self.title} ({status})>"