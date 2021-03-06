from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Parties

engine = create_engine('sqlite:///votingsystem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
Party1 = Parties(id=1, name="Congress", imageUrl='congress.jpg', count=0)
session.add(Party1)
session.commit()

Party2 = Parties(id=2, name="BJP", imageUrl='bjp.jpg', count=0)
session.add(Party2)
session.commit()

Party3 = Parties(id=3, name="AAP", imageUrl='aap.jpg', count=0)
session.add(Party3)
session.commit()

User1 = User(id=1, aadhar="219224447551", voted=False, name="Vishesh Goyal", age=21)
session.add(User1)
session.commit()

User2 = User(id=2, aadhar="236165097730", voted=False, name="Rachit Taluja", age=17)
session.add(User2)
session.commit()
