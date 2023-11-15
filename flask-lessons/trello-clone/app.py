from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

# Insert DB connection string into app.config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:charmander@127.0.0.1:5432/trello'
# connect to database
db = SQLAlchemy(app)

# declare model - default table name will be class name
class Card(db.Model):
    __tablename__ = 'cards'
    # make a Column (data Type, primary key)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    date_created = db.Column(db.Date())

# Create tables - make a terminal command - use flask db_create to run
@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('created tables')

# Seed database
@app.cli.command('db_seed')
def db_seed():
    card = Card(
        title='Start the project',
        description = 'Stage1 - Create ERD',
        date_created = date.today()
        )
    # Add to session queue
    db.session.add(card)
    # Execute session queue
    db.session.commit()
    print("Database seeded")

# Test to make sure we are connecting
@app.route('/')
def index():
    return ['Hello World!']

