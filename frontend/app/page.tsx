import { TriageForm } from "@/components/TriageForm";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      <main className="container mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
            Support Ticket Triage AI
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
            Automatically analyze and triage support tickets with AI-powered
            intent detection, urgency assessment, and recommended next steps.
          </p>
        </div>

        <TriageForm />
      </main>
    </div>
  );
}
