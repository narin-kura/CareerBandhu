import React, { useEffect, useMemo, useState } from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  TextInput,
  ActivityIndicator,
  ScrollView,
} from "react-native";
import { useRouter } from "expo-router";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";
import { useApi } from "../../hooks/useApi";

type SalaryRange = { min: number; max: number; currency: string; note?: string };
type CareerSummary = {
  id: string;
  title: string;
  category: string;
  growth_outlook: string;
  region?: string;
  collar?: string;
  salary_range?: SalaryRange | null;
  tags: string[];
};

const OUTLOOK_COLOR: Record<string, string> = {
  "Very High": Colors.success,
  High: Colors.secondary,
  Good: Colors.warning,
  Stable: Colors.textSecondary,
  Moderate: Colors.textMuted,
};

const COLLARS = [
  { key: "all", label: "All collars" },
  { key: "white", label: "White-collar" },
  { key: "blue", label: "Blue-collar" },
  { key: "no", label: "Freelance" },
];
const REGIONS = [
  { key: "all", label: "All" },
  { key: "IN", label: "🇮🇳 India" },
  { key: "US", label: "🇺🇸 US" },
];
const SORTS = [
  { key: "default", label: "Relevance" },
  { key: "salary", label: "Salary ↓" },
  { key: "az", label: "A → Z" },
];

function shortSalary(s?: SalaryRange | null): string | null {
  if (!s) return null;
  const f = (n: number) => (n >= 100000 ? `${Math.round(n / 1000)}k` : n.toLocaleString());
  const cur = s.currency?.includes("INR") ? "₹" : s.currency === "USD" ? "$" : "";
  const per = s.currency?.includes("month") ? "/mo" : "/yr";
  return `${cur}${f(s.min)}–${cur}${f(s.max)}${per}`;
}

