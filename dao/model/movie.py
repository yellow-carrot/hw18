from setup_db import db

from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()