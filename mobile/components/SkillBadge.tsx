import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { Colors } from "../constants/Colors";

type Props = {
  skill: string;
  type: "have" | "need" | "neutral";
  level: string;
};

const BG: Record<string, string> = {
  have: Colors.successLight,
  need: Colors.dangerLight,
  neutral: Colors.primaryLight,
};

const FG: Record<string, string> = {
  have: "#166534",
  need: "#991b1b",
  neutral: Colors.primaryDark,
};

export function SkillBadge({ skill, type, level }: Props) {
  return (
    <View style={[styles.badge, { backgroundColor: BG[type] }]}>
      <Text style={[styles.text, { color: FG[type] }]}>{skill}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: {
    borderRadius: 8,
    paddingHorizontal: 10,
    paddingVertical: 5,
  },
  text: { fontSize: 12, fontWeight: "600" },
});
