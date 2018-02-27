from models import Base
from sqlalchemy import create_engine

path='postgresql://localhost/test'
engine = create_engine(path)
Base.metadata.create_all(engine)
