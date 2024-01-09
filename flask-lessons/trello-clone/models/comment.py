from setup import db, ma
from marshmallow import fields

class Comment(db.Model):
    # TABLE NAME
    __tablename__ = 'comments'
    
    # PRIMARY KEY
    id = db.Column(db.Integer, primary_key=True)
    
    # TABLE COLUMNS
    message = db.Column(db.Text, nullable=False)
    
    # FOREIGN KEYS - established the Database FK
    # NOTE: (tablename_columnname - FK= tablename.columnname (NOTE: Not the Model Name))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="comments")
  
    card_id = db.Column(db.Integer, db.ForeignKey("cards.id"), nullable=False)
    card = db.relationship("Card", back_populates="comments")
    


class CommentSchema(ma.Schema):
    # This takes the SQLA relationship and creates a nested field 
    user = fields.Nested("UserSchema", only=["id", "name"])
    card = fields.Nested("CardSchema", only=["id", "title"])

    class Meta:
        fields = ("id", "message", "user", "card") # We add the nested field top the Schema