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
            title="Introduction & Goals",
            summary="A 30-minute, approachable program to align on AI and its role at C-TRAN.",
            sections=[
                ModuleSection(
                    title="Program Overview",
                    content=(
                        "<p>We’ll explore how AI is changing how organizations operate — and what it means for C-TRAN.</p>"
                        "<p>This isn’t about becoming data scientists; it’s about a shared understanding of AI today and creative ways it can help our agency.</p>"
                        "<p>You’ll see practical examples (transit and beyond) and ideas you can try on your own.</p>"
                    ),
                ),
                ModuleSection(
                    title="Program Goals",
                    content=(
                        "<ul class=\"list-disc ml-6\">"
                        "<li>Build a clear, hype-free understanding of AI</li>"
                        "<li>Get current on today’s capabilities and vendors</li>"
                        "<li>Start thinking innovatively about AI uses at C-TRAN for service, efficiency, and readiness</li>"
                        "</ul>"
                        "<p class=\"mt-3 text-slate-300\">No deep technical background required — just curiosity.</p>"
                    ),
                ),
                ModuleSection(
                    title="Agenda",
                    content=(
                        "<ul class=\"list-disc ml-6\">"
                        "<li>AI eras: rules/ML → foundational → agentic</li>"
                        "<li>Today’s models and vendors</li>"
                        "<li>Delivery frameworks (cloud APIs, integrated tools, fine-tuning, on-device)</li>"
                        "<li>How LLMs work and their limits</li>"
                        "<li>Using foundation models effectively</li>"
                        "<li>AI for programmers and IT</li>"
                        "<li>Transit use cases</li>"
                        "<li>Prompting basics and practice</li>"
                        "<li>Image creation examples</li>"
                        "</ul>"
                    ),
                ),
                ModuleSection(
                    title="Definitions",
                    content=(
                        "<p><strong>Artificial Intelligence (AI)</strong> is the broad field of making computers perform tasks that typically require human intelligence (reasoning, planning, perception, language).</p>"
                        "<p><strong>Machine Learning (ML)</strong> is a subset of AI focused on learning patterns from data to make predictions or decisions without being explicitly programmed for every rule.</p>"
                        "<p><strong>Generative AI</strong> refers to models that can create new content (text, images, audio, code) based on patterns learned from data.</p>"
                        "<p><strong>Large Language Models (LLMs)</strong> are a type of generative AI trained on vast text corpora to predict the next token, enabling tasks like summarization, Q&A, drafting, and translation.</p>"
                        "<ul class=\"list-disc ml-6 mt-2\">"
                        "<li><em>Strengths:</em> language understanding, drafting, summarization</li>"
                        "<li><em>Limits:</em> can hallucinate, reflect biases, require clear instructions and verification</li>"
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
                    title="From Rules to Learning: A Brief Timeline",
                    content="""
                    <ul class="list-disc ml-6 space-y-2 sm:space-y-3">
                      <li><strong>Rules & Classic ML (1980s–2010s):</strong> Expert systems (if‑then rules), regression, decision trees, and SVMs (Support Vector Machines) excel at narrow, structured problems with labeled features. <em>Examples:</em> spam filtering, credit scoring, demand forecasting, fraud detection.</li>
                      <li><strong>Early Transfer/Foundation (2018–2020):</strong> ELMo (Embeddings from Language Models), ULMFiT (Universal Language Model Fine‑tuning), and BERT (Bidirectional Encoder Representations from Transformers) bring contextual embeddings and task transfer, enabling strong performance with less task‑specific data. <em>Examples:</em> sentiment analysis, named‑entity recognition, document classification, improved search/ranking.</li>
                      <li><strong>2020 — GPT‑3:</strong> A very large language model (LLM) that signaled the emergence of high‑capability generative AI, enabling fluent long‑form text, few‑shot generalization, and broad task coverage. <em>Examples:</em> drafting emails and reports, summarization, translation, simple code generation, chat prototypes.</li>
                      <li><strong>2023–Now — Agentic:</strong> Models plan, call tools/APIs (function calling), retrieve knowledge (RAG), and iterate with memory/reflect loops to complete multi‑step goals. <em>Examples:</em> multi‑step report drafting with data pulls, meeting scheduling, ticket triage with workflow triggers.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Pioneers of AI",
                    content="""
                    <p>Today’s advances stand on decades of research. A few early pioneers:</p>
                    <ul class="list-disc ml-6">
                      <li><a class="text-cyan-300 underline" href="https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)" target="_blank" rel="noopener">John McCarthy</a> — coined the term “Artificial Intelligence,” organized the 1956 Dartmouth workshop.</li>
                      <li><a class="text-cyan-300 underline" href="https://en.wikipedia.org/wiki/Karen_Sp%C3%A4rck_Jones" target="_blank" rel="noopener">Karen Spärck Jones</a> — pioneer of information retrieval (IDF), shaping modern search and NLP.</li>
                    </ul>
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
                          <li>Give it a goal (“Draft a service alert based on today’s outage”).</li>
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
                      <li><strong>Myth:</strong> “LLMs know the truth.” <strong>Reality:</strong> They predict tokens; verify critical outputs.</li>
                      <li><strong>Myth:</strong> “AI replaces everyone.” <strong>Reality:</strong> Best outcomes are human + AI teams.</li>
                      <li><strong>Myth:</strong> “More prompts = better.” <strong>Reality:</strong> Clarity, context, and constraints matter most.</li>
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
                      <li>What does a good “human-in-the-loop” checkpoint look like for our teams?</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Pitfalls & Guardrails",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Privacy:</strong> Avoid PII in public tools; prefer approved options.</li>
                      <li><strong>Hallucinations:</strong> For critical facts, require sources and human review.</li>
                      <li><strong>Brittleness:</strong> Monitor agents; start small and measure impact.</li>
                      <li><strong>Equity & Safety:</strong> Audit outputs for bias; keep safety first.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="What’s Next?",
                    content="""
                    <p>Software engineering productivity is increasing rapidly, more autonomous agents will be capabale of self-improvement.</p>
                    """,
                ),
            ],
        ),
        Module(
            slug="llms",
            title="Understanding LLMs",
            summary="Foundation models, what LLMs are, how they work, where they shine and struggle — plus a quick mental picture.",
            sections=[
                ModuleSection(
                    title="Foundation Models (Definition)",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <p><strong>Foundation Model:</strong> a large model trained on broad, general‑purpose data (text, images, code, etc.) so it learns useful patterns that can be <em>adapted</em> to many tasks. You can use it as‑is (prompting), add your knowledge via <em>retrieval</em>, or <em>fine‑tune</em> it for specific styles and workflows.</p>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="What LLMs Are (and Aren’t)",
                    content="""
                    <p><strong>LLMs</strong> (Large Language Models) are a <em>type</em> of foundation model focused on language. They predict the next token (piece of text) extremely well, which lets them draft, summarize, translate, and reason in useful ways.</p>
                    <ul class="list-disc ml-6 mt-2">
                      <li><strong>They are</strong> general language engines you steer with instructions (prompts).</li>
                      <li><strong>They aren’t</strong> databases of truth — treat outputs as <em>drafts</em> and verify important facts.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="How They Work",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Tokens:</strong> Text is broken into tokens; the model predicts the next token given context.</li>
                      <li><strong>Transformers:</strong> The architecture uses <em>attention</em> to focus on relevant parts of the input for each prediction.</li>
                      <li><strong>Pretraining:</strong> Learn patterns from large corpora; no task‑specific labels required.</li>
                      <li><strong>Instruction‑tuning:</strong> Additional training makes models follow plain‑English instructions.</li>
                      <li><strong>RAG (Retrieval‑Augmented Generation):</strong> Bring your documents at answer time for grounded responses.</li>
                      <li><strong>Tool use:</strong> Some models can call functions/APIs (search, databases) to get facts or take actions.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="What They’re Great At",
                    content="""
                    <ul class="list-disc ml-6">
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
                    <ul class="list-disc ml-6">
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
                "Avoid sharing PII or sensitive data in public tools.",
                "Prefer business-approved tools for operational content.",
                "Verify critical outputs; treat AI responses as drafts, not ground truth.",
            ],
        ),
        Module(
            slug="current-models",
            title="Current AI Models & Vendors",
            summary="OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, and xAI — who does what today, at a glance.",
            sections=[
                ModuleSection(
                    title="Vendors at a Glance",
                    content="""
                    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                      <a href="https://openai.com" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/openai.png" alt="OpenAI" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'OA'}))">
                        <div>
                          <div class="font-semibold">OpenAI</div>
                          <div class="text-xs text-slate-400">GPT-4o, o4-mini, reasoning</div>
                        </div>
                      </a>
                      <a href="https://www.anthropic.com/claude" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/anthropic.png" alt="Anthropic" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'AN'}))">
                        <div>
                          <div class="font-semibold">Anthropic</div>
                          <div class="text-xs text-slate-400">Claude Opus 4.1, Sonnet 4</div>
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
                          <div class="text-xs text-slate-400">Llama 4 family</div>
                        </div>
                      </a>
                      <a href="https://mistral.ai/models/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/mistral.png" alt="Mistral" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'MI'}))">
                        <div>
                          <div class="font-semibold">Mistral</div>
                          <div class="text-xs text-slate-400">Large, Medium 3, Codestral</div>
                        </div>
                      </a>
                      <a href="https://www.deepseek.com/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/deepseek.png" alt="DeepSeek" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'DS'}))">
                        <div>
                          <div class="font-semibold">DeepSeek</div>
                          <div class="text-xs text-slate-400">V3 (chat), R1 (reasoner)</div>
                        </div>
                      </a>
                      <a href="https://x.ai/" target="_blank" rel="noopener" class="glass-effect p-3 rounded border border-slate-700/50 flex items-center gap-3 hover:border-slate-600">
                        <img src="/static/images/vendor_logos/xai.png" alt="xAI Grok" class="h-8" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-8 w-8 rounded bg-slate-700 flex items-center justify-center text-xs',textContent:'xAI'}))">
                        <div>
                          <div class="font-semibold">xAI</div>
                          <div class="text-xs text-slate-400">Grok 4 family</div>
                        </div>
                      </a>
                    </div>
                    <p class="text-xs text-slate-400 mt-2">Logos will show if placed under <code>/static/images/vendor_logos/</code> (e.g., <code>openai.png</code>). Otherwise, initials are shown.</p>
                    """,
                ),
                ModuleSection(
                    title="Model Snapshots (mid‑2025)",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>OpenAI:</strong> GPT‑4o and o4‑mini for multimodal + cost efficiency; research on o3 reasoning.</li>
                      <li><strong>Anthropic:</strong> Claude Opus 4.1 and Sonnet 4 emphasize reasoning, safety, and agentic use.</li>
                      <li><strong>Google:</strong> Gemini 2.5 (Pro, Flash, Flash‑Lite) with Deep Think mode and adaptive reasoning.</li>
                      <li><strong>Meta:</strong> Llama 4 (Maverick, Scout) natively multimodal; strong on long context and open ecosystem.</li>
                      <li><strong>Mistral:</strong> Large/Medium 3 for reasoning; Codestral for code; strong EU hosting options.</li>
                      <li><strong>DeepSeek:</strong> V3 (chat) and R1 (reasoning) with OpenAI‑compatible APIs; value‑focused pricing.</li>
                      <li><strong>xAI:</strong> Grok 4 with tool use and real‑time search integration.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Choosing a Model for a Pilot",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Task fit:</strong> summarization, generation, code, multilingual, or vision?</li>
                      <li><strong>Data sensitivity:</strong> approved enterprise tiers vs. public tools; consider on‑device options.</li>
                      <li><strong>Latency/cost:</strong> smaller variants (Flash/mini/Small) for high‑volume tasks.</li>
                      <li><strong>Deployment:</strong> API, VPC, on‑prem, or edge device? Support and SLAs?</li>
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
            ],
        ),
        Module(
            slug="use-foundation-models",
            title="Ways to Use Foundation Models",
            summary="Practical, LLM‑centered patterns you can apply immediately to save time and improve quality.",
            sections=[
                ModuleSection(
                    title="How We Use LLMs in Practice (simple workflow)",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                      <p>These patterns assume we’re using <strong>LLMs</strong> (language foundation models) with our own context.</p>
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
                      <li><em>Tips:</em> Specify audience and length; require citations when accuracy matters.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Drafting & Generation (you start, LLM elevates)",
                    content="""
                    <p>Begin with your ideas and context; ask the LLM to produce a clear, audience‑appropriate draft.</p>
                    <ul class="list-disc ml-6">
                      <li><em>Use cases:</em> emails, reports, job aids, policy updates, announcements.</li>
                      <li><em>Process:</em> provide your bullets + relevant excerpts; ask for structure, clarity, and tone; iterate.</li>
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
                    title="Extraction & Structuring",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Pull fields from emails, PDFs, or notes and output as JSON, CSV, or a table (e.g., dates, routes, contacts).</li>
                      <li>Normalize names, addresses, or IDs; validate formats with simple rules in the prompt.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Classification & Routing",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Tag messages (topic, urgency, department) and route to the right queue or person.</li>
                      <li>Apply policy labels or sensitivity flags based on brief criteria you provide.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Analysis & Quick Reports",
                    content="""
                    <ul class="list-disc ml-6">
                      <li>Ask for patterns and insights from qualitative notes or light tabular data (paste snippets or summaries).</li>
                      <li>Generate a short narrative with key findings, risks, and recommended next steps.</li>
                    </ul>
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
                        <li><strong>Role & task:</strong> “You are a comms specialist. Draft a one‑page rider notice.”</li>
                        <li><strong>Context:</strong> paste key excerpts, numbers, constraints (don’t include PII).</li>
                        <li><strong>Requirements:</strong> audience, tone, length, must‑include points, sources if needed.</li>
                        <li><strong>Format:</strong> bullets/table/memo/JSON; provide a tiny example when possible.</li>
                        <li><strong>Review:</strong> ask for uncertainties and a checklist for human verification.</li>
                      </ul>
                    </div>
                    """,
                ),
                ModuleSection(
                    title="Advanced: Ideate → Plan → Create",
                    content="""
                    <p>This advanced, <em>agentic</em> workflow uses an LLM to first <strong>ideate</strong> options, then <strong>plan</strong> the work, then <strong>create</strong> the deliverable — with tight human review in between.</p>
                    <figure class="space-y-2 mt-2">
                      <div class="mx-auto max-w-3xl md:max-w-5xl px-2 flex justify-center">
                        <a href="/static/images/ideate_plan_create.svg" target="_blank" rel="noopener" title="Open full-size">
                          <img src="/static/images/ideate_plan_create.svg" alt="Ideate, Plan, Create workflow diagram" class="block w-auto max-w-full h-auto object-contain max-h-[70vh] mx-auto rounded border border-slate-700/50 bg-slate-900" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'h-40 flex items-center justify-center text-xs bg-slate-800 rounded border border-slate-700/50',textContent:'Workflow diagram placeholder'}) )">
                        </a>
                      </div>
                      <figcaption class="text-xs md:text-sm text-slate-400 text-center">Workflow: generate options → choose and plan → draft and refine with human review.</figcaption>
                    </figure>
                    <div class="mt-3 grid md:grid-cols-2 gap-4">
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold">How to run it</h4>
                        <ol class="list-decimal ml-6 space-y-1">
                          <li><strong>Ideate:</strong> Ask for 3–5 approaches with pros/cons, risks, and required inputs.</li>
                          <li><strong>Plan:</strong> Pick one; ask for objectives, stakeholders, steps, timelines, and success criteria.</li>
                          <li><strong>Create:</strong> Provide your draft/notes and key excerpts; ask for a first draft in the required format.</li>
                          <li><strong>Review:</strong> Have the LLM list uncertainties and assumptions; you edit and confirm sources.</li>
                          <li><strong>Polish:</strong> Request tone, length, and formatting fixes (headings, tables, lists, alt text).</li>
                        </ol>
                      </div>
                      <div class="bg-slate-800/50 border border-slate-700 rounded p-3">
                        <h4 class="font-semibold">Prompting tips</h4>
                        <ul class="list-disc ml-6 space-y-1">
                          <li>State <em>audience</em>, <em>purpose</em>, and <em>constraints</em> (word count, style, must‑include points).</li>
                          <li>Paste relevant excerpts; for accuracy, ask for citations or quotes from your snippets.</li>
                          <li>Ask for a checklist you can verify before sending or publishing.</li>
                          <li>For packaging, request specific output types (memo, table, Markdown, JSON) for easy export.</li>
                        </ul>
                      </div>
                    </div>
                    <p class="mt-3 text-slate-300"><strong>When to use:</strong> important communications, policy updates, proposals, or plans that benefit from options, structure, and iteration — with humans in the loop.</p>
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
                      <p>Use LLMs to provide faster, clearer answers and consistent information across channels (web, phone, counters) — with human oversight where needed.</p>
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
                      <p>Use LLMs to summarize patterns and surface hypotheses from notes and historical summaries — not to replace schedulers.</p>
                      <ul class="list-disc ml-6">
                        <li><strong>Pattern insights:</strong> summarize recurring issues from operator notes and incident logs.</li>
                        <li><strong>Scenario narratives:</strong> draft “what‑if” considerations for proposed timetable adjustments.</li>
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
            ],
            guardrails=[
                "Coordinate with union workforce and stakeholders as appropriate.",
                "Respect data governance, retention, and privacy obligations.",
            ],
        ),
        Module(
            slug="prompting-basics",
            title="Prompting Basics",
            summary="Clear instructions, context, constraints — and practice.",
            sections=[
                ModuleSection("Clarity & Context", "Be specific; give background so models understand the situation."),
                ModuleSection("Constraints & Format", "State tone, length, and output format (bullets, table, letter, etc.)."),
                ModuleSection("Practice", "Compare prompts across tools (CoPilot, ChatGPT, Claude, Gemini) and iterate."),
            ],
        ),
        Module(
            slug="exercises",
            title="Practice Exercises",
            summary="Hands-on ideas to try in your preferred tools.",
            sections=[
                ModuleSection("Summarize & Draft", "Use Copilot to summarize an email or draft a response."),
                ModuleSection("Brainstorm", "Use ChatGPT to ideate rider support improvements; compare with Claude or Gemini."),
                ModuleSection("Compare Tools", "Run the same prompt in multiple tools and note differences."),
            ],
        ),
        Module(
            slug="refreshers",
            title="Refreshers & Wrap-Up",
            summary="Review, next steps, and continued exploration.",
            sections=[
                ModuleSection("Review", "We covered AI eras, current tools, delivery models, LLMs, usage patterns, and transit use cases."),
                ModuleSection("Next Steps", "Keep experimenting: try prompts, compare tools, identify where AI could help your team."),
                ModuleSection("Ongoing", "We’ll continue the conversation as technology evolves and opportunities emerge."),
            ],
            resources=[
                {"label": "NIST AI RMF", "url": "https://www.nist.gov/itl/ai-risk-management-framework"},
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
        title="AI Foundations for C-TRAN",
        summary="A 30-minute, approachable program to align on AI and its role at C-TRAN.",
        duration="~30 minutes",
        level="Introductory",
        hero_image="/static/images/courses/_defaults/hero.svg",
        thumbnail="/static/images/courses/_defaults/thumb.svg",
        og_image="/static/images/courses/_defaults/hero.svg",
        tags=["AI", "LLM", "Foundations"],
    )
