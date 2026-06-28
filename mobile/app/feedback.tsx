import React, { useState, useCallback } from "react";
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../constants/Colors";
import { useApi } from "../hooks/useApi";
import { StarRating } from "../components/StarRating";

const CATEGORIES = [
  { key: "general", label: "General", icon: "chatbubble-ellipses-outline" },
  { key: "bug", label: "Bug", icon: "bug-outline" },
  { key: "feature", label: "Feature idea", icon: "bulb-outline" },
  { key: "career_request", label: "Add a career", icon: "add-circle-outline" },
];

export default function FeedbackScreen() {
  const { call, loading } = useApi();
  const [category, setCategory] = useState("general");
  const [message, setMessage] = useState("");
  const [rating, setRating] = useState(0);
  const [email, setEmail] = useState("");
  const [done, setDone] = useState(false);

  const submit = useCallback(async () => {
    if (message.trim().length < 3) {
      Alert.alert("Add a message", "Please tell us a bit more (at least a few words).");
      return;
    }
    const res = await call<{ success: boolean }>("/api/feedback", {
      method: "POST",
      body: JSON.stringify({
        category,
        message: message.trim(),
        rating: rating || null,
        email: email.trim() || null,
      }),
    });
    if (res?.success) setDone(true);
  }, [category, message, rating, email, call]);

  if (done) {
    return (
      <View style={styles.doneWrap}>
        <Ionicons name="checkmark-circle" size={64} color={Colors.success} />
        <Text style={styles.doneTitle}>Thank you!</Text>
        <Text style={styles.doneText}>
          Your feedback helps make CareerCompass better. We read every message.
        </Text>
        <TouchableOpacity
          style={styles.againBtn}
          onPress={() => {
            setDone(false);
            setMessage("");
            setRating(0);
            setEmail("");
            setCategory("general");
          }}
        >
          <Text style={styles.againText}>Send more feedback</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={{ padding: 20, paddingBottom: 40 }} keyboardShouldPersistTaps="handled">
      <Text style={styles.label}>What's this about?</Text>
      <View style={styles.catGrid}>
        {CATEGORIES.map((c) => {
          const sel = c.key === category;
          return (
            <TouchableOpacity
              key={c.key}
              style={[styles.catChip, sel && styles.catChipActive]}
              onPress={() => setCategory(c.key)}
            >
              <Ionicons name={c.icon as any} size={16} color={sel ? "#fff" : Colors.textSecondary} />
              <Text style={[styles.catText, sel && styles.catTextActive]}>{c.label}</Text>
            </TouchableOpacity>
          );
        })}
      </View>

      <Text style={styles.label}>Your message</Text>
      <TextInput
        style={styles.messageInput}
        placeholder={
          category === "career_request"
            ? "Which career should we add? (e.g. a traditional craft, a new-age role...)"
            : "Tell us what you think, or what we can improve..."
        }
        placeholderTextColor={Colors.textMuted}
        value={message}
        onChangeText={setMessage}
        multiline
        numberOfLines={5}
      />

      <Text style={styles.label}>Rate the app (optional)</Text>
      <View style={styles.starWrap}>
        <StarRating value={rating} onChange={setRating} size={30} />
      </View>

      <Text style={styles.label}>Email (optional)</Text>
      <TextInput
        style={styles.emailInput}
        placeholder="So we can follow up"
        placeholderTextColor={Colors.textMuted}
        value={email}
        onChangeText={setEmail}
        autoCapitalize="none"
        keyboardType="email-address"
      />

      <TouchableOpacity style={[styles.submitBtn, loading && styles.submitDisabled]} onPress={submit} disabled={loading}>
        {loading ? (
          <ActivityIndicator color="#fff" />
        ) : (
          <>
            <Ionicons name="send" size={16} color="#fff" />
            <Text style={styles.submitText}>Send Feedback</Text>
          </>
        )}
      </TouchableOpacity>

      <Text style={styles.privacy}>
        We only store your message to improve the app. Email is optional and never shared.
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  label: { fontSize: 13, fontWeight: "700", color: Colors.textPrimary, marginBottom: 10, marginTop: 18 },
  catGrid: { flexDirection: "row", flexWrap: "wrap", gap: 8 },
  catChip: { flexDirection: "row", alignItems: "center", gap: 6, paddingHorizontal: 12, paddingVertical: 9, borderRadius: 20, backgroundColor: Colors.surface, borderWidth: 1, borderColor: Colors.border },
  catChipActive: { backgroundColor: Colors.primary, borderColor: Colors.primary },
  catText: { fontSize: 13, color: Colors.textSecondary, fontWeight: "600" },
  catTextActive: { color: "#fff" },
  messageInput: { backgroundColor: Colors.surface, borderWidth: 1, borderColor: Colors.border, borderRadius: 12, padding: 14, fontSize: 14, color: Colors.textPrimary, textAlignVertical: "top", minHeight: 120 },
  starWrap: { backgroundColor: Colors.surface, borderRadius: 12, borderWidth: 1, borderColor: Colors.border, padding: 14, alignItems: "center" },
  emailInput: { backgroundColor: Colors.surface, borderWidth: 1, borderColor: Colors.border, borderRadius: 12, padding: 14, fontSize: 14, color: Colors.textPrimary },
  submitBtn: { flexDirection: "row", alignItems: "center", justifyContent: "center", gap: 8, backgroundColor: Colors.primary, borderRadius: 12, paddingVertical: 15, marginTop: 24 },
  submitDisabled: { opacity: 0.7 },
  submitText: { color: "#fff", fontSize: 16, fontWeight: "700" },
  privacy: { fontSize: 11, color: Colors.textMuted, textAlign: "center", marginTop: 14, lineHeight: 16 },
  doneWrap: { flex: 1, backgroundColor: Colors.background, alignItems: "center", justifyContent: "center", padding: 40, gap: 14 },
  doneTitle: { fontSize: 22, fontWeight: "800", color: Colors.textPrimary },
  doneText: { fontSize: 14, color: Colors.textSecondary, textAlign: "center", lineHeight: 21 },
  againBtn: { marginTop: 16, paddingHorizontal: 20, paddingVertical: 12, borderRadius: 12, backgroundColor: Colors.primaryLight },
  againText: { color: Colors.primaryDark, fontWeight: "700", fontSize: 14 },
});
