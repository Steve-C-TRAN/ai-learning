# app/content/quizzes.py
# Updated quizzes aligned to "Coding with AI" modules

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
            prompt="Which outcome is emphasized in this program?",
            options={
                "a": "Fully automating production without tests",
                "b": "Configuring VS Code and Copilot safely and effectively",
                "c": "Using only one model for every task",
                "d": "Skipping code review to move faster"
            },
            correct="b",
            help="Configuration plus governance and quality are foundational."
        ),
        QuizQuestion(
            id="intro-2",
            prompt="Which practice is recommended when using AI to code at an agency?",
            options={
                "a": "Share internal tokens in prompts for context",
                "b": "Record model-assisted changes and verify with tests",
                "c": "Disable workspace trust for convenience",
                "d": "Accept all suggestions without review"
            },
            correct="b"
        ),
    ],
    "vscode-setup": [
        QuizQuestion(
            id="vsc-1",
            prompt="Which file should generally be excluded from prompts, version control, and telemetry?",
            options={
                "a": "README.md",
                "b": "requirements.txt",
                "c": ".env",
                "d": "LICENSE"
            },
            correct="c",
            help="Secrets belong in .env or secret stores and must not be shared with models."
        ),
        QuizQuestion(
            id="vsc-2",
            prompt="What is a good practice for reusable prompts in a repo?",
            options={
                "a": "Keep them only in personal notes",
                "b": "Create a /prompts folder under version control",
                "c": "Paste them into random issues",
                "d": "Rely on memory"
            },
            correct="b"
        ),
    ],
    "copilot-basics": [
        QuizQuestion(
            id="cpl-1",
            prompt="Which Copilot feature helps navigate and modify code across a workspace?",
            options={
                "a": "Inline suggestions only",
                "b": "Copilot Chat with @workspace context",
                "c": "Random code generator",
                "d": "Unattended shell access"
            },
            correct="b"
        ),
        QuizQuestion(
            id="cpl-2",
            prompt="What should you do before applying Copilot changes broadly?",
            options={
                "a": "Apply directly to main",
                "b": "Create a scratch branch and run tests",
                "c": "Disable linters",
                "d": "Remove code owners"
            },
            correct="b"
        ),
    ],
    "gpt-claude-integration": [
        QuizQuestion(
            id="gc-1",
            prompt="When is it better to use GPT/Claude over inline Copilot suggestions?",
            options={
                "a": "For long-form design or multi-file planning",
                "b": "For single-line autocompletion only",
                "c": "When you want to paste secrets",
                "d": "Never"
            },
            correct="a"
        ),
        QuizQuestion(
            id="gc-2",
            prompt="What should be included in a design prompt for the models?",
            options={
                "a": "No constraints to keep it creative",
                "b": "Explicit stack, patterns, testing, and acceptance criteria",
                "c": "Only emojis",
                "d": "Only the file names"
            },
            correct="b"
        ),
    ],
    "agentic-workflows": [
        QuizQuestion(
            id="ag-1",
            prompt="What is the recommended order in an agentic workflow?",
            options={
                "a": "Check → Act → Plan",
                "b": "Plan → Act → Check",
                "c": "Act only",
                "d": "Check only"
            },
            correct="b"
        ),
        QuizQuestion(
            id="ag-2",
            prompt="Which guardrail is appropriate for agentic coding in VS Code?",
            options={
                "a": "Permit unattended file writes",
                "b": "Require human approval for dependency changes",
                "c": "Run commands as root by default",
                "d": "Disable logs for privacy"
            },
            correct="b"
        ),
    ],
    "prompting-for-code": [
        QuizQuestion(
            id="pr-1",
            prompt="A strong prompt for implementing a function should request:",
            options={
                "a": "Only prose and no code",
                "b": "Type hints, docstring, input validation, and tests",
                "c": "Vague ideas without constraints",
                "d": "Screenshots"
            },
            correct="b"
        ),
        QuizQuestion(
            id="pr-2",
            prompt="When asking for a refactor, which output format improves reviewability?",
            options={
                "a": "Unified diff with rationale",
                "b": "Random file dump",
                "c": "Binary patch",
                "d": "Handwritten notes"
            },
            correct="a"
        ),
    ],
    "testing-debugging": [
        QuizQuestion(
            id="td-1",
            prompt="What should you do after the model proposes a fix for a bug?",
            options={
                "a": "Ship immediately",
                "b": "Add tests and run the suite",
                "c": "Delete the logs",
                "d": "Ignore code review"
            },
            correct="b"
        ),
        QuizQuestion(
            id="td-2",
            prompt="Which practice strengthens confidence against regressions?",
            options={
                "a": "Skipping linters",
                "b": "Property-based tests and edge-case scenarios",
                "c": "Forbidding CI",
                "d": "Merging directly to production"
            },
            correct="b"
        ),
    ],
    "security-governance": [
        QuizQuestion(
            id="sec-1",
            prompt="Which information must not be shared with public AI assistants?",
            options={
                "a": "Open-source license text",
                "b": "Public API docs",
                "c": "PII and credentials",
                "d": "Blog posts"
            },
            correct="c"
        ),
        QuizQuestion(
            id="sec-2",
            prompt="How should you handle license obligations when accepting generated code?",
            options={
                "a": "Ignore them to move faster",
                "b": "Ask the model to explain and then validate with legal/policy",
                "c": "Assume it is always MIT",
                "d": "Delete attribution files"
            },
            correct="b"
        ),
    ],
    "transit-dev-examples": [
        QuizQuestion(
            id="tr-1",
            prompt="Which is a realistic AI-assisted task for a transit agency?",
            options={
                "a": "Generating random ridership numbers",
                "b": "Building a GTFS validation CLI with tests",
                "c": "Issuing fines automatically",
                "d": "Editing labor contracts"
            },
            correct="b"
        ),
        QuizQuestion(
            id="tr-2",
            prompt="For hardening an operations script, which improvement is most appropriate?",
            options={
                "a": "Remove error handling",
                "b": "Add input validation, logging, and tests",
                "c": "Run as admin without checks",
                "d": "Disable audit logs"
            },
            correct="b"
        ),
    ],
    "final": [
        QuizQuestion(
            id="final-1",
            prompt="Which policy is most important when using AI to code at an agency?",
            options={
                "a": "Paste secrets to improve suggestions",
                "b": "Prefer enterprise tenants for sensitive data",
                "c": "Disable code review to save time",
                "d": "Skip tests if the model wrote the code"
            },
            correct="b"
        ),
        QuizQuestion(
            id="final-2",
            prompt="What is the agentic sequence recommended here?",
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
            prompt="Which practice reduces legal and security risk when accepting generated code?",
            options={
                "a": "Ignoring license compatibility",
                "b": "Validating licenses and scanning dependencies",
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