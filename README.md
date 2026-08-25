<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0B0E14,100:0B0E14&height=2&section=header" width="100%"/>
</div>

<br/>

```
$ whoami
```

<h1 align="center">Muhammad Yousaf</h1>
<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&pause=1200&color=C792EA&center=true&vCenter=true&width=600&lines=full-stack+developer+%2F%2F+MERN+%2B+Next.js;AI+systems+engineer+%2F%2F+LangGraph+%2B+RAG;builds+agents+that+ship+to+production" alt="Typing SVG"/>
</p>

<p align="center">
<a href="https://linkedin.com/in/yousaf-dev18/"><img src="https://img.shields.io/badge/linkedin-0B0E14?style=flat-square&logo=linkedin&logoColor=C792EA&labelColor=0B0E14"/></a>
<a href="mailto:yousaf.dev18@gmail.com"><img src="https://img.shields.io/badge/email-0B0E14?style=flat-square&logo=gmail&logoColor=F5A623&labelColor=0B0E14"/></a>
<a href="https://yousaf-dev18.vercel.app/"><img src="https://img.shields.io/badge/portfolio-0B0E14?style=flat-square&logo=vercel&logoColor=E6E6E6&labelColor=0B0E14"/></a>
<img src="https://komarev.com/ghpvc/?username=Yosf96633&style=flat-square&color=0B0E14&label=views"/>
</p>

<br/>

### `$ cat pipeline.log` — how I build things

The last thing I shipped was a 10-stage LangGraph agent. This is roughly how I think:

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  PARSE   │──▶│  SCRAPE  │──▶│  SCORE   │──▶│ GENERATE │──▶│  REVIEW  │
│  input   │   │  sources │   │ (LLM)    │   │ (LLM)    │   │  (human) │
└──────────┘   └──────────┘   └──────────┘   └────┬─────┘   └────┬─────┘
                                                    │              │
                                                    └──────────────┘
                                                  self-critique loop
                                                         │
                                                         ▼
                                                  ┌──────────────┐
                                                  │    SHIP IT   │
                                                  └──────────────┘
```

Parse the problem → gather context → let the model reason → generate → put a human in the loop → refine → ship. Same shape whether it's a job-application agent or a legal-doc assistant.

<br/>

### `$ cat mission.txt`

```
Building autonomous agents and RAG systems that go past the demo stage
and hold up in production. Consistency beats talent — I show up every day.
```

<br/>

## stack

<div align="center">
<img src="https://skillicons.dev/icons?i=js,ts,py,react,nextjs,redux,tailwind,nodejs,express,fastapi,mongodb,postgres,redis,docker,git,github,vercel,figma&theme=dark&perline=9"/>
</div>

<br/>

**AI / automation** &nbsp;·&nbsp; LangChain · LangGraph · OpenAI API · Groq · Cohere Rerank · Qdrant · n8n · RAG · MCP
**Auth & tooling** &nbsp;·&nbsp; NextAuth · Better Auth · JWT · Drizzle ORM · Mongoose · Zod · Postman

<br/>

## `$ ls -la ~/projects`

```bash
drwxr-xr-x  autohunt/               # autonomous AI job-application agent — 10-stage LangGraph pipeline
drwxr-xr-x  docsai/                 # legal-document RAG assistant — hybrid search + citation grounding
drwxr-xr-x  vidspire/               # YouTube sentiment analysis platform
drwxr-xr-x  cambot/                 # AI-powered conversational chatbot
drwxr-xr-x  better-auth-starter/    # production-ready auth boilerplate — OAuth, 2FA
```

<table width="100%">
<tr>
<td width="50%" valign="top">

**🤖 AutoHunt** — `LangGraph · Playwright · Next.js 16 · PostgreSQL`
Ten-stage workflow: parses your CV, scrapes job boards, scores relevance with an LLM, drafts cover letters with a self-critique refinement loop, then pauses for human review before Playwright submits anything.

[`→ github.com/Yosf96633/Autohunt`](https://github.com/Yosf96633/Autohunt)

</td>
<td width="50%" valign="top">

**⚖️ DocsAI** — `FastAPI · LangGraph · Qdrant · Cohere`
Dual LangGraph workflows for ingestion and RAG chat. Hybrid dense + sparse vector search, reranked with Cohere, chunked with position-awareness so every answer cites the exact page it came from.

[`→ github.com/Yosf96633/DocsAI`](https://github.com/Yosf96633/DocsAI)

</td>
</tr>
</table>

<br/>

## `$ git log --oneline --author=yousaf`

```
* Oct 2025 — Apr 2026   Frontend Developer, Mozzine Technologies
│                        built B2B SaaS dashboard UI · Next.js/TS/Tailwind
│                        20+ Figma designs → pixel-perfect ShadCN components
│
* Jul 2025 — Sep 2025    Full Stack Intern, Code Expert
                         multi-vendor e-commerce platform · 2 role-based dashboards
                         15+ REST endpoints · 40% faster queries via Mongoose indexing
```

<br/>

## `$ cat education.md`

```
BS Computer Science           Government College University Faisalabad     2021 – 2025
FSc Pre-Engineering           Royal College of Science, Narowal            2019 – 2021
```

<br/>

## stats

<div align="center">
<img width="49%" src="https://github-readme-stats.vercel.app/api?username=Yosf96633&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0B0E14&title_color=C792EA&icon_color=F5A623&text_color=E6E6E6"/>
<img width="49%" src="https://nirzak-streak-stats.vercel.app/?user=Yosf96633&theme=tokyonight&hide_border=true&background=0B0E14&ring=C792EA&fire=F5A623&currStreakLabel=C792EA"/>
</div>

<div align="center">
<img width="70%" src="https://github-readme-activity-graph.vercel.app/graph?username=Yosf96633&theme=tokyo-night&hide_border=true&bg_color=0B0E14&color=C792EA&line=C792EA&point=F5A623"/>
</div>

<br/>

<div align="center">

```
$ echo "let's build something" | mail yousaf.dev18@gmail.com
```

<a href="https://linkedin.com/in/yousaf-dev18/"><img src="https://img.shields.io/badge/linkedin-0B0E14?style=flat-square&logo=linkedin&logoColor=C792EA&labelColor=0B0E14"/></a>
<a href="mailto:yousaf.dev18@gmail.com"><img src="https://img.shields.io/badge/email-0B0E14?style=flat-square&logo=gmail&logoColor=F5A623&labelColor=0B0E14"/></a>
<a href="https://yousaf-dev18.vercel.app/"><img src="https://img.shields.io/badge/portfolio-0B0E14?style=flat-square&logo=vercel&logoColor=E6E6E6&labelColor=0B0E14"/></a>

<br/><br/>
<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0B0E14,100:0B0E14&height=2&section=footer" width="100%"/>
</div>
