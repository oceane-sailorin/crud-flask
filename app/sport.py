from app import db


class Wintersport(db.Model):

    """
    Create a Department table
    """

    __tablename__ = 'wintersports'

    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Wintersport: {}>".format(self.name)
