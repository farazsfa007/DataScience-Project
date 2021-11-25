from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class Classreport(Base):

    __tablename__ = "Class Report Generator"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class1 = Column(String)
    name = Column(String)
    course = Column(String)
    total_marks=Column(Integer)
    obtain_marks=Column(Integer)
    grade=Column(String)
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///mydatabase.sqlite3")
    Base.metadata.create_all(engine)