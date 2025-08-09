# app/models/quiz.py
from datetime import datetime
from app import db

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), index=True, nullable=False)
    module_slug = db.Column(db.String(100), index=True, nullable=False)
    question_id = db.Column(db.String(100), nullable=False)
    selected = db.Column(db.String(10), nullable=False)
    correct = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    __table_args__ = (
        db.Index('ix_attempt_session_module', 'session_id', 'module_slug'),
    )
