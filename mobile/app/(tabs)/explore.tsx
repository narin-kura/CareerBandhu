import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  TextInput,
  ActivityIndicator,
} from "react-native";
import { useRouter } from "expo-router";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";
import { useApi } from "../../hooks/useApi";

type CareerSummary = {
  id: string;
  title: string;
  category: string;
  growth_outlook: string;
  tags: string[];
};

const CATEGORIES = [
  "All", "Technology", "Data & Analytics", "Business & Management",
  "Finance", "Marketing & Sales", "Design & Creative",
  "Education & Training", "Human Resources", "Healthcare",
];

const OUTLOOK_COLOR: Record<string, string> = {
  "Very High": Colors.success,
  High: Colors.secondary,
  Good: Colors.warning,
  Stable: Colors.textSecondary,
  Moderate: Colors.textMuted,
};

export default function ExploreScreen() {
  const router = useRouter();
  const { call, loading } = useApi();
  const [careers, setCareers] = useState<CareerSummary[]>([]);
  const [filtered, setFiltered] = useState<CareerSummary[]>([]);
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("All");

  useEffect(() => {
    call<{ careers: CareerSummary[] }>("/api/careers").then((data) => {
      if (data) {
        setCareers(data.careers);
        setFiltered(data.careers);
      }
    });
  }, []);

  useEffect(() => {
    let result = careers;
    if (activeCategory !== "All") {
      result = result.filter((c) => c.category === activeCategory);
    }
    if (query.trim()) {
      const q = query.toLowerCase();
      result = result.filter(
        (c) =>
          c.title.toLowerCase().includes(q) ||
          c.category.toLowerCase().includes(q) ||
          c.tags.some((t) => t.toLowerCase().includes(q))
      );
    }
    setFiltered(result);
  }, [query, activeCategory, careers]);

  const renderCareer = ({ item }: { item: CareerSummary }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() =>
        router.push({ pathname: "/career/[id]", params: { id: item.id } })
      }
    >
      <View style={styles.cardTop}>
        <View style={{ flex: 1 }}>
          <Text style={styles.careerTitle}>{item.title}</Text>
          <Text style={styles.category}>{item.category}</Text>
        </View>
        <View style={[styles.outlookBadge, { backgroundColor: (OUTLOOK_COLOR[item.growth_outlook] ?? Colors.textMuted) + "20" }]}>
          <Text style={[styles.outlookText, { color: OUTLOOK_COLOR[item.growth_outlook] ?? Colors.textMuted }]}>
            {item.growth_outlook}
          </Text>
        </View>
      </View>
      <View style={styles.tagRow}>
        {item.tags.slice(0, 4).map((tag) => (
          <View key={tag} style={styles.tag}>
            <Text style={styles.tagText}>{tag}</Text>
          </View>
        ))}
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      {/* Search bar */}
      <View style={styles.searchBar}>
        <Ionicons name="search-outline" size={18} color={Colors.textMuted} />
        <TextInput
          style={styles.searchInput}
          placeholder="Search careers, categories, tags..."
          placeholderTextColor={Colors.textMuted}
          value={query}
          onChangeText={setQuery}
        />
        {query.length > 0 && (
          <TouchableOpacity onPress={() => setQuery("")}>
            <Ionicons name="close-circle" size={18} color={Colors.textMuted} />
          </TouchableOpacity>
        )}
      </View>

      {/* Category filter */}
      <FlatList
        horizontal
        data={CATEGORIES}
        keyExtractor={(c) => c}
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.categoryList}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={[
              styles.categoryPill,
              activeCategory === item && styles.categoryPillActive,
            ]}
            onPress={() => setActiveCategory(item)}
          >
            <Text
              style={[
                styles.categoryPillText,
                activeCategory === item && styles.categoryPillTextActive,
              ]}
            >
              {item}
            </Text>
          </TouchableOpacity>
        )}
      />

      {loading ? (
        <ActivityIndicator style={{ marginTop: 40 }} color={Colors.primary} size="large" />
      ) : (
        <FlatList
          data={filtered}
          keyExtractor={(c) => c.id}
          renderItem={renderCareer}
          contentContainerStyle={styles.list}
          ListEmptyComponent={
            <View style={styles.empty}>
              <Ionicons name="compass-outline" size={48} color={Colors.textMuted} />
              <Text style={styles.emptyText}>No careers match your search</Text>
            </View>
          }
          ListHeaderComponent={
            <Text style={styles.resultCount}>
              {filtered.length} career{filtered.length !== 1 ? "s" : ""}
            </Text>
          }
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  searchBar: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: Colors.surface,
    margin: 16,
    marginBottom: 8,
    borderRadius: 12,
    paddingHorizontal: 14,
    paddingVertical: 10,
    gap: 8,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  searchInput: { flex: 1, fontSize: 14, color: Colors.textPrimary },
  categoryList: { paddingHorizontal: 16, paddingBottom: 8, gap: 8 },
  categoryPill: {
    borderRadius: 20,
    paddingHorizontal: 14,
    paddingVertical: 7,
    backgroundColor: Colors.surface,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  categoryPillActive: {
    backgroundColor: Colors.primary,
    borderColor: Colors.primary,
  },
  categoryPillText: { fontSize: 13, color: Colors.textSecondary, fontWeight: "500" },
  categoryPillTextActive: { color: "#fff" },
  list: { paddingHorizontal: 16, paddingBottom: 32 },
  resultCount: {
    fontSize: 12,
    color: Colors.textMuted,
    fontWeight: "600",
    textTransform: "uppercase",
    marginBottom: 12,
    letterSpacing: 0.5,
  },
  card: {
    backgroundColor: Colors.surface,
    borderRadius: 14,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  cardTop: { flexDirection: "row", alignItems: "flex-start", gap: 12 },
  careerTitle: { fontSize: 15, fontWeight: "700", color: Colors.textPrimary, marginBottom: 2 },
  category: { fontSize: 12, color: Colors.textSecondary },
  outlookBadge: { borderRadius: 8, paddingHorizontal: 10, paddingVertical: 4 },
  outlookText: { fontSize: 11, fontWeight: "700" },
  tagRow: { flexDirection: "row", flexWrap: "wrap", gap: 6, marginTop: 10 },
  tag: {
    backgroundColor: Colors.primaryLight,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  tagText: { fontSize: 11, color: Colors.primaryDark, fontWeight: "500" },
  empty: { alignItems: "center", padding: 40 },
  emptyText: { fontSize: 14, color: Colors.textMuted, marginTop: 12 },
});
