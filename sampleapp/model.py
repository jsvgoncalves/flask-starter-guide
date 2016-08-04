# -*- coding: utf-8 -*-
#
# Joao Goncalves

from database import db


class User(db.Model):
    """Database model for SQLAlchemy."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r : %r>' % (self.name, self.email)
