# Support Triage AI - Frontend

This is the Next.js frontend application for the Support Triage AI system.

## Tech Stack

- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **React 19** - UI library
- **Tailwind CSS** - Utility-first CSS framework

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Backend API running on `http://localhost:8000` (or configure `NEXT_PUBLIC_API_URL`)

### Installation

```bash
npm install
```

### Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

If not set, it defaults to `http://localhost:8000`.

### Development

Run the development server:

```bash
npm run dev
```

Or from the project root:

```bash
npm run frontend
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

Build for production:

```bash
npm run build
```

Start production server:

```bash
npm start
```

## Project Structure

```
frontend/
├── app/              # Next.js App Router pages
│   ├── layout.tsx   # Root layout
│   └── page.tsx     # Home page
├── components/       # React components
│   ├── TriageForm.tsx    # Form for submitting tickets
│   └── TriageResult.tsx  # Component for displaying results
├── lib/             # Utility functions
│   └── api.ts       # API client functions
└── types/           # TypeScript type definitions
    └── triage.ts    # Types matching backend schemas
```

## Features

- **Ticket Triage Form**: Submit support ticket text for analysis
- **AI-Powered Analysis**: Get intent classification, urgency level, and recommended next steps
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Mode Support**: Automatic dark mode based on system preferences
