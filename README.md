<!-- Linux Desktop / violet edition. All decorative artwork is local. -->
<a name="profile-top"></a>

<img src=".github/assets/desktop/hero-ubuntu-v3.png" width="1200" alt="Muhammad Yousaf — Linux Systems, Agentic AI, and Full-stack Engineering. A violet Ubuntu-inspired desktop with a geometric penguin, the Ubuntu logo on a glass window, and a mountainous night sky.">

<h1 align="center">Hi, I'm Muhammad Yousaf</h1>

<p align="center">
  <strong>Linux systems · Agentic AI · Full-stack engineering</strong><br>
  From process groups and terminal control to stateful agents and cited answers.
</p>

<p align="center">
  <a href="#profile-about">About</a> &nbsp; / &nbsp;
  <a href="#profile-projects">Projects</a> &nbsp; / &nbsp;
  <a href="#profile-stack">Tech stack</a> &nbsp; / &nbsp;
  <a href="#profile-experience">Experience</a> &nbsp; / &nbsp;
  <a href="#profile-contact">Contact</a>
</p>

<p align="center">
  <a href="https://yousaf-dev18.vercel.app/">Portfolio ↗</a> &nbsp; / &nbsp;
  <a href="https://linkedin.com/in/yousaf-dev18/">LinkedIn ↗</a> &nbsp; / &nbsp;
  <a href="mailto:yousaf.dev18@gmail.com">Email ↗</a>
</p>

<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/building-mobile-static.png">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/building-static.png">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/building-mobile.gif">
  <img src=".github/assets/desktop/building.gif" width="1200" alt="Systems that think. Interfaces that work. An animated violet and cyan waveform.">
</picture>

<a name="profile-about"></a>

<h2><img src=".github/assets/desktop/section-about.svg" width="1200" alt="About me"></h2>

I build at the intersection of **Linux systems** and **agentic AI**. I wrote a Unix-like shell in C++20, and I build LangGraph workflows that turn model reasoning into useful actions and source-backed answers. I use TypeScript, Python, React, and Next.js to make those systems usable.

The details matter to me: process groups and terminal signals in a shell; explicit state, citations, validation, and human review in AI workflows.

<details>
<summary><strong>Inside ~/.config/yousaf/profile.toml</strong></summary>

```toml
# ~/.config/yousaf/profile.toml
shell = "zsh"
shell_project = "myShell"
editor = "VS Code"
focus = ["Linux systems", "Agentic AI", "Full-stack interfaces"]
approach = ["Process control", "Explicit state", "Traceable answers"]
```

</details>

<a name="profile-projects"></a>

<h2><img src=".github/assets/desktop/section-projects.svg" width="1200" alt="Selected builds — all five projects"></h2>

From Unix process control to AI workflows, retrieval, and full-stack applications.

<a href="https://github.com/Yosf96633/myshell">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/project-myshell-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/project-myshell-static.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/project-myshell-mobile.svg">
  <img src=".github/assets/desktop/project-myshell.svg" width="1200" alt="myShell">
</picture>
</a>

### [myShell](https://github.com/Yosf96633/myshell)

**A Unix-like shell built from the parser to the controlling terminal.**

<p>
  <a href="https://isocpp.org/"><img src=".github/assets/stack/cplusplus.svg" width="34" height="34" alt="C++" title="C++"></a>&nbsp;
  <a href="https://www.linux.org/"><img src=".github/assets/stack/linux.svg" width="34" height="34" alt="Linux" title="Linux"></a>&nbsp;
  <a href="https://cmake.org/"><img src=".github/assets/stack/cmake.svg" width="34" height="34" alt="CMake" title="CMake"></a>
</p>

A systems-programming project that implements quote-aware parsing, environment expansion, aliases, shell functions, pipelines, redirections, command history, signals, and foreground/background job control.

- **Clear execution boundary:** commands are fully parsed into `ParsedPipeline` data before execution mutates process, descriptor, or job state.
- **Unix process control:** concurrent pipeline stages share process groups, foreground jobs receive terminal signals, and `jobs`, `fg`, and `bg` manage background work.
- **Careful resource handling:** ordered redirections support file-descriptor duplication and closure, while parent-side changes are applied transactionally and restored afterward.
- **Terminal-level testing:** CTest covers parsing and exit behavior, while pseudo-terminal integration tests exercise signals, process groups, terminal handoff, and job control.

<details>
<summary><strong>Explore the implementation and architecture</strong></summary>

**Key Technical Achievements:**

