import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../constants/Colors";

export function HeroHeader() {
  return (
    <View style={styles.hero}>
      <View style={styles.logoRow}>
        <Ionicons name="globe-outline" size={32} color="#fff" />
        <Text style={styles.logoText}>Loka Bandhuv</Text>
      </View>
      <Text style={styles.tagline}>Your Career Companion</Text>
      <Text style={styles.subtitle}>
        Discover the right career for your skills. Get a personalized learning path and bridge every skill gap.
      </Text>
      <View style={styles.statsRow}>
        {[
          { n: "35+", label: "Careers" },
          { n: "200+", label: "Skills" },
          { n: "AI", label: "Powered" },
        ].map((s) => (
          <View key={s.label} style={styles.stat}>
            <Text style={styles.statNum}>{s.n}</Text>
            <Text style={styles.statLabel}>{s.label}</Text>
          </View>
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  hero: {
    backgroundColor: Colors.primary,
    padding: 28,
    paddingBottom: 32,
  },
  logoRow: { flexDirection: "row", alignItems: "center", gap: 10, marginBottom: 8 },
  logoText: { fontSize: 22, fontWeight: "800", color: "#fff" },
  tagline: { fontSize: 14, color: Colors.primaryLight, marginBottom: 8, fontWeight: "600" },
  subtitle: { fontSize: 13, color: "rgba(255,255,255,0.8)", lineHeight: 20, marginBottom: 20 },
  statsRow: { flexDirection: "row", gap: 24 },
  stat: { alignItems: "center" },
  statNum: { fontSize: 22, fontWeight: "800", color: "#fff" },
  statLabel: { fontSize: 11, color: Colors.primaryLight, fontWeight: "600" },
});
