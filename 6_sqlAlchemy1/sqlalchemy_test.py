# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, validates




if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    # engine = create_engine('sqlite:///hiking.db')
    engine = create_engine('sqlite:///social_media.db')


    with Session(engine) as session:

    #CREATE
        p1 = Post(
            title = "css 101",
            content = "css is cool",
            year = 2023
        )

        session.add(p1)
        session.commit()

    #READ

        all_post = session.query(Post).all()
        one_post = session.query(Post).limit(1).all()
        filter_post = session.query(Post).filter(Post.id == 1).first()

    #UPDATE
        one_post.year = 1990
        one_post.year = "New Content"
        session.add(one_post)
        session.commit()
    
    #DELETE
        second_post = session.query(Post).filter(Post.id == 2).first()

        #If you do .all instead of .first() you will get a list of objects

        session.delete(second_post)
        


    # create schema (which will create the mountain schema) 

    # Now we can use an with statement
    # with Session(engine) as session:
    # Within this with we now do anything with the session! 
    '''
    Session.add()
    Session.query()
        .all()
        .orderby() ex: Table.name.desc()
        .limit()
        .filter() ex Table.name = "name"
        .update() ex {Table.name: newname}
    Session.delete()
    Session.commit()
    '''
    # To drop a table use TableClass.__table__.drop(engine)
    pass