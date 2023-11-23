from flask import request, jsonify, abort, make_response
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import timedelta, date 

# Import Configuration
from setup import * # app, db, ma, bcrypt, jwt

#IMPORT MODELS
from models.user import User, UserSchema
from models.card import Card, CardSchema

from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp

def admin_required():
    # check is_admin
    identity = get_jwt_identity()
    stmt = db.select(User).where(User.email == identity)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return abort(jsonify(error=401, description="You must be an admin")), 401
        #abort(make_response(jsonify(message="Must be admin to proceed"), 401))


app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

#------------------------ROUTES ----------------|



@app.cli.command("some_cards")
def some_cards():
    stmt = db.select(Card).where(db.or_(Card.id < 2, Card.status != "Done")).order_by(Card.title.desc())
    # OR: where(db.or_(card.id > 2, Card.status != "Done"))
    # AND: where(card.id > 2, Card.status != "Done")
    cards = db.session.scalars(stmt)
    for card in cards:
        print(card.title)
    print(CardSchema(many=True).dump(cards))

# Test to make sure we are connecting
@app.route('/')
def index():
    return ['Hello World!']

@app.route("/cards")
@jwt_required()
def all_the_cards():
    # call is_admin check function
    # admin_required()

    stmt = db.select(Card)
    cards = db.session.scalars(stmt) #.all()
    print(cards)
    # dumps returns string, dump return list of dicts
    return CardSchema(many=True).dump(cards)

# ------------------------Error Handler --------------

# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     # print(err)
#     print((err.__dict__))
#     return {"error": str(err)}
