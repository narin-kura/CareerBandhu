import { Colors } from "./Colors";

/**
 * Shared display helpers for career metadata.
 *
 * growth_outlook in careers.json is free text, e.g.
 *   "Very strong - Houdini FX artists are scarce worldwide"
 *   "Stable - every company has one"
 * Badges only have room for the headline, so we split on the first
 * " - " / em-dash and colour by the strength word.
 */

export function shortOutlook(text?: string | null): string {
  if (!text) return "";
  const head = text.split(/\s[-–—]\s/)[0].trim();
  return head.length > 24 ? head.slice(0, 22).trimEnd() + "…" : head;
}

export function outlookColor(text?: string | null): string {
  const t = (text ?? "").toLowerCase();
  if (/very (strong|high)|booming|explosive/.test(t)) return Colors.success;
  if (/\b(strong|high)\b/.test(t)) return Colors.secondary;
  if (/growing|good|emerging|expanding/.test(t)) return Colors.warning;
  if (/stable|steady|moderate|niche/.test(t)) return Colors.textSecondary;
  return Colors.textMuted;
}

/** Mirrors COLLAR_META on the web app - keep the two in sync. */
export const COLLAR_LABEL: Record<string, string> = {
  white: "White-collar",
  blue: "Blue-collar",
  pink: "Service & care",
  gray: "Gray-collar (technical)",
  gold: "Gold-collar (specialist)",
  new: "New-collar (skills-first)",
  green: "Green job",
  red: "Government",
  brown: "Agriculture & field",
  no: "No-collar (creative / passion)",
  open: "Open-collar (remote / freelance)",
};

export const COLLAR_FILTERS: { key: string; label: string }[] = [
  { key: "all", label: "All types" },
  { key: "white", label: "White-collar" },
  { key: "blue", label: "Blue-collar" },
  { key: "pink", label: "Service" },
  { key: "gray", label: "Technical" },
  { key: "gold", label: "Specialist" },
  { key: "new", label: "Skills-first" },
  { key: "green", label: "Green" },
  { key: "red", label: "Government" },
  { key: "brown", label: "Field" },
  { key: "no", label: "Creative" },
  { key: "open", label: "Remote" },
];

/**
 * salary_range.currency in careers.json is one of "USD", "INR", "USD/year" or
 * "INR/month". Plain values are yearly. Rupee yearly figures read as lakhs.
 */
export function formatSalary(s?: { min: number; max: number; currency?: string } | null): string | null {
  if (!s) return null;
  const currency = s.currency ?? "";
  const isInr = currency.startsWith("INR");
  const monthly = currency.includes("month");
  const symbol = isInr ? "₹" : currency.startsWith("USD") ? "$" : "";
  const short = (n: number) => {
    if (isInr && n >= 100000) return `${Number((n / 100000).toFixed(1))}L`;
    if (n >= 1000) return `${Math.round(n / 1000)}k`;
    return String(n);
  };
  return `${symbol}${short(s.min)}–${symbol}${short(s.max)}${monthly ? "/mo" : "/yr"}`;
}
