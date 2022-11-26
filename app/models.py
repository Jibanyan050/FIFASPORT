from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    long_name = db.Column(db.Text(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    dob = db.Column(db.Text(), nullable=False)
    height_cm = db.Column(db.Integer(), nullable=False)
    weight_kg = db.Column(db.Integer(), nullable=False)
    club = db.Column(db.Text(), nullable=False)
    nationality = db.Column(db.Text(), nullable=False)
    overall = db.Column(db.Integer(), nullable=False)

    def to_dict(self):
        return{
           'long_name': self.long_name,
           'age': self.age,
           'dob': self.dob,
           'height_cm': self.height_cm,
           'weight_kg': self.weight_kg,
           'nationality': self.nationality,
           'club': self.club,
           'overall': self.overall
        }
