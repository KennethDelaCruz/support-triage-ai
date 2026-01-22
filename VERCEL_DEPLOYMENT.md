# Vercel Deployment Guide

This guide will help you deploy the Support Triage AI project to Vercel.

## Project Structure

This project consists of:
- **Frontend**: Next.js application in `frontend/` directory
- **Backend API**: FastAPI application in `backend/app/` directory
- **API Entry Point**: `api/index.py` (Vercel serverless function)

## Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com))
2. Vercel CLI installed: `npm i -g vercel` or `pnpm add -g vercel`

## Environment Variables

Set the following environment variables in Vercel (Project Settings → Environment Variables):

### Required
- `HF_TOKEN`: Your Hugging Face API token for AI model inference

### Optional (with defaults)
- `HF_MODEL`: Hugging Face model to use (default: `meta-llama/Meta-Llama-3-8B-Instruct`)
- `HF_BASE_URL`: Hugging Face API base URL (default: `https://router.huggingface.co/v1`)
- `HF_TIMEOUT_SECONDS`: Timeout for API requests in seconds (default: `25`)

### Setting Environment Variables

**Via Vercel Dashboard:**
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add each variable for Production, Preview, and Development environments

**Via Vercel CLI:**
```bash
vercel env add HF_TOKEN
vercel env add HF_MODEL
vercel env add HF_BASE_URL
vercel env add HF_TIMEOUT_SECONDS
```

## Deployment Steps

### 1. Initial Deployment

From the project root:

```bash
vercel
```

Follow the prompts to:
- Link to an existing project or create a new one
- Configure project settings

### 2. Production Deployment

```bash
vercel --prod
```

## Configuration Files

### `vercel.json`
- Configures both Next.js frontend and Python API
- Python API routes are available at `/api/*`
- Frontend routes are handled by Next.js

### `api/index.py`
- Entry point for Vercel's Python serverless functions
- Imports and exports the FastAPI application from `backend/app/main.py`

### `requirements.txt`
- Python dependencies required for the API
- Vercel automatically installs these during build

## Post-Deployment

### 1. Update CORS Settings

After deployment, update the CORS origins in `backend/app/main.py` to include your Vercel frontend URL:

```python
allow_origins=[
    "http://localhost:3000",
    "http://localhost:5173",
    "https://your-project.vercel.app",  # Add your Vercel URL
]
```

### 2. Test the Deployment

- Frontend: `https://your-project.vercel.app`
- API Health: `https://your-project.vercel.app/api/health`
- API Docs: `https://your-project.vercel.app/api/docs`
- Triage Endpoint: `https://your-project.vercel.app/api/triage`

## Troubleshooting

### Python Dependencies Not Installing
- Ensure `requirements.txt` is in the project root
- Check build logs in Vercel dashboard for specific errors

### API Routes Not Working
- Verify `api/index.py` exists and properly exports the FastAPI app
- Check that `vercel.json` routes are correctly configured
- Ensure Python version is set to 3.12 in `vercel.json`

### Environment Variables Not Loading
- Verify variables are set for the correct environment (Production/Preview/Development)
- Redeploy after adding new environment variables
- Check variable names match exactly (case-sensitive)

### Frontend Not Building
- Ensure `frontend/package.json` exists
- Check that Next.js is properly configured
- Review build logs in Vercel dashboard

## Monorepo Configuration

If deploying from a monorepo, you may need to configure the root directory in Vercel:
- Go to Project Settings → General
- Set "Root Directory" if needed
- Or use `vercel.json` to specify build settings

## Additional Resources

- [Vercel Python Documentation](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Vercel Next.js Documentation](https://vercel.com/docs/frameworks/nextjs)
- [FastAPI on Vercel](https://vercel.com/guides/deploying-fastapi-with-vercel)

