import React, { useEffect, useState, useCallback } from "react";
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  TextInput,
  ActivityIndicator,
  Alert,
  Linking,
} from "react-native";
import { useLocalSearchParams, useNavigation } from "expo-router";
import { Ionicons } from "@expo/vector-icons";
import { Colors } from "../../constants/Colors";
import { useApi } from "../../hooks/useApi";
import { SkillBadge } from "../../components/SkillBadge";
import { ResourceCard } from "../../components/ResourceCard";
import { StarRating } from "../../components/StarRating";

type Career = {
  id: string;
  title: string;
  category: string;
  description: string;
  salary_range: { min: number; max: number; currency: string; note: string };
  growth_outlook: string;
  work_style: string[];
  required_skills: { skill: string; level: string }[];
  entry_paths: string[];
  tags: string[];
};

type GapData = {
  score: number;
  matching_skills: { skill: string; level: string }[];
  gaps: { skill: string; level: string }[];
  resources: Record<string, any[]>;
  ai_advice: string | null;
  entry_paths: string[];
};

type CareerDetail = {
  career: Career;
  avg_rating: number | null;
  rating_count: number;
  recent_feedback: { rating: number; comment: string; pursuing: number; created_at: string }[];
};

const LEVEL_COLOR = {
  critical: Colors.levelCritical,
  important: Colors.levelImportant,
  helpful: Colors.levelHelpful,
};

const LEVEL_LABEL = {
  critical: "Must Have",
  important: "Important",
  helpful: "Nice to Have",
};

