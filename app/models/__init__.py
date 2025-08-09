# Minimal model exports for the C-TRAN AI Learning App
from app import db  # ensures db is available to submodules

# Export training app models
from .progress import ModuleProgress, ProgressEvent  # noqa: F401
from .quiz import QuizAttempt  # noqa: F401

__all__ = [
    'ModuleProgress', 'ProgressEvent', 'QuizAttempt'
]

