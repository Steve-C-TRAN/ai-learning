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
                    title="AI vs ML vs Generative AI vs LLMs",
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
                ModuleSection(
                    title="Dive Deeper: Enterprise AI Strategy and CEO Leadership (McKinsey)",
                    content="""
                    <p>In this talk, McKinsey's head of CEO services explores how senior leaders can navigate the rapidly evolving AI landscape, make smart trade-offs, and integrate AI into long-term strategy. This video is ideal for executives who want to lead AI adoption effectively.</p>
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/uTRKdCY4HdE" title="Enterprise AI Strategy and CEO Leadership - McKinsey" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    """,
                ),
            ],
            resources=[
                {"label": "C-TRAN Website", "url": "https://www.c-tran.com/"},
            ],
        ),
        Module(
            slug="ai-eras",
            title="AI Eras",
            summary="From rules and classic ML to agentic systems — how we got here, why it’s accelerating, and what it means for your team.",
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
                    title="The Agentic Era (Today)",
                    content="""
                    <p>Modern systems do more than chat — they <em>act</em> by calling tools, browsing data, and executing steps toward a goal.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Tool use:</strong> call functions, query databases, trigger workflows.</li>
                      <li><strong>Planning:</strong> break problems into steps; reflect and iterate.</li>
                      <li><strong>Multimodal:</strong> text + images (and increasingly audio/video) in a single workflow.</li>
                      <li><strong>Human + AI teamwork:</strong> draft, then route to people for review/approval.</li>
                    </ul>
                    <p class="mt-3 text-slate-300">Transit ideas:</p>
                    <ul class="list-disc ml-6">
                      <li>Draft rider alerts; a tool step posts to channels after supervisor approval.</li>
                      <li>Summarize daily ops reports and flag anomalies for supervisors.</li>
                      <li>Answer common staff questions using policy docs + search connectors.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Why Now? The Acceleration",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Scale:</strong> more compute + improved training techniques.</li>
                      <li><strong>Data:</strong> broader corpora and domain adaptation options.</li>
                      <li><strong>Architecture:</strong> instruction tuning, retrieval, tool-use, memory patterns.</li>
                      <li><strong>Ecosystem:</strong> APIs, plugins, and copilot-style interfaces everywhere.</li>
                      <li><strong>Economics:</strong> costs dropping; on-device models improving.</li>
                    </ul>
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
                    <p>Expect more autonomy and self-improvement — but value comes from safe, measurable pilots that help people, not hype.</p>
                    """,
                ),
            ],
        ),
        Module(
            slug="llms",
            title="Understanding LLMs",
            summary="What LLMs are, how they work, and how to use them well.",
            sections=[
                ModuleSection("What LLMs Are", "Models trained on massive text corpora to predict the next token and generate useful outputs."),
                ModuleSection("How They Work", "They learn patterns, facts, and reasoning; adapt to tasks like summarization or drafting."),
                ModuleSection("Strengths & Limits", "Great at language tasks; can hallucinate, be biased, or confidently wrong — use thoughtfully."),
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
                ModuleSection(
                    title="Dive Deeper: The AI Revolution Is Underhyped (Eric Schmidt, TED)",
                    content="""
                    <p>Former Google CEO Eric Schmidt explains why AI’s potential is far greater than most people realize, highlighting transformative opportunities and the need for bold, informed leadership.</p>
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/id4YRO7G0wE" title="The AI Revolution Is Underhyped - Eric Schmidt - TED Talk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
            summary="Patterns you can apply immediately to save time and improve quality.",
            sections=[
                ModuleSection("Summarization & Q&A", "Condense documents, highlight key points, answer targeted questions."),
                ModuleSection("Classification & Routing", "Tag tickets, triage requests, route workflows automatically."),
                ModuleSection("Generation", "Draft emails, reports, plans, and code with guidance and structure."),
                ModuleSection("Analysis & Reports", "Assist with data interpretation and quick narrative reports."),
            ],
        ),
        Module(
            slug="transit-use-cases",
            title="Transit Use Cases",
            summary="C-TRAN-aligned applications across service and operations.",
            sections=[
                ModuleSection("Customer Experience", "Faster, more accurate rider answers and tailored info."),
                ModuleSection("Rider Support", "Service alerts, trip planning assistance, accessibility prompts."),
                ModuleSection("Scheduling Support", "Pattern insights and suggestions based on history and conditions."),
                ModuleSection("IT End User Support", "Troubleshooting tips and task walkthroughs for staff."),
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
