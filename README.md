<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/terminal-mobile.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/terminal-header.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/terminal-mobile.gif">
  <img src=".github/assets/terminal-header.gif" width="100%" alt="Muhammad Yousaf — Full-Stack + AI Systems Engineer. Linux, TypeScript, Python, Next.js, NestJS, FastAPI, LangGraph and RAG.">
</picture>

<h1 align="center">Hi, I'm Muhammad Yousaf</h1>

<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/typing-intro-static.png">
    <img src=".github/assets/typing-intro.gif" width="800" alt="Building full-stack web apps, connecting AI agents to useful tools, turning documents into cited answers, and working in the Linux terminal.">
  </picture>
</p>

<p align="center">
  <strong>Full-Stack + AI Systems Engineer</strong><br>
  Building web applications, AI agents, and retrieval systems with clear paths from context to action.
</p>

<p align="center">
  <a href="https://github.com/Yosf96633/Autohunt">AutoHunt</a> &nbsp; / &nbsp;
  <a href="https://github.com/Yosf96633/DocsAI">DocsAI</a> &nbsp; / &nbsp;
  <a href="https://yousaf-dev18.vercel.app/">Portfolio</a> &nbsp; / &nbsp;
  <a href="https://linkedin.com/in/yousaf-dev18/">LinkedIn</a> &nbsp; / &nbsp;
  <a href="mailto:yousaf.dev18@gmail.com">Email</a>
</p>

## `$ whoami`

I work across **React and Next.js interfaces**, **TypeScript and Python backends**, and **AI workflows built with LangGraph**. My projects connect model reasoning to practical tools: searching documents, matching jobs, drafting responses, and automating browser tasks.

I care about the details that make those systems useful: source citations, validated outputs, persistent state, and human review before an agent submits an application.

```toml
# ~/.config/yousaf/profile.toml
shell = "zsh"
editor = "VS Code"
focus = ["Full-stack development", "AI agents", "RAG"]
approach = ["Typed interfaces", "Traceable answers", "Human review"]
```

## `$ ls ~/projects`

### [AutoHunt](https://github.com/Yosf96633/Autohunt)

**From CV to reviewed job application, in one stateful workflow.**

`LangGraph` · `Playwright` · `Next.js` · `TypeScript` · `PostgreSQL` · `Zod`

A **10-stage agent workflow** that parses a CV, discovers jobs, scores relevance, and drafts cover letters before browser-driven submission.

- **Review before action:** users review scored jobs and cover letters before automated submission.
- **Iterative drafting:** OpenAI and Groq support job–CV matching and a cover-letter self-critique loop.
- **Persistent state:** PostgreSQL-backed LangGraph checkpoints retain workflow progress; Zod validates extracted CV data, normalized jobs, and model outputs.
- **Visible progress:** a Next.js dashboard shows live agent status, job browsing, and skill matches.

