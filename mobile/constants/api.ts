import Constants from "expo-constants";

// In development, point to local backend.
// In production builds, set EXPO_PUBLIC_API_URL in your environment.
export const API_BASE =
  process.env.EXPO_PUBLIC_API_URL ??
  (Constants.expoConfig?.extra?.apiUrl as string) ??
  "http://localhost:8000";
