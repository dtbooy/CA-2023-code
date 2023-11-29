from setup import db, ma
from datetime import datetime
from marshmallow import fields


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
    user = db.relationship("User")

class CardSchema(ma.Schema):
    # This takes the SQLA relationship and creates a nested field 
    user = fields.Nested("UserSchema", exclude=["password"])

    class Meta:
        fields = ("id", "title", "description", "status", "date_created", "user") # We add the nested field top the Schema

