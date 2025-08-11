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
            title="Executive Introduction: Decisions, Risk, and a 90‑Day Plan",
            summary="Actionable guidance for directors and C‑level leaders to capture AI value safely in public transit.",
            sections=[
                ModuleSection(
                    title="Why AI, Why Now for Public Transit",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li><strong>Cost and capacity pressure:</strong> do more with constrained budgets and hiring challenges.</li>
                          <li><strong>Rider expectations:</strong> faster, clearer, multilingual information across channels.</li>
                          <li><strong>Operations:</strong> quicker summaries, triage, and decision support from existing data.</li>
                          <li><strong>Safety and compliance:</strong> consistent language, policy alignment, and better documentation.</li>
                          <li><strong>Technology shift:</strong> practical gains from copilots, RAG over agency documents, and workflow automations.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Executive Decisions to Make in the Next Quarter",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li><strong>Priority use cases:</strong> select 2–3 with measurable outcomes and low risk.</li>
                          <li><strong>Delivery model:</strong> public assistant (no sensitive data), enterprise copilots, cloud APIs, or C‑TRAN‑hosted open‑source.</li>
                          <li><strong>Data strategy:</strong> source systems, document scope for retrieval, retention, residency, and access controls.</li>
                          <li><strong>Operating model:</strong> accountable product owner, tech lead, risk/compliance partner, and review cadence.</li>
                          <li><strong>Guardrails & policy:</strong> PII handling, human‑in‑the‑loop, logging/audit, red‑teaming before go‑live.</li>
                          <li><strong>Funding & procurement:</strong> buy/build/partner decision, small pilot budget, contract protections.</li>
                          <li><strong>Measurement:</strong> define KPIs, quality and safety thresholds, and an evaluation harness.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="30–60–90 Day Action Plan",
                    content=(
                        """
                        <div class="bg-slate-800/60 border border-slate-700 rounded p-4">
                          <ol class="list-decimal ml-6 space-y-1">
                            <li><strong>Day 0–30:</strong> pick use cases; assign sponsor and owner; approve guardrails; complete privacy/legal review; inventory documents/data; baseline KPIs.</li>
                            <li><strong>Day 31–60:</strong> build small pilots (RAG/copilot); set up eval set and A/B testing; train pilot users; capture benefits and issues.</li>
                            <li><strong>Day 61–90:</strong> go/no‑go; production hardening (monitoring, audit, fallback); change‑management plan; scale decision and budget.</li>
                          </ol>
                        </div>
                        """
                    ),
                ),
                ModuleSection(
                    title="Governance You Must Stand Up",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>PII minimization, approved tools only, and content review for public outputs.</li>
                          <li>Data residency and vendor risk reviews; model/version logging and traceability.</li>
                          <li>Human‑in‑the‑loop checkpoints for safety‑critical or public communications.</li>
                          <li>Incident response: rollback, escalation, and user‑visible notices if needed.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Operating Model and Accountabilities",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li><strong>Executive sponsor:</strong> clears roadblocks, owns outcomes.</li>
                          <li><strong>Product owner:</strong> prioritizes use cases, defines requirements, and accepts results.</li>
                          <li><strong>Technical lead:</strong> delivery model, architecture, and quality gates.</li>
                          <li><strong>Risk & compliance:</strong> privacy, records, accessibility, and audit.</li>
                          <li><strong>Change management & training:</strong> communications, enablement, and adoption.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Metrics and Review Cadence",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li><strong>Business KPIs:</strong> e.g., time‑to‑publish alerts, first‑contact resolution, cost per ticket.</li>
                          <li><strong>Quality & safety:</strong> accuracy with citations, policy alignment, red‑team findings resolved.</li>
                          <li><strong>Experience:</strong> adoption, satisfaction, and measured time savings.</li>
                          <li><strong>Ops:</strong> latency, availability, cost per task; fallback rate.</li>
                          <li>Publish a simple dashboard and review monthly at the leadership team.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Use‑Case Selection Checklist",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Clear, measurable outcome tied to a business owner.</li>
                          <li>Low‑risk scope and availability of source documents/data.</li>
                          <li>Human‑in‑the‑loop feasible; public outputs reviewed.</li>
                          <li>Small, diverse evaluation set to test quality and safety.</li>
                          <li>Baseline and target metrics defined before starting.</li>
                        </ul>
                        """
                    ),
                ),
                # Keep data-driven external snapshot for leaders
                ModuleSection(
                    title="Stanford Report: How AI Is Transforming the Business World (Article, ~10 min)",
                    content="""
                    <div class="bg-slate-800/60 border border-slate-700 rounded p-4 space-y-2">
                    <p>This Big Think interview with a Stanford HAI researcher draws on the 2024 AI Index Report to share evidence‑based insights. It highlights where AI is already boosting worker <strong>productivity</strong> and <strong>quality of work</strong>, while noting that many managers anticipate <strong>workforce changes</strong> that call for reskilling and role redesign. Use this as a quick, data‑driven briefing to separate hype from reality.</p>
                    <ul class="list-disc ml-6">
                        <li>Evidence from the 2024 AI Index: adoption trends, performance benchmarks, and economic signals.</li>
                        <li>Productivity and quality gains across certain tasks; limits and caveats for high‑stakes work.</li>
                        <li>Manager outlook: expected job/task shifts → prioritize training, guardrails, and change management.</li>
                        <li>Leadership takeaways: define use cases, measure ROI and quality, and align with governance.</li>
                    </ul>
                    <p class="mt-2">
                        <a class="text-cyan-300 underline" href="https://aiindex.stanford.edu/report/" target="_blank" rel="noopener">Stanford HAI — 2024 AI Index Report</a>
                    </p>
                    </div>
                    """,
                ),
            ],
            resources=[
                {"label": "Harvard Kennedy School Working Paper (context)", "url": "https://www.hks.harvard.edu/sites/default/files/centers/mrcbg/Final_AWP_244.pdf"},
                {"label": "Stanford HAI — 2024 AI Index", "url": "https://aiindex.stanford.edu/report/"},
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
        Module(
            slug="leadership-insights",
            title="Leadership Insights",
            summary="Executive perspectives on AI strategy, governance, and responsible adoption.",
            sections=[
                ModuleSection(
                    title="Enterprise AI Strategy and CEO Leadership (McKinsey)",
                    content="""
                    <p>In this talk, McKinsey's head of CEO services explores how senior leaders can navigate the rapidly evolving AI landscape, make smart trade-offs, and integrate AI into long-term strategy. This video is ideal for executives who want to lead AI adoption effectively.</p>
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/uTRKdCY4HdE" title="Enterprise AI Strategy and CEO Leadership - McKinsey" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    """,
                ),
                ModuleSection(
                    title="Dig Deeper: The Last 6 Decades of AI — and What Comes Next (TED)",
                    content="""
                    <p>A visionary TED Talk by futurist Ray Kurzweil that puts the AI revolution in perspective and peers into the coming decades. Kurzweil charts AI’s exponential progress over the past 60 years and predicts how it will unfold into the future — including the advent of artificial general intelligence and the potential merging of human intelligence with AI. This forward-looking talk challenges leaders to think beyond immediate plans and consider how AI might fundamentally reshape industries, work, and human potential.</p>
                    <div class="mt-3">
                      <iframe width="560" height="315" src="https://embed.ted.com/talks/ray_kurzweil_the_last_6_decades_of_ai_and_what_comes_next" title="Ray Kurzweil: The Last 6 Decades of AI — and What Comes Next (TED)" frameborder="0" scrolling="no" allowfullscreen></iframe>
                    </div>
                    <p class="text-slate-400 text-sm mt-2">If the embed doesn’t load, <a class="text-cyan-300 underline" href="https://www.ted.com/talks/ray_kurzweil_the_last_6_decades_of_ai_and_what_comes_next" target="_blank" rel="noopener">open the talk on TED.com</a>.</p>
                    """,
                ),
            ],
            resources=[
                {"label": "McKinsey Article Hub", "url": "https://www.mckinsey.com/featured-insights/artificial-intelligence"},
                {"label": "Ray Kurzweil TED Talk", "url": "https://www.ted.com/talks/ray_kurzweil_the_last_6_decades_of_ai_and_what_comes_next"}
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
        slug="course-4",
        title="AI for Executives: Leading in the AI Era",
        summary="Case studies, frameworks, and leadership insights for AI adoption as a business leader.",
        duration="~30–45 minutes",
        level="Intermediate-advanced",
        hero_image="/static/images/courses/exec/hero.png",
        thumbnail="/static/images/courses/exec/thumb.png",
        og_image="/static/images/courses/exec/hero.png",
        tags=["Leadership", "Innovation"],
    )
