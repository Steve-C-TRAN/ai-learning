# app/content/modules.py
# Defines Course 1 learning modules and sections for the C-TRAN AI Learning App

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class ModuleSection:
    title: str
    content: str

@dataclass
class Module:
    slug: str
    title: str
    summary: str
    sections: List[ModuleSection]
    resources: List[Dict[str, str]] = field(default_factory=list)
    guardrails: List[str] = field(default_factory=list)

@dataclass
class CourseMeta:
    slug: str
    title: str
    summary: str
    duration: str
    level: str
    hero_image: str
    thumbnail: str
    og_image: str
    tags: List[str] = field(default_factory=list)


def get_modules() -> List[Module]:
    return [
        Module(
            slug="introduction",
            title="Welcome to AI Foundations!",
            summary="The course is designed to give you an overview of AI, how it works, and some potential applications for it in the public transit industry.",
            sections=[
                ModuleSection(
                    title="Objectives",
                    content=(
                        "<ul class=\"list-disc ml-6\">"
                        "<li>Learn the basic concepts of AI and its applications in business.</li>"
                        "<li>Explore the <strong>AI landscape</strong> and identify key players and technologies.</li>"
                        "<li>Use only <strong>IT-approved tools</strong> for work AI tasks; save prompts and outputs for public records.</li>"
                        "<li>Leave with <strong>1–2 ideas to try</strong> explore with your team.</li>"
                        "</ul>"
                        "<p class=\"mt-3 text-slate-300\">Upscale your AI knowledge.</p>"
                    ),
                ),
                ModuleSection(
                    title="Agenda",
                    content=(
                        "<ul class=\"list-disc ml-6\">"
                        "<li><strong>Foundations:</strong> key terms and eras (AI, ML, LLMs).</li>"
                        "<li><strong>Mental model:</strong> how LLMs work and where they struggle.</li>"
                        "<li><strong>Landscape:</strong> leading vendors and model families.</li>"
                        "<li><strong>Practical patterns:</strong> summarize, draft, transform, extract, classify, report.</li>"
                        "<li><strong>Transit use cases:</strong> CX, rider support, scheduling, IT support.</li>"
                        "<li><strong>Prompting basics:</strong> role, context, constraints, examples, self‑check.</li>"
                        "<li><strong>Practice:</strong> quick exercises you can try today.</li>"
                        "<li><strong>Final quiz:</strong> quick knowledge check to complete the program.</li>"
                        "</ul>"
                    ),
                ),
                ModuleSection(
                    title="Definitions",
                    content=(
                        "<p><strong>Artificial Intelligence (AI)</strong> is the broad field of making computers perform tasks that typically require human intelligence (reasoning, planning, perception, language).</p>"
                        "<p class=\"mt-3\"><strong>Machine Learning (ML)</strong> is a subset of AI focused on learning patterns from data to make predictions or decisions without being explicitly programmed for every rule.</p>"
                        "<p class=\"mt-3\"><strong>Generative AI</strong> refers to models that can create new content (text, images, audio, code) based on patterns learned from data.</p>"
                        "<p class=\"mt-3\"><strong>Large Language Models (LLMs)</strong> are a type of generative AI trained on vast text corpora to predict the next token, enabling tasks like summarization, Q&A, drafting, and translation.</p>"
                        "<ul class=\"list-disc ml-6 mt-2\">"
                        "</ul>"
                    ),
                ),
            ],
            resources=[
                {"label": "C-TRAN Website", "url": "https://www.c-tran.com/"},
            ],
        ),
        Module(
            slug="ai-eras",
            title="AI Eras",
            summary="From rules and classic ML to agentic systems.",
            sections=[
                ModuleSection(
                    title="How AI Got Here: Three Eras",
                    content="""
                    <ul class="list-disc ml-6 space-y-4">
                      <li>
                        <strong>Era 1: Computers Follow Rules (1980s–2010s):</strong>
                        Early AI worked by following rules that programmers wrote by hand. "If the email contains the word 'winner,' mark it spam." Useful for narrow, predictable tasks, but brittle. Change the rules of the world and the system breaks.
                        <em class="block mt-1 text-slate-400">Examples: spam filters, credit scoring, fraud detection.</em>
                      </li>
                      <li>
                        <strong>Era 2: Computers Learn From Text (2018–2022):</strong>
                        Instead of hand-coded rules, systems learned by reading enormous amounts of text. In 2020, GPT-3 showed that a model trained on enough text could write, reason, and answer questions in a genuinely useful way. This was the moment generative AI became real for everyday use.
                        <em class="block mt-1 text-slate-400">Examples: drafting emails, summarizing documents, answering questions in plain English.</em>
                      </li>
                      <li>
                        <strong>Era 3: AI Takes Action (2023–Now):</strong>
                        Today's models don't just respond to questions. They can break a goal into steps, use tools like search or calendars, and work toward a result with minimal hand-holding. This is called the "agentic" era.
                        <em class="block mt-1 text-slate-400">Examples: booking meetings, drafting reports using live data, routing and triaging requests automatically.</em>
                      </li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Pioneers Worth Knowing",
                    content="""
                    <p class="text-slate-400 text-sm">Today’s AI stands on decades of research. <a class="text-cyan-300 underline" href="https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)" target="_blank" rel="noopener">John McCarthy</a> coined the term "Artificial Intelligence" in 1956. <a class="text-cyan-300 underline" href="https://en.wikipedia.org/wiki/Karen_Sp%C3%A4rck_Jones" target="_blank" rel="noopener">Karen Spärck Jones</a> developed foundational ideas in how computers find relevant information, work that underpins modern search and today’s AI retrieval systems.</p>
                    """,
                ),
                ModuleSection(
                    title="What Is an Agent?",
                    content="""
                    <p>An <strong>agent</strong> is software that can pursue a goal by deciding <em>what to do next</em>, often by calling tools and following steps.</p>
                    <div class="grid md:grid-cols-2 gap-4 mt-3">
                      <div>
                        <h4 class="font-semibold">In plain English</h4>
                        <ul class="list-disc ml-6">
                          <li>Give it a goal ("Draft a service alert based on today’s outage").</li>
                          <li>It figures out steps (read data → draft alert → ask for approval).</li>
                          <li>It uses tools (APIs, search, calendars) to get work done.</li>
                        </ul>
                      </div>
                      <div>
                        <h4 class="font-semibold">Under the hood</h4>
                        <ul class="list-disc ml-6">
                          <li><em>Planner:</em> breaks tasks into steps and decides next action.</li>
                          <li><em>Tools:</em> functions/APIs the model can call with structured inputs.</li>
                          <li><em>Memory/Retrieval:</em> recalls prior context, fetches relevant info.</li>
                          <li><em>Loop:</em> act → observe → reflect → continue or stop.</li>
                        </ul>
                      </div>
                    </div>
                    <p class="mt-3 text-slate-300">Start small: keep humans in the loop, monitor outputs, and restrict tools to safe actions.</p>
                    """,
                ),
                ModuleSection(
                    title="Myths vs. Reality",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Myth:</strong> "LLMs know the truth." <strong>Reality:</strong> They predict tokens; verify critical outputs.</li>
                      <li><strong>Myth:</strong> "AI replaces everyone." <strong>Reality:</strong> Best outcomes are human + AI teams.</li>
                      <li><strong>Myth:</strong> "More prompts = better." <strong>Reality:</strong> Clarity, context, and constraints matter most.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Questions to Explore at C-TRAN",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Which 2–3 weekly decisions could be faster with a draft or summary?</li>
                      <li>Where do riders or staff wait for information that could be automated with review?</li>
                      <li>Which workflows are safe to pilot using non-sensitive data?</li>
                      <li>What does a good "human-in-the-loop" checkpoint look like for our teams?</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Pitfalls & Guardrails",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Policy:</strong> Use only IT-approved tools for work AI tasks. Save prompts and AI outputs — they may be subject to public records requests.</li>
                      <li><strong>Privacy:</strong> Never paste personally identifiable information into an AI tool unless it has been specifically cleared for that data.</li>
                      <li><strong>Hallucinations:</strong> For critical facts, require sources and human review.</li>
                      <li><strong>Brittleness:</strong> Monitor agents; start small and measure impact.</li>
                      <li><strong>Equity & Safety:</strong> Audit outputs for bias; keep safety first.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="What’s Next?",
                    content="""
                    <p>Software engineering productivity is increasing rapidly, and more autonomous agents will be capable of handling complex, multi-step work with less human direction.</p>
                    """,
                ),
            ],
        ),
        Module(
            slug="llms",
            title="Understanding LLMs",
            summary="Foundation models, what LLMs are, how they work, where they shine and struggle, plus a quick mental picture.",
            sections=[
                ModuleSection(
                    title="You’ve Already Used One",
                    content="""
                    <div class="bg-slate-800/60 border border-emerald-700/40 rounded p-4">
                      <p class="text-emerald-300 font-semibold">Sound familiar?</p>
                      <p class="mt-1">If you’ve used ChatGPT, you’ve already used an LLM. ChatGPT is built on GPT, a Large Language Model made by OpenAI. Claude, Gemini, and Microsoft Copilot are all LLMs too. They’re the same type of technology, just from different companies with different strengths.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="What LLMs Are (and Aren’t)",
                    content="""
                    <p><strong>LLMs</strong> (Large Language Models) are AI systems trained to understand and generate text. They’re remarkably good at drafting, summarizing, translating, and reasoning, as long as you keep their limits in mind.</p>
                    <ul class="list-disc ml-6 mt-3 space-y-2">
                      <li><strong>They are</strong> general language engines you steer with plain-English instructions (called prompts).</li>
                      <li><strong>They aren’t</strong> search engines or databases of truth. Treat outputs as <em>drafts</em> and verify anything important.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="How They Work (Plain English)",
                    content="""
                    <ul class="list-disc ml-6 space-y-3">
                      <li><strong>Tokens:</strong> The model reads text in small chunks called tokens (roughly a word or part of a word). It predicts what should come next, one token at a time, like autocomplete, but far more powerful.</li>
                      <li><strong>Training:</strong> The model learned by reading enormous amounts of text: books, websites, code. It got good at predicting what comes next in any kind of writing, which turns out to enable a lot of useful things.</li>
                      <li><strong>Instructions:</strong> It was then taught to follow plain-English instructions, so you can just ask it what you need in natural language.</li>
                      <li><strong>RAG (Retrieval-Augmented Generation):</strong> You can also give the model your own documents at the time you ask a question. It answers based on your content rather than just its training. This is great for internal policies, reports, or knowledge bases.</li>
                      <li><strong>Tool use:</strong> Some models can also search the web, query databases, or take actions, not just answer questions.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="What They’re Great At",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li>Summarizing long material into key points.</li>
                      <li>Drafting emails, reports, job aids, policies (with guidance).</li>
                      <li>Rewriting for tone, length, and audience.</li>
                      <li>Classifying/routing messages and requests.</li>
                      <li>Multilingual support and translation.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Where They Struggle",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li>Factual accuracy without sources; may <em>hallucinate</em>.</li>
                      <li>Out‑of‑date knowledge unless you add retrieval or tools.</li>
                      <li>Hidden biases from training data; needs oversight.</li>
                      <li>Very detailed calculations or niche domain knowledge without context.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Visual: A mental picture of an LLM",
                    content="""
                    <figure class="space-y-2">
                      <div class="mx-auto max-w-3xl md:max-w-5xl px-2 flex justify-center">
                        <a href="/static/images/llm_diagram.svg" target="_blank" rel="noopener" title="Open full-size">
                          <img src="/static/images/llm_diagram.svg" alt="LLM (Transformer) mental model diagram" class="block w-auto max-w-full h-auto object-contain max-h-[80vh] mx-auto rounded border border-slate-700/50 bg-slate-900" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-40 flex items-center justify-center text-xs bg-slate-800 rounded border border-slate-700/50',textContent:'LLM diagram placeholder'}) )">
                        </a>
                      </div>
                      <figcaption class="text-xs md:text-sm text-slate-400 text-center">Illustration: Token → Embeddings → Transformer stack → Output tokens.</figcaption>
                    </figure>
                    """,
                ),
            ],
            guardrails=[
                "Use only IT-approved AI tools for work tasks; do not use public consumer tools for operational content.",
                "Avoid PII in AI tools unless specifically cleared for that data.",
                "Save your prompts and AI outputs — work-related AI use may be subject to public records requests.",
                "Verify critical outputs; treat AI responses as drafts, not ground truth.",
            ],
        ),
        Module(
            slug="current-models",
            title="Overview of Key AI Companies and Models",
            summary="There are thousands of companies competing in the AI space. These companies are among the leaders in the development of foundational models for text, image, and audio generation. Explore them to see more about what is out there.",
            sections=[
                ModuleSection(
                    title="Vendors at a Glance",
                    content="""
                    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                      <a href="https://openai.com" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/openai.png" alt="OpenAI" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'OA'}))">
                        <div>
                          <div class="font-semibold">OpenAI</div>
                          <div class="text-xs text-slate-400">GPT 5, GPT-4o, reasoning</div>
                        </div>
                      </a>
                      <a href="https://www.anthropic.com/claude" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/anthropic.png" alt="Anthropic" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'AN'}))">
                        <div>
                          <div class="font-semibold">Anthropic</div>
                          <div class="text-xs text-slate-400">Claude Opus 4.1, Sonnet 4, coding</div>
                        </div>
                      </a>
                      <a href="https://deepmind.google/technologies/gemini/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/google.png" alt="Google Gemini" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'GG'}))">
                        <div>
                          <div class="font-semibold">Google</div>
                          <div class="text-xs text-slate-400">Gemini 2.5 (Pro, Flash, Flash‑Lite)</div>
                        </div>
                      </a>
                      <a href="https://ai.meta.com/llama/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/meta.png" alt="Meta Llama" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'ME'}))">
                        <div>
                          <div class="font-semibold">Meta</div>
                          <div class="text-xs text-slate-400">Llama 4 family; embedded in Facebook</div>
                        </div>
                      </a>
                      <a href="https://mistral.ai/models/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/mistral.png" alt="Mistral" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'MI'}))">
                        <div>
                          <div class="font-semibold">Mistral</div>
                          <div class="text-xs text-slate-400">France: Large, Medium 3, Codestral</div>
                        </div>
                      </a>
                      <a href="https://www.deepseek.com/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/deepseek.png" alt="DeepSeek" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'DS'}))">
                        <div>
                          <div class="font-semibold">DeepSeek</div>
                          <div class="text-xs text-slate-400">China: V3 (chat), R1 (reasoner)</div>
                        </div>
                      </a>
                      <a href="https://x.ai/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/xai.png" alt="xAI Grok" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'xAI'}))">
                        <div>
                          <div class="font-semibold">xAI</div>
                          <div class="text-xs text-slate-400">Grok 4 family, integrated with X platform</div>
                        </div>
                      </a>
                      <a href="https://www.midjourney.com/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/midjourney.png" alt="Midjourney" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'MJ'}))">
                        <div>
                          <div class="font-semibold">Midjourney</div>
                          <div class="text-xs text-slate-400">Image generation (v6/v7), Style Tuner</div>
                        </div>
                      </a>
                      <a href="https://elevenlabs.io/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/elevenlabs.png" alt="ElevenLabs" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'11'}))">
                        <div>
                          <div class="font-semibold">ElevenLabs</div>
                          <div class="text-xs text-slate-400">Text‑to‑Speech, Voice Cloning, Sound FX</div>
                        </div>
                      </a>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Model Snapshots (mid‑2025)",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>OpenAI:</strong> Release GPT 5 in August 2025; focused on coding, multimodal capabilities and improved tool calling.</li>
                      <li><strong>Anthropic:</strong> Claude Opus 4.1 and Sonnet 4 emphasize reasoning, safety, and agentic use; best coding models.</li>
                      <li><strong>Google:</strong> Gemini 2.5 (Pro, Flash, Flash‑Lite) with Deep Think mode and adaptive reasoning.</li>
                      <li><strong>Meta:</strong> Llama 4 (Maverick, Scout) natively multimodal; strong on long context and open source ecosystem.</li>
                      <li><strong>Mistral:</strong> Large/Medium 3 for reasoning; Codestral for code; strong EU hosting options.</li>
                      <li><strong>DeepSeek:</strong> V3 (chat) and R1 (reasoning) with OpenAI‑compatible APIs; value‑focused pricing; Chinese ownership.</li>
                      <li><strong>xAI:</strong> Grok 4 with tool use and real‑time search integration, integrated with X (former Twitter).</li>
                      <li><strong>Midjourney:</strong> v6/v7 for high‑quality image generation; strong composition/photorealism; Style Tuner.</li>
                      <li><strong>ElevenLabs:</strong> neural text to speech, voice cloning, multilingual; also speech‑to‑speech and sound effects API.</li>
                    </ul>
                    """,
                ),
            ],
            resources=[
                {"label": "OpenAI", "url": "https://openai.com"},
                {"label": "Anthropic / Claude", "url": "https://www.anthropic.com/claude"},
                {"label": "Google / Gemini", "url": "https://deepmind.google/technologies/gemini/"},
                {"label": "Meta / Llama", "url": "https://ai.meta.com/llama/"},
                {"label": "Mistral", "url": "https://mistral.ai/models/"},
                {"label": "DeepSeek", "url": "https://www.deepseek.com/"},
                {"label": "xAI / Grok", "url": "https://x.ai/"},
                {"label": "Midjourney", "url": "https://www.midjourney.com/"},
                {"label": "ElevenLabs", "url": "https://elevenlabs.io/"},
            ],
        ),
        Module(
            slug="use-foundation-models",
            title="Ways to Use Foundation Models",
            summary="Practical, LLM‑centered patterns you can apply immediately to save time and improve quality.",
            sections=[
                ModuleSection(
                    title="AI Assisted Document Creation",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <ol class="list-decimal ml-6 space-y-1 mt-2">
                        <li><strong>Draft:</strong> Start with bullet points or a rough paragraph in your voice.</li>
                        <li><strong>Context:</strong> Paste key snippets from policies, emails, spreadsheets, or link to docs and state what matters.</li>
                        <li><strong>Ask:</strong> Tell the LLM the <em>purpose, audience, tone, length</em>, and the <em>format</em> you want (bullets, memo, table, JSON).</li>
                        <li><strong>Organize & enhance:</strong> Have it structure the content, fix gaps, propose options, and format consistently.</li>
                        <li><strong>Review:</strong> Verify facts, adjust tone, and finalize. Treat output as a draft.</li>
                      </ol>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Summarization & Q&A (with optional retrieval)",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><em>What it is:</em> Turn long material into key points; ask targeted questions.</li>
                      <li><em>Inputs:</em> meeting notes, emails, policies, web pages; optionally add retrieval over your docs.</li>
                      <li><em>Outputs:</em> bullet summaries, executive briefs, FAQs, next‑step lists.</li>
                      <li><em>Tips:</em> Specify audience and length; require (AND VERIFY) citations when accuracy matters.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Drafting & Generation (you start, LLM elevates)",
                    content="""
                    <p>Begin with your ideas and context; ask the LLM to produce a clear, audience‑appropriate draft.</p>
                    <ul class="list-disc ml-6 space-y-2">
                      <li><em>Use cases:</em> reports, job aids, policy summaries, announcements, meeting notes, and SOPs.</li>
                      <li><em>Process:</em> start with your own ideas and any relevant excerpts; ask for structure, clarity, and tone; iterate.</li>
                      <li><em>Formatting:</em> request headings, lists, tables, and consistent style (AP, plain language, etc.).</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Transformation & Rewrite",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Change tone (formal, friendly, neutral), length (50/150/300 words), or reading level (Plain Language).</li>
                      <li>Translate between languages or convert bullet points into narrative (and vice versa).</li>
                      <li>Turn dense text into checklists, action plans, or slides outlines.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Working with PDFs and Documents",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <p class="text-slate-300 mb-3">Copy text from a PDF and paste it into your AI tool — then tell it exactly what to extract or how to restructure it.</p>
                      <ul class="list-disc ml-6 space-y-2">
                        <li><strong>Extract key fields:</strong> Paste a contract or vendor document and ask the AI to pull out dates, parties, payment terms, SLAs, and renewal conditions — returned as a clean table.</li>
                        <li><strong>PDF to Word:</strong> Copy PDF content and ask the AI to reformat it with proper headings, numbered sections, and clean paragraph structure ready to paste into Word.</li>
                        <li><strong>Summarize long reports:</strong> Paste sections of a lengthy policy or vendor report and get a concise executive summary with key decisions and action items.</li>
                        <li><strong>Compare two documents:</strong> Paste two versions of a policy or contract and ask the AI to list what changed, what was added, and what was removed.</li>
                        <li><strong>Normalize data:</strong> Extract names, route numbers, addresses, or IDs from unstructured text and return them in a consistent, table-ready format.</li>
                      </ul>
                      <p class="mt-3 text-slate-400 text-sm"><strong>Tip:</strong> Copy text directly from the PDF rather than uploading a file. Paste only the relevant section and tell the AI exactly what format you need.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Analyzing Data",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <p class="text-slate-300 mb-3">Paste data snippets, tables, or qualitative notes and ask the AI to find patterns, surface outliers, and generate a narrative you can use directly.</p>
                      <ul class="list-disc ml-6 space-y-2">
                        <li><strong>Trend analysis:</strong> Paste ridership numbers or incident logs and ask: "Which routes show consistent decline over the last 3 months? Rank by change and suggest 2–3 questions worth investigating."</li>
                        <li><strong>Qualitative themes:</strong> Paste complaint logs or operator notes and ask the AI to identify recurring themes, frequency, and a priority ranking.</li>
                        <li><strong>Outlier detection:</strong> Ask the AI to flag rows that look anomalous based on context you provide.</li>
                        <li><strong>Narrative from data:</strong> Give the AI a table of numbers and ask for a short paragraph summarizing key findings, risks, and recommended next steps for a team meeting.</li>
                      </ul>
                      <p class="mt-3 text-slate-400 text-sm"><strong>Guardrail:</strong> Remove sensitive fields before pasting data. Paste representative samples, not full exports.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Building and Enhancing Excel Files",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <p class="text-slate-300 mb-3">Describe what you need in plain English and get back formulas, table structures, or automation scripts ready to use.</p>
                      <ul class="list-disc ml-6 space-y-2">
                        <li><strong>Generate formulas:</strong> "Sum column B where column A equals 'Route 4'" → get the correct SUMIF, VLOOKUP, or INDEX/MATCH formula with an explanation of how it works.</li>
                        <li><strong>Build table structures:</strong> Describe your data and get a CSV with headers and sample rows — paste directly into Excel or import as a new sheet.</li>
                        <li><strong>Pivot table layout:</strong> Describe your data and your question; ask the AI which fields to use as rows, columns, values, and filters.</li>
                        <li><strong>Conditional formatting rules:</strong> Ask for step-by-step instructions to highlight cells that meet your criteria (e.g., ridership below threshold).</li>
                        <li><strong>Automate repetitive tasks:</strong> Describe a multi-step task and ask for a VBA macro or Power Query M script — paste into Excel and run.</li>
                        <li><strong>Enhance existing data:</strong> Paste a messy table and ask the AI to clean column names, standardize formats, add calculated columns, or flag missing values.</li>
                      </ul>
                      <p class="mt-3 text-slate-400 text-sm"><strong>Tip:</strong> Always test formulas and macros on a small sample before applying to your full dataset.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Formatting & Packaging",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Request output as an email, memo, SOP, table, Markdown, or JSON schema you define.</li>
                      <li>Enforce sections and headings; ask for a one‑page and an executive 5‑bullet version.</li>
                      <li>Downloadable formats via tools/integrations: Word (.docx), PowerPoint (.pptx), Excel/CSV (.xlsx/.csv), and images (.png/.svg). Ask the LLM to structure content precisely so it can be exported to these files.</li>
                      <li>Tips: for documents/slides, specify slide titles and bullet counts; for spreadsheets, specify column names and sample rows; for images, request size/aspect and alt text. If needed, ask for Markdown/HTML/CSV that downstream scripts can convert to files.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="A Reusable Prompt Pattern",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <ul class="list-disc ml-6">
                        <li><strong>Role & task:</strong> "You are a comms specialist. Draft a one‑page rider notice."</li>
                        <li><strong>Context:</strong> paste key excerpts, numbers, constraints (don’t include PII).</li>
                        <li><strong>Requirements:</strong> audience, tone, length, must‑include points, sources if needed.</li>
                        <li><strong>Format:</strong> bullets/table/memo/JSON; provide a tiny example when possible.</li>
                        <li><strong>Review:</strong> ask for uncertainties and a checklist for human verification.</li>
                      </ul>
                    </div>
                    """,
                ),
            ],
        ),
        Module(
            slug="transit-use-cases",
            title="Transit Use Cases",
            summary="C-TRAN-aligned applications across service and operations.",
            sections=[
                ModuleSection(
                    title="Customer Experience",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                      <p>Use LLMs to provide faster, clearer answers and consistent information across channels (web, phone, counters), with human oversight where needed.</p>
                      <div class="grid md:grid-cols-2 gap-3">
                        <div>
                          <h4 class="font-semibold">Typical applications</h4>
                          <ul class="list-disc ml-6">
                            <li>Natural‑language FAQs and policy Q&A with citations to official sources.</li>
                            <li>Multilingual responses for common questions (fares, passes, accessibility).</li>
                            <li>Drafting public‑facing explanations based on policy text, reviewed by staff.</li>
                          </ul>
                        </div>
                        <div>
                          <h4 class="font-semibold">Inputs → Outputs</h4>
                          <ul class="list-disc ml-6">
                            <li><em>Inputs:</em> website copy, policy PDFs, service pages, approved answers.</li>
                            <li><em>Outputs:</em> short answers, snippets for web/IVR, translated content.</li>
                          </ul>
                        </div>
                      </div>
                      <p class="text-slate-300 text-sm"><strong>Measure:</strong> first‑contact resolution, response time, and accuracy via spot checks.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Rider Support",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                      <p>Assist riders with timely, accessible information. Keep humans in the loop for publishing and safety‑critical content.</p>
                      <ul class="list-disc ml-6">
                        <li><strong>Service alerts draft:</strong> model drafts a concise alert from operations notes; supervisor approves before posting.</li>
                        <li><strong>Trip help (text‑only):</strong> clarify route options, transfers, and fare rules using official timetables.</li>
                        <li><strong>Accessibility prompts:</strong> generate alt text and plain‑language summaries for key updates.</li>
                      </ul>
                      <p class="text-slate-300 text-sm"><strong>Guardrails:</strong> no real‑time navigation promises; cite sources; require approval on public posts.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Scheduling Support",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                      <p>Use LLMs to summarize patterns and surface hypotheses from notes and historical summaries, not to replace schedulers.</p>
                      <ul class="list-disc ml-6">
                        <li><strong>Pattern insights:</strong> summarize recurring issues from operator notes and incident logs.</li>
                        <li><strong>Scenario narratives:</strong> draft "what‑if" considerations for proposed timetable adjustments.</li>
                        <li><strong>Change summaries:</strong> produce stakeholder updates describing rationale, benefits, and risks.</li>
                      </ul>
                      <p class="text-slate-300 text-sm"><strong>Guardrails:</strong> avoid PII; keep source excerpts; decisions remain with scheduling professionals.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="IT End User Support",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                      <p>Accelerate staff support with clear troubleshooting steps and consistent knowledge articles.</p>
                      <ul class="list-disc ml-6">
                        <li><strong>Triage & routing:</strong> classify tickets by product/urgency; suggest next actions.</li>
                        <li><strong>Guided walkthroughs:</strong> turn SOPs into step‑by‑step instructions with checks.</li>
                        <li><strong>Knowledge upkeep:</strong> summarize change logs into KB article updates for review.</li>
                      </ul>
                      <p class="text-slate-300 text-sm"><strong>Measure:</strong> time‑to‑resolution, deflection rate, and KB accuracy via audits.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Dive Deeper: Artificial Intelligence in Public Transport (UITP, 2025)",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                      <p>This concise industry report from UITP outlines how public transport agencies are adopting AI, from customer information to operations, and the governance practices that keep rollouts safe and responsible.</p>
                      <ul class="list-disc ml-6">
                        <li>Where AI adds value across service and operations.</li>
                        <li>Risks, ethics, data governance, and safety guardrails.</li>
                        <li>Implementation patterns, skills, and procurement considerations.</li>
                      </ul>
                      <p class="mt-2">
                        <a class="text-cyan-300 underline" href="https://cms.uitp.org/wp/wp-content/uploads/2025/03/20250325_Artificial-Intelligence-in-Public-Transport.pdf" target="_blank" rel="noopener">Open the UITP report (PDF)</a>
                      </p>
                    </div>
                    """,
                ),
            ],
            guardrails=[
                "Use only IT-approved AI tools for work tasks.",
                "Save AI prompts and outputs — work-related AI use may be subject to public records requests.",
                "Coordinate with union workforce and stakeholders as appropriate.",
                "Respect data governance, retention, and privacy obligations.",
            ],
        ),
        Module(
            slug="prompting-basics",
            title="Prompting Basics",
            summary="Get better results with simple patterns: role, context, constraints, tiny examples, and a quick review.",
            sections=[
                ModuleSection(
                    title="Start with a clear task (Role + Goal)",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li><strong>Role:</strong> "You are a communications specialist at a public transit agency."</li>
                      <li><strong>Goal:</strong> "Draft a 150–200 word rider notice about a weekend service change."</li>
                      <li><strong>Audience & tone:</strong> "General riders; plain language; friendly and factual."</li>
                    </ul>
                    <p class="mt-2 text-slate-300 text-sm">One sentence for each is enough. Clear beats clever.</p>
                    """,
                ),
                ModuleSection(
                    title="Give context (paste what matters)",
                    content="""
                    <p>Copy in short, relevant snippets the model should use. Call out what is most important.</p>
                    <ul class="list-disc ml-6 space-y-2">
                      <li>"Key facts: Route 105 detour Sat–Sun (8am–6pm); stops 5412 and 5414 closed; use stop 5420."</li>
                      <li>"Policy excerpt (quote): ‘Operators must …’ Use this wording where appropriate."</li>
                      <li>"Do <em>not</em> mention internal ticket numbers or staff names."</li>
                    </ul>
                    <p class="mt-2 text-slate-300 text-sm">When accuracy matters, ask the model to <strong>quote</strong> or <strong>cite</strong> from your pasted snippets.</p>
                    """,
                ),
                ModuleSection(
                    title="Set constraints and format",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li><strong>Length:</strong> "150–200 words" or "5 bullets, max 14 words each."</li>
                      <li><strong>Structure:</strong> "Headings: What’s changing, When, Affected stops, Alternatives."</li>
                      <li><strong>Output type:</strong> "Give as a bulleted list" or "Return JSON with keys: title, body, next_steps."</li>
                      <li><strong>Accessibility:</strong> "Plain language; include alt text for any images."</li>
                    </ul>
                    <p class="mt-2 text-slate-300 text-sm">See "Formatting & Packaging" for exporting to Word/PowerPoint/Excel via structured output.</p>
                    """,
                ),
                ModuleSection(
                    title="Show one tiny example (few‑shot)",
                    content="""
                    <p>A short example teaches style. Keep it tiny and obviously different from your request.</p>
                    <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>Example style (different topic):
Title: Elevator maintenance this Friday
Body: On Friday, March 12, the north garage elevator will be offline from 10am–2pm
for maintenance. Please use the south elevator or stairs. We appreciate your patience.</code></pre>
                    <p class="text-slate-300 text-sm mt-2">Then say: "Use the format and tone shown in the example."</p>
                    """,
                ),
                ModuleSection(
                    title="Ask for a plan, then the deliverable",
                    content="""
                    <p>For trickier tasks, ask the model to outline steps first, then produce the draft.</p>
                    <ul class="list-disc ml-6">
                      <li>"First list the sections you’ll include and why (1–2 bullets each). Then draft the notice."</li>
                      <li>"If any required detail is missing, list questions before drafting."</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Ask for a self‑check",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li>"After the draft, list 3 uncertainties or assumptions you made."</li>
                      <li>"Provide a 5‑item checklist I can verify (dates, stops, times, links, approvals)."</li>
                      <li>"Flag anything that might confuse riders."</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Iterate: refine tone and length",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li>"Shorten by ~20% and keep the most important details up front."</li>
                      <li>"Rewrite for plain language (8th‑grade reading level) and remove jargon."</li>
                      <li>"Give a Spanish translation after the English version."</li>
                    </ul>
                    <p class="mt-2 text-slate-300 text-sm">Small, specific edits work better than "make it better."</p>
                    """,
                ),
                ModuleSection(
                    title="Reusable prompt template",
                    content="""
                    <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>Role: You are a &lt;role&gt; at a public transit agency.
Goal: &lt;what to produce&gt; for &lt;audience&gt; in &lt;tone&gt;.
Context: &lt;3–6 key facts or quoted snippets&gt; (do not include PII).
Format: &lt;bullets / memo / table / JSON keys: ...&gt;.
Constraints: length, headings, must‑include points, dates/times, links.
Process: (1) list sections or questions, (2) draft, (3) self‑check with 3 uncertainties and a 5‑item verification list.
</code></pre>
                    """,
                ),
                ModuleSection(
                    title="Everyday examples",
                    content="""
                    <p class="text-slate-400 text-sm mb-3">These patterns work in any IT-approved AI tool and apply across many types of work, not just transit.</p>
                    <div class="space-y-4">
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold mb-1">Analyzing a report or dataset</h4>
                        <p class="text-sm text-slate-300">Instead of: <em>"What does this data say?"</em></p>
                        <p class="text-sm mt-1">Try: <em>"You are a transit operations analyst. Review the ridership numbers below and identify: (1) the top 3 trends, (2) any routes with consistent decline over the past 3 months, and (3) two questions worth investigating. Return as 5 bullets for a weekly operations meeting."</em></p>
                      </div>
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold mb-1">Summarizing a long document</h4>
                        <p class="text-sm text-slate-300">Instead of: <em>"Summarize this."</em></p>
                        <p class="text-sm mt-1">Try: <em>"Summarize the text below for a non-technical manager. Use 4 bullets. Each bullet should be one sentence. Focus on decisions that need to be made, not background detail."</em></p>
                      </div>
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold mb-1">Rewriting for a different audience</h4>
                        <p class="text-sm text-slate-300">Instead of: <em>"Make this simpler."</em></p>
                        <p class="text-sm mt-1">Try: <em>"Rewrite the following for someone with no technical background. Plain language, 8th-grade reading level, no jargon. Keep the key message but cut the length by about 30%."</em></p>
                      </div>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Quick before/after example (transit)",
                    content="""
                    <div class="grid md:grid-cols-2 gap-4">
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold mb-2">Vague prompt</h4>
                        <p>"Write something about the service change."</p>
                      </div>
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold mb-2">Clear prompt</h4>
                        <p>"You are a C‑TRAN comms specialist. Draft a 150–200 word rider notice about the Route 105 weekend detour. Audience: general riders; tone: plain language. Key facts: detour Sat–Sun 8am–6pm; stops 5412 and 5414 closed; use stop 5420; normal schedule resumes Monday. Headings: What’s changing, When, Affected stops, Alternatives. After the draft, list 3 uncertainties and a 5‑item verification checklist."</p>
                      </div>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Safety and good judgment",
                    content="""
                    <ul class="list-disc ml-6 space-y-2">
                      <li><strong>Use only IT-approved tools</strong> for work AI tasks. Do not use public consumer tools for C-TRAN work.</li>
                      <li><strong>Save your prompts and AI outputs.</strong> Work-related AI use may be subject to public records requests.</li>
                      <li>Avoid pasting personally identifiable information (names, contact info, rider data) into AI tools unless specifically cleared.</li>
                      <li>For facts and policies, paste short quotes and ask for citations. Verify before using.</li>
                      <li>Keep humans in the loop for public posts and safety‑critical messages.</li>
                    </ul>
                    """,
                ),
            ],
        ),
        Module(
            slug="exercises",
            title="Practice Exercises",
            summary="Try these quick, copy‑paste exercises in any approved AI tool.",
            sections=[
                ModuleSection(
                    title="Summarize a document or report",
                    content="""
                    <p>Objective: Get a clear, short summary with key decisions and next steps.</p>
                    <ul class="list-disc ml-6 space-y-1">
                      <li>Prompt: "Summarize the text below for a coworker. Include 3 bullets covering the key points and 2 next steps."</li>
                      <li>Paste a section of a report, policy, or meeting notes (remove PII first).</li>
                      <li>Follow up: "Now give me a one-sentence version for a status update."</li>
                    </ul>
                    <p class="text-sm text-slate-400"><strong>Use your IT-approved AI tool.</strong> Save your prompt and the AI's response as part of your work records.</p>
                    """,
                ),
                ModuleSection(
                    title="Extract data from a PDF or document",
                    content="""
                    <p>Objective: Pull structured information out of unstructured text.</p>
                    <ul class="list-disc ml-6 space-y-1">
                      <li>Copy text from a contract, report, or policy PDF (remove any PII or sensitive fields first).</li>
                      <li>Prompt: "From the text below, extract: (1) key dates, (2) responsible parties, (3) obligations or requirements. Return as a table with columns: Item, Detail."</li>
                      <li>Follow up: "Now reformat this with proper headings and numbered sections, ready to paste into Word."</li>
                    </ul>
                    <p class="text-sm text-slate-400"><strong>Use your IT-approved AI tool.</strong> Save your prompt and the AI's response as part of your work records.</p>
                    """,
                ),
                ModuleSection(
                    title="Build or enhance an Excel table",
                    content="""
                    <p>Objective: Generate formulas, clean data, or create a table structure from scratch.</p>
                    <ul class="list-disc ml-6 space-y-1">
                      <li>Describe what you need: "Write an Excel formula that sums column C where column A equals 'Route 4' and column B is after 1/1/2025."</li>
                      <li>Or paste a messy data snippet and ask: "Clean this table — standardize the date format, fix capitalization in the Name column, and flag any rows with missing values."</li>
                      <li>Ask for a CSV: "Give me a CSV with headers and 3 sample rows for tracking monthly ridership by route and stop."</li>
                    </ul>
                    <p class="text-sm text-slate-400"><strong>Tip:</strong> Test formulas on a small sample first. Use your IT-approved AI tool and save your work records.</p>
                    """,
                ),
                ModuleSection(
                    title="Draft a rider notice",
                    content="""
                    <p>Objective: Create a clear, public‑facing update.</p>
                    <ul class="list-disc ml-6">
                      <li>Role & goal: "You are a transit comms specialist. Draft a 150–200 word rider notice."</li>
                      <li>Facts: route, dates/times, affected stops, alternatives (paste brief snippets).</li>
                      <li>Format: "Headings: What’s changing, When, Affected stops, Alternatives."</li>
                    </ul>
                    <p class="text-sm text-slate-400">Tip: Ask for a 5‑item verification checklist.</p>
                    """,
                ),
                ModuleSection(
                    title="Rewrite for tone or length",
                    content="""
                    <p>Objective: Make content easier to read.</p>
                    <ul class="list-disc ml-6">
                      <li>"Rewrite in plain language at 8th‑grade level."</li>
                      <li>"Shorten by ~20% and keep key points up top."</li>
                      <li>"Provide a Spanish translation below the English."</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Classify and route a request",
                    content="""
                    <p>Objective: Tag and triage messages consistently.</p>
                    <ul class="list-disc ml-6">
                      <li>Categories: "fares, passes, accessibility, schedule, complaint, compliment, other."</li>
                      <li>Prompt: "Return JSON: {category, urgency: low|med|high, suggested_team}."</li>
                      <li>Paste one short message to start.</li>
                    </ul>
                    """,
                ),
            ],
        ),
        Module(
            slug="final",
            title="Final Quiz",
            summary="Capstone knowledge check. Answer all questions correctly to complete the program.",
            sections=[
                ModuleSection(
                    title="How this works",
                    content=(
                        "This final quiz covers guardrails, delivery models, LLM limits, task patterns, and transit use cases. "
                        "When you have answered all questions correctly, use the Complete button to finish."
                    ),
                ),
            ],
            guardrails=[
                "Treat answers as guidance; confirm critical decisions with policy owners.",
            ],
        ),
    ]


def get_module(slug: str) -> Optional[Module]:
    for m in get_modules():
        if m.slug == slug:
            return m
    return None


def get_course_meta() -> CourseMeta:
    return CourseMeta(
        slug="course-1",
        title="AI Foundations",
        summary="A 30-minute, approachable program to align on AI and its role at C-TRAN.",
        duration="~30 minutes",
        level="Introductory",
        hero_image="/static/images/courses/intro/hero.png",
        thumbnail="/static/images/courses/intro/thumb.png",
        og_image="/static/images/courses/intro/hero.png",
        tags=["AI", "LLM", "Foundations"],
    )
