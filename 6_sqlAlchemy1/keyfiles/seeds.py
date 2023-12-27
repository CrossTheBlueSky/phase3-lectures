from models import *
from faker import Faker
import random

if __name__ == '__main__':
    Post.__table__.drop(engine)
    Comments.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for i in range(10):
            p = Post(
                title = Faker().sentence(),
                content = Faker().paragraph(),
                year = random.randint(2000, 3000)
            )
            session.add(p)
        session.commit()

        for i in range(100):
            c = Comments(
                user = Faker().name(),
                content = Faker().paragraph(),
                post_id = random.randint(1, 10)
            )
            session.add(c)
        session.commit()