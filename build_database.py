import os
from config import db
from models import Director, Movie

# Create the database
db.create_all()

db.session.commit()
