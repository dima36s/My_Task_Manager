from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Manger(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.TEXT)
    is_complete = db.Column(db.BOOLEAN)