export default function CareerDetailScreen() {
  const { id, skills: skillsParam } = useLocalSearchParams<{ id: string; skills?: string }>();
  const navigation = useNavigation();
  const { call, loading } = useApi();

  const [detail, setDetail] = useState<CareerDetail | null>(null);
  const [gapData, setGapData] = useState<GapData | null>(null);
  const [userSkills] = useState<string[]>(
    skillsParam ? JSON.parse(skillsParam) : []
  );

  // Rating state
  const [userRating, setUserRating] = useState(0);
  const [comment, setComment] = useState("");
  const [pursuing, setPursuing] = useState(false);
  const [ratingSubmitted, setRatingSubmitted] = useState(false);
  const [submittingRating, setSubmittingRating] = useState(false);

  // UI sections
  const [showFeedback, setShowFeedback] = useState(false);

  useEffect(() => {
    if (!id) return;

    // Load career detail
    call<CareerDetail>(`/api/career/${id}`).then((data) => {
      if (data) {
        setDetail(data);
        navigation.setOptions({ title: data.career.title });
      }
    });

    // Load gap analysis if skills provided
    if (userSkills.length > 0) {
      call<GapData>(`/api/career/${id}/gap`, {
        method: "POST",
        body: JSON.stringify({ skills: userSkills }),
      }).then((data) => {
        if (data) setGapData(data);
      });
    }
  }, [id]);

  const submitRating = useCallback(async () => {
    if (userRating === 0) {
      Alert.alert("Select a rating", "Please select 1–5 stars before submitting.");
      return;
    }
    setSubmittingRating(true);
    const result = await call("/api/rate", {
      method: "POST",
      body: JSON.stringify({
        career_id: id,
        rating: userRating,
        comment: comment.trim() || null,
        pursuing,
        skills: userSkills,
      }),
    });
    setSubmittingRating(false);
    if (result) {
      setRatingSubmitted(true);
      // Refresh detail to show new rating
      const fresh = await call<CareerDetail>(`/api/career/${id}`);
      if (fresh) setDetail(fresh);
    }
  }, [id, userRating, comment, pursuing, userSkills, call]);

  if (loading && !detail) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color={Colors.primary} />
      </View>
    );
  }

  if (!detail) return null;

  const { career, avg_rating, rating_count, recent_feedback } = detail;
  const score = gapData?.score;

  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.headerRow}>
          <View style={{ flex: 1 }}>
            <Text style={styles.category}>{career.category}</Text>
            <Text style={styles.title}>{career.title}</Text>
          </View>
          {score !== undefined && (
            <View style={styles.scoreBadge}>
              <Text style={styles.scoreText}>{score}%</Text>
              <Text style={styles.scoreLabel}>match</Text>
            </View>
          )}
        </View>

        <Text style={styles.description}>{career.description}</Text>

        {/* Meta row */}
        <View style={styles.metaRow}>
          <View style={styles.metaItem}>
            <Ionicons name="trending-up-outline" size={16} color={Colors.primary} />
            <Text style={styles.metaMuted}>Growth: </Text>
            <Text style={styles.metaVal}>{career.growth_outlook}</Text>
          </View>
          {career.salary_range && (
            <View style={styles.metaItem}>
              <Ionicons name="cash-outline" size={16} color={Colors.primary} />
              <Text style={styles.metaMuted}>Salary: </Text>
              <Text style={styles.metaVal}>
                {career.salary_range.currency}
                {(career.salary_range.min / 1000).toFixed(0)}k–
                {(career.salary_range.max / 1000).toFixed(0)}k
              </Text>
            </View>
          )}
        </View>

        {/* Rating summary */}
        {avg_rating && (
          <View style={styles.ratingRow}>
            <StarRating value={avg_rating} readonly size={16} />
            <Text style={styles.ratingMeta}>
              {avg_rating.toFixed(1)} · {rating_count} rating{rating_count !== 1 ? "s" : ""}
            </Text>
          </View>
        )}

        {/* Work style tags */}
        <View style={styles.tagRow}>
          {career.work_style.map((w) => (
            <View key={w} style={styles.workTag}>
              <Text style={styles.workTagText}>{w}</Text>
            </View>
          ))}
        </View>
      </View>

      {/* Gap Analysis Section */}
      {gapData && (
        <>
          {/* Match progress */}
          <View style={styles.card}>
            <Text style={styles.cardTitle}>Your Match Score</Text>
            <View style={styles.progressBar}>
              <View style={[styles.progressFill, { width: `${gapData.score}%` as any }]} />
            </View>
            <Text style={styles.progressLabel}>{gapData.score}% of required skills covered</Text>
          </View>

          {/* Skills you have */}
          {gapData.matching_skills.length > 0 && (
            <View style={styles.card}>
              <Text style={styles.cardTitle}>
                <Ionicons name="checkmark-circle-outline" size={16} color={Colors.success} />
                {" "}Skills You Have ({gapData.matching_skills.length})
              </Text>
              <View style={styles.chipRow}>
                {gapData.matching_skills.map((s) => (
                  <SkillBadge key={s.skill} skill={s.skill} type="have" level={s.level} />
                ))}
              </View>
            </View>
          )}

          {/* Skills you need */}
          {gapData.gaps.length > 0 && (
            <View style={styles.card}>
              <Text style={styles.cardTitle}>
                <Ionicons name="arrow-up-circle-outline" size={16} color={Colors.danger} />
                {" "}Skills to Acquire ({gapData.gaps.length})
              </Text>
              {["critical", "important", "helpful"].map((level) => {
                const items = gapData.gaps.filter((g) => g.level === level);
                if (!items.length) return null;
                return (
                  <View key={level} style={{ marginBottom: 12 }}>
                    <View style={[styles.levelHeader, { backgroundColor: (LEVEL_COLOR as any)[level] + "15" }]}>
                      <Text style={[styles.levelLabel, { color: (LEVEL_COLOR as any)[level] }]}>
                        {(LEVEL_LABEL as any)[level]}
                      </Text>
                    </View>
                    {items.map((g) => {
                      const resources = gapData.resources[g.skill] || [];
                      return (
                        <View key={g.skill} style={styles.gapItem}>
                          <View style={styles.gapHeader}>
                            <Ionicons name="ellipse" size={8} color={(LEVEL_COLOR as any)[level]} />
                            <Text style={styles.gapSkill}>{g.skill}</Text>
                          </View>
                          {resources.slice(0, 2).map((r: any) => (
                            <ResourceCard key={r.name} resource={r} />
                          ))}
                        </View>
                      );
                    })}
                  </View>
                );
              })}
            </View>
          )}

          {/* AI Advice */}
          {gapData.ai_advice && (
            <View style={[styles.card, styles.aiCard]}>
              <View style={styles.aiHeader}>
                <Ionicons name="sparkles-outline" size={18} color={Colors.primary} />
                <Text style={styles.aiTitle}>AI Coaching Tips</Text>
              </View>
              <Text style={styles.aiText}>{gapData.ai_advice}</Text>
            </View>
          )}
        </>
      )}

      {/* Entry Paths */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>How to Enter This Career</Text>
        {career.entry_paths.map((path) => (
          <View key={path} style={styles.pathRow}>
            <Ionicons name="checkmark-outline" size={16} color={Colors.secondary} />
            <Text style={styles.pathText}>{path}</Text>
          </View>
        ))}
      </View>

      {/* Required Skills Overview */}
      {!gapData && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Required Skills</Text>
          {["critical", "important", "helpful"].map((level) => {
            const items = career.required_skills.filter((s) => s.level === level);
            if (!items.length) return null;
            return (
              <View key={level} style={{ marginBottom: 10 }}>
                <Text style={[styles.levelLabel, { color: (LEVEL_COLOR as any)[level], marginBottom: 6 }]}>
                  {(LEVEL_LABEL as any)[level]}
                </Text>
                <View style={styles.chipRow}>
                  {items.map((s) => (
                    <SkillBadge key={s.skill} skill={s.skill} type="neutral" level={s.level} />
                  ))}
                </View>
              </View>
            );
          })}
        </View>
      )}

      {/* Rate this career */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Rate This Recommendation</Text>
        {ratingSubmitted ? (
          <View style={styles.thankYou}>
            <Ionicons name="heart" size={32} color={Colors.primary} />
            <Text style={styles.thankYouText}>Thanks for your feedback!</Text>
          </View>
        ) : (
          <>
            <Text style={styles.ratePrompt}>Was this career recommendation useful?</Text>
            <StarRating
              value={userRating}
              onChange={setUserRating}
              size={32}
            />
            <TextInput
              style={styles.commentInput}
              placeholder="Share your experience or thoughts (optional)"
              placeholderTextColor={Colors.textMuted}
              value={comment}
              onChangeText={setComment}
              multiline
              numberOfLines={3}
            />
            <TouchableOpacity
              style={styles.pursuingRow}
              onPress={() => setPursuing(!pursuing)}
            >
              <View style={[styles.checkbox, pursuing && styles.checkboxChecked]}>
                {pursuing && <Ionicons name="checkmark" size={14} color="#fff" />}
              </View>
              <Text style={styles.pursuingLabel}>I'm pursuing / considering this career</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.submitBtn, submittingRating && styles.submitBtnDisabled]}
              onPress={submitRating}
              disabled={submittingRating}
            >
              {submittingRating ? (
                <ActivityIndicator color="#fff" />
              ) : (
                <Text style={styles.submitBtnText}>Submit Rating</Text>
              )}
            </TouchableOpacity>
          </>
        )}
      </View>

      {/* Community Feedback */}
      {recent_feedback.length > 0 && (
        <View style={styles.card}>
          <TouchableOpacity
            style={styles.feedbackToggle}
            onPress={() => setShowFeedback(!showFeedback)}
          >
            <Text style={styles.cardTitle}>
              Community Feedback ({recent_feedback.length})
            </Text>
            <Ionicons
              name={showFeedback ? "chevron-up" : "chevron-down"}
              size={18}
              color={Colors.textMuted}
            />
          </TouchableOpacity>
          {showFeedback &&
            recent_feedback.map((fb, i) => (
              <View key={i} style={styles.feedbackItem}>
                <View style={styles.feedbackHeader}>
                  <StarRating value={fb.rating} readonly size={14} />
                  {fb.pursuing === 1 && (
                    <Text style={styles.pursuingBadge}>Pursuing this career</Text>
                  )}
                </View>
                {fb.comment ? (
                  <Text style={styles.feedbackComment}>{fb.comment}</Text>
                ) : null}
              </View>
            ))}
        </View>
      )}

      <View style={{ height: 40 }} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  center: { flex: 1, justifyContent: "center", alignItems: "center" },
  header: {
    backgroundColor: Colors.surface,
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: Colors.border,
  },
  headerRow: { flexDirection: "row", alignItems: "flex-start", marginBottom: 12 },
  category: { fontSize: 12, color: Colors.primary, fontWeight: "600", textTransform: "uppercase", marginBottom: 4 },
  title: { fontSize: 22, fontWeight: "800", color: Colors.textPrimary },
  description: { fontSize: 14, color: Colors.textSecondary, lineHeight: 22, marginBottom: 14 },
  scoreBadge: {
    backgroundColor: Colors.primary,
    borderRadius: 12,
    paddingHorizontal: 14,
    paddingVertical: 8,
    alignItems: "center",
    minWidth: 64,
  },
  scoreText: { color: "#fff", fontSize: 20, fontWeight: "800" },
  scoreLabel: { color: "rgba(255,255,255,0.8)", fontSize: 10, fontWeight: "600" },
  metaRow: { flexDirection: "row", gap: 16, marginBottom: 12, flexWrap: "wrap" },
  metaItem: { flexDirection: "row", alignItems: "center", gap: 4 },
  metaMuted: { fontSize: 13, color: Colors.textMuted },
  metaVal: { fontSize: 13, color: Colors.textPrimary, fontWeight: "600" },
  ratingRow: { flexDirection: "row", alignItems: "center", gap: 8, marginBottom: 10 },
  ratingMeta: { fontSize: 13, color: Colors.textSecondary },
  tagRow: { flexDirection: "row", flexWrap: "wrap", gap: 6 },
  workTag: {
    backgroundColor: Colors.primaryLight,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 4,
  },
  workTagText: { fontSize: 11, color: Colors.primaryDark, fontWeight: "500" },
  card: {
    backgroundColor: Colors.surface,
    marginHorizontal: 16,
    marginTop: 14,
    borderRadius: 16,
    padding: 18,
    borderWidth: 1,
    borderColor: Colors.border,
  },
  cardTitle: { fontSize: 15, fontWeight: "700", color: Colors.textPrimary, marginBottom: 14 },
  progressBar: {
    height: 10,
    backgroundColor: Colors.border,
    borderRadius: 5,
    overflow: "hidden",
    marginBottom: 6,
  },
  progressFill: { height: "100%", backgroundColor: Colors.primary, borderRadius: 5 },
  progressLabel: { fontSize: 12, color: Colors.textSecondary },
  chipRow: { flexDirection: "row", flexWrap: "wrap", gap: 8 },
  levelHeader: { borderRadius: 6, paddingHorizontal: 10, paddingVertical: 4, marginBottom: 8, alignSelf: "flex-start" },
  levelLabel: { fontSize: 11, fontWeight: "700", textTransform: "uppercase", letterSpacing: 0.5 },
  gapItem: { marginBottom: 12 },
  gapHeader: { flexDirection: "row", alignItems: "center", gap: 8, marginBottom: 6 },
  gapSkill: { fontSize: 14, fontWeight: "600", color: Colors.textPrimary },
  aiCard: { borderColor: Colors.primaryLight, borderWidth: 1.5 },
  aiHeader: { flexDirection: "row", alignItems: "center", gap: 8, marginBottom: 10 },
  aiTitle: { fontSize: 15, fontWeight: "700", color: Colors.primary },
  aiText: { fontSize: 14, color: Colors.textSecondary, lineHeight: 22 },
  pathRow: { flexDirection: "row", alignItems: "flex-start", gap: 8, marginBottom: 8 },
  pathText: { fontSize: 14, color: Colors.textSecondary, flex: 1 },
  ratePrompt: { fontSize: 14, color: Colors.textSecondary, marginBottom: 14 },
  commentInput: {
    borderWidth: 1.5,
    borderColor: Colors.border,
    borderRadius: 10,
    padding: 12,
    marginTop: 14,
    fontSize: 14,
    color: Colors.textPrimary,
    backgroundColor: Colors.background,
    textAlignVertical: "top",
    minHeight: 80,
  },
  pursuingRow: { flexDirection: "row", alignItems: "center", gap: 10, marginTop: 14 },
  checkbox: {
    width: 22,
    height: 22,
    borderWidth: 2,
    borderColor: Colors.primary,
    borderRadius: 6,
    alignItems: "center",
    justifyContent: "center",
  },
  checkboxChecked: { backgroundColor: Colors.primary },
  pursuingLabel: { fontSize: 13, color: Colors.textSecondary, flex: 1 },
  submitBtn: {
    backgroundColor: Colors.primary,
    borderRadius: 12,
    paddingVertical: 13,
    alignItems: "center",
    marginTop: 14,
  },
  submitBtnDisabled: { opacity: 0.7 },
  submitBtnText: { color: "#fff", fontSize: 15, fontWeight: "700" },
  thankYou: { alignItems: "center", padding: 20 },
  thankYouText: { fontSize: 16, fontWeight: "700", color: Colors.textPrimary, marginTop: 10 },
  feedbackToggle: { flexDirection: "row", alignItems: "center", justifyContent: "space-between" },
  feedbackItem: {
    borderTopWidth: 1,
    borderTopColor: Colors.border,
    paddingTop: 12,
    marginTop: 12,
  },
  feedbackHeader: { flexDirection: "row", alignItems: "center", gap: 10, marginBottom: 6 },
  pursuingBadge: {
    backgroundColor: Colors.secondaryLight,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 3,
    fontSize: 11,
    color: Colors.secondary,
    fontWeight: "600",
  },
  feedbackComment: { fontSize: 13, color: Colors.textSecondary, lineHeight: 19 },
});
