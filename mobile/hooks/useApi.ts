import { useState, useCallback } from "react";
import { API_BASE } from "../constants/api";

// Cloud Run scales to zero; the first request after idle can take ~10-20s.
// Without a timeout a hung request leaves the UI spinning forever (the same
// bug the web app fixed with fetchJSON + AbortController).
const TIMEOUT_MS = 35000;

export function describeError(e: unknown): string {
  const msg = e instanceof Error ? e.message : String(e ?? "");
  if (msg === "AbortError" || /abort/i.test(msg)) {
    return "The server is taking too long to respond. It may be waking up - please try again.";
  }
  if (/network request failed|failed to fetch|network error/i.test(msg)) {
    return "Could not reach the server. Check your internet connection and try again.";
  }
  if (/HTTP 5\d\d/.test(msg)) {
    return "The server is temporarily unavailable. Please try again in a moment.";
  }
  return msg || "Something went wrong. Please try again.";
}

export function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const call = useCallback(
    async <T,>(endpoint: string, options?: RequestInit): Promise<T | null> => {
      setLoading(true);
      setError(null);
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
      try {
        const res = await fetch(`${API_BASE}${endpoint}`, {
          headers: { "Content-Type": "application/json" },
          signal: controller.signal,
          ...options,
        });
        if (!res.ok) {
          const body = await res.json().catch(() => ({}));
          throw new Error(body.detail ?? `HTTP ${res.status}`);
        }
        return (await res.json()) as T;
      } catch (e: unknown) {
        const name = (e as { name?: string })?.name;
        setError(describeError(name === "AbortError" ? new Error("AbortError") : e));
        return null;
      } finally {
        clearTimeout(timer);
        setLoading(false);
      }
    },
    []
  );

  return { call, loading, error, clearError: () => setError(null) };
}
