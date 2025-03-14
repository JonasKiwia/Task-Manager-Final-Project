from models import Base, engine
from models.project import Project
from models.task import Task

if __name__ == '__main__':
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Done!")