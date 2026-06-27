import Constants from "expo-constants";

// Resolution order:
//   1. EXPO_PUBLIC_API_URL  — set at build time (e.g. in eas.json env)
//   2. app.json > expo.extra.apiUrl  — the CareerBandhu Cloud Run URL
//   3. localhost  — local dev fallback
// Production points at GCP Cloud Run (not the HF Space).
export const API_BASE =
  process.env.EXPO_PUBLIC_API_URL ??
  (Constants.expoConfig?.extra?.apiUrl as string) ??
  "http://localhost:8000";
