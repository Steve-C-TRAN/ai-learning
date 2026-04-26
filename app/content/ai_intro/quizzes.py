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
            prompt="ChatGPT is made by OpenAI. Which company makes Claude?",
            options={
                "a": "Google",
                "b": "Anthropic",
                "c": "Meta",
                "d": "Microsoft"
            },
            correct="b",
            help="Claude is made by Anthropic. Google makes Gemini; Meta makes Llama; Microsoft licenses OpenAI's models for Copilot."
        ),
        QuizQuestion(
            id="models-5",
            prompt="Your team needs an AI assistant with strong safety controls for handling sensitive work documents. What should you look for?",
            options={
                "a": "The newest model regardless of vendor",
                "b": "A model with enterprise safety features and data privacy controls",
                "c": "The cheapest available option",
                "d": "An open-source model with no restrictions",
            },
            correct="b",
            help="For sensitive work content, prioritize enterprise-grade tools with clear data privacy policies — like Microsoft 365 Copilot or Claude for Enterprise."
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
            prompt="Which is a key limitation to keep in mind when using LLMs like ChatGPT?",
            options={
                "a": "They cannot summarize text",
                "b": "They always require a paid subscription",
                "c": "They can be confidently wrong — making up plausible-sounding information",
                "d": "They can only answer questions in English"
            },
            correct="c",
            help="This is called 'hallucination.' LLMs predict what text should come next, not what is factually true. Always verify important facts."
        ),
        QuizQuestion(
            id="llms-2",
            prompt="You asked an AI to summarize a contract and it added a clause that wasn't in the original document. What happened?",
            options={
                "a": "The AI improved the contract for you",
                "b": "The AI hallucinated — it confidently invented something that wasn't there",
                "c": "The original contract was missing the clause",
                "d": "You used the wrong type of AI"
            },
            correct="b",
            help="This is a hallucination. LLMs generate plausible text, not verified facts. Always compare AI output against your source material for anything important."
        ),
        QuizQuestion(
            id="llms-3",
            prompt="Your coworker says 'The AI said it, so it must be true.' What's the best response?",
            options={
                "a": "Agree — AI models are trained on verified facts",
                "b": "Only older AI models make mistakes; newer ones are always accurate",
                "c": "AI can be confidently wrong; important facts always need human verification",
                "d": "AI is never reliable and shouldn't be used at work"
            },
            correct="c",
            help="LLMs predict plausible text, not verified truth. Use AI output as a starting point, and verify anything that matters."
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
            prompt="Which is a realistic way AI can help with rider support today?",
            options={
                "a": "Automatically publishing service alerts without any human review",
                "b": "Drafting service alerts from operations notes for a supervisor to approve before posting",
                "c": "Making real-time routing decisions without operator input",
                "d": "Replacing the customer service team entirely"
            },
            correct="b",
            help="AI works best as a drafting assistant here — a human reviews and approves before anything goes public."
        ),
        QuizQuestion(
            id="transit-2",
            prompt="You’re using ChatGPT at work and want to paste in a rider complaint that includes their name, phone number, and address. Should you?",
            options={
                "a": "Yes — more detail helps the AI give better answers",
                "b": "Only if it’s a work computer",
                "c": "No — remove personal information before pasting into any public AI tool",
                "d": "Yes — ChatGPT encrypts and deletes everything automatically"
            },
            correct="c",
            help="Avoid pasting personally identifiable information (PII) into public AI tools. Remove names, addresses, and contact details before using AI to help draft a response."
        ),
        QuizQuestion(
            id="transit-3",
            prompt="Which guardrail is most important when using AI for transit operations?",
            options={
                "a": "Move as fast as possible and fix problems later",
                "b": "Keep humans in the loop for decisions that affect riders or staff",
                "c": "Only use AI for tasks that have never been done before",
                "d": "Avoid AI entirely until it is 100% accurate"
            },
            correct="b",
            help="Human oversight is the key guardrail. AI is a powerful assistant, but consequential decisions — public communications, safety, staffing — should have a person reviewing and approving."
        ),
    ],
    "prompting-basics": [
        QuizQuestion(
            id="prompt-1",
            prompt="Which practice generally gets better results from AI tools like ChatGPT?",
            options={
                "a": "Keeping prompts as short as possible",
                "b": "Clearly stating the role, goal, audience, and format you want",
                "c": "Asking multiple unrelated questions at once",
                "d": "Using technical jargon so the AI knows you're serious"
            },
            correct="b",
            help="Clear context — who you are, what you need, who it's for, and how you want it — gives the model what it needs to produce a useful response."
        ),
        QuizQuestion(
            id="prompt-2",
            prompt="You want the AI to write a formal email to a senior leader. What's the most important thing to include in your prompt?",
            options={
                "a": "Your login credentials",
                "b": "The role, goal, audience, tone, and key facts",
                "c": "As many keywords as possible",
                "d": "The full history of your organization"
            },
            correct="b",
            help="Specifying role, goal, audience, tone, and key facts gives the model the context it needs to produce a useful draft on the first try."
        ),
        QuizQuestion(
            id="prompt-3",
            prompt="The AI gives you a response that's too long and too formal. What's the best next step?",
            options={
                "a": "Give up and write it yourself",
                "b": "Accept it since AI output shouldn't be edited",
                "c": "Refine your prompt: 'Shorten by 30% and use a friendly, plain-language tone'",
                "d": "Switch to a different AI immediately"
            },
            correct="c",
            help="Iteration is normal and expected. Small, specific refinements work much better than starting over or accepting a poor output."
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
            prompt="Which is the right approach when using public AI tools like ChatGPT for work tasks?",
            options={
                "a": "Include rider names and addresses so the AI can personalize responses",
                "b": "Avoid pasting PII or sensitive data; use business-approved tools for operational content",
                "c": "Share internal passwords to give the AI access to your systems",
                "d": "Skip human review since AI output is reliable enough for public posts"
            },
            correct="b",
            help="Public AI tools are not a secure environment for sensitive data. Remove PII before using them, and use approved enterprise tools when the work involves confidential content."
        ),
        QuizQuestion(
            id="final-3",
            prompt="Which of these is AI currently best suited to help with at work?",
            options={
                "a": "Making final decisions on safety-critical operations without human review",
                "b": "Drafting, summarizing, and rewriting content for a human to review and finalize",
                "c": "Running your department without any oversight",
                "d": "Guaranteeing factual accuracy in all outputs"
            },
            correct="b",
            help="AI excels at drafting and summarizing — with humans in the loop to verify and finalize. It should augment judgment, not replace it."
        ),
        QuizQuestion(
            id="final-4",
            prompt="Which task fits the 'classification and routing' pattern?",
            options={
                "a": "Drafting a press release",
                "b": "Tagging and triaging incoming requests by category and urgency",
                "c": "Rendering 3D graphics",
                "d": "Designing a new bus route"
            },
            correct="b",
            help="Classification and routing means labeling or sorting inputs — like tagging a support ticket as 'fares / high urgency' so it reaches the right team."
        ),
        QuizQuestion(
            id="final-5",
            prompt="An AI gives you a response that sounds completely confident but contains a fact you know is wrong. What should you do?",
            options={
                "a": "Trust it — AI models don't make things up",
                "b": "Use it anyway since the rest is probably correct",
                "c": "Correct the error, verify the surrounding facts, and treat the whole output as a draft",
                "d": "Report a bug to the AI company"
            },
            correct="c",
            help="Hallucination is a known LLM limitation. If one fact is wrong, others may be too. Always treat AI output as a draft and verify anything consequential."
        ),
        QuizQuestion(
            id="final-6",
            prompt="What is the most important habit when using AI for work tasks?",
            options={
                "a": "Use the most expensive model available",
                "b": "Keep humans in the loop — review outputs before acting or publishing",
                "c": "Always use AI without editing so you get the 'true' answer",
                "d": "Avoid telling coworkers you used AI"
            },
            correct="b",
            help="Human oversight is the core guardrail. AI is a powerful assistant, but you are responsible for what goes out the door."
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
