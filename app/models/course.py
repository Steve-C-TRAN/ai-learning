# models/tran.py

from datetime import datetime
from app import db
import enum

# Association Tables

# Enums

# Core Models
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    