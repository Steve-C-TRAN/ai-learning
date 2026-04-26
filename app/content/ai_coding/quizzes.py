# app/content/quizzes.py
# Updated quizzes aligned to the Claude Code in VS Code, template-first course

from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class QuizQuestion:
    id: str
    prompt: str
    options: Dict[str, str]  # key -> label (e.g., 'a' -> 'Answer text')
    correct: str             # key of the correct option
    help: Optional[str] = None

# Map module slug -> list of QuizQuestion
QUIZZES: Dict[str, List[QuizQuestion]] = {
    "introduction": [
        QuizQuestion(
            id="intro-1",
            prompt="What should happen before Claude Code starts implementing a production feature?",
            options={
                "a": "Ask it to invent a fresh architecture from scratch",
                "b": "Start from the approved template architecture and identify safe extension points",
                "c": "Disable tests so the model can move faster",
                "d": "Let it edit any file in the repo without constraints"
            },
            correct="b",
            help="The course is explicitly template-first: Claude Code extends an approved architecture rather than creating one ad hoc."
        ),
        QuizQuestion(
            id="intro-2",
            prompt="What is an approved template architecture in this course?",
            options={
                "a": "A starter repo plus the organization&apos;s agreed stack, structure, controls, and delivery patterns",
                "b": "Any project layout Claude Code prefers on a given day",
                "c": "A prompt library with no code or deployment conventions",
                "d": "A blank workspace that the model fills in from scratch"
            },
            correct="a"
        ),
    ],
    "vscode-setup": [
        QuizQuestion(
            id="vsc-1",
            prompt="Which workspace setup is preferred before using Claude Code on a real task?",
            options={
                "a": "An empty folder with no repo context",
                "b": "The approved repository or a project derived from the approved template",
                "c": "A downloads directory containing random files",
                "d": "A workspace with secrets committed so the model can see them"
            },
            correct="b",
            help="Open the real repo or template-derived project so the model inherits the existing architecture and standards."
        ),
        QuizQuestion(
            id="vsc-2",
            prompt="Which file should still be excluded from prompts, version control, and model sharing?",
            options={
                "a": "README.md",
                "b": "requirements.txt",
                "c": ".env",
                "d": "tests/test_app.py"
            },
            correct="c"
        ),
    ],
    "copilot-basics": [
        QuizQuestion(
            id="cpl-1",
            prompt="What is the best first prompt to Claude Code when entering an existing repo?",
            options={
                "a": "Rewrite the whole app in your preferred framework",
                "b": "Explain which template this repo follows, where extension points are, and what must stay unchanged",
                "c": "Delete the tests and then start coding",
                "d": "Generate as much code as possible before reading files"
            },
            correct="b"
        ),
        QuizQuestion(
            id="cpl-2",
            prompt="How should Claude Code usually be asked to implement work?",
            options={
                "a": "As a small diff in named files with validation commands",
                "b": "As a brand-new architecture with no constraints",
                "c": "As direct edits to production without review",
                "d": "As a single massive patch touching every layer"
            },
            correct="a"
        ),
    ],
    "gpt-claude-integration": [
        QuizQuestion(
            id="gc-1",
            prompt="Which of the following usually belongs to the fixed part of an approved template architecture?",
            options={
                "a": "The organization&apos;s logging, config, auth, and deployment patterns",
                "b": "Only the temporary variable names inside one function",
                "c": "The exact bug fix being implemented this week",
                "d": "Nothing; Claude Code should redefine the architecture each time"
            },
            correct="a"
        ),
        QuizQuestion(
            id="gc-2",
            prompt="Which task should be escalated for human approval instead of handed directly to Claude Code?",
            options={
                "a": "Adding focused tests inside the existing suite",
                "b": "Editing one handler and its service logic",
                "c": "Replacing the approved framework and deployment pattern with a new stack",
                "d": "Updating documentation for an existing extension point"
            },
            correct="c"
        ),
    ],
    "agentic-workflows": [
        QuizQuestion(
            id="ag-1",
            prompt="What should the planning step identify before Claude Code starts editing?",
            options={
                "a": "The template boundary, safe files to edit, and validation commands",
                "b": "Only a target number of lines changed",
                "c": "A new framework to migrate to immediately",
                "d": "No plan is needed if the task looks small"
            },
            correct="a"
        ),
        QuizQuestion(
            id="ag-2",
            prompt="Which workflow order is recommended in this course?",
            options={
                "a": "Act -> Plan -> Hope",
                "b": "Plan -> Act -> Check",
                "c": "Check -> Act -> Plan",
                "d": "Act only"
            },
            correct="b"
        ),
    ],
    "prompting-for-code": [
        QuizQuestion(
            id="pr-1",
            prompt="A strong Claude Code prompt for feature work should include:",
            options={
                "a": "The exact files or extension points, the constraints, and the validation commands",
                "b": "Only a vague goal and a request to surprise you",
                "c": "A request to redesign the system however it wants",
                "d": "No reference to tests or architecture"
            },
            correct="a"
        ),
        QuizQuestion(
            id="pr-2",
            prompt="If Claude Code cannot tell which template rules apply, what should it do?",
            options={
                "a": "Guess and start editing anyway",
                "b": "Stop and ask for clarification before making architectural assumptions",
                "c": "Delete unrelated files until the repo is simpler",
                "d": "Invent a new service boundary"
            },
            correct="b"
        ),
    ],
    "testing-debugging": [
        QuizQuestion(
            id="td-1",
            prompt="What should you do after Claude Code proposes a bug fix?",
            options={
                "a": "Ship immediately",
                "b": "Run the relevant tests and review whether the patch stays inside the template conventions",
                "c": "Disable the linter to avoid noise",
                "d": "Skip review because the model already checked itself"
            },
            correct="b"
        ),
        QuizQuestion(
            id="td-2",
            prompt="Which review question best matches this course?",
            options={
                "a": "Did the patch preserve the approved architecture and add enough coverage for the change?",
                "b": "Did the patch maximize the number of files edited?",
                "c": "Did the patch remove the test harness so future edits are faster?",
                "d": "Did the patch avoid all comments, logs, and documentation?"
            },
            correct="a"
        ),
    ],
    "security-governance": [
        QuizQuestion(
            id="sec-1",
            prompt="Why does the course emphasize approved templates from a governance perspective?",
            options={
                "a": "They reduce cost by eliminating code review",
                "b": "They inherit known patterns for auth, logging, config, CI, and deployment",
                "c": "They allow the model to skip reading the codebase",
                "d": "They make tests optional"
            },
            correct="b"
        ),
        QuizQuestion(
            id="sec-2",
            prompt="Which information must still never be shared with a public assistant?",
            options={
                "a": "PII and credentials",
                "b": "Published framework documentation",
                "c": "The project README",
                "d": "A list of test names"
            },
            correct="a"
        ),
    ],
    "transit-dev-examples": [
        QuizQuestion(
            id="tr-1",
            prompt="Which approach best fits the GTFS example taught here?",
            options={
                "a": "Start from the approved service template and add GTFS validation logic plus tests",
                "b": "Ask Claude Code to invent a new platform unrelated to current operations",
                "c": "Skip testing because transit data changes often",
                "d": "Let the model choose any deployment method it likes"
            },
            correct="a"
        ),
        QuizQuestion(
            id="tr-2",
            prompt="For hardening an operations script, which improvement is most appropriate?",
            options={
                "a": "Remove error handling",
                "b": "Add input validation, logging, and tests within the approved automation pattern",
                "c": "Run as admin without checks",
                "d": "Disable audit logs"
            },
            correct="b"
        ),
    ],
    "final": [
        QuizQuestion(
            id="final-1",
            prompt="What is the default starting point for production-oriented AI-assisted coding in this course?",
            options={
                "a": "A blank prompt and a blank repo",
                "b": "The approved template architecture for that class of system",
                "c": "Whatever framework the model last recommended",
                "d": "Direct edits to production"
            },
            correct="b"
        ),
        QuizQuestion(
            id="final-2",
            prompt="What is the recommended sequence for Claude Code-assisted work?",
            options={
                "a": "Plan → Act → Check",
                "b": "Act → Plan → Check",
                "c": "Check → Plan → Act",
                "d": "Act only"
            },
            correct="a"
        ),
        QuizQuestion(
            id="final-3",
            prompt="What strengthens auditability of AI-assisted changes?",
            options={
                "a": "Deleting prompts and PR notes",
                "b": "Recording sanitized prompts, model versions, and rationale in PRs",
                "c": "Pushing directly to main",
                "d": "Bypassing CI"
            },
            correct="b"
        ),
        QuizQuestion(
            id="final-4",
            prompt="Which practice reduces architectural, legal, and security risk when accepting generated code?",
            options={
                "a": "Ignoring license compatibility",
                "b": "Validating licenses and scanning dependencies while staying inside the approved template",
                "c": "Bundling unknown binaries",
                "d": "Turning off SCA tools"
            },
            correct="b"
        ),
    ],
}


def get_quiz(slug: str) -> List[QuizQuestion]:
    return QUIZZES.get(slug, [])


def get_question(slug: str, qid: str) -> Optional[QuizQuestion]:
    for q in QUIZZES.get(slug, []):
        if q.id == qid:
            return q
    return None