from setup import db, ma

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

