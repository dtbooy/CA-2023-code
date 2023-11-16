from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Insert DB connection string into app.config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:charmander@127.0.0.1:5432/trello'
# connect to database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# declare model - default table name will be class name
class Card(db.Model):
    __tablename__ = 'cards'
    # make a Column (data Type, primary key)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.String(100))
    date_created = db.Column(db.Date())

class CardSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "status", "date_created")


# Create tables - make a terminal command - use flask db_create to run
@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('created tables')

# Seed database
@app.cli.command('db_seed')
def db_seed():
    # card1 = Card(
    #     title='Start the project',
    #     description = 'Stage1 - Create ERD',
    #     date_created = date.today()
    #     )
    # # Add to session queue
    # db.session.add(card1)

    # card2 = Card(
    #     title='Eat a pie',
    #     description = 'Stage2 - have a snack',
    #     date_created = date.today()
    #     )
    # # Add to session queue
    # db.session.add(card2)    

    # card3 = Card(
    # title='Marshmallow',
    # description = 'Stage3 - have another snack',
    # date_created = date.today()
    # )
    # # Add to session queue
    # db.session.add(card3)    

    cards = [
        Card(
            title='Start the project',
            description = 'Stage1 - Create ERD',
            status = "Done",
            date_created = date.today()
            ),
    
        Card(
            title='Eat a pie',
            description = 'Stage2 - have a snack',
            status = "In progress",
            date_created = date.today()
            ),
        Card(
        title='Marshmallow',
        description = 'Stage3 - have another snack',
        status = "In progress",
        date_created = date.today()
        )]
    # Execute session queue
    db.session.add_all(cards)
    db.session.commit()
    print("Database seeded")

# Drop tables command 
@app.cli.command("db_clear_tables")
def drop_all():
    db.drop_all()
    print("Tables Dropped")

@app.cli.command("all_cards")
def all_cards():
    #select * cards;
    # stmt = db.select(Card) # By default SELECT ALL unless specified
    # stmt is the SLQ statement generated by sqlalchemy
    # print(stmt) # -> SELECT cards.id, cards.title, cards.description, cards.date_created FROM cards

    # Execute statement:
    # cards = db.session.execute(stmt)
    # cards is an iterable object
    # print(cards) #-> <sqlalchemy.engine.result.ChunkedIteratorResult object at 0x7f6ccb5e9340>
    # print(cards.all()) #-> returns tuple (card object, columns selected)

    #Instead of execute call scalars ,will only return cards
    # cards = db.session.scalars(stmt)

    #print(cards) #-> [<Card 1>, <Card 2>, <Card 3>]
    # for card in cards:
    #     #print(card.__dict__)
    #     print(card.title)

    stmt = db.select(Card).limit(2)
    # If it's only 1 result we can use scalar to output string
    cards = db.session.scalars(stmt)    
    print(list(cards))

@app.cli.command("some_cards")
def some_cards():
    stmt = db.select(Card).where(db.or_(Card.id < 2, Card.status != "Done")).order_by(Card.title.desc())
    # OR: where(db.or_(card.id > 2, Card.status != "Done"))
    # AND: where(card.id > 2, Card.status != "Done")
    cards = db.session.scalars(stmt)
    for card in cards:
        print(card.title)

# Test to make sure we are connecting
@app.route('/')
def index():
    return ['Hello World!']

@app.route("/cards")
def all_the_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt) #.all()
    print(cards)
    # dumps returns string, dump return list of dicts
    return CardSchema(many=True).dump(cards)

