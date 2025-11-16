# Frontend - Portfolio

Frontend for my personal portfolio built with Astro, Svelte, and TailwindCSS.

## Tech Stack

- **Framework**: [Astro](https://astro.build/) 5.x
- **UI Components**: [Svelte](https://svelte.dev/) 5.x
- **Styling**: [TailwindCSS](https://tailwindcss.com/) 4.x
- **Package Manager**: [Bun](https://bun.sh/)
- **Deployment**: [Vercel](https://vercel.com/)

## Project Structure

```
frontend/
├── public/
│   ├── favicon.svg         # Site icon
│   └── quack.mp3           # Duck sound
├── src/
│   ├── assets/             # Images and resources
│   │   ├── 404.webp        # 404 page image
│   │   ├── duck.webp       # Duck illustration
│   │   └── hiw.webp        # "How it works" image
│   ├── components/
│   │   └── ChatInput.svelte # AI chat component
│   ├── layouts/
│   │   └── Layout.astro    # Main layout
│   ├── pages/
│   │   ├── index.astro     # Home page
│   │   ├── 404.astro       # Error page
│   │   └── how-it-works.astro # Explanatory page
│   └── global.css          # Global styles
├── .gitignore bun.lock
├── astro.config.mjs        # Astro configuration
├── bun.lock                # Bun configuration
├── package.json
├── README.md               # Frontend documentation
├── svelte.config.js        # Svelte configuration
└── tsconfig.json           # TypeScript configuration
```

## Installation

### Prerequisites

- [Bun](https://bun.sh/) installed on your machine

### Steps

1. Install dependencies:
```bash
bun install
```

2. Create a `.env` file at the root of the frontend folder:
```bash
PUBLIC_BACKEND_URL=http://localhost:8000
```

3. Start the development server:
```bash
bun run dev
```

The site will be accessible at `http://localhost:4321/`

## Available Commands

| Command | Action |
|----------|--------|
| `bun install` | Installs dependencies |
| `bun run dev` | Starts the development server |

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `PUBLIC_BACKEND_URL` | Backend API URL | `http://localhost:8000` |

## Features

### Interactive AI Chat
The `ChatInput.svelte` component allows you to:
- Send messages to the backend API
- Display AI responses
- Auto-resize textarea
- Support Enter to send (Shift+Enter for new line)

### Easter Egg
Click on the duck to hear a "quack"! 🦆

### Pages
- **Home** (`/`): AI chat interface
- **How it works** (`/how-it-works`): Explanations about eco-friendly operation
- **404**: Custom error page

## Deployment

The frontend is deployed on [Vercel](https://vercel.com/).
Vercel will automatically detect Astro and deploy the site

## Configuration

### Astro

The `astro.config.mjs` file configures:
- Svelte integration
- TailwindCSS via Vite
- Static output mode

### TailwindCSS

Tailwind v4 is integrated via `@tailwindcss/vite` and configured in `global.css`.

## 🤝 Feedback

Feedback are welcome! Feel free to open an [issue](https://github.com/Gautierpicon/Portfolio/issues) or a [pull request](https://github.com/Gautierpicon/Portfolio/pulls) on the GitHub repository.

## 🔗 Useful Links

- [Astro Documentation](https://docs.astro.build)
- [Svelte Documentation](https://svelte.dev/docs)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Backend README](../backend/README.md)