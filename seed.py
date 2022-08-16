
from model import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

p1=Pet(name="Skip", species="cat",photo_url="https://images.unsplash.com/photo-1573865526739-10659fec78a5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=415&q=80", age=1, notes="A very good boy", available=True)
p2=Pet(name="Ned", species="dog",photo_url="https://images.unsplash.com/photo-1587518102280-8d5fdcb68d13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=876&q=80", age=14, notes="A sweet elderly dog", available=True)

db.session.add_all([p1,p2])

db.session.commit()