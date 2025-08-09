# app/routes/main.py
from flask import Blueprint, render_template, jsonify, request
from app import db
from datetime import datetime

from app.content.modules import get_modules, get_module
from app.content.quizzes import get_quiz, get_question
from app.models.progress import ModuleProgress, ProgressEvent
from app.models.quiz import QuizAttempt
from app.utils.errors import json_error_response

main = Blueprint("main", __name__)

@main.route("/")
def index():
    modules = get_modules()
    return render_template("index.html", modules=modules)

@main.route("/module/<slug>")
def module_view(slug: str):
    module = get_module(slug)
    if not module:
        return json_error_response("Module not found", 404)
    questions = get_quiz(slug)

    # Determine the next module in sequence for navigation
    modules = get_modules()
    next_module = None
    for i, m in enumerate(modules):
        if m.slug == slug:
            if i + 1 < len(modules):
                next_module = modules[i + 1]
            break

    return render_template("module.html", module=module, questions=questions, next_module=next_module)

# Health and utility endpoints
@main.route("/api/health")
def health_check():
    try:
        db.session.execute(db.text('SELECT 1'))
        return jsonify({
            "status": "ok", 
            "timestamp": datetime.utcnow().isoformat(),
            "database": "connected"
        })
    except Exception as e:
        return json_error_response(f"Health check failed: {str(e)}", 500)

# Anonymous progress APIs
@main.route("/api/progress", methods=["GET"])  # expects ?session_id=... 
def get_progress():
    session_id = request.args.get("session_id")
    if not session_id:
        return json_error_response("session_id required", 400)

    rows = ModuleProgress.query.filter_by(session_id=session_id).all()
    data = {row.module_slug: {"completed": row.completed, "last_accessed_at": row.last_accessed_at.isoformat()} for row in rows}
    return jsonify({"status": "success", "data": data})

@main.route("/api/progress", methods=["POST"])  # JSON: {session_id, module_slug, completed?}
def upsert_progress():
    payload = request.get_json(silent=True) or {}
    session_id = payload.get("session_id")
    module_slug = payload.get("module_slug")
    completed = bool(payload.get("completed", False))

    if not session_id or not module_slug:
        return json_error_response("session_id and module_slug are required", 400)

    row = ModuleProgress.query.filter_by(session_id=session_id, module_slug=module_slug).first()
    if not row:
        row = ModuleProgress(session_id=session_id, module_slug=module_slug)
        db.session.add(row)
    row.completed = completed or row.completed
    row.last_accessed_at = datetime.utcnow()
    db.session.commit()

    return jsonify({"status": "success"})

@main.route("/api/event", methods=["POST"])  # JSON: {session_id, event_type, module_slug?, page?}
def record_event():
    payload = request.get_json(silent=True) or {}
    session_id = payload.get("session_id")
    event_type = payload.get("event_type")
    module_slug = payload.get("module_slug")
    page = payload.get("page")

    if not session_id or not event_type:
        return json_error_response("session_id and event_type are required", 400)

    evt = ProgressEvent(session_id=session_id, event_type=event_type, module_slug=module_slug, page=page)
    db.session.add(evt)
    db.session.commit()

    return jsonify({"status": "success"})

# Quiz APIs
@main.route("/api/quiz/<slug>", methods=["GET"])  # rotate one question
def quiz_next(slug: str):
    session_id = request.args.get("session_id")
    if not session_id:
        return json_error_response("session_id required", 400)

    questions = get_quiz(slug)
    if not questions:
        return jsonify({"status": "success", "data": None, "completed": True, "remaining": 0, "total": 0})

    # Determine which questions have been answered correctly
    correct_ids = {a.question_id for a in QuizAttempt.query.filter_by(session_id=session_id, module_slug=slug, correct=True).all()}
    remaining = [q for q in questions if q.id not in correct_ids]

    if not remaining:
        # All questions answered correctly
        return jsonify({
            "status": "success",
            "data": None,
            "completed": True,
            "remaining": 0,
            "total": len(questions)
        })

    # Next question to attempt (first remaining not-yet-correct)
    q = remaining[0]
    return jsonify({
        "status": "success",
        "data": {
            "id": q.id,
            "prompt": q.prompt,
            "options": q.options
        },
        "completed": False,
        "remaining": len(remaining),
        "total": len(questions)
    })

@main.route("/api/quiz/<slug>", methods=["POST"])  # submit answer
def quiz_submit(slug: str):
    payload = request.get_json(silent=True) or {}
    session_id = payload.get("session_id")
    qid = payload.get("question_id")
    selected = payload.get("selected")

    if not session_id or not qid or not selected:
        return json_error_response("session_id, question_id and selected are required", 400)

    q = get_question(slug, qid)
    if not q:
        return json_error_response("Question not found", 404)

    is_correct = (selected == q.correct)

    att = QuizAttempt(session_id=session_id, module_slug=slug, question_id=qid, selected=selected, correct=is_correct)
    db.session.add(att)
    db.session.commit()

    return jsonify({
        "status": "success",
        "data": {
            "correct": is_correct,
            "help": q.help
        }
    })
