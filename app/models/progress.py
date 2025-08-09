# app/models/progress.py
from datetime import datetime
from app import db

class ModuleProgress(db.Model):
    __tablename__ = 'module_progress'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), index=True, nullable=False)
    module_slug = db.Column(db.String(100), index=True, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    last_accessed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('session_id', 'module_slug', name='uq_session_module'),
    )

class ProgressEvent(db.Model):
    __tablename__ = 'progress_events'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), index=True, nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    module_slug = db.Column(db.String(100), nullable=True)
    page = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
