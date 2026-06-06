import React from "react";
import { View, Text, ScrollView, StyleSheet, TouchableOpacity, Linking } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";

const FEATURES = [
  { icon: "search-outline", title: "Skill Matching", desc: "Tell us what you know and we rank every career by match score." },
  { icon: "git-branch-outline", title: "Gap Analysis", desc: "See exactly which skills you need for any career, prioritized by importance." },
  { icon: "school-outline", title: "Learning Resources", desc: "Curated courses, certifications, and free resources for every skill gap." },
  { icon: "star-outline", title: "Community Ratings", desc: "Rate career recommendations and see what others pursuing the same path say." },
  { icon: "trending-up-outline", title: "Growth Outlook", desc: "Each career shows demand outlook so you invest in the right direction." },
  { icon: "phone-portrait-outline", title: "Mobile + Web", desc: "Works seamlessly on your phone and in the browser — one experience everywhere." },
];

export default function AboutScreen() {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.hero}>
        <Text style={styles.logo}>Loka Bandhuv</Text>
        <Text style={styles.tagline}>Your Career Companion</Text>
        <Text style={styles.meaning}>"Friend of the World" — guiding every student, parent, and career shifter</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>What We Do</Text>
        <Text style={styles.body}>
          Loka Bandhuv helps you discover the right career path based on skills you already have,
          then coaches you on exactly what to learn next — with real resources, not vague advice.
        </Text>
        <Text style={styles.body}>
          Whether you're a student choosing your first career, a parent advising your child,
          or a professional ready for a change — we have you covered.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Features</Text>
        {FEATURES.map((f) => (
          <View key={f.title} style={styles.featureRow}>
            <View style={styles.featureIcon}>
              <Ionicons name={f.icon as any} size={22} color={Colors.primary} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.featureTitle}>{f.title}</Text>
              <Text style={styles.featureDesc}>{f.desc}</Text>
            </View>
          </View>
        ))}
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Who It's For</Text>
        {[
          "🎓 Students choosing their first career",
          "👨‍👩‍👧 Parents helping their children decide",
          "🔄 Professionals seeking a career shift",
          "🌍 Anyone wanting to upskill and grow",
        ].map((item) => (
          <Text key={item} style={styles.bullet}>{item}</Text>
        ))}
      </View>

      <View style={[styles.section, styles.versionCard]}>
        <Text style={styles.versionText}>Version 1.0.0</Text>
        <Text style={styles.versionSubtext}>Built with FastAPI + Expo + Claude AI</Text>
      </View>

      <View style={{ height: 40 }} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  hero: {
    backgroundColor: Colors.primary,
    padding: 32,
    alignItems: "center",
  },
  logo: { fontSize: 28, fontWeight: "800", color: "#fff", marginBottom: 4 },
  tagline: { fontSize: 16, color: Colors.primaryLight, marginBottom: 8 },
  meaning: { fontSize: 13, color: "rgba(255,255,255,0.7)", textAlign: "center" },
  section: {
    backgroundColor: Colors.surface,
    marginHorizontal: 16,
    marginTop: 16,
    borderRadius: 16,
    padding: 20,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: "700",
    color: Colors.textPrimary,
    marginBottom: 12,
  },
  body: {
    fontSize: 14,
    color: Colors.textSecondary,
    lineHeight: 22,
    marginBottom: 8,
  },
  featureRow: { flexDirection: "row", gap: 14, marginBottom: 16 },
  featureIcon: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: Colors.primaryLight,
    alignItems: "center",
    justifyContent: "center",
  },
  featureTitle: { fontSize: 14, fontWeight: "700", color: Colors.textPrimary, marginBottom: 2 },
  featureDesc: { fontSize: 13, color: Colors.textSecondary, lineHeight: 18 },
  bullet: { fontSize: 14, color: Colors.textSecondary, marginBottom: 10, lineHeight: 20 },
  versionCard: { alignItems: "center", marginBottom: 0 },
  versionText: { fontSize: 14, fontWeight: "700", color: Colors.textMuted },
  versionSubtext: { fontSize: 12, color: Colors.textMuted, marginTop: 4 },
});