export default function ExploreScreen() {
  const router = useRouter();
  const { call, loading } = useApi();
  const [careers, setCareers] = useState<CareerSummary[]>([]);
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("All");
  const [collar, setCollar] = useState("all");
  const [region, setRegion] = useState("all");
  const [sort, setSort] = useState("default");
  const [showFilters, setShowFilters] = useState(false);

  useEffect(() => {
    call<{ careers: CareerSummary[] }>("/api/careers").then((data) => {
      if (data) setCareers(data.careers);
    });
  }, []);

  // Categories derived from the data (All first, then by frequency)
  const categories = useMemo(() => {
    const counts: Record<string, number> = {};
    careers.forEach((c) => (counts[c.category] = (counts[c.category] || 0) + 1));
    const sorted = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
    return ["All", ...sorted];
  }, [careers]);

  const filtered = useMemo(() => {
    let result = careers;
    if (activeCategory !== "All") result = result.filter((c) => c.category === activeCategory);
    if (collar !== "all") result = result.filter((c) => (c.collar ?? "white") === collar);
    if (region !== "all") result = result.filter((c) => (c.region ?? "IN") === region);
    if (query.trim()) {
      const q = query.toLowerCase();
      result = result.filter(
        (c) =>
          c.title.toLowerCase().includes(q) ||
          c.category.toLowerCase().includes(q) ||
          c.tags.some((t) => t.toLowerCase().includes(q))
      );
    }
    if (sort === "salary") {
      result = [...result].sort((a, b) => (b.salary_range?.min ?? 0) - (a.salary_range?.min ?? 0));
    } else if (sort === "az") {
      result = [...result].sort((a, b) => a.title.localeCompare(b.title));
    }
    return result;
  }, [careers, activeCategory, collar, region, query, sort]);

  const activeFilterCount = (collar !== "all" ? 1 : 0) + (region !== "all" ? 1 : 0) + (sort !== "default" ? 1 : 0);

  const renderCareer = ({ item }: { item: CareerSummary }) => {
    const salary = shortSalary(item.salary_range);
    return (
      <TouchableOpacity
        style={styles.card}
        onPress={() => router.push({ pathname: "/career/[id]", params: { id: item.id } })}
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
        <View style={styles.metaLine}>
          {salary && (
            <View style={styles.metaChip}>
              <Ionicons name="cash-outline" size={12} color={Colors.primary} />
              <Text style={styles.metaChipText}>{salary}</Text>
            </View>
          )}
          <View style={styles.metaChip}>
            <Ionicons name="location-outline" size={12} color={Colors.textMuted} />
            <Text style={styles.metaChipText}>{item.region ?? "IN"}</Text>
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
  };

  return (
    <View style={styles.container}>
      {/* Search + filter toggle */}
      <View style={styles.searchRow}>
        <View style={styles.searchBar}>
          <Ionicons name="search-outline" size={18} color={Colors.textMuted} />
          <TextInput
            style={styles.searchInput}
            placeholder="Search 300+ careers..."
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
        <TouchableOpacity
          style={[styles.filterBtn, activeFilterCount > 0 && styles.filterBtnActive]}
          onPress={() => setShowFilters((s) => !s)}
        >
          <Ionicons name="options-outline" size={20} color={activeFilterCount > 0 ? "#fff" : Colors.textSecondary} />
          {activeFilterCount > 0 && <Text style={styles.filterCount}>{activeFilterCount}</Text>}
        </TouchableOpacity>
      </View>

      {/* Filters panel */}
      {showFilters && (
        <View style={styles.filtersPanel}>
          <FilterRow label="Type" options={COLLARS} active={collar} onChange={setCollar} />
          <FilterRow label="Region" options={REGIONS} active={region} onChange={setRegion} />
          <FilterRow label="Sort" options={SORTS} active={sort} onChange={setSort} />
        </View>
      )}

      {/* Category pills */}
      <FlatList
        horizontal
        data={categories}
        keyExtractor={(c) => c}
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.categoryList}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={[styles.categoryPill, activeCategory === item && styles.categoryPillActive]}
            onPress={() => setActiveCategory(item)}
          >
            <Text style={[styles.categoryPillText, activeCategory === item && styles.categoryPillTextActive]}>
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
              <Text style={styles.emptyText}>No careers match your filters</Text>
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

function FilterRow({ label, options, active, onChange }: { label: string; options: { key: string; label: string }[]; active: string; onChange: (k: string) => void }) {
  return (
    <View style={styles.filterRow}>
      <Text style={styles.filterLabel}>{label}</Text>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={{ gap: 8 }}>
        {options.map((o) => {
          const sel = o.key === active;
          return (
            <TouchableOpacity
              key={o.key}
              style={[styles.filterChip, sel && styles.filterChipActive]}
              onPress={() => onChange(o.key)}
            >
              <Text style={[styles.filterChipText, sel && styles.filterChipTextActive]}>{o.label}</Text>
            </TouchableOpacity>
          );
        })}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  searchRow: { flexDirection: "row", gap: 8, margin: 16, marginBottom: 8 },
  searchBar: {
    flex: 1,
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: Colors.surface,
    borderRadius: 12,
    paddingHorizontal: 14,
    paddingVertical: 10,
    gap: 8,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  searchInput: { flex: 1, fontSize: 14, color: Colors.textPrimary },
  filterBtn: {
    width: 46,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: Colors.surface,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: Colors.border,
    gap: 2,
  },
  filterBtnActive: { backgroundColor: Colors.primary, borderColor: Colors.primary },
  filterCount: { color: "#fff", fontSize: 12, fontWeight: "800" },
  filtersPanel: { backgroundColor: Colors.surface, marginHorizontal: 16, borderRadius: 12, padding: 12, borderWidth: 1, borderColor: Colors.border, gap: 10, marginBottom: 8 },
  filterRow: { gap: 8 },
  filterLabel: { fontSize: 11, color: Colors.textMuted, fontWeight: "700", textTransform: "uppercase", letterSpacing: 0.5 },
  filterChip: { paddingHorizontal: 12, paddingVertical: 6, borderRadius: 16, backgroundColor: Colors.background, borderWidth: 1, borderColor: Colors.border },
  filterChipActive: { backgroundColor: Colors.primaryLight, borderColor: Colors.primary },
  filterChipText: { fontSize: 12, color: Colors.textSecondary, fontWeight: "600" },
  filterChipTextActive: { color: Colors.primaryDark },
  categoryList: { paddingHorizontal: 16, paddingBottom: 8, gap: 8 },
  categoryPill: { borderRadius: 20, paddingHorizontal: 14, paddingVertical: 7, backgroundColor: Colors.surface, borderWidth: 1, borderColor: Colors.border },
  categoryPillActive: { backgroundColor: Colors.primary, borderColor: Colors.primary },
  categoryPillText: { fontSize: 13, color: Colors.textSecondary, fontWeight: "500" },
  categoryPillTextActive: { color: "#fff" },
  list: { paddingHorizontal: 16, paddingBottom: 32 },
  resultCount: { fontSize: 12, color: Colors.textMuted, fontWeight: "600", textTransform: "uppercase", marginBottom: 12, letterSpacing: 0.5 },
  card: { backgroundColor: Colors.surface, borderRadius: 14, padding: 16, marginBottom: 12, borderWidth: 1, borderColor: Colors.border },
  cardTop: { flexDirection: "row", alignItems: "flex-start", gap: 12 },
  careerTitle: { fontSize: 15, fontWeight: "700", color: Colors.textPrimary, marginBottom: 2 },
  category: { fontSize: 12, color: Colors.textSecondary },
  outlookBadge: { borderRadius: 8, paddingHorizontal: 10, paddingVertical: 4 },
  outlookText: { fontSize: 11, fontWeight: "700" },
  metaLine: { flexDirection: "row", gap: 8, marginTop: 10 },
  metaChip: { flexDirection: "row", alignItems: "center", gap: 4 },
  metaChipText: { fontSize: 12, color: Colors.textSecondary, fontWeight: "600" },
  tagRow: { flexDirection: "row", flexWrap: "wrap", gap: 6, marginTop: 10 },
  tag: { backgroundColor: Colors.primaryLight, borderRadius: 6, paddingHorizontal: 8, paddingVertical: 3 },
  tagText: { fontSize: 11, color: Colors.primaryDark, fontWeight: "500" },
  empty: { alignItems: "center", padding: 40 },
  emptyText: { fontSize: 14, color: Colors.textMuted, marginTop: 12 },
});
