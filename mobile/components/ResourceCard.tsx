import React from "react";
import { View, Text, TouchableOpacity, StyleSheet, Linking } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../constants/Colors";

type Resource = {
  name: string;
  platform: string;
  type: string;
  level: string;
  free: boolean;
  url: string;
};

const TYPE_ICON: Record<string, string> = {
  course: "school-outline",
  certification: "ribbon-outline",
  book: "book-outline",
  documentation: "document-text-outline",
  interactive: "game-controller-outline",
  guide: "map-outline",
  video: "play-circle-outline",
  tutorial: "code-slash-outline",
  tool: "construct-outline",
  articles: "newspaper-outline",
  resource: "library-outline",
  software: "apps-outline",
};

export function ResourceCard({ resource }: { resource: Resource }) {
  const icon = TYPE_ICON[resource.type] ?? "link-outline";

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => Linking.openURL(resource.url)}
      activeOpacity={0.75}
    >
      <View style={styles.iconBox}>
        <Ionicons name={icon as any} size={18} color={Colors.primary} />
      </View>
      <View style={{ flex: 1 }}>
        <Text style={styles.name} numberOfLines={2}>{resource.name}</Text>
        <Text style={styles.meta}>
          {resource.platform} · {resource.level}
        </Text>
      </View>
      <View style={[styles.badge, resource.free ? styles.badgeFree : styles.badgePaid]}>
        <Text style={[styles.badgeText, resource.free ? styles.badgeFreeText : styles.badgePaidText]}>
          {resource.free ? "FREE" : "PAID"}
        </Text>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  card: {
    flexDirection: "row",
    alignItems: "center",
    gap: 10,
    backgroundColor: Colors.background,
    borderRadius: 10,
    padding: 10,
    marginBottom: 6,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  iconBox: {
    width: 36,
    height: 36,
    backgroundColor: Colors.primaryLight,
    borderRadius: 8,
    alignItems: "center",
    justifyContent: "center",
  },
  name: { fontSize: 13, fontWeight: "600", color: Colors.textPrimary, marginBottom: 2 },
  meta: { fontSize: 11, color: Colors.textMuted },
  badge: { borderRadius: 6, paddingHorizontal: 7, paddingVertical: 3 },
  badgeFree: { backgroundColor: Colors.successLight },
  badgePaid: { backgroundColor: Colors.warningLight },
  badgeFreeText: { fontSize: 10, fontWeight: "700", color: "#166534" },
  badgePaidText: { fontSize: 10, fontWeight: "700", color: "#92400e" },
});
