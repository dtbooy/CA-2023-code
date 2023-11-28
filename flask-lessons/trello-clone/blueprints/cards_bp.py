from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from setup import db
from models.card import Card, CardSchema
from auth import admin_required

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# Get All Cards
@cards_bp.route("/")
@jwt_required()
def get_all_cards():
    # call is_admin check function
    admin_required()

    stmt = db.select(Card)
    cards = db.session.scalars(stmt) #.all()
    # dumps returns string, dump return list of dicts
    return CardSchema(many=True).dump(cards)

# Get a single Card 
@cards_bp.route("/<int:id>")
@jwt_required()
def get_single_card(id):
    # call is_admin check function
    admin_required()
    
    # Find card ID in database 
    stmt = db.select(Card).filter_by(id=id) # where(Card.id == id)
    card = db.session.scalar(stmt)

    # If card ID doesn't exist return 404
    if not card:
        return {"Error": "Card not Found"}, 404
    
    # dumps returns string, dump return list of dicts
    return CardSchema().dump(card)

@cards_bp.route("/", methods=["POST"])
@jwt_required()
def create_card():
    card_info = CardSchema(exclude=["id", "date_created"]).load(request.json)
    print(card_info)
    return request.json

# ------------------------Error Handler --------------

# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     # print(err)
#     print((err.__dict__))
#     return {"error": str(err)}