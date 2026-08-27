<div align="center">
<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0B0E14,100:0B0E14&height=2&section=header" width="100%"/>
</div>

<br/>

```
yousaf@dev:~$ neofetch
```

<table>
<tr>
<td valign="top">

```
        _nnnn_
       dGGGGMMb
      @p~qp~~qMb
      M|@||@) M|
      @,----.JM|
     JS^\__/  qKL
    dZP        qKRb
   dZP          qKKb
  fZP            SMMb
  HZM            MMMM
  FqM            MMMM
__| ".        |\dS"qML
|    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--'
```

</td>
<td valign="top">

```
yousaf@dev
-----------
OS:        Linux x86_64
Host:      Full-Stack + AI Systems Engineer
Shell:     zsh
Editor:    VS Code
Languages: TypeScript, Python, JavaScript
Stack:     Next.js · FastAPI · LangGraph
Focus:     Autonomous agents, RAG pipelines
Uptime:    shipping since 2021
```

</td>
</tr>
</table>

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

## stack

<div align="center">
<img src="https://skillicons.dev/icons?i=linux,js,ts,py,react,nextjs,redux,tailwind,nodejs,express,fastapi,mongodb,postgres,redis,docker,git,github,vercel,figma&theme=dark&perline=9"/>
</div>

<br/>

<div align="center">

**AI / automation**

<img src="https://img.shields.io/badge/OpenAI-0B0E14?style=flat-square&logo=openai&logoColor=74AA9C&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/LangChain-0B0E14?style=flat-square&logo=langchain&logoColor=C792EA&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/LangGraph-0B0E14?style=flat-square&logo=graphql&logoColor=F5A623&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Groq-0B0E14?style=flat-square&logo=lightning&logoColor=F5A623&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Cohere-0B0E14?style=flat-square&logo=cohere&logoColor=E6E6E6&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Qdrant-0B0E14?style=flat-square&logo=qdrant&logoColor=C792EA&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/n8n-0B0E14?style=flat-square&logo=n8n&logoColor=F5A623&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/RAG-0B0E14?style=flat-square&labelColor=0B0E14&color=0B0E14"/>
<img src="https://img.shields.io/badge/MCP-0B0E14?style=flat-square&labelColor=0B0E14&color=0B0E14"/>

**auth & tooling**

<img src="https://img.shields.io/badge/NextAuth-0B0E14?style=flat-square&labelColor=0B0E14&color=0B0E14"/>
<img src="https://img.shields.io/badge/JWT-0B0E14?style=flat-square&logo=jsonwebtokens&logoColor=C792EA&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Drizzle-0B0E14?style=flat-square&logo=drizzle&logoColor=F5A623&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Zod-0B0E14?style=flat-square&logo=zod&logoColor=E6E6E6&labelColor=0B0E14"/>
<img src="https://img.shields.io/badge/Postman-0B0E14?style=flat-square&logo=postman&logoColor=F5A623&labelColor=0B0E14"/>

</div>

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

## stats

<div align="center">
<img width="49%" src="https://github-readme-stats.vercel.app/api?username=Yosf96633&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0B0E14&title_color=C792EA&icon_color=F5A623&text_color=E6E6E6"/>
<img width="49%" src="https://streak-stats.demolab.com?user=Yosf96633&theme=tokyonight&hide_border=true&background=0B0E14&ring=C792EA&fire=F5A623&currStreakLabel=C792EA"/>
</div>

<div align="center">
<img width="70%" src="https://github-readme-activity-graph.vercel.app/graph?username=Yosf96633&theme=tokyo-night&hide_border=true&bg_color=0B0E14&color=C792EA&line=C792EA&point=F5A623"/>
</div>

> these three widgets are served from free, shared community instances — GitHub's image proxy occasionally can't reach them and you'll see a broken-image icon. It's not your README; refreshing the page usually fixes it. If it keeps happening, forking `anuraghazra/github-readme-stats` to your own Vercel account gives you a dedicated instance that won't rate-limit.

<br/>

<div align="center">

```
yousaf@dev:~$ echo "let's build something" | mail yousaf.dev18@gmail.com
```

<a href="https://linkedin.com/in/yousaf-dev18/"><img src="https://img.shields.io/badge/linkedin-0B0E14?style=flat-square&logo=linkedin&logoColor=C792EA&labelColor=0B0E14"/></a>
<a href="mailto:yousaf.dev18@gmail.com"><img src="https://img.shields.io/badge/email-0B0E14?style=flat-square&logo=gmail&logoColor=F5A623&labelColor=0B0E14"/></a>
<a href="https://yousaf-dev18.vercel.app/"><img src="https://img.shields.io/badge/portfolio-0B0E14?style=flat-square&logo=vercel&logoColor=E6E6E6&labelColor=0B0E14"/></a>

<br/><br/>
<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0B0E14,100:0B0E14&height=2&section=footer" width="100%"/>
</div>
