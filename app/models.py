from . import db
from sqlalchemy.sql import func

class TodoModel (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = func.now())
    
    #user.id points to User class. One to many relation (one user, many to do)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    def __repr__(self):
        return f"<Task({self._id}),    content = ({self.content})>"

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'content'    : self.content,
           'date_created': dump_datetime(self.date_created)
       }
    
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150))
    #TodoModel  points to TodoModel  class. Stores all the to_do the user owns.
    # to_dos = db.relationship('TodoModel')

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]