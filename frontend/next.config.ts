import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Vercel will handle /api/* routes via serverless functions
  // No rewrites needed - Vercel auto-routes to api/ directory
};

export default nextConfig;
