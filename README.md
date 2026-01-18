[![header](.github/readme-header.png)](https://gautierpicon.com)

# My Portfolio [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

My personal protfolio. Have fun !!
[gautierpicon.com](https://gautierpicon.com)

## Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/GP-Portfolio/issues) or a [pull request](https://github.com/Gautierpicon/GP-Portfolio/pulls) on the GitHub repository.

## Tech Stack

**Client:** Bun, Astro, Svelte, TailwindCSS

**Server:** FastAPI (Python)

**Hosting:** backend: selfhost // Frontend: Vercel

## Features

Chat with the AI and find out who I am, my background, the tools I'm proficient in, and much more. Feel free to ask any questions you may have. I've provided the AI with enough context about myself for it to be able to answer your questions and even provide useful links. 

## Operating Diagram

```bash
┌──────────────────────┐
│  Vercel              │ ← Frontend
│                      │
└──────────┬───────────┘
           │
           │ Call my API via the Internet
           │
           ▼
┌──────────────────────┐
│  Serveur             │ ← Backend that I host
│                      │
│  ┌────────────────┐  │
│  │ FastAPI      ◀──────── The API
│  │                │  │
│  └────────┬───────┘  │
│           ▼          │
│  ┌────────────────┐  │
│  │ Ollama       ◀──────── Local AI
│  │                │  │
│  └────────────────┘  │
└──────────────────────┘
```
## contribute to or launch the project locally

To contribute or launch the project locally, set up each part of the project: backend, frontend, and AI. Go to the READMEs associated with each to do so.

- [Backend README](https://github.com/Gautierpicon/Portfolio/tree/main/backend)
- [Frontend README](https://github.com/Gautierpicon/Portfolio/tree/main/frontend)
- [Model README](https://github.com/Gautierpicon/GP-Portfolio/tree/main/ollama)

## Repository structure

```bash
Portfolio/
├── backend/
│   ├── main.py
│   ├── README.md
│   └── pyproject.toml
│
├── frontend/
│   ├── public/
│   │   ├── favicon.svg
│   │   └── quack.mp3
│   ├── src/
│   │   ├── assets/
│   │   │   └── ...
│   │   ├── components/
│   │   │   ├── ChatInput.svelte
│   │   │   └── ConversationView.svelte
│   │   ├── data/
│   │   │   └── ...
│   │   ├── layouts/
│   │   │   └── Layout.astro
│   │   ├── pages/
│   │   │   ├── 404.astro
│   │   │   ├── chat.astro
│   │   │   ├── how-it-works.astro
│   │   │   └── index.astro
│   │   └── global.css
│   └── README.md
│
├── ollama/
│   ├── Modelfile
│   └── README.md
│
├── LICENSE.md
└── README.md
```

## Privacy

This site respects users and their data. The data collected ANONYMOUSLY and INDEPENDENTLY from each other through [Vercel analytics](https://vercel.com/docs/analytics) are: your country, your operating system and web browser, your origin and the pages visited.
If this data collection bothers you, feel free to use an [ad blocker](https://en.wikipedia.org/wiki/Ad_blocking) (such as [uBlock](https://ublockorigin.com/fr)) that blocks trackers.