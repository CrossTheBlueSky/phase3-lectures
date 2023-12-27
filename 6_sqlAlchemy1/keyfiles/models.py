from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, validates

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content}, year={self.year})"

    #Set up a __tablename__ as the tablename!

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    content = Column(String)
    post_id = Column(Integer, ForeignKey="posts.id")


    #Validation for the year
    #This replaces the setter method
    @validates("year")
    def validate_year(self, key, year):
        if type(year) is int and 2000<year < 3000:
            return year
        else:
            raise ValueError("Not Valid Year")
    
    #If you want to validate multiple columns
    #that have the same requirements:
    @validates("title", "content")
    def validate_text(self, key, text):
        if type(text) is str and len(text) > 0:
            return text
        else:
            raise ValueError("Not Valid Text")
        
engine = create_engine('sqlite:///social_media.db')