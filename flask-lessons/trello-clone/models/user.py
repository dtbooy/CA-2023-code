from setup import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="Annon")
    email = db.Column(db.String, nullable=False, unique=True) # to specify NOT NULL we use nullable=False
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Establish SQL Relationship back to Card Model to embed card objects related to user
    # to do this we need to link it to the user
    cards = db.relationship("Card", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")

class UserSchema(ma.Schema):
    #cards = fields.Nested("CardSchema", many=True, exclude=["user"])
    cards = fields.List(fields.Nested("CardSchema", exclude=["user"])) # alternative method
    comments = fields.Nested("CommentSchema", many=True, exclude=["user"])

    # Validation 
    email = fields.Email(required=True) # ensures email conforms to a valid email address: [string]@[string].[string]
    password = fields.String(required=True, validate=Length(min=6, error="Password must be at least 8 characters"))
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "cards")

