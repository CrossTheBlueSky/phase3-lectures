# You may see within the reading Table(), it is a way of doing our
# current declrative mapping (Setting it up with a class)
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-mapping
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, DeclarativeBase,relationship
# one to many (relating table object in quotes)
# ONE
# relationship('Many_object', backref = 'one_table_name')
# Many
# Column(Integer(), ForeignKey('one_table.id'))
class Base(DeclarativeBase):
    pass

#Creating a class that works with a table (child component of the base)
class Student(Base):
    __tablename__:"students"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    email = Column(String)
    emergency_email = Column(string)
    schedules_conn = relationship("Schedule", back_populates="students")

class Schedule(Base):
    __tablename__:"schedules"
    id = Column(Integer, primary_key=True)
    class_name = Column(String)
    period = Column(String)
    studentId = Column(Integer, ForeignKey("students.id"))
    student_conn = relationship("Student", back_populates='schedules')


engine = create_engine('sqlite:///one_to_many.db')
Base.metadata.create_all(engine)

# Many to many (Join) (relating table object in quotes)
# MANY

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
Base = declarative_base()
engine = create_engine('sqlite:///many_to_many.db')