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
            help="For sensitive work content, always use IT-approved tools with clear data privacy and retention policies. Check with IT before using any new AI tool for operational work."
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
            prompt="A staff member copies text from a vendor contract PDF and asks an AI tool to extract the start date, end date, payment terms, and SLA penalties into a table. Which AI pattern does this describe?",
            options={
                "a": "Drafting and generation",
                "b": "Transformation and rewrite",
                "c": "Extraction and structuring",
                "d": "Classification and routing"
            },
            correct="c",
            help="Extraction and structuring means pulling specific fields out of unstructured text and returning them in a clean, usable format — like a table or CSV."
        ),
        QuizQuestion(
            id="use-2",
            prompt="You describe what you need in plain English — 'sum column B where column A says Route 4' — and the AI returns the correct Excel SUMIF formula. What makes this approach work?",
            options={
                "a": "The AI has direct access to your spreadsheet",
                "b": "You gave it a specific, plain-language description of the logic you needed",
                "c": "Excel formulas are pre-programmed into every AI model",
                "d": "You used the right keyword to trigger formula mode"
            },
            correct="b",
            help="Plain-English descriptions of logic are one of AI's most practical uses for spreadsheet work. The more specific you are about the condition and the output, the more accurate the formula."
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
            prompt="You’re drafting a response to a rider complaint using your IT-approved AI tool. The complaint includes the rider’s name, address, and phone number. What do you do first?",
            options={
                "a": "Include all the details so the AI can personalize the response",
                "b": "Remove the personal information before pasting anything into the AI tool",
                "c": "It’s fine as long as the tool is IT-approved",
                "d": "Submit an IT help ticket before using AI for any rider communications"
            },
            correct="b",
            help="Even IT-approved tools should not receive personally identifiable information (PII) unless specifically cleared for it. Remove names, addresses, and contact details before using AI to help draft responses."
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
            prompt="Which practice generally gets better results from your IT-approved AI tool?",
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
            prompt="You paste ridership data into your IT-approved AI tool and ask it to 'find trends.' The response is vague and unhelpful. What should you add to your prompt?",
            options={
                "a": "Your system credentials so the AI can pull the full dataset directly",
                "b": "Specific questions to answer, the timeframe to focus on, and the output format you need",
                "c": "More raw data — the AI needs the complete export to find trends",
                "d": "A request to make the response longer and more detailed"
            },
            correct="b",
            help="'Find trends' is too vague. Tell the AI what to look for (e.g., routes with declining ridership), over what period, and what format the output should take — like 5 bullets for a weekly operations meeting."
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
            prompt="You used your IT-approved AI tool to help draft a memo about a service change. What should you do with the prompt you entered and the AI's response?",
            options={
                "a": "Delete them once the memo is final — they were just working notes",
                "b": "Keep them private so the public can't see your working process",
                "c": "Save them as part of your work records — they may be subject to public records requests",
                "d": "Only save them if your supervisor specifically asks"
            },
            correct="c",
            help="AI-assisted work at a public agency can be subject to public records laws. Save your prompts and AI outputs just like any other work document."
        ),
        QuizQuestion(
            id="final-2",
            prompt="A coworker wants to paste a rider complaint — including the rider's name, address, and phone number — into a public AI chatbot to help draft a response. What's the right guidance?",
            options={
                "a": "It's fine as long as they delete the conversation afterward",
                "b": "Only do it from a work computer on the VPN",
                "c": "Remove the personal information and use an IT-approved tool instead",
                "d": "Avoid using AI for anything involving rider information"
            },
            correct="c",
            help="C-TRAN policy requires using IT-approved tools for work AI tasks. Personally identifiable information should be removed before using any AI tool, unless it has been specifically cleared for that data."
        ),
        QuizQuestion(
            id="final-3",
            prompt="You ask AI to summarize a city policy document. The summary sounds authoritative, but one detail doesn't match what you remember reading. What should you do?",
            options={
                "a": "Trust the AI — it has read more documents than any person",
                "b": "Correct just that one detail and use the rest of the summary as-is",
                "c": "Verify the full summary against the source — if one fact is wrong, others may be too",
                "d": "Ask the AI to re-read the document and try again"
            },
            correct="c",
            help="LLMs can hallucinate — confidently state things that are not true. If one fact is off, treat the entire output with skepticism and verify against your source material."
        ),
        QuizQuestion(
            id="final-4",
            prompt="Incoming rider emails are automatically tagged as 'fares,' 'accessibility,' or 'schedule complaint' and routed to the right team. Which AI pattern does this describe?",
            options={
                "a": "Summarization and Q&A",
                "b": "Drafting and generation",
                "c": "Classification and routing",
                "d": "Retrieval-Augmented Generation (RAG)"
            },
            correct="c",
            help="Classification and routing means labeling and sorting inputs — a great fit for triaging incoming messages so they reach the right person faster."
        ),
        QuizQuestion(
            id="final-5",
            prompt="Your department is piloting AI to auto-post service alerts to social media the moment an incident is logged — no human review before posting. What's the key risk?",
            options={
                "a": "The posts might not match the agency's visual branding",
                "b": "The AI could publish inaccurate or premature alerts before anyone can catch and correct them",
                "c": "Riders might receive information faster than they expect",
                "d": "AI tools are generally not permitted to access social media platforms"
            },
            correct="b",
            help="Human review is essential before anything goes public. AI drafts, humans approve — especially for safety- or operations-related communications."
        ),
        QuizQuestion(
            id="final-6",
            prompt="You ask an AI to 'help with the Route 4 update' and get a vague, generic response. What's the most likely reason?",
            options={
                "a": "AI tools can't handle transit-specific topics",
                "b": "Route 4 isn't in the AI's training data",
                "c": "The prompt lacked role, audience, key facts, and format",
                "d": "You need a higher-tier AI subscription for operational tasks"
            },
            correct="c",
            help="Vague prompts get vague answers. Give the AI a clear role, the audience it's writing for, the key facts it needs, and the format you want — and results will be much more useful."
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
