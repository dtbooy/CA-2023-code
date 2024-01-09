from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.card import Card, CardSchema
from auth import authorize
from blueprints.comments_bp import comments_bp


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")
cards_bp.register_blueprint(comments_bp)

# Get All Cards
@cards_bp.route("/")
@jwt_required()
def get_all_cards():
    # call is_admin check function
    authorize()

    stmt = db.select(Card)
    cards = db.session.scalars(stmt) #.all()
    # dumps returns string, dump return list of dicts
    return CardSchema(many=True, exclude=["user.cards"]).dump(cards)

# Get a single Card 
@cards_bp.route("/<int:id>")
@jwt_required()
def get_single_card(id):
    
    # Find card ID in database 
    stmt = db.select(Card).filter_by(id=id) # where(Card.id == id)
    card = db.session.scalar(stmt)

    # If card ID doesn't exist return 404
    if not card:
        return {"Error": "Card not Found"}, 404
    
    # dumps returns string, dump return list of dicts
    # print(card.user) # Now that we have established user as a nested property of card we can access 
    return CardSchema().dump(card)

# Add a card
@cards_bp.route("/", methods=["POST"])
@jwt_required()
def create_card():

    card_info = CardSchema(exclude=["id", "date_created"]).load(request.json)
    card = Card(
        title = card_info["title"],
        description = card_info.get("description", ""),
        status = card_info.get("status", "To Do"),
        user_id = get_jwt_identity()
    )
    db.session.add(card)
    db.session.commit()
    return CardSchema().dump(card), 201


# Update a card
@cards_bp.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_card(id):
    # Validate card exists
    card_info = CardSchema(exclude=["id", "date_created"]).load(request.json)
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if not card:
        return {"Error" : "Card Not Found"}, 404

    # Authorization - pass the user_id of the card to authorization fn
    authorize(card.user_id)

    #update card
    card.title = card_info.get("title", card.title)
    card.description = card_info.get("description", card.description)
    card.status = card_info.get("status", card.status)

    # do not need to add card (already a db object) just commit to save changes to db
    db.session.commit()
    return CardSchema().dump(card), 200

#delete a card
@cards_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        # Authorization - pass the user_id of the card to authorization fn
        authorize(card.user_id)

        db.session.delete(card)
        db.session.commit()
        return {}, 200
    else:
        return {"Error" : "Card not found"}, 404

# ------------------------Error Handler --------------

# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     # print(err)
#     print((err.__dict__))
#     return {"error": str(err)}