[Explore the repository →](https://github.com/Yosf96633/Autohunt)

### [DocsAI](https://github.com/Yosf96633/DocsAI)

**Ask questions about legal documents and trace answers to the source.**

`FastAPI` · `Next.js` · `LangGraph` · `Qdrant` · `Cohere` · `PostgreSQL`

A document analysis assistant with **separate ingestion and RAG chat workflows**, connecting PDF processing to streamed answers and source citations.

- **Hybrid retrieval:** Qdrant combines dense embeddings and SPLADE sparse vectors, followed by Cohere reranking for semantic and keyword relevance.
- **Source visibility:** position-aware PDF chunks retain page and estimated text coordinates for citation highlighting.
- **Streaming responses:** server-sent events deliver generated text and citations to the Next.js interface.
- **Conversation isolation:** PostgreSQL-backed thread context keeps chat histories separate.

[Explore the repository →](https://github.com/Yosf96633/DocsAI)

<details>
<summary><strong>More in ~/projects</strong></summary>

| Project | What it does |
| :--- | :--- |
| **Vidspire** | YouTube sentiment analysis platform. |
| **CamBot** | AI-powered conversational chatbot. |
| **Better Auth Starter** | Authentication implementation with OAuth and two-factor authentication. |

[Browse my repositories →](https://github.com/Yosf96633?tab=repositories)

</details>

## `$ cat ~/workflows/autohunt`

AutoHunt separates discovery, evaluation, drafting, and submission into explicit steps, with a revision loop and a human review checkpoint.

<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/pipeline.svg">
    <img src=".github/assets/pipeline.gif" width="480" alt="Simplified AutoHunt flow: parse CV, discover jobs, score relevance, draft, critique, human review, then submit. Critique can return to drafting. Submission requires approval.">
  </picture>
</p>

Shared state connects the steps. Conditional edges route drafts back for revision, and approval unlocks browser submission.

## `$ cat ~/.config/stack.toml`

<p align="center">
  <a href="https://skillicons.dev">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=ts,py,js,nextjs,react,redux,tailwind,nestjs,fastapi,nodejs,express,postgres,mongodb,redis,linux,docker,git,vercel,postman,figma&amp;theme=light&amp;perline=10">
      <img src="https://skillicons.dev/icons?i=ts,py,js,nextjs,react,redux,tailwind,nestjs,fastapi,nodejs,express,postgres,mongodb,redis,linux,docker,git,vercel,postman,figma&amp;theme=dark&amp;perline=10" width="480" alt="Tech stack: TypeScript, Python, JavaScript, Next.js, React, Redux, Tailwind CSS, NestJS, FastAPI, Node.js, Express, PostgreSQL, MongoDB, Redis, Linux, Docker, Git, Vercel, Postman, and Figma.">
    </picture>
  </a>
</p>

| Layer | Tools |
| :--- | :--- |
| **Languages** | TypeScript · Python · JavaScript |
| **Frontend** | Next.js · React · Redux · Zustand · Tailwind CSS · shadcn/ui |
| **Backend** | NestJS · FastAPI · Node.js · Express |
| **Data** | PostgreSQL · MongoDB · Redis · Qdrant · Drizzle ORM · Mongoose |
| **AI & automation** | LangGraph · LangChain · RAG · MCP · n8n · Cohere Rerank |
| **Auth & validation** | Better Auth · Auth.js · JWT · Zod |
| **Operating system** | Linux |
| **Infrastructure & tools** | Docker · Git · Vercel · Render · Playwright · Postman · Figma |

<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/stack-flow-static.png">
    <img src=".github/assets/stack-flow.gif" width="720" alt="Decorative animated connections across my stack: web, APIs, data, AI, and Linux.">
  </picture>
</p>

## `$ git log --author="Muhammad Yousaf"`

### `2025-10 → 2026-04` · Frontend Developer

**Mozzine Technologies**

- Developed B2B SaaS dashboard features with Next.js, TypeScript, and Tailwind CSS.
- Translated **20+ Figma designs** into responsive components with shadcn/ui, maintaining consistency across desktop and mobile.
- Integrated REST APIs with Redux and Zustand, and resolved UI bugs across browsers and dashboard modules.

### `2025-07 → 2025-09` · Full Stack Intern

**Code Expert**

- Developed a multi-vendor e-commerce platform with **2 role-based dashboards** for food and gift product modules.
- Built **15+ REST API endpoints** for orders, products, and vendor operations, with shared MongoDB schemas and validation middleware.
- Improved database query response times by **40%** using Mongoose lean queries, projections, and compound indexes.
- Implemented NextAuth.js authentication, JWT sessions, role-based access, and transactional emails through Resend.

## `$ cat ~/education`

**BS Computer Science** · Government College University Faisalabad · 2021–2025

## `$ cat ~/notes/engineering.md`

I'm going deeper into the parts that make these systems dependable:

- **Agent design:** explicit state, conditional routing, persistence, and human review.
- **Retrieval:** hybrid search, reranking, and evaluation against source documents.
- **Backend architecture:** clear boundaries, authentication, and authorization.
- **Linux fundamentals:** processes, permissions, services, and how software runs underneath the framework.

## `$ git shortlog -sn`

[Repositories](https://github.com/Yosf96633?tab=repositories) · [GitHub activity](https://github.com/Yosf96633)

<details>
<summary>Optional telemetry · GitHub stats</summary>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Yosf96633&amp;show_icons=true&amp;hide_rank=true&amp;hide_border=true&amp;bg_color=0B0E14&amp;title_color=C792EA&amp;text_color=E6E6E6&amp;icon_color=7CFFB2" width="480" alt="Muhammad Yousaf's GitHub statistics, provided by GitHub Readme Stats.">
</p>

</details>

---

**Let's build something useful.**

For full-stack development, AI workflows, or document retrieval projects, get in touch:

[Email](mailto:yousaf.dev18@gmail.com) · [LinkedIn](https://linkedin.com/in/yousaf-dev18/) · [Portfolio](https://yousaf-dev18.vercel.app/)

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/footer.svg">
  <img src=".github/assets/footer.gif" width="480" alt="yousaf@github: ./contact --human — Connection kept alive.">
</picture>