- **Quote-Aware Command Parser**: Built a dedicated parser for single and double quotes backslash escaping environment assignments parameter expansion and syntax validation while correctly distinguishing quoted pipeline and background operators from shell control syntax
- **Concurrent Pipeline Execution**: Implemented multi-stage pipelines with one child process per stage shared process groups correct file-descriptor wiring and final-stage exit status propagation
- **Foreground and Background Job Control**: Added process-group based job management with terminal handoff background execution and the `jobs` `fg` and `bg` built-ins while preventing zombie processes through background reaping
- **Signal-Safe Interactive Behavior**: Coordinated `Ctrl+C` `Ctrl+\` and `Ctrl+Z` handling so signals reach foreground jobs without terminating the shell and prompt editing remains responsive
- **Transactional Redirection Engine**: Supported input output append descriptor duplication and descriptor closure with left-to-right shell semantics plus automatic restoration of parent file descriptors after built-ins complete
- **Command Resolution Cache**: Created PATH-based executable lookup with reusable path caching hit tracking invalidation when PATH changes and inspection through `hash` and `type` built-ins
- **Extensible Shell Features**: Developed a built-in registry aliases simple single-line functions recursion protection persistent environment assignments and session history with arrow-key navigation
- **Pseudo-Terminal Integration Testing**: Built automated CTest coverage for parsing execution exit statuses signals process groups terminal ownership and interactive job control using pseudo-terminals

**Technical Architecture:**

- Runtime: C++20 application using POSIX process signal file-descriptor and terminal APIs
- Parsing: Two-stage pipeline and command parser producing structured commands before execution begins
- Execution: Parent-side dispatch for stateful built-ins plus fork and exec process groups for external commands pipelines and background jobs
- Terminal Control: termios-based line editing process-group management and explicit terminal ownership handoff
- Build and Testing: CMake with compiler warnings CTest unit tests and pseudo-terminal integration tests

</details>

[Explore the repository →](https://github.com/Yosf96633/myshell)

<a href="https://github.com/Yosf96633/Autohunt">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/project-autohunt-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/project-autohunt-static.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/project-autohunt-mobile.svg">
  <img src=".github/assets/desktop/project-autohunt.svg" width="1200" alt="AutoHunt">
</picture>
</a>

### [AutoHunt](https://github.com/Yosf96633/Autohunt)

**From CV to reviewed job application, in one stateful workflow.**

<p>
  <a href="https://www.langchain.com/langgraph"><img src=".github/assets/stack/langgraph.svg" width="34" height="34" alt="LangGraph" title="LangGraph"></a>&nbsp;
  <a href="https://playwright.dev/"><img src=".github/assets/stack/playwright.svg" width="34" height="34" alt="Playwright" title="Playwright"></a>&nbsp;
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://www.typescriptlang.org/"><img src=".github/assets/stack/typescript.svg" width="34" height="34" alt="TypeScript" title="TypeScript"></a>&nbsp;
  <a href="https://www.postgresql.org/"><img src=".github/assets/stack/postgresql.svg" width="34" height="34" alt="PostgreSQL" title="PostgreSQL"></a>&nbsp;
  <a href="https://zod.dev/"><img src=".github/assets/stack/zod.svg" width="34" height="34" alt="Zod" title="Zod"></a>&nbsp;
  <a href="https://openai.com/"><img src=".github/assets/stack/openai.svg" width="34" height="34" alt="OpenAI" title="OpenAI"></a>&nbsp;
  <a href="https://groq.com/"><img src=".github/assets/stack/groq.svg" width="34" height="34" alt="Groq" title="Groq"></a>
</p>

A **10-stage agent workflow** that parses a CV, discovers jobs, scores relevance, and drafts cover letters before browser-driven submission.

- **Review before action:** users review scored jobs and cover letters before automated submission.
- **Iterative drafting:** OpenAI and Groq support job–CV matching and a cover-letter self-critique loop.
- **Persistent state:** PostgreSQL-backed LangGraph checkpoints retain workflow progress; Zod validates extracted CV data, normalized jobs, and model outputs.
- **Visible progress:** a Next.js dashboard shows live agent status, job browsing, and skill matches.

<details>
<summary><strong>Explore the implementation and architecture</strong></summary>

**Key Technical Achievements:**

- **Stateful LangGraph Workflow**: Orchestrated a complex 10-node state machine handling CV parsing job scraping relevance scoring filtering cover letter generation self-critique refinement human interruption browser automation tracking and email digest composition
- **Browser Automation Pipeline**: Built robust Playwright scripts that navigate job portals dynamically locate form fields and auto-fill applications based on structured resume data extraction
- **Multi-LLM Evaluation System**: Integrated OpenAI and Groq Llama 3.3 for dual-purpose evaluation including semantic job-CV matching with percentage scoring and iterative cover letter generation with critic-refiner loop for quality assurance
- **Document Intelligence**: Implemented pdfjs-dist based PDF parsing pipeline that extracts structured professional data from uploaded resumes including skills experience education and contact information
- **Human-in-the-Loop Architecture**: Designed graph interruption mechanism allowing users to review scored jobs and generated cover letters before automated submission combining AI efficiency with human judgment
- **Modern Full-Stack Dashboard**: Built real-time monitoring interface with Next.js 16 App Router React 19 Tailwind CSS v4 and shadcn/ui featuring live agent status job board browsing visualization skill matching analytics and application statistics
- **Type-Safe Validation**: Enforced strict schema validation throughout the workflow using Zod for CV data job listings LLM outputs and application forms ensuring data integrity across all pipeline stages
- **Database Integration**: Configured PostgreSQL with LangGraph checkpointing for workflow state persistence and SQLite for local job tracking with comprehensive application history logging

**Technical Architecture:**

- Backend: Node.js plus Express plus TypeScript with LangGraph state management
- Frontend: Next.js 16 App Router plus React 19 plus Tailwind CSS v4 plus shadcn/ui plus Framer Motion
- AI/ML: OpenAI API plus Groq Llama 3.3 plus pdfjs-dist plus semantic scoring algorithms
- Automation: Playwright for cross-platform browser automation with anti-detection measures
- Database: PostgreSQL for LangGraph checkpoints plus SQLite for job tracking

</details>

[Explore the repository →](https://github.com/Yosf96633/Autohunt)

<a href="https://github.com/Yosf96633/DocsAI">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/project-docsai-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/project-docsai-static.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/project-docsai-mobile.svg">
  <img src=".github/assets/desktop/project-docsai.svg" width="1200" alt="DocsAI">
</picture>
</a>

### [DocsAI](https://github.com/Yosf96633/DocsAI)

**Ask questions about legal documents and trace answers to the source.**

<p>
  <a href="https://www.python.org/"><img src=".github/assets/stack/python.svg" width="34" height="34" alt="Python" title="Python"></a>&nbsp;
  <a href="https://fastapi.tiangolo.com/"><img src=".github/assets/stack/fastapi.svg" width="34" height="34" alt="FastAPI" title="FastAPI"></a>&nbsp;
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://www.langchain.com/langgraph"><img src=".github/assets/stack/langgraph.svg" width="34" height="34" alt="LangGraph" title="LangGraph"></a>&nbsp;
  <a href="https://qdrant.tech/"><img src=".github/assets/stack/qdrant.svg" width="34" height="34" alt="Qdrant" title="Qdrant"></a>&nbsp;
  <a href="https://cohere.com/"><img src=".github/assets/stack/cohere.png" width="34" height="34" alt="Cohere" title="Cohere"></a>&nbsp;
  <a href="https://www.postgresql.org/"><img src=".github/assets/stack/postgresql.svg" width="34" height="34" alt="PostgreSQL" title="PostgreSQL"></a>&nbsp;
  <a href="https://openai.com/"><img src=".github/assets/stack/openai.svg" width="34" height="34" alt="OpenAI" title="OpenAI"></a>&nbsp;
  <a href="https://groq.com/"><img src=".github/assets/stack/groq.svg" width="34" height="34" alt="Groq" title="Groq"></a>&nbsp;
  <a href="https://cloudinary.com/"><img src=".github/assets/stack/cloudinary.svg" width="34" height="34" alt="Cloudinary" title="Cloudinary"></a>
</p>

A document analysis assistant with **separate ingestion and RAG chat workflows**, connecting PDF processing to streamed answers and source citations.

- **Hybrid retrieval:** Qdrant combines dense embeddings and SPLADE sparse vectors, followed by Cohere reranking for semantic and keyword relevance.
- **Source visibility:** position-aware PDF chunks retain page and estimated text coordinates for citation highlighting.
- **Streaming responses:** server-sent events deliver generated text and citations to the Next.js interface.
- **Conversation isolation:** PostgreSQL-backed thread context keeps chat histories separate.

<details>
<summary><strong>Explore the implementation and architecture</strong></summary>

**Key Technical Achievements:**

- **Legal Document Validation Pipeline**: Built an AI-powered pre-check system using GPT-4o-mini that analyzes uploaded PDFs to confirm they contain legal or compliance content before processing begins preventing wasted resources on irrelevant files
- **Hybrid Search Retrieval**: Implemented dual-vector search combining dense embeddings from OpenAI and sparse SPLADE vectors in Qdrant to capture both semantic meaning and exact keyword matches in legal terminology
- **Cohere Reranking Integration**: Added a reranking step after initial retrieval to sort results by true relevance ensuring only the most pertinent document sections inform the final answer
- **Streaming Response Architecture**: Developed server-sent events endpoint that delivers AI-generated tokens and citation sources in real time creating a responsive chat experience without page reloads
- **Multi-Provider LLM Orchestration**: Integrated Groq Llama 3.3 for generation OpenAI for embeddings and Cohere for reranking within a single LangGraph workflow optimizing cost and performance across different task types
- **Position-Aware Chunking**: Created custom PDF parsing logic that estimates vertical position of each text chunk enabling precise citation highlighting in the frontend document viewer
- **Thread-Isolated Context Management**: Designed PostgreSQL-backed thread system ensuring chat history and document context remain completely separate per conversation maintaining privacy and accuracy

**Technical Architecture:**

- Backend: Python FastAPI with LangGraph state machine orchestration
- Frontend: Next.js 16 App Router plus React 19 plus Tailwind CSS v4 plus Radix UI components
- AI Stack: Groq Llama 3.3 for generation plus OpenAI text-embedding-3-small for vectorization plus Cohere Reranker for result refinement
- Storage: Qdrant hybrid vector database plus PostgreSQL for metadata and thread management plus Cloudinary for PDF storage
- Workflow: Two independent LangGraph pipelines handling document ingestion and chat generation separately

</details>

[Explore the repository →](https://github.com/Yosf96633/DocsAI)

<a href="https://getvidly.com/">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/project-vidspire-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/project-vidspire-static.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/project-vidspire-mobile.svg">
  <img src=".github/assets/desktop/project-vidspire.svg" width="1200" alt="Vidspire / Vidly — YouTube sentiment analysis">
</picture>
</a>

### [Vidspire / Vidly](https://getvidly.com/)

**YouTube sentiment analysis platform.**

<p>
  <a href="https://nodejs.org/"><img src=".github/assets/stack/nodejs.svg" width="34" height="34" alt="Node.js" title="Node.js"></a>&nbsp;
  <a href="https://expressjs.com/"><img src=".github/assets/stack/express.svg" width="34" height="34" alt="Express" title="Express"></a>&nbsp;
  <a href="https://www.typescriptlang.org/"><img src=".github/assets/stack/typescript.svg" width="34" height="34" alt="TypeScript" title="TypeScript"></a>&nbsp;
  <a href="https://www.langchain.com/"><img src=".github/assets/stack/langchain.svg" width="34" height="34" alt="LangChain" title="LangChain"></a>&nbsp;
  <a href="https://www.langchain.com/langgraph"><img src=".github/assets/stack/langgraph.svg" width="34" height="34" alt="LangGraph" title="LangGraph"></a>&nbsp;
  <a href="https://bullmq.io/"><img src=".github/assets/stack/bullmq.png" width="99" height="34" alt="BullMQ" title="BullMQ"></a>&nbsp;
  <a href="https://redis.io/"><img src=".github/assets/stack/redis.svg" width="34" height="34" alt="Redis" title="Redis"></a>&nbsp;
  <a href="https://socket.io/"><img src=".github/assets/stack/socketio.svg" width="34" height="34" alt="Socket.IO" title="Socket.IO"></a>&nbsp;
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://resend.com/"><img src=".github/assets/stack/resend.svg" width="34" height="34" alt="Resend" title="Resend"></a>&nbsp;
  <a href="https://render.com/"><img src=".github/assets/stack/render.svg" width="34" height="34" alt="Render" title="Render"></a>&nbsp;
  <a href="https://vercel.com/"><img src=".github/assets/stack/vercel.svg" width="34" height="34" alt="Vercel" title="Vercel"></a>
</p>

An AI-powered platform that analyzes YouTube comments and transcripts to surface sentiment, emotions, content patterns, and actionable insights. Co-developed with **80% backend contribution** and **20% frontend contribution**.

- **Asynchronous processing:** BullMQ and Redis queue analysis jobs and coordinate workers, with concurrency and rate limits controlling workload.
- **Seven-stage analysis:** LangGraph runs sentiment classification and parallel analysis for emotions, patterns, loved aspects, improvements, and viewer requests.
- **Visible progress:** WebSocket updates follow each stage from queuing and data fetching through analysis and completion.
- **Resilient integrations:** parallel comment/transcript fetching, structured Zod outputs, Gemini key rotation, and Redis-backed rate limiting support processing.
- **Full-stack delivery:** deployed the backend on Render, configured Resend notifications, and contributed Next.js UI and SEO improvements on Vercel.

<details>
<summary><strong>Explore the implementation and architecture</strong></summary>

**Key Technical Achievements:**

- **Asynchronous Job Processing**: Architected queue-based system using BullMQ and Redis where sentiment analysis requests generate job IDs and are queued for processing by available workers preventing server overload and ensuring optimal resource utilization
- **LangGraph Workflow Engine**: Built multi-stage AI workflow with parallel processing pipelines featuring sentiment classification emotional analysis content pattern detection and actionable insights generation across 7 distinct stages
- **API Key Rotation & Load Balancing**: Implemented intelligent rotation across 8 Google Gemini API keys with automatic load distribution to optimize throughput and prevent rate limit bottlenecks
- **Real-time Progress Tracking**: Integrated WebSocket communication providing live progress updates through stages including queued fetching comments transcript retrieval classification parallel analysis summarization and completion
- **Parallel Data Fetching**: Optimized data retrieval using Promise.allSettled for concurrent YouTube comments and transcript fetching with graceful fallback handling
- **Redis-Based Rate Limiting**: Applied feature-specific throttling with express-rate-limit and Redis store to ensure system stability under high concurrent load
- **Production Deployment**: Configured backend deployment on Render implemented Resend for transactional email notifications and optimized Next.js frontend with SEO enhancements on Vercel with custom domain integration
- **Worker Concurrency Control**: Configured BullMQ workers with concurrency of 3 and rate limiting for optimal performance
- **Frontend Contributions**: Developed UI enhancements implemented SEO optimization in Next.js and improved overall user experience with 20% frontend contribution

**Technical Architecture:**

- Backend processes comments in batches using structured LLM outputs via Zod schemas
- Parallel analysis branches for emotions patterns loved aspects improvements and viewer requests
- Automatic transcript availability detection with non-blocking error handling
- Job progress tracking with percentage-based updates and stage-specific messages

</details>

[Live platform →](https://getvidly.com/) · [Backend →](https://github.com/Yosf96633/Vidly_backend) · [Frontend →](https://github.com/Yosf96633/Vidly_frontend)

<a href="https://github.com/Yosf96633/Better_auth_starter">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset=".github/assets/desktop/project-better-auth-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset=".github/assets/desktop/project-better-auth-static.svg">
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/project-better-auth-mobile.svg">
  <img src=".github/assets/desktop/project-better-auth.svg" width="1200" alt="Better Auth Starter — OAuth and two-factor authentication">
</picture>
</a>

### [Better Auth Starter](https://github.com/Yosf96633/Better_auth_starter)

**Authentication implementation with OAuth and two-factor authentication.**

<p>
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://react.dev/"><img src=".github/assets/stack/react.svg" width="34" height="34" alt="React" title="React"></a>&nbsp;
  <a href="https://www.typescriptlang.org/"><img src=".github/assets/stack/typescript.svg" width="34" height="34" alt="TypeScript" title="TypeScript"></a>&nbsp;
  <a href="https://tailwindcss.com/"><img src=".github/assets/stack/tailwindcss.svg" width="34" height="34" alt="Tailwind CSS" title="Tailwind CSS"></a>&nbsp;
  <a href="https://www.better-auth.com/"><img src=".github/assets/stack/betterauth.svg" width="34" height="34" alt="Better Auth" title="Better Auth"></a>&nbsp;
  <a href="https://www.postgresql.org/"><img src=".github/assets/stack/postgresql.svg" width="34" height="34" alt="PostgreSQL" title="PostgreSQL"></a>&nbsp;
  <a href="https://orm.drizzle.team/"><img src=".github/assets/stack/drizzle.svg" width="34" height="34" alt="Drizzle ORM" title="Drizzle ORM"></a>&nbsp;
  <a href="https://zod.dev/"><img src=".github/assets/stack/zod.svg" width="34" height="34" alt="Zod" title="Zod"></a>&nbsp;
  <a href="https://resend.com/"><img src=".github/assets/stack/resend.svg" width="34" height="34" alt="Resend" title="Resend"></a>
</p>

A Next.js and Better Auth starter covering sign-in, account management, and transactional email.

- **Sign-in options:** email/password authentication and GitHub/Google OAuth, with email verification and account linking.
- **Two-factor authentication:** TOTP verification, backup codes, and session management.
- **Account workflows:** profile updates, password changes and resets, and account deletion.
- **Data and email:** PostgreSQL with Drizzle ORM, Zod validation, and Resend/React Email templates.

[Explore the repository →](https://github.com/Yosf96633/Better_auth_starter)

[Browse all repositories →](https://github.com/Yosf96633?tab=repositories)

<a name="profile-stack"></a>

<h2><img src=".github/assets/desktop/section-stack.svg" width="1200" alt="Tech stack — linked technology icons"></h2>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-languages-mobile.svg">
  <img src=".github/assets/desktop/stack-languages.svg" width="1200" alt="Languages technologies">
</picture></p>

<p align="center">
  <a href="https://www.typescriptlang.org/"><img src=".github/assets/stack/typescript.svg" width="48" height="48" alt="TypeScript" title="TypeScript"></a>&nbsp;
  <a href="https://developer.mozilla.org/docs/Web/JavaScript"><img src=".github/assets/stack/javascript.svg" width="48" height="48" alt="JavaScript" title="JavaScript"></a>&nbsp;
  <a href="https://www.python.org/"><img src=".github/assets/stack/python.svg" width="48" height="48" alt="Python" title="Python"></a>&nbsp;
  <a href="https://isocpp.org/"><img src=".github/assets/stack/cplusplus.svg" width="48" height="48" alt="C++" title="C++"></a>&nbsp;
  <a href="https://www.c-language.org/"><img src=".github/assets/stack/c.svg" width="48" height="48" alt="C" title="C"></a>&nbsp;
  <a href="https://www.rust-lang.org/"><img src=".github/assets/stack/rust.svg" width="48" height="48" alt="Rust" title="Rust"></a>&nbsp;
  <a href="https://www.gnu.org/software/bash/"><img src=".github/assets/stack/bash.svg" width="48" height="48" alt="Bash" title="Bash"></a>&nbsp;
  <a href="https://www.php.net/"><img src=".github/assets/stack/php.svg" width="48" height="48" alt="PHP" title="PHP"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-frontend-mobile.svg">
  <img src=".github/assets/desktop/stack-frontend.svg" width="1200" alt="Frontend technologies">
</picture></p>

<p align="center">
  <a href="https://developer.mozilla.org/docs/Web/HTML"><img src=".github/assets/stack/html5.svg" width="48" height="48" alt="HTML" title="HTML"></a>&nbsp;
  <a href="https://developer.mozilla.org/docs/Web/CSS"><img src=".github/assets/stack/css3.svg" width="48" height="48" alt="CSS" title="CSS"></a>&nbsp;
  <a href="https://react.dev/"><img src=".github/assets/stack/react.svg" width="48" height="48" alt="React" title="React"></a>&nbsp;
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="48" height="48" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://tailwindcss.com/"><img src=".github/assets/stack/tailwindcss.svg" width="48" height="48" alt="Tailwind CSS" title="Tailwind CSS"></a>&nbsp;
  <a href="https://ui.shadcn.com/"><img src=".github/assets/stack/shadcnui.svg" width="48" height="48" alt="shadcn/ui" title="shadcn/ui"></a>&nbsp;
  <a href="https://redux.js.org/"><img src=".github/assets/stack/redux.svg" width="48" height="48" alt="Redux" title="Redux"></a>&nbsp;
  <a href="https://zustand-demo.pmnd.rs/"><img src=".github/assets/stack/zustand.png" width="48" height="48" alt="Zustand" title="Zustand"></a>&nbsp;
  <a href="https://playwright.dev/"><img src=".github/assets/stack/playwright.svg" width="48" height="48" alt="Playwright" title="Playwright"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-backend-mobile.svg">
  <img src=".github/assets/desktop/stack-backend.svg" width="1200" alt="Backend technologies">
</picture></p>

<p align="center">
  <a href="https://nodejs.org/"><img src=".github/assets/stack/nodejs.svg" width="48" height="48" alt="Node.js" title="Node.js"></a>&nbsp;
  <a href="https://expressjs.com/"><img src=".github/assets/stack/express.svg" width="48" height="48" alt="Express" title="Express"></a>&nbsp;
  <a href="https://nestjs.com/"><img src=".github/assets/stack/nestjs.svg" width="48" height="48" alt="NestJS" title="NestJS"></a>&nbsp;
  <a href="https://fastapi.tiangolo.com/"><img src=".github/assets/stack/fastapi.svg" width="48" height="48" alt="FastAPI" title="FastAPI"></a>&nbsp;
  <a href="https://laravel.com/"><img src=".github/assets/stack/laravel.svg" width="48" height="48" alt="Laravel" title="Laravel"></a>&nbsp;
  <a href="https://www.better-auth.com/"><img src=".github/assets/stack/betterauth.svg" width="48" height="48" alt="Better Auth" title="Better Auth"></a>&nbsp;
  <a href="https://authjs.dev/"><img src=".github/assets/stack/authjs.png" width="48" height="48" alt="Auth.js" title="Auth.js"></a>&nbsp;
  <a href="https://jwt.io/"><img src=".github/assets/stack/jsonwebtokens.svg" width="48" height="48" alt="JSON Web Tokens" title="JSON Web Tokens"></a>&nbsp;
  <a href="https://zod.dev/"><img src=".github/assets/stack/zod.svg" width="48" height="48" alt="Zod" title="Zod"></a>&nbsp;
  <a href="https://developer.mozilla.org/docs/Web/API/WebSockets_API"><img src=".github/assets/stack/websockets.svg" width="48" height="48" alt="WebSockets" title="WebSockets"></a>&nbsp;
  <a href="https://socket.io/"><img src=".github/assets/stack/socketio.svg" width="48" height="48" alt="Socket.IO" title="Socket.IO"></a>&nbsp;
  <a href="https://bullmq.io/"><img src=".github/assets/stack/bullmq.png" width="140" height="48" alt="BullMQ" title="BullMQ"></a>&nbsp;
  <a href="https://resend.com/"><img src=".github/assets/stack/resend.svg" width="48" height="48" alt="Resend" title="Resend"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-data-mobile.svg">
  <img src=".github/assets/desktop/stack-data.svg" width="1200" alt="Data technologies">
</picture></p>

<p align="center">
  <a href="https://www.postgresql.org/"><img src=".github/assets/stack/postgresql.svg" width="48" height="48" alt="PostgreSQL" title="PostgreSQL"></a>&nbsp;
  <a href="https://www.mongodb.com/"><img src=".github/assets/stack/mongodb.svg" width="48" height="48" alt="MongoDB" title="MongoDB"></a>&nbsp;
  <a href="https://www.mysql.com/"><img src=".github/assets/stack/mysql.svg" width="48" height="48" alt="MySQL" title="MySQL"></a>&nbsp;
  <a href="https://redis.io/"><img src=".github/assets/stack/redis.svg" width="48" height="48" alt="Redis" title="Redis"></a>&nbsp;
  <a href="https://qdrant.tech/"><img src=".github/assets/stack/qdrant.svg" width="48" height="48" alt="Qdrant" title="Qdrant"></a>&nbsp;
  <a href="https://www.prisma.io/"><img src=".github/assets/stack/prisma.svg" width="48" height="48" alt="Prisma ORM" title="Prisma ORM"></a>&nbsp;
  <a href="https://orm.drizzle.team/"><img src=".github/assets/stack/drizzle.svg" width="48" height="48" alt="Drizzle ORM" title="Drizzle ORM"></a>&nbsp;
  <a href="https://mongoosejs.com/"><img src=".github/assets/stack/mongoose.svg" width="48" height="48" alt="Mongoose" title="Mongoose"></a>&nbsp;
  <a href="https://sqlite.org/"><img src=".github/assets/stack/sqlite.svg" width="48" height="48" alt="SQLite" title="SQLite"></a>&nbsp;
  <a href="https://cloudinary.com/"><img src=".github/assets/stack/cloudinary.svg" width="48" height="48" alt="Cloudinary" title="Cloudinary"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-ai-mobile.svg">
  <img src=".github/assets/desktop/stack-ai.svg" width="1200" alt="Ai technologies">
</picture></p>

<p align="center">
  <a href="https://www.langchain.com/"><img src=".github/assets/stack/langchain.svg" width="48" height="48" alt="LangChain" title="LangChain"></a>&nbsp;
  <a href="https://www.langchain.com/langgraph"><img src=".github/assets/stack/langgraph.svg" width="48" height="48" alt="LangGraph" title="LangGraph"></a>&nbsp;
  <a href="https://openai.com/"><img src=".github/assets/stack/openai.svg" width="48" height="48" alt="OpenAI" title="OpenAI"></a>&nbsp;
  <a href="https://groq.com/"><img src=".github/assets/stack/groq.svg" width="48" height="48" alt="Groq" title="Groq"></a>&nbsp;
  <a href="https://cohere.com/"><img src=".github/assets/stack/cohere.png" width="48" height="48" alt="Cohere" title="Cohere"></a>&nbsp;
  <a href="https://n8n.io/"><img src=".github/assets/stack/n8n.svg" width="48" height="48" alt="n8n" title="n8n"></a>&nbsp;
  <a href="https://modelcontextprotocol.io/"><img src=".github/assets/stack/modelcontextprotocol.svg" width="48" height="48" alt="Model Context Protocol" title="Model Context Protocol"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-linux-mobile.svg">
  <img src=".github/assets/desktop/stack-linux.svg" width="1200" alt="Linux technologies">
</picture></p>

<p align="center">
  <a href="https://www.linux.org/"><img src=".github/assets/stack/linux.svg" width="48" height="48" alt="Linux" title="Linux"></a>&nbsp;
  <a href="https://nmap.org/"><img src=".github/assets/stack/nmap.png" width="48" height="48" alt="Nmap" title="Nmap"></a>&nbsp;
  <a href="https://www.metasploit.com/"><img src=".github/assets/stack/metasploit.png" width="48" height="48" alt="Metasploit" title="Metasploit"></a>&nbsp;
  <a href="https://www.wireshark.org/"><img src=".github/assets/stack/wireshark.png" width="48" height="48" alt="Wireshark" title="Wireshark"></a>&nbsp;
  <a href="https://portswigger.net/burp"><img src=".github/assets/stack/burpsuite.svg" width="48" height="48" alt="Burp Suite" title="Burp Suite"></a>
</p>

<p><picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/stack-tooling-mobile.svg">
  <img src=".github/assets/desktop/stack-tooling.svg" width="1200" alt="Tooling technologies">
</picture></p>

<p align="center">
  <a href="https://git-scm.com/"><img src=".github/assets/stack/git.svg" width="48" height="48" alt="Git" title="Git"></a>&nbsp;
  <a href="https://github.com/"><img src=".github/assets/stack/github.svg" width="48" height="48" alt="GitHub" title="GitHub"></a>&nbsp;
  <a href="https://cmake.org/"><img src=".github/assets/stack/cmake.svg" width="48" height="48" alt="CMake" title="CMake"></a>&nbsp;
  <a href="https://www.docker.com/"><img src=".github/assets/stack/docker.svg" width="48" height="48" alt="Docker" title="Docker"></a>&nbsp;
  <a href="https://vercel.com/"><img src=".github/assets/stack/vercel.svg" width="48" height="48" alt="Vercel" title="Vercel"></a>&nbsp;
  <a href="https://render.com/"><img src=".github/assets/stack/render.svg" width="48" height="48" alt="Render" title="Render"></a>
</p>

<a name="profile-experience"></a>

<h2><img src=".github/assets/desktop/section-experience.svg" width="1200" alt="Work experience"></h2>

<picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/experience-independent-mobile.svg">
  <img src=".github/assets/desktop/experience-independent.svg" width="1200" alt="Self-Employed · Independent · May 2026 to present">
</picture>

### `2026-05 → Present` · Self-Employed

**Independent**

<picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/experience-mozzine-mobile.svg">
  <img src=".github/assets/desktop/experience-mozzine.svg" width="1200" alt="Frontend Developer · Mozzine Technologies · October 2025 to April 2026">
</picture>

### `2025-10 → 2026-04` · Frontend Developer

**Mozzine Technologies**

- Developed B2B SaaS dashboard features with Next.js, TypeScript, and Tailwind CSS.
- Translated **20+ Figma designs** into responsive components with shadcn/ui, maintaining consistency across desktop and mobile.
- Integrated REST APIs with Redux and Zustand, and resolved UI bugs across browsers and dashboard modules.

<p>
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://www.typescriptlang.org/"><img src=".github/assets/stack/typescript.svg" width="34" height="34" alt="TypeScript" title="TypeScript"></a>&nbsp;
  <a href="https://tailwindcss.com/"><img src=".github/assets/stack/tailwindcss.svg" width="34" height="34" alt="Tailwind CSS" title="Tailwind CSS"></a>&nbsp;
  <a href="https://ui.shadcn.com/"><img src=".github/assets/stack/shadcnui.svg" width="34" height="34" alt="shadcn/ui" title="shadcn/ui"></a>&nbsp;
  <a href="https://redux.js.org/"><img src=".github/assets/stack/redux.svg" width="34" height="34" alt="Redux" title="Redux"></a>&nbsp;
  <a href="https://zustand-demo.pmnd.rs/"><img src=".github/assets/stack/zustand.png" width="34" height="34" alt="Zustand" title="Zustand"></a>
</p>

<picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/experience-code-expert-mobile.svg">
  <img src=".github/assets/desktop/experience-code-expert.svg" width="1200" alt="Full Stack Intern · Code Expert · July to September 2025">
</picture>

### `2025-07 → 2025-09` · Full Stack Intern

**Code Expert**

- Developed a multi-vendor e-commerce platform with **2 role-based dashboards** for food and gift product modules.
- Built **15+ REST API endpoints** for orders, products, and vendor operations, with shared MongoDB schemas and validation middleware.
- Improved database query response times by **40%** using Mongoose lean queries, projections, and compound indexes.
- Implemented NextAuth.js authentication, JWT sessions, role-based access, and transactional emails through Resend.

<p>
  <a href="https://nextjs.org/"><img src=".github/assets/stack/nextjs.svg" width="34" height="34" alt="Next.js" title="Next.js"></a>&nbsp;
  <a href="https://expressjs.com/"><img src=".github/assets/stack/express.svg" width="34" height="34" alt="Express" title="Express"></a>&nbsp;
  <a href="https://nodejs.org/"><img src=".github/assets/stack/nodejs.svg" width="34" height="34" alt="Node.js" title="Node.js"></a>&nbsp;
  <a href="https://tailwindcss.com/"><img src=".github/assets/stack/tailwindcss.svg" width="34" height="34" alt="Tailwind CSS" title="Tailwind CSS"></a>&nbsp;
  <a href="https://www.mongodb.com/"><img src=".github/assets/stack/mongodb.svg" width="34" height="34" alt="MongoDB" title="MongoDB"></a>&nbsp;
  <a href="https://mongoosejs.com/"><img src=".github/assets/stack/mongoose.svg" width="34" height="34" alt="Mongoose" title="Mongoose"></a>&nbsp;
  <a href="https://authjs.dev/"><img src=".github/assets/stack/authjs.png" width="34" height="34" alt="Auth.js" title="Auth.js"></a>&nbsp;
  <a href="https://jwt.io/"><img src=".github/assets/stack/jsonwebtokens.svg" width="34" height="34" alt="JSON Web Tokens" title="JSON Web Tokens"></a>&nbsp;
  <a href="https://resend.com/"><img src=".github/assets/stack/resend.svg" width="34" height="34" alt="Resend" title="Resend"></a>
</p>

<picture>
  <source media="(max-width: 600px)" srcset=".github/assets/desktop/experience-hiba-logics-mobile.svg">
  <img src=".github/assets/desktop/experience-hiba-logics.svg" width="1200" alt="PHP Laravel Intern · Hiba Logics · May to June 2025">
</picture>

### `2025-05 → 2025-06` · PHP Laravel Intern

**Hiba Logics**

- Applied Laravel routing, controllers, Eloquent ORM, and Blade templates in backend development.
- Built server-side logic and database interactions using the Model–View–Controller pattern.
- Worked with MySQL queries, migrations, and Laravel's schema builder.
- Collaborated with senior developers, participated in code reviews, and followed team development practices.

<p>
  <a href="https://www.php.net/"><img src=".github/assets/stack/php.svg" width="34" height="34" alt="PHP" title="PHP"></a>&nbsp;
  <a href="https://laravel.com/"><img src=".github/assets/stack/laravel.svg" width="34" height="34" alt="Laravel" title="Laravel"></a>&nbsp;
  <a href="https://www.mysql.com/"><img src=".github/assets/stack/mysql.svg" width="34" height="34" alt="MySQL" title="MySQL"></a>&nbsp;
  <a href="https://git-scm.com/"><img src=".github/assets/stack/git.svg" width="34" height="34" alt="Git" title="Git"></a>
</p>

<a name="profile-education"></a>

<h2><img src=".github/assets/desktop/section-education.svg" width="1200" alt="Education"></h2>

**BS Computer Science** · Government College University Faisalabad · 2021–2025

<a name="profile-notes"></a>

<h2><img src=".github/assets/desktop/section-notes.svg" width="1200" alt="Engineering notes"></h2>

I'm going deeper into the parts that make these systems dependable:

- **Agent design:** explicit state, conditional routing, persistence, and human review.
- **Retrieval:** hybrid search, reranking, and evaluation against source documents.
- **Backend architecture:** clear boundaries, authentication, and authorization.
- **Linux fundamentals:** processes, permissions, services, and how software runs underneath the framework.

<a name="profile-activity"></a>

<h2><img src=".github/assets/desktop/section-activity.svg" width="1200" alt="Open source and GitHub activity"></h2>

[Repositories](https://github.com/Yosf96633?tab=repositories) · [GitHub activity](https://github.com/Yosf96633)

<details>
<summary>Optional telemetry · GitHub stats</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Yosf96633&amp;theme=github_dark">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Yosf96633&amp;theme=github" width="360" alt="Muhammad Yousaf's GitHub statistics.">
  </picture>
</p>

</details>

<a name="profile-contact"></a>

<h2><img src=".github/assets/desktop/section-contact.svg" width="1200" alt="Let's connect"></h2>

**Let's build something useful.**

For Linux systems, agentic AI, or full-stack projects, get in touch:

<p align="center">
  <a href="https://yousaf-dev18.vercel.app/"><img src=".github/assets/desktop/contact-portfolio.svg" width="31%" alt="Portfolio — explore the work"></a>
  <a href="https://linkedin.com/in/yousaf-dev18/"><img src=".github/assets/desktop/contact-linkedin.svg" width="31%" alt="LinkedIn — connect with me"></a>
  <a href="mailto:yousaf.dev18@gmail.com"><img src=".github/assets/desktop/contact-email.svg" width="31%" alt="Email — let's build something useful"></a>
</p>

[Email](mailto:yousaf.dev18@gmail.com) · [LinkedIn](https://linkedin.com/in/yousaf-dev18/) · [Portfolio](https://yousaf-dev18.vercel.app/) · [Back to top ↑](#profile-top)
