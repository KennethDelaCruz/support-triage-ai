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

- Uses Vercel's modern configuration (no deprecated `builds` property)
- Configures Next.js build commands for the `frontend/` subdirectory
- Python API in `api/` directory is auto-detected by Vercel
- Python API routes are automatically available at `/api/*`

### `runtime.txt`

- Specifies Python version (3.12) for Vercel's Python runtime
- Prevents the "No Python version specified" warning

### `api/index.py`

- Entry point for Vercel's Python serverless functions
- Imports and exports the FastAPI application from `backend/app/main.py`
- Automatically detected by Vercel (no explicit configuration needed)

### `requirements.txt`

- Python dependencies required for the API
- Must be in the project root directory
- Vercel automatically installs these during build

## Post-Deployment

### 1. Update CORS Settings (Optional)

The CORS configuration in `backend/app/main.py` already supports all Vercel deployments automatically via regex pattern. If you need to add specific origins, you can set the `VERCEL_ORIGINS` environment variable (comma-separated list).

The current configuration automatically allows:

- All `*.vercel.app` domains (preview and production deployments)
- Local development origins (localhost:3000, localhost:5173)
- Any origins specified in the `VERCEL_ORIGINS` environment variable

### 2. Test the Deployment

- Frontend: `https://your-project.vercel.app`
- API Health: `https://your-project.vercel.app/api/health`
- API Docs: `https://your-project.vercel.app/api/docs`
- Triage Endpoint: `https://your-project.vercel.app/api/triage`

## Troubleshooting

### Python Dependencies Not Installing

- Ensure `requirements.txt` is in the project root
- Check build logs in Vercel dashboard for specific errors

### API Routes Not Working / 500 Internal Server Error

- Verify `api/index.py` exists and properly exports the FastAPI app
- Vercel auto-detects serverless functions in `api/` directory - no explicit routing needed
- Ensure Python version is specified in `runtime.txt` (not in `vercel.json`)
- Check that routes are accessible at `/api/health` and `/api/triage`
- **If you see `FUNCTION_INVOCATION_FAILED` or 500 errors:**
  - Check Vercel function logs in the dashboard for detailed error messages
  - Verify that the `backend/` directory and all its files are included in the deployment
  - Ensure `requirements.txt` is in the project root and includes all dependencies
  - The `api/index.py` file includes error handling that will print detailed debug info to logs
  - Common issues:
    - Missing `__init__.py` files in `backend/app/` or `backend/app/services/`
    - Import path resolution issues (check logs for Python path information)
    - Missing environment variables (check that `HF_TOKEN` is set if using AI features)

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
