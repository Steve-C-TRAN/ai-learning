# app/content/modules2.py
# Defines Course 2 learning modules and sections for the C-TRAN AI Learning App

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
            slug="delivery-models",
            title="AI Frameworks & Delivery Models",
            summary="Clear ways to deliver AI at C‑TRAN: public assistants, cloud APIs, integrated tools, locally hosted open‑source, fine‑tuning/RAG, and on‑device.",
            sections=[
                ModuleSection(
                    title="How to think about delivery",
                    content="""
                    <p>There isn’t one “right” way to use AI. Choose the option that fits the task, sensitivity of data, speed/cost needs, and IT manageability.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Start simple:</strong> try approved tools; prove value fast.</li>
                      <li><strong>Match sensitivity:</strong> public vs. enterprise vs. C‑TRAN‑hosted.</li>
                      <li><strong>Scale deliberately:</strong> move from prototypes to managed services.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Public AI Assistants (ChatGPT, Claude.ai, Gemini)",
                    content="""
                    <p>These are the familiar, public websites and mobile apps. They are great for <em>learning, brainstorming, and non‑sensitive drafting</em>.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Where this sits:</strong> Vendor‑hosted, consumer interfaces. Data handling depends on the product tier.</li>
                      <li><strong>Use when:</strong> experimenting, ideation, or creating generic content with <em>no sensitive data</em>.</li>
                      <li><strong>Avoid:</strong> PII, confidential, or operationally sensitive information.</li>
                      <li><strong>Enterprise options exist:</strong> business tiers (e.g., Microsoft Copilot, ChatGPT Team/Enterprise, Claude for Business) add controls and protections.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Cloud APIs (Managed)",
                    content="""
                    <p>Call models over HTTPS from your applications. The vendor runs the infrastructure; you control prompts, data flow, and guardrails.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Pros:</strong> fast to adopt, scalable, access to latest models and features.</li>
                      <li><strong>Cons:</strong> data residency/integration reviews; ongoing usage costs.</li>
                      <li><strong>Good for:</strong> chatbots, summarization services, internal copilots, analytics helpers.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Integrated in Business Tools (Copilot & friends)",
                    content="""
                    <p>AI features embedded in apps we already use (email, documents, spreadsheets, CRM, ticketing).</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Pros:</strong> no new UI to learn; immediate productivity wins.</li>
                      <li><strong>Cons:</strong> less control over prompts/outputs; varies by vendor.</li>
                      <li><strong>Good for:</strong> drafting, summarizing, meeting notes, spreadsheet help.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Locally Hosted (Open‑Source, C‑TRAN managed)",
                    content="""
                    <p>Run <em>open‑source or open‑weight</em> models (e.g., Llama, Mistral variants) on infrastructure that C‑TRAN controls — on‑prem or in a C‑TRAN cloud account.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Pros:</strong> strongest data control, network isolation, customization, cost predictability at scale.</li>
                      <li><strong>Cons:</strong> requires engineering/ops to deploy, monitor, and update models; performance depends on hardware.</li>
                      <li><strong>Good for:</strong> workflows with sensitive data, strict governance, or custom pipelines. Can be deployed in VPC/Kubernetes with audit and access controls.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Fine‑Tuning & Retrieval (RAG)",
                    content="""
                    <p>Improve answers with your own knowledge. Two common approaches:</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Retrieval‑Augmented Generation (RAG):</strong> keep your documents outside the model; fetch relevant passages at query time for grounded answers.</li>
                      <li><strong>Fine‑tuning:</strong> adjust a base model with examples to match style or tasks. Best when tasks are consistent and data is available.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="On‑Device & Edge",
                    content="""
                    <p>Run smaller models on laptops, phones, kiosks, or vehicle devices for privacy and offline use.</p>
                    <ul class="list-disc ml-6">
                      <li><strong>Pros:</strong> low latency, offline, privacy by default.</li>
                      <li><strong>Cons:</strong> limited capacity/accuracy vs. large cloud models.</li>
                      <li><strong>Good for:</strong> quick text assist, simple classifications, templated outputs close to where work happens.</li>
                    </ul>
                    """,
                ),
                ModuleSection(
                    title="Choosing what fits",
                    content="""
                    <ul class="list-disc ml-6">
                      <li><strong>Low risk, fast value:</strong> Integrated tools or public assistants (no sensitive data).</li>
                      <li><strong>Operational apps:</strong> Cloud APIs with enterprise agreements and logging.</li>
                      <li><strong>High‑sensitivity:</strong> Locally hosted open‑source in a C‑TRAN‑controlled environment.</li>
                      <li><strong>Knowledge heavy:</strong> Add RAG; consider fine‑tuning if tasks are stable and data exists.</li>
                    </ul>
                    """,
                ),
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
            slug="ai-in-it",
            title="AI for Programmers & IT",
            summary="Where AI is already paying off in engineering and support.",
            sections=[
                ModuleSection("Coding Assistants", "Generate code from descriptions, accelerate boilerplate, and suggest fixes."),
                ModuleSection("Debugging & Guidance", "Explain errors, propose patches, walk through configuration tasks."),
                ModuleSection("Knowledge Search", "Answer questions from large KBs and playbooks quickly."),
            ],
        ),
        Module(
            slug="advanced-use-cases",
            title="Advanced Use Cases",
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
            slug="prompting-strategies",
            title="Prompting Strategies",
            summary="Clear instructions, context, constraints — and practice.",
            sections=[
                ModuleSection("Clarity & Context", "Be specific; give background so models understand the situation."),
                ModuleSection("Constraints & Format", "State tone, length, and output format (bullets, table, letter, etc.)."),
                ModuleSection("Practice", "Compare prompts across tools (CoPilot, ChatGPT, Claude, Gemini) and iterate."),
            ],
        ),
        Module(
            slug="image-examples",
            title="Image Creation Examples",
            summary="Generate and edit images for communications and campaigns.",
            sections=[
                ModuleSection("Generate from Text", "Create visuals from text prompts — from realistic to artistic."),
                ModuleSection("Edit Existing Images", "Change backgrounds, add or remove objects, apply styles and effects."),
                ModuleSection("Use Cases", "Enhance reports, presentations, and public-facing materials."),
                ModuleSection(
                    title="Dive Deeper: Spatial Intelligence in Computer Vision (Fei‑Fei Li, TED)",
                    content="""
                    <p>Renowned AI visionary Fei‑Fei Li explores how AI is evolving from merely seeing to understanding and acting within three-dimensional spaces. She introduces the concept of “spatial intelligence”—the next frontier in computer vision that could transform how machines interact meaningfully with the physical world.</p>
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/y8NtMZ7VGmU" title="With Spatial Intelligence, AI Will Understand the Real World – Fei-Fei Li" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    """,
                ),
                ModuleSection(
                    title="Dive Deeper: In the Age of AI Art — What Can Originality Look Like? (Eileen Isagon Skyers)",
                    content="""
                    <p>Media art curator Eileen Isagon Skyers examines the evolving relationship between human creativity and machine-generated art. She challenges traditional notions of originality by showcasing AI’s ability to co-create new visual narratives—from classic portraits to surreal, otherworldly forms.</p>
                    <iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/rKj1CN9Ttok\" title=\"In the Age of AI Art, What Can Originality Look Like? – Eileen Isagon Skyers\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>
                    """,
                ),
            ],
        ),
        Module(
            slug="practice",
            title="Practice Section",
            summary="Mini-challenges to reinforce key ideas.",
            sections=[
                ModuleSection("Challenge 1", "Compare two prompts for clarity and constraints; refine for better results."),
                ModuleSection("Challenge 2", "Draft a plan for an AI pilot in your area: problem, approach, guardrails, metrics."),
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
