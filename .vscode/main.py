from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database connection URL
db_url = 'postgresql://postgres.gnfkhgexfjijwpnnispg:[2712Ytnjkjubz!]@aws-0-eu-central-1.pooler.supabase.com:6543/postgres'
engine = create_engine(db_url.replace("postgres://", "postgresql://", 1))
Session = sessionmaker(bind=engine)
session = Session()

# Define a model
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create the table
Base.metadata.create_all(engine)

# Insert a record
new_user = User(name='John Doe')
session.add(new_user)
session.commit()

# Query records
users = session.query(User).all()
for user in users:
    print(user.id, user.name)

# Print a success message
print("Hurray! database connection is working.")
