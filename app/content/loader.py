# app/content/loader.py
"""
Lightweight course discovery for the C-TRAN AI Learning App.

Discovers any course package under app.content that exposes:
- modules.py with get_course_meta() (must include a 'slug' attribute)
- modules.py with get_modules() -> list of Module-like objects
- quizzes.py (optional) with QUIZZES mapping

Returns simple Python dicts so we don't depend on identical dataclass types
across course files.
"""
from __future__ import annotations

import importlib
import pkgutil
from typing import Any, Dict, List, Optional

PACKAGE = "app.content"

# In-memory cache to avoid re-importing on every request
_DISCOVERY_CACHE: Optional[List[Dict[str, Any]]] = None


def _is_course_module(mod: Any) -> bool:
    return hasattr(mod, "get_course_meta") and hasattr(mod, "get_modules")


def _safe_get_attr(obj: Any, attr: str, default: Any = None) -> Any:
    try:
        return getattr(obj, attr)
    except Exception:
        return default


def discover_courses(force_reload: bool = False) -> List[Dict[str, Any]]:
    """Discover courses under app.content using a package-per-course layout.

    Expected layout per course:
      app/content/<course>/
        __init__.py
        modules.py  -> defines get_course_meta(), get_modules()
        quizzes.py  -> defines QUIZZES (optional)

    Returns a list of dicts with keys:
      - slug: str
      - meta: Any (object returned by get_course_meta())
      - modules: list[Any] (objects returned by get_modules())
      - source: str (python module path to the course modules, e.g., app.content.ai_intro.modules)
    """
    global _DISCOVERY_CACHE
    if _DISCOVERY_CACHE is not None and not force_reload:
        return _DISCOVERY_CACHE

    results: List[Dict[str, Any]] = []

    pkg = importlib.import_module(PACKAGE)
    for _, name, ispkg in pkgutil.iter_modules(pkg.__path__):
        # Only consider packages as courses
        if not ispkg:
            continue
        mod_path = f"{PACKAGE}.{name}.modules"
        try:
            mod = importlib.import_module(mod_path)
        except Exception:
            # Skip folders without a modules.py or with import errors
            continue
        if not _is_course_module(mod):
            continue
        try:
            meta = mod.get_course_meta()
            modules = mod.get_modules()
            slug = _safe_get_attr(meta, "slug", name)
            results.append({
                "slug": slug,
                "meta": meta,
                "modules": modules,
                "source": mod_path,
            })
        except Exception:
            # Skip courses that raise during accessors
            continue

    _DISCOVERY_CACHE = results
    return results


def get_course_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Return a single discovered course by its meta.slug."""
    for c in discover_courses():
        if str(c.get("slug")) == slug:
            return c
    return None


def list_course_summaries() -> List[Dict[str, Any]]:
    """Return summaries convenient for card rendering on the landing page.

    Each dict includes: slug, title, summary, duration, level, thumbnail, hero_image, og_image, tags.
    All fields are best-effort; missing values fall back to None.

    Sorting (hybrid):
      1) If meta.order is provided (number or numeric string), sort ascending by it
      2) Otherwise by level rank (Introductory/Beginner -> Intermediate -> Advanced)
      3) Tie-break by title (A–Z)
    """
    items: List[Dict[str, Any]] = []
    for c in discover_courses():
        meta = c.get("meta")
        items.append({
            "slug": c.get("slug"),
            "title": _safe_get_attr(meta, "title"),
            "summary": _safe_get_attr(meta, "summary"),
            "duration": _safe_get_attr(meta, "duration"),
            "level": _safe_get_attr(meta, "level"),
            "hero_image": _safe_get_attr(meta, "hero_image"),
            "thumbnail": _safe_get_attr(meta, "thumbnail"),
            "og_image": _safe_get_attr(meta, "og_image"),
            "tags": _safe_get_attr(meta, "tags", []),
            # Optional explicit ordering if the course meta defines it
            "order": _safe_get_attr(meta, "order"),
        })

    def level_rank(level_val: Optional[str]) -> int:
        lvl = (level_val or "").strip().lower()
        if lvl in {"introductory", "intro", "beginner", "foundational", "foundations"}:
            return 0
        if lvl in {"intermediate"}:
            return 1
        if lvl in {"advanced", "expert"}:
            return 2
        return 99

    def sort_key(it: Dict[str, Any]):
        ord_raw = it.get("order")
        # Courses with explicit order come first (bucket 0), others later (bucket 1)
        try:
            ord_val = float(ord_raw)
            order_bucket = 0
        except Exception:
            ord_val = float("inf")
            order_bucket = 1
        return (
            order_bucket,
            ord_val,
            level_rank(it.get("level")),
            (it.get("title") or "").lower(),
        )

    items.sort(key=sort_key)
    return items


# --- Quizzes helpers (per-course) ---

def _quizzes_module_path_from_source(source: str) -> Optional[str]:
    """Given a source like 'app.content.<course>.modules', return 'app.content.<course>.quizzes'."""
    try:
        if source.endswith(".modules"):
            return source.rsplit(".", 1)[0] + ".quizzes"
    except Exception:
        pass
    return None


def import_course_quizzes_module_by_slug(course_slug: str):
    """Import the quizzes module for a given course slug, or return None if missing."""
    course = get_course_by_slug(course_slug)
    if not course:
        return None
    qpath = _quizzes_module_path_from_source(course.get("source", ""))
    if not qpath:
        return None
    try:
        return importlib.import_module(qpath)
    except Exception:
        return None


def get_course_quizzes(course_slug: str) -> Dict[str, Any]:
    """Return the QUIZZES dict for a course, or {} if not present."""
    qmod = import_course_quizzes_module_by_slug(course_slug)
    if not qmod:
        return {}
    return getattr(qmod, "QUIZZES", {}) or {}


def get_module_quiz(course_slug: str, module_slug: str) -> List[Any]:
    """Return the list of questions for a module within a course (raw objects from quizzes.py)."""
    quizzes = get_course_quizzes(course_slug)
    return quizzes.get(module_slug, [])


def get_module_question(course_slug: str, module_slug: str, question_id: str) -> Optional[Any]:
    """Return a single question object for a module within a course by id, or None."""
    for q in get_module_quiz(course_slug, module_slug):
        if getattr(q, "id", None) == question_id:
            return q
    return None
