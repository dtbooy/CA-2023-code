from setup import db, ma
from datetime import datetime
from marshmallow import fields
from marshmallow.validate import OneOf, Regexp, Length, And
# RegEx: regular expressions

VALID_STATUSES = ("To Do", "Done", "In Progress", "Testing", "Deployed", "Cancelled")

# declare model - default table name will be class name
class Card(db.Model):
    # TABLE NAME
    __tablename__ = 'cards'
    
    # PRIMARY KEY
    id = db.Column(db.Integer, primary_key=True)
    
    # TABLE COLUMNS
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    status = db.Column(db.String(100), default="To Do")
    date_created = db.Column(db.Date(), default=datetime.now().strftime("%Y-%m-%d"))

    # FOREIGN KEYS - established the Database FK
    # NOTE: (tablename_columnname - FK= tablename.columnname (NOTE: Not the Model Name))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Establish an SLQAlchemy relationship: (Model_Name)
    # NOTE: This does not impact DB, this is just an SQLA relationship
    # NOTE: we need to link this to the relationship in Cards
    user = db.relationship("User", back_populates="cards")
    comments = db.relationship("Comment", back_populates="card")

class CardSchema(ma.Schema):
    # This takes the SQLA relationship and creates a nested field 
    user = fields.Nested("UserSchema", exclude=["password", "cards"])
    comments = fields.Nested("CommentSchema", many=True, exclude=["card"])

    # validation
    status = fields.String(validate=OneOf(VALID_STATUSES))
    # Title can only use letters, numbers or spaces
    title = fields.String(required=True, validate=And(
        Regexp("^[0-9a-zA-Z ]+$", error="Title must contain only letters, numbers and spaces."),
        Length(min=3, error="Title must be at least 3 characters long")
        ))

    class Meta:
        fields = ("id", "title", "description", "status", "date_created", "user", "comments") # We add the nested field top the Schema

