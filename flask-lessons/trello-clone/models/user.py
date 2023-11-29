from setup import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True) # to specify NOT NULL we use nullable=False
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Establish SQL Relationship back to Card Model to embed card objects related to user
    # to do this we need to link it to the user
    cards = db.relationship("Card", back_populates="user")

class UserSchema(ma.Schema):
    #cards = fields.Nested("CardSchema", many=True, exclude=["user"])
    cards = fields.List(fields.Nested("CardSchema", exclude=["user"])) # alternative method
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "cards")

