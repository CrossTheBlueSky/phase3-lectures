# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, DeclarativeBase

#initialize with decrative base
class Base(DeclarativeBase):
    pass

#Creating a class that works with a table (child component of the base)

#Create tables
    #Create the engine
    #Create the tables based on out parent base

class Student(Base):
    __tablename__:"students"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    email = Column(String)
    emergency_email = Column(string)

    @validates('email')
    def validate_email(self, key, value):
        if type(value) is str and "@" in value:
            return value
        else:
            raise Exception("Not valid email")

engine = create_engine('sqlite:///school.db')
Student.__tablename__.drop(engine)
Base.metadata.create_all(engine)




# Delete all our tables and remake them


# Add a object
    # Create the engine
    # Create a session from that engine (Allowing us to create tables)
        # Using .add we can now add an object
        # Make sure to commit

with Session(engine) as session:
    

    jack = Student(
        name = "Jack"
        email = "jack@jack.com"
        emergency_email = "jack2@jack.com"
    )
    session.add(jack)
    session.commit()

#Get all data
    def get_students():
        session.query(Student).all()
    

# Filter
    def find_student():
        session.query(Student).filter(Student.name == "Jack").first()

#Update
    def update_student():
        #variablize the object you want to update, update it locally, then add it to the table
        jack = session.query(Student).filter(Student.name == "Jack")
        jack.email = "jackojack@jack.com"
        session.add(jack)
        session.commit()

#With a delete we need to first query!
    def delete_student():
        session.query(Student).filter(Student.name == "Jack").delete()
        session.commit()