# app/content/modules2.py
# Course 3: Coding with AI — Updated modules focused on VS Code, Copilot, GPT, Claude, and agentic workflows

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
            title="Introduction & Objectives",
            summary="Practical, hands-on program to accelerate software delivery using AI in VS Code with Copilot, GPT, and Claude.",
            sections=[
                ModuleSection(
                    title="What You Will Learn",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Install, configure, and govern <strong>VS Code</strong> with the <strong>GitHub Copilot</strong> extension and policies.</li>
                          <li>Use <strong>GPT</strong> and <strong>Claude</strong> effectively for coding tasks, design reviews, refactoring, and documentation.</li>
                          <li>Apply <strong>agentic workflows</strong> inside VS Code (planning → tool use → verification).</li>
                          <li>Design <strong>secure prompts</strong>, handle <strong>PII/secrets</strong>, and respect <strong>licensing</strong>.</li>
                          <li>Adopt <strong>test-first practices</strong> with AI: unit tests, property tests, and CI integration.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Who This Is For",
                    content=(
                        """
                        <p>Developers, SRE/DevOps, data specialists, and IT engineers building scripts, services, integrations, and automation for a mid-sized public transit agency.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Outcomes",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Ship a working utility or service faster with AI support while maintaining quality and compliance.</li>
                          <li>Establish guardrails for production-grade AI-assisted coding at an agency.</li>
                          <li>Create reproducible prompts, templates, and checklists for your team.</li>
                        </ul>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Never paste secrets, API keys, tokens, passwords, or PII into public models.",
                "Prefer enterprise/tenant-protected offerings when sensitive information is unavoidable.",
                "Record design decisions and verify outputs with tests and code review.",
            ],
            resources=[
                {"label": "Visual Studio Code", "url": "https://code.visualstudio.com/"},
                {"label": "GitHub Copilot", "url": "https://github.com/features/copilot"},
                {"label": "OpenAI", "url": "https://platform.openai.com/"},
                {"label": "Anthropic Claude", "url": "https://www.anthropic.com/"},
            ],
        ),
        Module(
            slug="vscode-setup",
            title="VS Code Setup for AI-Accelerated Development",
            summary="Configure VS Code, extensions, workspaces, and policy to safely use AI at work.",
            sections=[
                ModuleSection(
                    title="Extensions & Settings",
                    content=(
                        """
                        <p>Install the GitHub Copilot extension (and Copilot Chat, if licensed). Enable telemetry appropriate for the agency. Configure file and folder exclusions to avoid sending secrets.</p>
                        <pre><code>{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.chat.advancedEditing": true,
  "files.exclude": {
    "**/.env": true,
    "**/.secrets/**": true
  },
  "security.workspace.trust.enabled": true
}</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Secret Hygiene",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Use environment variables, secret stores (e.g., Key Vault/Secrets Manager), and .env files <em>never</em> shared with models.</li>
                          <li>Add <code>.env</code> and secret directories to <code>.gitignore</code> and Copilot deny lists.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Prompt Library in Workspace",
                    content=(
                        """
                        <p>Create a <code>/prompts</code> folder with reusable instruction templates for code generation, refactoring, tests, and docs. Keep prompts versioned with your repo.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="copilot-basics",
            title="Copilot Basics in VS Code",
            summary="Inline suggestions, Copilot Chat, and pair-programming patterns.",
            sections=[
                ModuleSection(
                    title="Inline Completion",
                    content=(
                        """
                        <p>Use descriptive function and variable names and write comments that preview the next step. Accept or cycle suggestions with keyboard shortcuts. Decline suggestions that import unknown packages or bypass validation.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Copilot Chat for Tasks",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Commands: <code>@workspace</code> for repo-aware tasks; ask to generate scaffolding, explain errors, or propose refactors.</li>
                          <li>Constrain outputs: language, framework, lint rules, and test framework.</li>
                          <li>Use <em>edit-and-review</em>: apply changes in a scratch branch; run tests before merging.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="When to Switch to GPT/Claude",
                    content=(
                        """
                        <p>For long-form planning, multi-file designs, or deep reasoning, switch to GPT or Claude with a structured prompt and paste minimal, relevant context only.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="gpt-claude-integration",
            title="Using GPT and Claude for Engineering Work",
            summary="Effective prompts for design, code generation, refactoring, and documentation.",
            sections=[
                ModuleSection(
                    title="Design & Planning",
                    content=(
                        """
                        <p>Ask the model to generate an implementation plan with explicit constraints: stack, style, tests, and acceptance criteria. Use bullet lists and numbered steps for clarity.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Refactoring & Migration",
                    content=(
                        """
                        <p>Provide representative code snippets and target patterns (e.g., migrate from requests to httpx, or from Flask blueprints to FastAPI routers). Request a <em>codemod</em> plan and verify with tests.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Documentation & Comments",
                    content=(
                        """
                        <p>Generate docstrings and README sections from code and tests. Require the model to include usage examples and limitations.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="agentic-workflows",
            title="Agentic Workflows in VS Code",
            summary="Plan → act → check: multi-step flows that use tools, terminals, and tests.",
            sections=[
                ModuleSection(
                    title="Plan First",
                    content=(
                        """
                        <p>Ask the assistant to create a concise plan: tasks, files to change, commands to run, and a test strategy. Approve or edit the plan before executing.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Use Tools",
                    content=(
                        """
                        <p>Within Copilot Chat or external assistants, run commands safely in a sandbox or dev container. Prefer <code>--dry-run</code> and <code>--check</code> flags where available.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Verify & Iterate",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Run unit tests and linters; require green checks before merge.</li>
                          <li>Ask the model to propose additional edge-case tests.</li>
                          <li>Use <em>self-check prompts</em>: “List 5 potential bugs or security risks introduced by this change.”</li>
                        </ul>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Do not grant unattended shell execution to AI agents.",
                "Require human approval for file writes and dependency changes.",
                "Log and review model-assisted changes in PR descriptions.",
            ],
        ),
        Module(
            slug="prompting-for-code",
            title="Prompting Patterns for Code",
            summary="Templates that improve quality, determinism, and reviewability.",
            sections=[
                ModuleSection(
                    title="Template: Implement a Function",
                    content=(
                        """
                        <pre><code>ROLE: Senior engineer
OBJECTIVE: Implement &lt;function&gt; in &lt;file&gt;
CONTEXT: Constraints, interfaces, data shapes
REQUIRE: Type hints, docstring, input validation
TESTS: Provide pytest cases
FORMAT: Single code block; no commentary</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Template: Refactor Safely",
                    content=(
                        """
                        <pre><code>OBJECTIVE: Refactor module X for readability and performance
CONSTRAINTS: Keep public API stable; pass mypy/flake8; 100% existing tests pass
STEPS: 1) Plan; 2) Patch; 3) Explain deltas; 4) Risks
OUTPUT: Unified diff</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Template: Write Docs",
                    content=(
                        """
                        <pre><code>AUDIENCE: New contributor
OBJECTIVE: Write README section for setup and usage
INCLUDE: Prereqs, install, run, test, troubleshooting
FORMAT: Markdown; code blocks with commands</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Prompt engineering essentials: Getting better results from LLMs | Tutorial",
                    content=(
                        """
                        <p>This ~10-minute tutorial from GitHub walks through core prompt engineering techniques for large language models in 2025. It covers how to structure prompts for clarity, provide context and constraints, and iteratively refine outputs. The video also highlights best practices to avoid common pitfalls, including overloading prompts or using ambiguous instructions. Designed for developers and technical professionals, it delivers concise, actionable guidance that applies across popular LLM platforms.</p>
                        <div class="mt-3 flex justify-center">
                          <div class="w-full max-w-3xl">
                            <div class="aspect-video rounded border border-slate-700 overflow-hidden bg-black">
                              <iframe src="https://www.youtube.com/embed/LAF-lACf2QY" title="Prompt engineering essentials: Getting better results from LLMs | Tutorial" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="w-full h-full"></iframe>
                            </div>
                          </div>
                        </div>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="testing-debugging",
            title="Testing, Debugging, and Code Review with AI",
            summary="Combine AI with automated tests, linters, and review checklists.",
            sections=[
                ModuleSection(
                    title="Test-First with AI",
                    content=(
                        """
                        <p>Have the model draft unit tests from a spec, then implement code to satisfy them. Use property-based tests for critical logic.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Debugging Sessions",
                    content=(
                        """
                        <p>Paste error messages and minimal code into GPT/Claude or use Copilot Chat to propose fixes. Ask for root-cause analysis and alternative approaches.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="AI-Assisted Code Review",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Generate a review checklist: security, performance, compliance, accessibility.</li>
                          <li>Ask for potential regressions and missing tests.</li>
                          <li>Summarize PR context and rationale for non-technical reviewers.</li>
                        </ul>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="security-governance",
            title="Security, Licensing, and Data Governance",
            summary="Operate within agency policy while benefiting from AI.",
            sections=[
                ModuleSection(
                    title="Secrets & PII",
                    content=(
                        """
                        <p>Never share PII, credentials, or internal tokens with public assistants. Use enterprise tenants, private endpoints, or local models for sensitive work.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Open-Source Licenses",
                    content=(
                        """
                        <p>Check license compatibility when accepting code. Ask the model to explain license obligations and generate attribution files, but validate with legal.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Model Attribution & Logs",
                    content=(
                        """
                        <p>Record which assistant produced changes and why. Include prompts (sanitized) and model versions in PR notes for auditability.</p>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Prefer enterprise offerings and private model endpoints for regulated data.",
                "Validate third-party code and dependencies for license and security risk.",
                "Retain audit logs of AI-assisted changes where feasible.",
            ],
        ),
        Module(
            slug="transit-dev-examples",
            title="Transit-Focused Development Examples",
            summary="Targeted scenarios for a bus-centric public agency.",
            sections=[
                ModuleSection(
                    title="GTFS & Service Alerts Utility",
                    content=(
                        """
                        <p>Use the assistant to draft a Python CLI that validates GTFS feeds, checks headway rules, and emits alerts to a messaging topic. Require tests on sample feeds.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Ops Script Hardening",
                    content=(
                        """
                        <p>Refactor a PowerShell or Bash script with the model to add input validation, logging, and error handling. Generate before/after diffs and tests.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Knowledge-Base Updater",
                    content=(
                        """
                        <p>Generate a small service that converts runbooks to Markdown with front matter, then opens a PR to your docs site with change notes.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="practice",
            title="Hands-On Lab: Flask Chatbot with SQLite",
            summary="Scaffold a Flask + SQLAlchemy + SQLite app that persists chat history and calls a model provider API.",
            sections=[
                ModuleSection(
                    title="Build a Flask Chatbot (60–90 min)",
                    content=
                        """
                        <p>Goal: Create a small Flask app with SQLite storage and a chat endpoint that calls a model provider (e.g., OpenAI or Anthropic) via API.</p>
                        <ol class="list-decimal ml-6 space-y-2">
                          <li>
                            <strong>Scaffold project</strong>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>mkdir flask-chatbot &amp;&amp; cd flask-chatbot
python3 -m venv .venv &amp;&amp; source .venv/bin/activate
pip install flask flask_sqlalchemy python-dotenv httpx
# Optional provider SDKs:
# pip install openai anthropic
</code></pre>
                          </li>
                          <li>
                            <strong>Set secrets</strong>
                            <p>Create a <code>.env</code> file (never commit):</p>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>OPENAI_API_KEY=your_key_here  # or ANTHROPIC_API_KEY=...
MODEL_NAME=gpt-4o-mini        # or claude-3-5-sonnet</code></pre>
                          </li>
                          <li>
                            <strong>Create .gitignore</strong>
                            <p>Add a minimal ignore file:</p>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>.env
.DS_Store
__pycache__/
*.pyc
.venv/</code></pre>
                          </li>
                          <li>
                            <strong>Create app.py</strong>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os, httpx
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def index():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return render_template("index.html", messages=messages)

@app.post("/api/chat")
def chat():
    data = request.get_json() or {}
    user_msg = (data.get("message") or "").strip()
    if not user_msg:
        return jsonify({"error":"message required"}), 400
    db.session.add(Message(role="user", content=user_msg))
    db.session.commit()

    # Call a provider (OpenAI example over HTTP)
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("MODEL_NAME", "gpt-4o-mini")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": model, "messages": [{"role":"user","content": user_msg}]}
    try:
        r = httpx.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        reply = r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        reply = "Sorry, I had trouble reaching the model API."

    db.session.add(Message(role="assistant", content=reply))
    db.session.commit()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)</code></pre>
                          </li>
                          <li>
                            <strong>Templates</strong>
                            <p>Create <code>templates/index.html</code> with a simple chat UI:</p>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>&lt;!doctype html&gt;
&lt;meta charset="utf-8"&gt;
&lt;title&gt;Flask Chatbot&lt;/title&gt;
&lt;body style="font-family:sans-serif; max-width:720px; margin:2rem auto"&gt;
  &lt;h1&gt;Chatbot&lt;/h1&gt;
  &lt;div id="log" style="border:1px solid #ccc; padding:1rem; min-height:200px"&gt;
    {% for m in messages %}
      &lt;div&gt;&lt;strong&gt;{{ m.role }}:&lt;/strong&gt; {{ m.content }}&lt;/div&gt;
    {% endfor %}
  &lt;/div&gt;
  &lt;form id="f" style="margin-top:1rem"&gt;
    &lt;input id="msg" placeholder="Say something..." style="width:75%"/&gt;
    &lt;button&gt;Send&lt;/button&gt;
  &lt;/form&gt;
  &lt;script&gt;
    const f = document.getElementById('f');
    const msg = document.getElementById('msg');
    const log = document.getElementById('log');
    f.addEventListener('submit', async (e) =&gt; {
      e.preventDefault();
      const text = msg.value.trim();
      if (!text) return;
      log.insertAdjacentHTML('beforeend', `&lt;div&gt;&lt;strong&gt;user:&lt;/strong&gt; ${text}&lt;/div&gt;`);
      msg.value = '';
      const r = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message:text})});
      const j = await r.json();
      log.insertAdjacentHTML('beforeend', `&lt;div&gt;&lt;strong&gt;assistant:&lt;/strong&gt; ${j.reply || '(no reply)'}&lt;/div&gt;`);
      log.scrollTop = log.scrollHeight;
    });
  &lt;/script&gt;
&lt;/body&gt;</code></pre>
                          </li>
                          <li>
                            <strong>Run</strong>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>export FLASK_APP=app.py
flask run</code></pre>
                            <p>Open <code>http://127.0.0.1:5000</code>. You should see messages persist in <code>app.db</code>.</p>
                          </li>
                        </ol>
                        <div class="mt-3 bg-slate-800/50 border border-slate-700 rounded p-3">
                          <h4 class="font-semibold">Stretch goals</h4>
                          <ul class="list-disc ml-6">
                            <li>Add a Conversation table; group messages by conversation_id.</li>
                            <li>Stream responses (Server-Sent Events) for typing effect.</li>
                            <li>Swap providers (Anthropic) or call a local model via an API gateway.</li>
                            <li>Add basic tests (pytest) and a Dockerfile.</li>
                          </ul>
                        </div>
                        <p class="text-slate-300 text-sm mt-2"><strong>Guardrails:</strong> Keep API keys in <code>.env</code>; set timeouts; handle provider errors; avoid PII in prompts/logs.</p>
                        """,
                ),
            ],
            resources=[
                {"label": "Flask", "url": "https://flask.palletsprojects.com/"},
                {"label": "Flask-SQLAlchemy", "url": "https://flask-sqlalchemy.palletsprojects.com/"},
                {"label": "SQLAlchemy", "url": "https://docs.sqlalchemy.org/"},
                {"label": "OpenAI Chat Completions API", "url": "https://platform.openai.com/docs/api-reference/chat/create"},
                {"label": "Anthropic Messages API", "url": "https://docs.anthropic.com/claude/reference/messages_post"},
            ],
            guardrails=[
                "Never commit or paste API keys; keep them in .env and your secret store.",
                "Avoid PII in prompts and stored logs; use data minimization.",
                "Configure request timeouts and error handling for provider calls.",
            ],
        ),
        Module(
            slug="final",
            title="Final Quiz & Completion",
            summary="Validate knowledge across configuration, prompting, agentic workflows, and governance.",
            sections=[
                ModuleSection(
                    title="How This Works",
                    content=(
                        "Answer all questions correctly to complete the course. Treat outputs as guidance and confirm critical decisions with policy owners."
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
        slug="course-3",
        title="Coding with AI: VS Code, Copilot, GPT & Claude",
        summary="Practical techniques for AI-assisted software development and DevOps in a public transit agency.",
        duration="~60–90 minutes",
        level="Intermediate–Advanced",
        hero_image="/static/images/courses/coding/hero.png",
        thumbnail="/static/images/courses/coding/thumb.png",
        og_image="/static/images/courses/coding/hero.png",
        tags=["Coding", "Agentic Workflows", "Governance"],
    )