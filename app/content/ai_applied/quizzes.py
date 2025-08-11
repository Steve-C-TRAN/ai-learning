# app/content/quizzes.py
# Quiz content stored in code for easy editing. Anonymous attempts stored in DB.
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
            prompt="What is the primary goal of this training?",
            options={
                "a": "Master advanced AI model fine-tuning",
                "b": "Understand AI basics and how to apply AI at C-TRAN",
                "c": "Build production AI APIs for C-TRAN",
                "d": "Implement SSO and authentication"
            },
            correct="b",
            help="Participants should understand AI concepts and think about practical applications."
        ),
        QuizQuestion(
            id="intro-2",
            prompt="About how long is this program designed to take?",
            options={
                "a": "~10 minutes",
                "b": "~30 minutes",
                "c": "~2 hours",
                "d": "All day"
            },
            correct="b",
            help="The program targets about 30 minutes of self-guided learning."
        ),
    ],
    "ai-eras": [
        QuizQuestion(
            id="eras-1",
            prompt="Which sequence best reflects the progression of AI described?",
            options={
                "a": "Self-replication → Rules-based → Foundational models",
                "b": "Rules/ML → Foundational models → Agentic era",
                "c": "Foundational models → Rules-based → Agentic era",
                "d": "Agentic era → Rules-based → Foundational models"
            },
            correct="b"
        ),
        QuizQuestion(
            id="eras-2",
            prompt="What characterizes the current 'agentic' era?",
            options={
                "a": "Only rule-based logic",
                "b": "Manual data labeling for every task",
                "c": "Models that can plan, use tools, and follow multi-step instructions",
                "d": "Models that cannot take any actions"
            },
            correct="c"
        ),
    ],
    "current-models": [
        QuizQuestion(
            id="models-1",
            prompt="Which vendors are associated with Claude and Gemini respectively?",
            options={
                "a": "OpenAI and Google",
                "b": "Anthropic and Google",
                "c": "Meta and OpenAI",
                "d": "Mistral and Anthropic"
            },
            correct="b"
        ),
        QuizQuestion(
            id="models-2",
            prompt="Grok is developed by which organization?",
            options={
                "a": "xAI",
                "b": "Deepseek",
                "c": "OpenAI",
                "d": "Mistral"
            },
            correct="a"
        ),
        QuizQuestion(
            id="models-3",
            prompt="Which vendor offers the Gemini 2.5 family of models (Pro, Flash, Flash‑Lite)?",
            options={
                "a": "OpenAI",
                "b": "Anthropic",
                "c": "Google",
                "d": "Mistral",
            },
            correct="c",
            help="Gemini is Google DeepMind's family; 2.5 is the current generation with Pro/Flash variants."
        ),
        QuizQuestion(
            id="models-4",
            prompt="Llama 4 models are primarily associated with which organization?",
            options={
                "a": "Meta",
                "b": "xAI",
                "c": "DeepSeek",
                "d": "Anthropic",
            },
            correct="a",
            help="Llama is Meta's open‑weight model family."
        ),
        QuizQuestion(
            id="models-5",
            prompt="A team needs strong reasoning with enterprise safety controls. Which model family is commonly chosen?",
            options={
                "a": "Claude (Anthropic)",
                "b": "Grok (xAI)",
                "c": "Llama (Meta)",
                "d": "Codestral (Mistral)",
            },
            correct="a",
            help="Claude Opus/Sonnet emphasize reasoning and safety with strong enterprise features."
        ),
    ],
    "delivery-models": [
        QuizQuestion(
            id="deliv-1",
            prompt="Which delivery approach runs models locally for privacy or offline use?",
            options={
                "a": "Cloud APIs",
                "b": "Integrated tools",
                "c": "Fine-tuning",
                "d": "On-device models"
            },
            correct="d"
        ),
        QuizQuestion(
            id="deliv-2",
            prompt="Which is an example of an integrated tool?",
            options={
                "a": "Microsoft Copilot",
                "b": "Raw REST API",
                "c": "Custom GPU cluster",
                "d": "ETL pipeline"
            },
            correct="a"
        ),
    ],
    "llms": [
        QuizQuestion(
            id="llms-1",
            prompt="Which is a key limitation to consider when using LLMs?",
            options={
                "a": "They cannot summarize text",
                "b": "They always require GPUs",
                "c": "They may hallucinate or be confidently wrong",
                "d": "They cannot follow any instructions"
            },
            correct="c"
        ),
        QuizQuestion(
            id="llms-2",
            prompt="What do LLMs predict during generation?",
            options={
                "a": "The next database row",
                "b": "The next token based on context",
                "c": "The next image frame",
                "d": "The next network packet"
            },
            correct="b"
        ),
    ],
    "use-foundation-models": [
        QuizQuestion(
            id="use-1",
            prompt="Which is a common pattern for applying foundation models?",
            options={
                "a": "Manual rule entry for every scenario",
                "b": "Summarization and Q&A over documents",
                "c": "Only image generation",
                "d": "Only spreadsheet formulas"
            },
            correct="b"
        ),
        QuizQuestion(
            id="use-2",
            prompt="Which task fits 'classification & routing'?",
            options={
                "a": "Adding watermarks to images",
                "b": "Tagging tickets and triaging requests",
                "c": "Encrypting databases",
                "d": "Rendering video"
            },
            correct="b"
        ),
    ],
    "ai-in-it": [
        QuizQuestion(
            id="it-1",
            prompt="Which is a realistic AI assist for developers?",
            options={
                "a": "Write every production system automatically",
                "b": "Suggest code and explain errors",
                "c": "Replace version control",
                "d": "Eliminate testing"
            },
            correct="b"
        ),
        QuizQuestion(
            id="it-2",
            prompt="Which support task can AI help with today?",
            options={
                "a": "Replacing all IT staff",
                "b": "Searching KBs and surfacing relevant steps",
                "c": "Physically installing hardware",
                "d": "Approving budgets"
            },
            correct="b"
        ),
    ],
    "transit-use-cases": [
        QuizQuestion(
            id="transit-1",
            prompt="Which is a plausible rider support use case?",
            options={
                "a": "Predicting lottery numbers",
                "b": "Assisting with service alerts and trip planning",
                "c": "Issuing legal fines",
                "d": "Altering union contracts"
            },
            correct="b"
        ),
        QuizQuestion(
            id="transit-2",
            prompt="Scheduling support could include which capability?",
            options={
                "a": "Altering tax codes",
                "b": "Pattern insights from history and conditions",
                "c": "Issuing driver’s licenses",
                "d": "Replacing safety protocols"
            },
            correct="b"
        ),
        QuizQuestion(
            id="transit-3",
            prompt="Which guardrail is appropriate for transit AI initiatives?",
            options={
                "a": "Ignore privacy to move faster",
                "b": "Coordinate with union workforce where relevant",
                "c": "Publish sensitive logs externally",
                "d": "Bypass data governance"
            },
            correct="b"
        ),
    ],
    "prompting-basics": [
        QuizQuestion(
            id="prompt-1",
            prompt="Which practice generally improves prompt outcomes?",
            options={
                "a": "Avoiding any context to keep prompts short",
                "b": "Clearly stating role, objective, and desired format",
                "c": "Asking multiple unrelated questions at once",
                "d": "Using only one-word prompts"
            },
            correct="b"
        ),
        QuizQuestion(
            id="prompt-2",
            prompt="What should you do when you need a specific output structure?",
            options={
                "a": "Let the model guess",
                "b": "Explicitly specify the format (e.g., bullets, table)",
                "c": "Add emojis",
                "d": "Ask for the longest response"
            },
            correct="b"
        ),
    ],
    "image-examples": [
        QuizQuestion(
            id="img-1",
            prompt="Which is an example of image editing with AI?",
            options={
                "a": "Changing backgrounds and removing objects",
                "b": "Compiling code",
                "c": "Encrypting email",
                "d": "Scheduling shifts"
            },
            correct="a"
        ),
    ],
    "final": [
        QuizQuestion(
            id="final-1",
            prompt="For C-TRAN, which is an appropriate guardrail when using public AI tools?",
            options={
                "a": "Include PII for better personalization",
                "b": "Share sensitive operational data for more context",
                "c": "Avoid PII/sensitive data; prefer business-approved tools",
                "d": "Copy internal passwords to improve access"
            },
            correct="c"
        ),
        QuizQuestion(
            id="final-2",
            prompt="Which delivery option is best for privacy/offline constraints?",
            options={
                "a": "Cloud API only",
                "b": "On-device models",
                "c": "Public forum posts",
                "d": "Manual spreadsheets"
            },
            correct="b"
        ),
        QuizQuestion(
            id="final-3",
            prompt="A key limitation of LLMs to keep in mind is:",
            options={
                "a": "They never make mistakes",
                "b": "They always cite sources",
                "c": "They can hallucinate details",
                "d": "They require gigabit internet"
            },
            correct="c"
        ),
        QuizQuestion(
            id="final-4",
            prompt="Which task aligns with 'classification & routing'?",
            options={
                "a": "Drafting a press release",
                "b": "Tagging and triaging incoming requests",
                "c": "Rendering 3D scenes",
                "d": "Designing bus livery"
            },
            correct="b"
        ),
        QuizQuestion(
            id="final-5",
            prompt="A transit-relevant use case from this program is:",
            options={
                "a": "Editing source code licenses",
                "b": "Service alerts and rider trip assistance",
                "c": "Issuing parking citations",
                "d": "Changing labor laws"
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
