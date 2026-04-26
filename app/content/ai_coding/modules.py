# app/content/modules2.py
# Course 3: Coding with AI — updated to focus on Claude Code in VS Code and template-first delivery

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
            summary="Practical, hands-on program to deliver software changes with Claude Code in VS Code, starting from an approved template architecture.",
            sections=[
                ModuleSection(
                    title="What You Will Learn",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Configure <strong>VS Code</strong> so Claude Code is working inside a trusted, policy-compliant workspace.</li>
                          <li>Start every feature from an <strong>approved template architecture</strong> instead of asking the model to invent a new application shape.</li>
                          <li>Use <strong>Claude Code</strong> for planning, editing, refactoring, and test generation in small, reviewable slices.</li>
                          <li>Understand which parts of the template are fixed standards and which extension points are safe to modify.</li>
                          <li>Verify AI-assisted changes with tests, code review, and architecture checks before merge.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Who This Is For",
                    content=(
                        """
                        <p>Developers, SRE/DevOps staff, analysts, and IT engineers who need to extend internal services, scripts, and web apps without drifting away from the organization&apos;s approved engineering patterns.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Outcomes",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Ship changes faster with Claude Code while staying inside approved stack, security, and deployment boundaries.</li>
                          <li>Know how to describe work to Claude Code in terms of existing architecture, extension points, and acceptance tests.</li>
                          <li>Create reusable prompts and checklists that reinforce template-first delivery across the team.</li>
                        </ul>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Never paste secrets, API keys, tokens, passwords, or PII into public models.",
                "Prefer enterprise or tenant-protected model access when sensitive information is unavoidable.",
                "Do not start greenfield production work from a blank prompt when an approved template already exists.",
                "Record design decisions and verify outputs with tests, code review, and architecture checks.",
            ],
            resources=[
                {"label": "Visual Studio Code", "url": "https://code.visualstudio.com/"},
                {"label": "Claude Code Documentation", "url": "https://docs.anthropic.com/"},
                {"label": "Anthropic Claude", "url": "https://www.anthropic.com/"},
            ],
        ),
        Module(
            slug="vscode-setup",
            title="VS Code Setup for Claude Code",
            summary="Configure VS Code, workspace trust, and repo context so Claude Code operates inside approved boundaries.",
            sections=[
                ModuleSection(
                    title="Workspace Checklist",
                    content=(
                        """
                        <ul class="list-disc ml-6 space-y-1">
                          <li>Open the <strong>approved repository or template-derived project</strong>, not an empty folder.</li>
                          <li>Enable <strong>Workspace Trust</strong> so tool execution and project context behave predictably.</li>
                          <li>Confirm Claude Code can see the files that matter: source, tests, README, prompts, and architecture notes.</li>
                          <li>Exclude <code>.env</code>, secrets folders, exported data, and other sensitive files from accidental sharing or indexing.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Secret Hygiene",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Use environment variables, secret stores (e.g., Key Vault/Secrets Manager), and .env files <em>never</em> shared with models.</li>
                          <li>Add <code>.env</code> and secret directories to <code>.gitignore</code>, search exclusions, and any model-sharing deny lists.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Instructions and Context Files",
                    content=(
                        """
                        <p>Keep a versioned <code>/prompts</code> folder, architecture notes, and template README files in the repo. Claude Code performs best when the workspace already explains coding standards, extension points, test commands, and deployment expectations.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="copilot-basics",
            title="Claude Code Basics in VS Code",
            summary="Use Claude Code as a repo-aware pair programmer that plans, edits, and verifies within an existing template.",
            sections=[
                ModuleSection(
                    title="Start from the Template",
                    content=(
                        """
                        <p>Begin by asking Claude Code to explain the project shape: where routes live, where business logic belongs, how tests are organized, and which files define configuration, logging, auth, and deployment. If the model cannot describe the template correctly, do not let it start coding yet.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Ask for Small Diffs",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Describe the task in terms of <strong>specific files</strong>, extension points, constraints, and acceptance tests.</li>
                          <li>Ask for a plan and a small patch, not a full app rewrite.</li>
                          <li>Require the model to preserve project conventions for imports, config, logging, migrations, and tests.</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="Review Before You Apply",
                    content=(
                        """
                        <p>Claude Code is most valuable when you treat it like a fast implementation partner, not an autonomous architect. Review the proposed diff, compare it against template rules, and run the local validation commands before accepting the change.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="gpt-claude-integration",
            title="Approved Template Architecture",
            summary="Understand the architecture contract Claude Code must inherit rather than invent.",
            sections=[
                ModuleSection(
                    title="What It Means",
                    content=(
                        """
                        <p>An <strong>approved template architecture</strong> is the organization&apos;s blessed starting point for a class of applications. It is more than a starter repo: it captures the agreed stack, directory layout, deployment path, observability, security controls, test harness, and operational expectations for that kind of system.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="What Stays Fixed",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Language, framework, and dependency approach</li>
                          <li>Folder and module layout</li>
                          <li>Auth, config, logging, and error-handling patterns</li>
                          <li>Secrets management, CI/CD, deployment, and monitoring hooks</li>
                          <li>Required tests, linters, and code review checkpoints</li>
                        </ul>
                        """
                    ),
                ),
                ModuleSection(
                    title="What Claude Code Can Change",
                    content=(
                        """
                        <p>Claude Code should usually work inside the template&apos;s extension points: handlers, service logic, UI components, schema changes, tests, documentation, and wiring that the template explicitly anticipates. If the requested change needs a new architecture, a new framework, or a new deployment path, that is a design decision for humans to approve first.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="agentic-workflows",
            title="Agentic Workflows in VS Code",
            summary="Plan -> act -> check, with the template boundary identified before Claude Code touches the codebase.",
            sections=[
                ModuleSection(
                    title="Plan First",
                    content=(
                        """
                        <p>Ask Claude Code to produce a concise plan that starts with the architecture contract: which template this repo derives from, which files are safe extension points, what commands validate the change, and what should stay untouched.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Use Tools",
                    content=(
                        """
                        <p>Let Claude Code inspect files, propose edits, and run targeted checks in the workspace. Prefer small, reversible edits and validation commands such as focused tests, lint, and type checks over broad regeneration.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Verify & Iterate",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Run the template&apos;s required tests and linters; require green checks before merge.</li>
                          <li>Ask the model to identify risks introduced by the diff, especially violations of the template contract.</li>
                          <li>Use self-check prompts such as: "What assumptions did you make about the architecture, and where could those assumptions be wrong?"</li>
                        </ul>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Do not grant unattended shell execution to AI agents.",
                "Require human approval for file writes and dependency changes.",
                "Require the plan to identify template boundaries before implementation begins.",
                "Log and review model-assisted changes in PR descriptions.",
            ],
        ),
        Module(
            slug="prompting-for-code",
            title="Prompting Claude Code for Safe Diffs",
            summary="Prompt patterns that keep Claude Code anchored to the approved template architecture.",
            sections=[
                ModuleSection(
                    title="Template: Extend an Existing Feature",
                    content=(
                        """
                        <pre><code>ROLE: Senior engineer working inside an approved template
OBJECTIVE: Extend &lt;feature&gt; without changing the project architecture
FILES: &lt;list the exact files or folders Claude Code may edit&gt;
CONTEXT: Existing interfaces, data shapes, and extension points
DO NOT CHANGE: auth, config, deployment, logging conventions, or dependency strategy
TESTS: Update or add focused tests and list the validation commands
FORMAT: plan first, then minimal diff</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Template: Architecture Check",
                    content=(
                        """
                        <pre><code>Before editing, explain:
1. Which approved template or project pattern this repo follows
2. Which files are extension points for this task
3. Which architectural rules must remain unchanged
4. Which tests and checks prove the change is safe
If any of that is unclear, stop and ask for clarification.</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Template: Write Docs",
                    content=(
                        """
                        <pre><code>AUDIENCE: New contributor extending the approved template
OBJECTIVE: Document where this feature fits in the architecture
INCLUDE: extension points used, config required, tests to run, and operational notes
FORMAT: Markdown with commands and file references</code></pre>
                        """
                    ),
                ),
                ModuleSection(
                    title="Prompt Engineering Essentials: Getting Better Results from LLMs | Tutorial",
                    content=(
                        """
                        <p>This short tutorial is useful background for structuring prompts with clear context and constraints. In this course, apply those same techniques to Claude Code by grounding every request in the approved template, the exact files to touch, and the checks that must pass.</p>
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
            summary="Use Claude Code to accelerate debugging and test writing without bypassing the template's quality gates.",
            sections=[
                ModuleSection(
                    title="Test-First with AI",
                    content=(
                        """
                        <p>Have Claude Code draft tests from the feature request and the existing template conventions, then implement only enough code to satisfy those tests. For critical logic, ask for boundary cases and failure modes, not just happy-path assertions.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Debugging Sessions",
                    content=(
                        """
                        <p>Share the error, the relevant stack trace, and the smallest set of files needed for Claude Code to reason about the bug. Ask for root cause first, then a minimal patch that respects the template architecture.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="AI-Assisted Code Review",
                    content=(
                        """
                        <ul class="list-disc ml-6">
                          <li>Generate a review checklist that includes architecture compliance, security, performance, and operations.</li>
                          <li>Ask for potential regressions, missing tests, and any accidental violations of shared template patterns.</li>
                          <li>Summarize PR context so reviewers can see why the diff stays within the approved design.</li>
                        </ul>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="security-governance",
            title="Security, Licensing, and Data Governance",
            summary="Use Claude Code inside agency policy, with templates carrying as much of the security and operations baseline as possible.",
            sections=[
                ModuleSection(
                    title="Secrets & PII",
                    content=(
                        """
                        <p>Never share PII, credentials, or internal tokens with public assistants. Use enterprise tenants, private endpoints, or local models for sensitive work, and rely on the template&apos;s secret-management pattern rather than inventing a new one.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Open-Source Licenses",
                    content=(
                        """
                        <p>Check license compatibility when accepting code or new dependencies. Claude Code can summarize obligations, but the human reviewer still owns the final decision.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Templates as Governance",
                    content=(
                        """
                        <p>Approved templates reduce risk because they already define how auth, logging, environment configuration, CI, and deployment should work. That means Claude Code is filling in business logic and tests inside a known safe frame, not improvising the entire production system.</p>
                        """
                    ),
                ),
            ],
            guardrails=[
                "Prefer enterprise offerings and private model endpoints for regulated data.",
                "Validate third-party code and dependencies for license and security risk.",
                "Use approved templates so security and operational controls are inherited by default.",
                "Retain audit logs of AI-assisted changes where feasible.",
            ],
        ),
        Module(
            slug="transit-dev-examples",
            title="Transit-Focused Development Examples",
            summary="Targeted scenarios that extend approved service and operations templates instead of inventing one-off solutions.",
            sections=[
                ModuleSection(
                    title="GTFS & Service Alerts Utility",
                    content=(
                        """
                        <p>Start from the approved data-processing or service template, then ask Claude Code to add GTFS validation rules, alert generation, and tests on sample feeds. Keep deployment, logging, and configuration patterns inherited from the template.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Ops Script Hardening",
                    content=(
                        """
                        <p>Use the team&apos;s approved automation skeleton or script template, then ask Claude Code to add input validation, structured logging, and error handling. Generate a focused diff and tests rather than rewriting the whole script.</p>
                        """
                    ),
                ),
                ModuleSection(
                    title="Knowledge-Base Updater",
                    content=(
                        """
                        <p>Extend the approved documentation or integration template so runbooks can be converted to Markdown with front matter and opened as a pull request with review notes.</p>
                        """
                    ),
                ),
            ],
        ),
        Module(
            slug="practice",
            title="Hands-On Lab: Extend an Approved Flask Template",
            summary="Use Claude Code in VS Code to extend a pre-approved Flask service template instead of scaffolding from scratch.",
            sections=[
                ModuleSection(
                    title="Template-First Lab (60–90 min)",
                    content=
                        """
                        <p>Goal: Start from an approved Flask service template that already includes app setup, config, logging, tests, and deployment wiring. Use Claude Code to add one new feature without changing the architecture.</p>
                        <ol class="list-decimal ml-6 space-y-2">
                          <li>
                            <strong>Review the approved template</strong>
                            <p>Read the template README and identify the architecture contract: app factory pattern, config loading, logging, database access, tests, and deployment path.</p>
                          </li>
                          <li>
                            <strong>Ask Claude Code to map extension points</strong>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>Read this repo and explain:
- which approved template it follows
- where request handlers, services, models, and tests belong
- which files are safe to edit for a new feature
- which validation commands I must run before merge</code></pre>
                          </li>
                          <li>
                            <strong>Choose one small feature</strong>
                            <p>Examples: add request notes, add a status field, add a search filter, or add a small admin page. The feature should fit the current template and not require a new framework, new auth model, or new deployment path.</p>
                          </li>
                          <li>
                            <strong>Constrain the implementation prompt</strong>
                            <pre class="bg-slate-800/70 border border-slate-700 rounded p-3 text-xs overflow-auto"><code>Implement the feature inside this approved Flask template.
Only edit the files needed for the feature.
Preserve the existing app structure, config pattern, logging, auth hooks, and tests.
Show the plan first, then the minimal diff, then the commands to validate it.</code></pre>
                          </li>
                          <li>
                            <strong>Implement and test</strong>
                            <p>Have Claude Code generate or update the focused tests first, apply the small patch, and run the template&apos;s validation commands. If the feature pressures the template boundaries, stop and escalate that architectural decision.</p>
                          </li>
                          <li>
                            <strong>Document the result</strong>
                            <p>Ask Claude Code to draft a short PR summary describing which extension points were used, what tests were added, and why the change stays inside the approved architecture.</p>
                          </li>
                        </ol>
                        <div class="mt-3 bg-slate-800/50 border border-slate-700 rounded p-3">
                          <h4 class="font-semibold">Stretch goals</h4>
                          <ul class="list-disc ml-6">
                            <li>Add a migration, API validation, and a template-consistent UI update.</li>
                            <li>Improve test coverage around one failure mode or authorization edge case.</li>
                            <li>Draft documentation for future contributors explaining the extension point you used.</li>
                            <li>Ask Claude Code for a self-review focused on architecture drift and operational risk.</li>
                          </ul>
                        </div>
                        <p class="text-slate-300 text-sm mt-2"><strong>Guardrails:</strong> Start from the approved template, keep secrets out of prompts, avoid architecture drift, and stop for human review when a feature needs a new pattern.</p>
                        """,
                ),
            ],
            resources=[
                {"label": "Flask", "url": "https://flask.palletsprojects.com/"},
                {"label": "Flask-SQLAlchemy", "url": "https://flask-sqlalchemy.palletsprojects.com/"},
                {"label": "SQLAlchemy", "url": "https://docs.sqlalchemy.org/"},
                {"label": "Anthropic Messages API", "url": "https://docs.anthropic.com/claude/reference/messages_post"},
            ],
            guardrails=[
                "Never commit or paste API keys; keep them in .env and your secret store.",
                "Avoid PII in prompts and stored logs; use data minimization.",
                "Use the approved template so logging, auth, and deployment controls are inherited.",
                "Escalate architectural changes before the model implements them.",
            ],
        ),
        Module(
            slug="final",
            title="Final Quiz & Completion",
            summary="Validate knowledge across Claude Code workflows, approved templates, prompting, and governance.",
            sections=[
                ModuleSection(
                    title="How This Works",
                    content=(
                        "Answer all questions correctly to complete the course. Treat Claude Code outputs as guidance, confirm architectural decisions with the right owners, and prefer template-first delivery over blank-page generation."
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
        title="Coding with AI: Claude Code in VS Code",
        summary="Practical techniques for extending approved templates with Claude Code in VS Code at an agency.",
        duration="~60–90 minutes",
        level="Intermediate–Advanced",
        hero_image="/static/images/courses/coding/hero.png",
        thumbnail="/static/images/courses/coding/thumb.png",
        og_image="/static/images/courses/coding/hero.png",
        tags=["Coding", "Claude Code", "VS Code", "Template Architecture"],
    )