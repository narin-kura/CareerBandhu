import React, { useState, useCallback } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Alert,
  ActivityIndicator,
  FlatList,
} from "react-native";
import { useRouter } from "expo-router";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";
import { useApi } from "../../hooks/useApi";
import { SkillChip } from "../../components/SkillChip";
import { CareerCard } from "../../components/CareerCard";
import { HeroHeader } from "../../components/HeroHeader";

const POPULAR_SKILLS = [
  "Python", "JavaScript", "SQL", "Excel", "Communication",
  "Project Management", "Leadership", "Data Analysis", "React", "Machine Learning",
  "Digital Marketing", "SEO", "Figma", "Java", "C++",
];

type Recommendation = {
  career: {
    id: string;
    title: string;
    category: string;
    description: string;
    salary_range: { min: number; max: number; currency: string; note: string };
    growth_outlook: string;
    work_style: string[];
    tags: string[];
  };
  score: number;
  matching_skills: { skill: string; level: string }[];
  top_gaps: { skill: string; level: string }[];
};

export default function FindCareerScreen() {
  const router = useRouter();
  const { call, loading } = useApi();

  const [inputText, setInputText] = useState("");
  const [selectedSkills, setSelectedSkills] = useState<string[]>([]);
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [hasSearched, setHasSearched] = useState(false);

  const addSkill = useCallback(
    (skill: string) => {
      const trimmed = skill.trim();
      if (!trimmed || selectedSkills.includes(trimmed)) return;
      setSelectedSkills((prev) => [...prev, trimmed]);
      setInputText("");
    },
    [selectedSkills]
  );

  const removeSkill = useCallback((skill: string) => {
    setSelectedSkills((prev) => prev.filter((s) => s !== skill));
  }, []);

  const handleSearch = useCallback(async () => {
    if (inputText.trim()) addSkill(inputText);
    const skills = inputText.trim()
      ? [...selectedSkills, inputText.trim()]
      : selectedSkills;

    if (skills.length === 0) {
      Alert.alert("Add skills", "Please add at least one skill to get recommendations.");
      return;
    }

    const data = await call<{ recommendations: Recommendation[] }>(
      "/api/recommend",
      {
        method: "POST",
        body: JSON.stringify({ skills }),
      }
    );

    if (data) {
      setRecommendations(data.recommendations);
      setHasSearched(true);
    }
  }, [call, inputText, selectedSkills, addSkill]);

  return (
    <ScrollView style={styles.container} keyboardShouldPersistTaps="handled">
      {!hasSearched && <HeroHeader />}

      {/* Skill Input Card */}
      <View style={styles.card}>
        <Text style={styles.sectionTitle}>
          {hasSearched ? "Your Skills" : "What skills do you have?"}
        </Text>
        <Text style={styles.sectionSubtitle}>
          Add your current skills and we'll find the best career matches
        </Text>

        <View style={styles.inputRow}>
          <TextInput
            style={styles.input}
            placeholder="Type a skill (e.g. Python, Excel)"
            placeholderTextColor={Colors.textMuted}
            value={inputText}
            onChangeText={setInputText}
            onSubmitEditing={() => addSkill(inputText)}
            returnKeyType="done"
          />
          <TouchableOpacity style={styles.addBtn} onPress={() => addSkill(inputText)}>
            <Ionicons name="add" size={22} color="#fff" />
          </TouchableOpacity>
        </View>

        {/* Selected skills */}
        {selectedSkills.length > 0 && (
          <View style={styles.chipRow}>
            {selectedSkills.map((s) => (
              <SkillChip key={s} skill={s} onRemove={() => removeSkill(s)} selected />
            ))}
          </View>
        )}

        {/* Popular skill suggestions */}
        {selectedSkills.length < 3 && (
          <>
            <Text style={styles.suggestLabel}>Popular skills</Text>
            <View style={styles.chipRow}>
              {POPULAR_SKILLS.filter((s) => !selectedSkills.includes(s))
                .slice(0, 10)
                .map((s) => (
                  <SkillChip key={s} skill={s} onPress={() => addSkill(s)} />
                ))}
            </View>
          </>
        )}

        <TouchableOpacity
          style={[styles.searchBtn, loading && styles.searchBtnDisabled]}
          onPress={handleSearch}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#fff" />
          ) : (
            <>
              <Ionicons name="rocket-outline" size={18} color="#fff" />
              <Text style={styles.searchBtnText}>
                {hasSearched ? "Update Results" : "Find My Career Path"}
              </Text>
            </>
          )}
        </TouchableOpacity>
      </View>

      {/* Results */}
      {hasSearched && recommendations.length === 0 && !loading && (
        <View style={styles.emptyState}>
          <Ionicons name="search-outline" size={48} color={Colors.textMuted} />
          <Text style={styles.emptyTitle}>No matches found</Text>
          <Text style={styles.emptyText}>
            Try adding more varied skills — technical, business, or creative.
          </Text>
        </View>
      )}

      {recommendations.length > 0 && (
        <View style={styles.resultsSection}>
          <Text style={styles.resultsTitle}>
            Top {recommendations.length} Career Matches
          </Text>
          {recommendations.map((rec, i) => (
            <CareerCard
              key={rec.career.id}
              rank={i + 1}
              career={rec.career}
              score={rec.score}
              matchingSkills={rec.matching_skills}
              topGaps={rec.top_gaps}
              onPress={() =>
                router.push({
                  pathname: "/career/[id]",
                  params: {
                    id: rec.career.id,
                    skills: JSON.stringify(selectedSkills),
                  },
                })
              }
            />
          ))}
        </View>
      )}

      <View style={{ height: 32 }} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  card: {
    backgroundColor: Colors.surface,
    marginHorizontal: 16,
    marginTop: 16,
    borderRadius: 16,
    padding: 20,
    shadowColor: "#000",
    shadowOpacity: 0.06,
    shadowRadius: 8,
    shadowOffset: { width: 0, height: 2 },
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "700",
    color: Colors.textPrimary,
    marginBottom: 4,
  },
  sectionSubtitle: {
    fontSize: 13,
    color: Colors.textSecondary,
    marginBottom: 16,
  },
  inputRow: { flexDirection: "row", gap: 8, marginBottom: 12 },
  input: {
    flex: 1,
    borderWidth: 1.5,
    borderColor: Colors.border,
    borderRadius: 10,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14,
    color: Colors.textPrimary,
    backgroundColor: Colors.background,
  },
  addBtn: {
    backgroundColor: Colors.primary,
    borderRadius: 10,
    width: 44,
    alignItems: "center",
    justifyContent: "center",
  },
  chipRow: { flexDirection: "row", flexWrap: "wrap", gap: 8, marginBottom: 12 },
  suggestLabel: {
    fontSize: 12,
    color: Colors.textMuted,
    marginBottom: 8,
    fontWeight: "600",
    textTransform: "uppercase",
    letterSpacing: 0.5,
  },
  searchBtn: {
    backgroundColor: Colors.primary,
    borderRadius: 12,
    paddingVertical: 14,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    marginTop: 8,
  },
  searchBtnDisabled: { opacity: 0.7 },
  searchBtnText: { color: "#fff", fontSize: 16, fontWeight: "700" },
  resultsSection: { marginHorizontal: 16, marginTop: 24 },
  resultsTitle: {
    fontSize: 18,
    fontWeight: "700",
    color: Colors.textPrimary,
    marginBottom: 12,
  },
  emptyState: {
    alignItems: "center",
    padding: 40,
    marginTop: 16,
  },
  emptyTitle: {
    fontSize: 18,
    fontWeight: "700",
    color: Colors.textSecondary,
    marginTop: 12,
    marginBottom: 8,
  },
  emptyText: { fontSize: 14, color: Colors.textMuted, textAlign: "center" },
});
