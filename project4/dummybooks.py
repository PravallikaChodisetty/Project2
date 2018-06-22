from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, BookDB, User

engine = create_engine('sqlite:///BookCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="rohini.chodisetty@gmail.com")
session.add(User1)
session.commit()

# Dummy books data
book1 = BookDB(bookName="Digital Fortress",
               authorName="DanBrown",
               coverUrl="static/images/df.jpg",
               description="a techno thriller",
               category="Thriller", user_id=1)

session.add(book1)
session.commit()

book2 = BookDB(bookName="SorceresRing",
               authorName="Morgan Rice",
               coverUrl="static/images/sr.jpg",
               description="a royal fantasy series",
               category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = BookDB(bookName="Harappa The curse of blood river",
               authorName="Vineeth bajpai",
               coverUrl="static/images/hc.jpg",
               description="a stunning mythological series",
               category="Fantasy", user_id=1)

session.add(book3)
session.commit()

book4 = BookDB(bookName="The Ramachandra Series",
               authorName="Amish Tripathi",
               coverUrl="static/images/si.jpg",
               description="Mind blowing Historical series",
               category="Mythology", user_id=1)

session.add(book4)
session.commit()

book5 = BookDB(bookName="Two States",
               authorName="Chetan Bhagath",
               coverUrl="static/images/st.jpg",
               description="A indian love story",
               category="Romance", user_id=1)

session.add(book5)
session.commit()


print ("added Books!")
