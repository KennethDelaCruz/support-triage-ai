"use client";

import { TriageResponse } from "@/types/triage";

interface TriageResultProps {
  result: TriageResponse;
}

const urgencyColors: Record<string, string> = {
  P0: "bg-red-100 text-red-800 border-red-300 dark:bg-red-900/20 dark:text-red-300 dark:border-red-800",
  P1: "bg-orange-100 text-orange-800 border-orange-300 dark:bg-orange-900/20 dark:text-orange-300 dark:border-orange-800",
  P2: "bg-yellow-100 text-yellow-800 border-yellow-300 dark:bg-yellow-900/20 dark:text-yellow-300 dark:border-yellow-800",
  P3: "bg-green-100 text-green-800 border-green-300 dark:bg-green-900/20 dark:text-green-300 dark:border-green-800",
};

const intentColors: Record<string, string> = {
  billing_refund:
    "bg-purple-100 text-purple-800 dark:bg-purple-900/20 dark:text-purple-300",
  auth_sso_issue:
    "bg-blue-100 text-blue-800 dark:bg-blue-900/20 dark:text-blue-300",
  performance_outage:
    "bg-red-100 text-red-800 dark:bg-red-900/20 dark:text-red-300",
  how_to_question:
    "bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-300",
};

export function TriageResult({ result }: TriageResultProps) {
  const urgencyColor = urgencyColors[result.urgency] || urgencyColors.P3;
  const intentColor =
    intentColors[result.intent] ||
    "bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-300";

  return (
    <div className="mt-8 space-y-6">
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 p-6">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          Triage Results
        </h2>

        <div className="space-y-4">
          {/* Summary */}
          <div>
            <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase tracking-wide mb-2">
              Summary
            </h3>
            <p className="text-gray-900 dark:text-gray-100">{result.summary}</p>
          </div>

          {/* Intent and Urgency */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase tracking-wide mb-2">
                Intent
              </h3>
              <span
                className={`inline-block px-3 py-1 rounded-md text-sm font-medium border ${intentColor}`}
              >
                {result.intent
                  .replace(/_/g, " ")
                  .replace(/\b\w/g, (l) => l.toUpperCase())}
              </span>
            </div>
            <div>
              <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase tracking-wide mb-2">
                Urgency
              </h3>
              <span
                className={`inline-block px-3 py-1 rounded-md text-sm font-medium border ${urgencyColor}`}
              >
                {result.urgency}
              </span>
            </div>
          </div>

          {/* Next Step */}
          <div>
            <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase tracking-wide mb-2">
              Recommended Next Step
            </h3>
            <p className="text-gray-900 dark:text-gray-100 bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg border border-blue-200 dark:border-blue-800">
              {result.nextStep}
            </p>
          </div>

          {/* Metadata */}
          <div className="pt-4 border-t border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase tracking-wide mb-3">
              Metadata
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              <div>
                <span className="text-gray-600 dark:text-gray-400">Model:</span>{" "}
                <span className="font-medium text-gray-900 dark:text-gray-100">
                  {result.meta.model}
                </span>
              </div>
              <div>
                <span className="text-gray-600 dark:text-gray-400">
                  Confidence:
                </span>{" "}
                <span className="font-medium text-gray-900 dark:text-gray-100">
                  {(result.meta.confidence * 100).toFixed(0)}%
                </span>
              </div>
              <div>
                <span className="text-gray-600 dark:text-gray-400">
                  Fallback Used:
                </span>{" "}
                <span className="font-medium text-gray-900 dark:text-gray-100">
                  {result.meta.fallbackUsed ? "Yes" : "No"}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
