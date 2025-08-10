# app/content/loader.py
"""
Lightweight course discovery for the C-TRAN AI Learning App.

Discovers any Python module under app.content that exposes both:
- get_course_meta() -> CourseMeta-like object (must include a 'slug' attribute)
- get_modules() -> list of Module-like objects

Returns simple Python dicts so we don't depend on identical dataclass types
across course files.
"""
from __future__ import annotations

import importlib
import pkgutil
from typing import Any, Dict, List, Optional

PACKAGE = "app.content"

# In-memory cache to avoid re-importing on every request
_DISCOVERY_CACHE: Optional[List[Dict[str, Any]]]= None


def _is_course_module(mod: Any) -> bool:
    return hasattr(mod, "get_course_meta") and hasattr(mod, "get_modules")


def _safe_get_attr(obj: Any, attr: str, default: Any = None) -> Any:
    try:
        return getattr(obj, attr)
    except Exception:
        return default


def discover_courses(force_reload: bool = False) -> List[Dict[str, Any]]:
    """Discover courses under app.content.

    Returns a list of dicts with keys:
      - slug: str
      - meta: Any (object returned by get_course_meta())
      - modules: list[Any] (objects returned by get_modules())
      - source: str (python module path)
    """
    global _DISCOVERY_CACHE
    if _DISCOVERY_CACHE is not None and not force_reload:
        return _DISCOVERY_CACHE

    results: List[Dict[str, Any]] = []

    pkg = importlib.import_module(PACKAGE)
    for _, name, ispkg in pkgutil.iter_modules(pkg.__path__):
        # Skip packages (folders) and obvious non-course files by convention
        if ispkg:
            continue
        if name in {"__init__", "quizzes", "quizzes2", "models", "routes", "forms", "utils"}:
            continue
        mod_path = f"{PACKAGE}.{name}"
        try:
            mod = importlib.import_module(mod_path)
        except Exception:
            # Ignore broken imports; we only care about valid course files
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
            # If a course file raises during accessor calls, skip it
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
        })
    return items
