"use client";

import { useState } from "react";
import { TriageRequest, TriageResponse } from "@/types/triage";
import { triageTicket } from "@/lib/api";
import { TriageResult } from "./TriageResult";

export function TriageForm() {
  const [ticketText, setTicketText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<TriageResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!ticketText.trim()) {
      setError("Please enter ticket text");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const request: TriageRequest = { ticketText };
      const response = await triageTicket(request);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto">
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label
            htmlFor="ticket-text"
            className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
          >
            Support Ticket Text
          </label>
          <textarea
            id="ticket-text"
            value={ticketText}
            onChange={(e) => setTicketText(e.target.value)}
            placeholder="Enter the support ticket content here..."
            rows={8}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white dark:placeholder-gray-400 resize-none"
            disabled={loading}
          />
        </div>

        <button
          type="submit"
          disabled={loading || !ticketText.trim()}
          className="w-full px-6 py-3 bg-blue-600 text-white font-medium rounded-lg shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {loading ? "Triaging..." : "Triage Ticket"}
        </button>
      </form>

      {error && (
        <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg dark:bg-red-900/20 dark:border-red-800">
          <p className="text-sm text-red-800 dark:text-red-200">{error}</p>
        </div>
      )}

      {result && <TriageResult result={result} />}
    </div>
  );
}
