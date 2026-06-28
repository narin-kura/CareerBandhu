import React, { useEffect, useMemo, useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  FlatList,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from "react-native";
import { useRouter } from "expo-router";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";
import { useApi } from "../../hooks/useApi";

type Summary = { id: string; title: string; category: string };
type Skill = { skill: string; level: string };
type FullCareer = {
  career: {
    id: string;
    title: string;
    category: string;
    growth_outlook: string;
    salary_range?: { min: number; max: number; currency: string } | null;
    required_skills: Skill[];
    work_style: string[];
  };
  detail?: { collar: string; region: string; roadmap: { total_estimate: string } };
};

function salaryStr(s?: { min: number; max: number; currency: string } | null): string {
  if (!s) return "—";
  const f = (n: number) => (n >= 100000 ? `${Math.round(n / 1000)}k` : n.toLocaleString());
  const cur = s.currency?.includes("INR") ? "₹" : s.currency === "USD" ? "$" : "";
  const per = s.currency?.includes("month") ? "/mo" : "/yr";
  return `${cur}${f(s.min)}–${cur}${f(s.max)}${per}`;
}

export default function CompareScreen() {
  const router = useRouter();
  const { call } = useApi();
  const [all, setAll] = useState<Summary[]>([]);
  const [slots, setSlots] = useState<(FullCareer | null)[]>([null, null]);
  const [picking, setPicking] = useState<number | null>(null);
  const [query, setQuery] = useState("");

  useEffect(() => {
    call<{ careers: Summary[] }>("/api/careers").then((d) => d && setAll(d.careers));
  }, []);

  const results = useMemo(() => {
    if (!query.trim()) return all.slice(0, 30);
    const q = query.toLowerCase();
    return all.filter((c) => c.title.toLowerCase().includes(q) || c.category.toLowerCase().includes(q)).slice(0, 40);
  }, [all, query]);

  const pick = async (slot: number, id: string) => {
    setPicking(null);
    setQuery("");
    const full = await call<FullCareer>(`/api/career/${id}`);
    if (full) setSlots((s) => s.map((v, i) => (i === slot ? full : v)));
  };

  const clear = (slot: number) => setSlots((s) => s.map((v, i) => (i === slot ? null : v)));

  const [a, b] = slots;
  const shared = useMemo(() => {
    if (!a || !b) return [];
    const bSet = new Set(b.career.required_skills.map((s) => s.skill.toLowerCase()));
    return a.career.required_skills.filter((s) => bSet.has(s.skill.toLowerCase())).map((s) => s.skill);
  }, [a, b]);

  if (picking !== null) {
    return (
      <View style={styles.container}>
        <View style={styles.pickerHeader}>
          <TouchableOpacity onPress={() => setPicking(null)}>
            <Ionicons name="close" size={24} color={Colors.textPrimary} />
          </TouchableOpacity>
          <Text style={styles.pickerTitle}>Pick a career</Text>
          <View style={{ width: 24 }} />
        </View>
        <View style={styles.searchBar}>
          <Ionicons name="search-outline" size={18} color={Colors.textMuted} />
          <TextInput
            style={styles.searchInput}
            placeholder="Search careers..."
            placeholderTextColor={Colors.textMuted}
            value={query}
            onChangeText={setQuery}
            autoFocus
          />
        </View>
        <FlatList
          data={results}
          keyExtractor={(c) => c.id}
          renderItem={({ item }) => (
            <TouchableOpacity style={styles.pickRow} onPress={() => pick(picking, item.id)}>
              <View>
                <Text style={styles.pickTitle}>{item.title}</Text>
                <Text style={styles.pickCat}>{item.category}</Text>
              </View>
              <Ionicons name="add-circle-outline" size={22} color={Colors.primary} />
            </TouchableOpacity>
          )}
        />
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={{ padding: 16, paddingBottom: 40 }}>
      <Text style={styles.intro}>Compare two careers side by side.</Text>

      <View style={styles.slotRow}>
        {[0, 1].map((i) => {
          const c = slots[i];
          return (
            <View key={i} style={styles.slot}>
              {c ? (
                <>
                  <TouchableOpacity style={styles.slotClear} onPress={() => clear(i)}>
                    <Ionicons name="close-circle" size={18} color={Colors.textMuted} />
                  </TouchableOpacity>
                  <Text style={styles.slotTitle} numberOfLines={2}>{c.career.title}</Text>
                  <Text style={styles.slotCat} numberOfLines={1}>{c.career.category}</Text>
                </>
              ) : (
                <TouchableOpacity style={styles.slotEmpty} onPress={() => setPicking(i)}>
                  <Ionicons name="add-circle" size={28} color={Colors.primary} />
                  <Text style={styles.slotEmptyText}>Add career {i + 1}</Text>
                </TouchableOpacity>
              )}
            </View>
          );
        })}
      </View>

      {a && b ? (
        <>
          <CompareRow label="Salary" a={salaryStr(a.career.salary_range)} b={salaryStr(b.career.salary_range)} />
          <CompareRow label="Growth outlook" a={a.career.growth_outlook} b={b.career.growth_outlook} />
          <CompareRow label="Type" a={a.detail?.collar ?? "—"} b={b.detail?.collar ?? "—"} />
          <CompareRow label="Region" a={a.detail?.region ?? "—"} b={b.detail?.region ?? "—"} />
          <CompareRow label="Skills required" a={`${a.career.required_skills.length}`} b={`${b.career.required_skills.length}`} />
          <CompareRow label="Time to learn" a={a.detail?.roadmap?.total_estimate ?? "—"} b={b.detail?.roadmap?.total_estimate ?? "—"} />

          <View style={styles.sharedCard}>
            <Text style={styles.sharedTitle}>
              {shared.length} shared skill{shared.length !== 1 ? "s" : ""}
            </Text>
            {shared.length > 0 ? (
              <View style={styles.chipRow}>
                {shared.map((s) => (
                  <View key={s} style={styles.chip}>
                    <Text style={styles.chipText}>{s}</Text>
                  </View>
                ))}
              </View>
            ) : (
              <Text style={styles.sharedNone}>These careers need quite different skill sets.</Text>
            )}
          </View>

          <View style={styles.openRow}>
            {[a, b].map((c) => (
              <TouchableOpacity
                key={c.career.id}
                style={styles.openBtn}
                onPress={() => router.push({ pathname: "/career/[id]", params: { id: c.career.id } })}
              >
                <Text style={styles.openBtnText} numberOfLines={1}>Open {c.career.title}</Text>
                <Ionicons name="chevron-forward" size={16} color={Colors.primary} />
              </TouchableOpacity>
            ))}
          </View>
        </>
      ) : (
        <View style={styles.hint}>
          <Ionicons name="git-compare-outline" size={42} color={Colors.textMuted} />
          <Text style={styles.hintText}>Add two careers above to see a side-by-side comparison.</Text>
        </View>
      )}
    </ScrollView>
  );
}

function CompareRow({ label, a, b }: { label: string; a: string; b: string }) {
  return (
    <View style={styles.cmpRow}>
      <Text style={styles.cmpLabel}>{label}</Text>
      <View style={styles.cmpVals}>
        <Text style={styles.cmpVal}>{a}</Text>
        <Text style={styles.cmpVal}>{b}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  intro: { fontSize: 14, color: Colors.textSecondary, marginBottom: 14 },
  slotRow: { flexDirection: "row", gap: 12, marginBottom: 18 },
  slot: { flex: 1, minHeight: 90, backgroundColor: Colors.surface, borderRadius: 14, borderWidth: 1, borderColor: Colors.border, padding: 14, justifyContent: "center" },
  slotClear: { position: "absolute", top: 8, right: 8 },
  slotTitle: { fontSize: 15, fontWeight: "800", color: Colors.textPrimary },
  slotCat: { fontSize: 12, color: Colors.textMuted, marginTop: 4 },
  slotEmpty: { alignItems: "center", gap: 8 },
  slotEmptyText: { fontSize: 13, color: Colors.primary, fontWeight: "600" },
  cmpRow: { backgroundColor: Colors.surface, borderRadius: 12, borderWidth: 1, borderColor: Colors.border, padding: 12, marginBottom: 8 },
  cmpLabel: { fontSize: 11, color: Colors.textMuted, fontWeight: "700", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 6 },
  cmpVals: { flexDirection: "row" },
  cmpVal: { flex: 1, fontSize: 14, color: Colors.textPrimary, fontWeight: "600", paddingRight: 8 },
  sharedCard: { backgroundColor: Colors.surface, borderRadius: 12, borderWidth: 1, borderColor: Colors.border, padding: 14, marginTop: 8 },
  sharedTitle: { fontSize: 14, fontWeight: "700", color: Colors.textPrimary, marginBottom: 10 },
  sharedNone: { fontSize: 13, color: Colors.textMuted },
  chipRow: { flexDirection: "row", flexWrap: "wrap", gap: 8 },
  chip: { backgroundColor: Colors.successLight, borderRadius: 6, paddingHorizontal: 9, paddingVertical: 4 },
  chipText: { fontSize: 12, color: Colors.success, fontWeight: "600" },
  openRow: { flexDirection: "row", gap: 12, marginTop: 16 },
  openBtn: { flex: 1, flexDirection: "row", alignItems: "center", justifyContent: "center", gap: 4, backgroundColor: Colors.primaryLight, borderRadius: 10, paddingVertical: 11, paddingHorizontal: 8 },
  openBtnText: { fontSize: 12, color: Colors.primaryDark, fontWeight: "700", flexShrink: 1 },
  hint: { alignItems: "center", padding: 40, gap: 12 },
  hintText: { fontSize: 14, color: Colors.textMuted, textAlign: "center", lineHeight: 20 },
  pickerHeader: { flexDirection: "row", alignItems: "center", justifyContent: "space-between", padding: 16, backgroundColor: Colors.surface },
  pickerTitle: { fontSize: 16, fontWeight: "700", color: Colors.textPrimary },
  searchBar: { flexDirection: "row", alignItems: "center", gap: 8, backgroundColor: Colors.surface, borderRadius: 12, borderWidth: 1, borderColor: Colors.border, paddingHorizontal: 14, paddingVertical: 10, margin: 16 },
  searchInput: { flex: 1, fontSize: 14, color: Colors.textPrimary },
  pickRow: { flexDirection: "row", alignItems: "center", justifyContent: "space-between", paddingVertical: 14, paddingHorizontal: 18, borderBottomWidth: 1, borderBottomColor: Colors.border },
  pickTitle: { fontSize: 14, fontWeight: "600", color: Colors.textPrimary },
  pickCat: { fontSize: 12, color: Colors.textMuted, marginTop: 2 },
});
