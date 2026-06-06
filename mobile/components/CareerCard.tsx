import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../constants/Colors";

type Skill = { skill: string; level: string };
type Career = {
  id: string;
  title: string;
  category: string;
  description: string;
  salary_range?: { min: number; max: number; currency: string; note: string };
  growth_outlook: string;
  work_style: string[];
  tags: string[];
};

type Props = {
  rank: number;
  career: Career;
  score: number;
  matchingSkills: Skill[];
  topGaps: Skill[];
  onPress: () => void;
};

const SCORE_COLOR = (s: number) =>
  s >= 70 ? Colors.success : s >= 40 ? Colors.warning : Colors.danger;

const OUTLOOK_ICON: Record<string, string> = {
  "Very High": "trending-up",
  High: "trending-up",
  Good: "remove",
  Stable: "remove",
  Moderate: "trending-down",
};

export function CareerCard({ rank, career, score, matchingSkills, topGaps, onPress }: Props) {
  const color = SCORE_COLOR(score);

  return (
    <TouchableOpacity style={styles.card} onPress={onPress} activeOpacity={0.85}>
      {/* Rank + title row */}
      <View style={styles.headerRow}>
        <View style={[styles.rankBadge, { backgroundColor: color + "20" }]}>
          <Text style={[styles.rankText, { color }]}>#{rank}</Text>
        </View>
        <View style={{ flex: 1 }}>
          <Text style={styles.title}>{career.title}</Text>
          <Text style={styles.category}>{career.category}</Text>
        </View>
        <View style={[styles.scorePill, { backgroundColor: color }]}>
          <Text style={styles.scoreText}>{score}%</Text>
        </View>
      </View>

      {/* Description */}
      <Text style={styles.description} numberOfLines={2}>
        {career.description}
      </Text>

      {/* Score bar */}
      <View style={styles.barBg}>
        <View style={[styles.barFill, { width: `${score}%` as any, backgroundColor: color }]} />
      </View>

      {/* Skills preview */}
      <View style={styles.skillsRow}>
        {matchingSkills.slice(0, 3).map((s) => (
          <View key={s.skill} style={styles.haveChip}>
            <Text style={styles.haveChipText}>✓ {s.skill}</Text>
          </View>
        ))}
        {topGaps.slice(0, 2).map((s) => (
          <View key={s.skill} style={styles.needChip}>
            <Text style={styles.needChipText}>+ {s.skill}</Text>
          </View>
        ))}
      </View>

      {/* Footer */}
      <View style={styles.footer}>
        <View style={styles.footerMeta}>
          {career.salary_range && (
            <Text style={styles.salary}>
              💰 {career.salary_range.currency}
              {(career.salary_range.min / 1000).toFixed(0)}k–
              {(career.salary_range.max / 1000).toFixed(0)}k
            </Text>
          )}
          <Text style={styles.outlook}>📈 {career.growth_outlook}</Text>
        </View>
        <View style={styles.exploreBtn}>
          <Text style={styles.exploreBtnText}>Explore</Text>
          <Ionicons name="arrow-forward" size={14} color={Colors.primary} />
        </View>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: Colors.surface,
    borderRadius: 16,
    padding: 16,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: Colors.border,
    shadowColor: "#000",
    shadowOpacity: 0.05,
    shadowRadius: 6,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  headerRow: { flexDirection: "row", alignItems: "center", gap: 10, marginBottom: 10 },
  rankBadge: { width: 32, height: 32, borderRadius: 8, alignItems: "center", justifyContent: "center" },
  rankText: { fontSize: 12, fontWeight: "800" },
  title: { fontSize: 15, fontWeight: "700", color: Colors.textPrimary },
  category: { fontSize: 11, color: Colors.textMuted, marginTop: 1 },
  scorePill: { borderRadius: 20, paddingHorizontal: 10, paddingVertical: 4 },
  scoreText: { color: "#fff", fontSize: 13, fontWeight: "800" },
  description: { fontSize: 13, color: Colors.textSecondary, lineHeight: 19, marginBottom: 10 },
  barBg: { height: 6, backgroundColor: Colors.border, borderRadius: 3, marginBottom: 12, overflow: "hidden" },
  barFill: { height: "100%", borderRadius: 3 },
  skillsRow: { flexDirection: "row", flexWrap: "wrap", gap: 6, marginBottom: 12 },
  haveChip: {
    backgroundColor: Colors.successLight,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  haveChipText: { fontSize: 11, color: "#166534", fontWeight: "600" },
  needChip: {
    backgroundColor: Colors.warningLight,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  needChipText: { fontSize: 11, color: "#92400e", fontWeight: "600" },
  footer: { flexDirection: "row", alignItems: "center", justifyContent: "space-between" },
  footerMeta: { flexDirection: "row", gap: 12 },
  salary: { fontSize: 12, color: Colors.textSecondary },
  outlook: { fontSize: 12, color: Colors.textSecondary },
  exploreBtn: { flexDirection: "row", alignItems: "center", gap: 4 },
  exploreBtnText: { fontSize: 13, fontWeight: "700", color: Colors.primary },
});
