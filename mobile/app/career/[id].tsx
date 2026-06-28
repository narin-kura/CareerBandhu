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
} from "react-native";
import { useLocalSearchParams, useNavigation, useRouter } from "expo-router";
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

type RoadmapPhase = {
  level: string;
  name: string;
  blurb: string;
  skills: string[];
  weeks: number;
  estimate: string;
};

type Roadmap = { phases: RoadmapPhase[]; total_weeks: number; total_estimate: string };

type GapData = {
  score: number;
  matching_skills: { skill: string; level: string }[];
  gaps: { skill: string; level: string; weeks?: number }[];
  resources: Record<string, any[]>;
  roadmap?: Roadmap;
  ai_advice: string | null;
  entry_paths: string[];
};

type RelatedCareer = {
  id: string;
  title: string;
  category: string;
  growth_outlook: string;
  shared_skills: number;
};

type CareerExtra = {
  collar: string;
  region: string;
  qualifications: string[];
  job_ladder: { title: string; note: string }[];
  roadmap: Roadmap;
  related: RelatedCareer[];
};

type CareerDetail = {
  career: Career;
  detail?: CareerExtra;
  avg_rating: number | null;
  rating_count: number;
  recent_feedback: { rating: number; comment: string; pursuing: number; created_at: string }[];
};

const LEVEL_COLOR: Record<string, string> = {
  critical: Colors.levelCritical,
  important: Colors.levelImportant,
  helpful: Colors.levelHelpful,
};

const LEVEL_LABEL: Record<string, string> = {
  critical: "Must Have",
  important: "Important",
  helpful: "Nice to Have",
};

const COLLAR_LABEL: Record<string, string> = {
  white: "White-collar", blue: "Blue-collar", grey: "Grey-collar",
  pink: "Service", green: "Green job", new: "New-collar", no: "No-collar / Freelance",
};

type TabKey = "overview" | "skills" | "roadmap" | "reviews";
const TABS: { key: TabKey; label: string; icon: string }[] = [
  { key: "overview", label: "Overview", icon: "document-text-outline" },
  { key: "skills", label: "Skills", icon: "construct-outline" },
  { key: "roadmap", label: "Roadmap", icon: "map-outline" },
  { key: "reviews", label: "Reviews", icon: "star-outline" },
];

export default function CareerDetailScreen() {
  const { id, skills: skillsParam } = useLocalSearchParams<{ id: string; skills?: string }>();
  const navigation = useNavigation();
  const router = useRouter();
  const { call, loading } = useApi();

  const [detail, setDetail] = useState<CareerDetail | null>(null);
  const [gapData, setGapData] = useState<GapData | null>(null);
  const [userSkills] = useState<string[]>(skillsParam ? JSON.parse(skillsParam) : []);
  const [tab, setTab] = useState<TabKey>("overview");

  // Rating state
  const [userRating, setUserRating] = useState(0);
  const [comment, setComment] = useState("");
  const [pursuing, setPursuing] = useState(false);
  const [ratingSubmitted, setRatingSubmitted] = useState(false);
  const [submittingRating, setSubmittingRating] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);

  useEffect(() => {
    if (!id) return;
    setTab("overview");
    call<CareerDetail>(`/api/career/${id}`).then((data) => {
      if (data) {
        setDetail(data);
        navigation.setOptions({ title: data.career.title });
      }
    });
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
  const extra = detail.detail;
  const score = gapData?.score;
  const roadmap = gapData?.roadmap ?? extra?.roadmap;

  return (
    <View style={styles.container}>
      {/* Sticky header */}
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
        {extra && (
          <View style={styles.badgeRow}>
            <View style={styles.metaBadge}>
              <Ionicons name="briefcase-outline" size={12} color={Colors.primary} />
              <Text style={styles.metaBadgeText}>{COLLAR_LABEL[extra.collar] ?? extra.collar}</Text>
            </View>
            <View style={styles.metaBadge}>
              <Ionicons name="location-outline" size={12} color={Colors.primary} />
              <Text style={styles.metaBadgeText}>{extra.region}</Text>
            </View>
            {avg_rating != null && (
              <View style={styles.metaBadge}>
                <Ionicons name="star" size={12} color={Colors.warning} />
                <Text style={styles.metaBadgeText}>
                  {avg_rating.toFixed(1)} ({rating_count})
                </Text>
              </View>
            )}
          </View>
        )}
      </View>

      {/* Tab bar */}
      <View style={styles.tabBar}>
        {TABS.map((t) => {
          const active = t.key === tab;
          return (
            <TouchableOpacity
              key={t.key}
              style={[styles.tabItem, active && styles.tabItemActive]}
              onPress={() => setTab(t.key)}
            >
              <Ionicons name={t.icon as any} size={16} color={active ? Colors.primary : Colors.textMuted} />
              <Text style={[styles.tabLabel, active && styles.tabLabelActive]}>{t.label}</Text>
            </TouchableOpacity>
          );
        })}
      </View>

      <ScrollView style={{ flex: 1 }} contentContainerStyle={{ paddingBottom: 40 }}>
        {tab === "overview" && (
          <OverviewTab career={career} extra={extra} router={router} />
        )}
        {tab === "skills" && (
          <SkillsTab career={career} gapData={gapData} />
        )}
        {tab === "roadmap" && (
          <RoadmapTab roadmap={roadmap} extra={extra} personalized={!!gapData} />
        )}
        {tab === "reviews" && (
          <ReviewsTab
            avg_rating={avg_rating}
            rating_count={rating_count}
            recent_feedback={recent_feedback}
            userRating={userRating}
            setUserRating={setUserRating}
            comment={comment}
            setComment={setComment}
            pursuing={pursuing}
            setPursuing={setPursuing}
            ratingSubmitted={ratingSubmitted}
            submittingRating={submittingRating}
            submitRating={submitRating}
            showFeedback={showFeedback}
            setShowFeedback={setShowFeedback}
          />
        )}
      </ScrollView>
    </View>
  );
}

/* ---------------- Overview tab ---------------- */
function OverviewTab({ career, extra, router }: { career: Career; extra?: CareerExtra; router: any }) {
  return (
    <View>
      <View style={styles.card}>
        <Text style={styles.description}>{career.description}</Text>
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
                {career.salary_range.currency} {career.salary_range.min.toLocaleString()}–
                {career.salary_range.max.toLocaleString()}
              </Text>
            </View>
          )}
        </View>
        {!!career.salary_range?.note && <Text style={styles.salaryNote}>{career.salary_range.note}</Text>}
        <View style={styles.tagRow}>
          {career.work_style.map((w) => (
            <View key={w} style={styles.workTag}>
              <Text style={styles.workTagText}>{w}</Text>
            </View>
          ))}
        </View>
      </View>

      {extra && extra.qualifications.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Qualifications & Credentials</Text>
          {extra.qualifications.map((q) => (
            <View key={q} style={styles.pathRow}>
              <Ionicons name="ribbon-outline" size={16} color={Colors.primary} />
              <Text style={styles.pathText}>{q}</Text>
            </View>
          ))}
        </View>
      )}

      <View style={styles.card}>
        <Text style={styles.cardTitle}>How to Enter This Career</Text>
        {career.entry_paths.map((path) => (
          <View key={path} style={styles.pathRow}>
            <Ionicons name="checkmark-outline" size={16} color={Colors.secondary} />
            <Text style={styles.pathText}>{path}</Text>
          </View>
        ))}
      </View>

      {extra && extra.related.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Related Careers</Text>
          {extra.related.map((r) => (
            <TouchableOpacity
              key={r.id}
              style={styles.relatedRow}
              onPress={() => router.push({ pathname: "/career/[id]", params: { id: r.id } })}
            >
              <View style={{ flex: 1 }}>
                <Text style={styles.relatedTitle}>{r.title}</Text>
                <Text style={styles.relatedMeta}>
                  {r.category}
                  {r.shared_skills > 0 ? `  ·  ${r.shared_skills} shared skill${r.shared_skills !== 1 ? "s" : ""}` : ""}
                </Text>
              </View>
              <Ionicons name="chevron-forward" size={18} color={Colors.textMuted} />
            </TouchableOpacity>
          ))}
        </View>
      )}
    </View>
  );
}

/* ---------------- Skills tab ---------------- */
function SkillsTab({ career, gapData }: { career: Career; gapData: GapData | null }) {
  if (!gapData) {
    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Required Skills</Text>
        <Text style={styles.hintText}>
          Run a search with your skills (from the Find Career tab) to see your personal match and gaps.
        </Text>
        {["critical", "important", "helpful"].map((level) => {
          const items = career.required_skills.filter((s) => s.level === level);
          if (!items.length) return null;
          return (
            <View key={level} style={{ marginTop: 12 }}>
              <Text style={[styles.levelLabel, { color: LEVEL_COLOR[level], marginBottom: 6 }]}>
                {LEVEL_LABEL[level]}
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
    );
  }

  return (
    <View>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Your Match Score</Text>
        <View style={styles.progressBar}>
          <View style={[styles.progressFill, { width: `${gapData.score}%` as any }]} />
        </View>
        <Text style={styles.progressLabel}>{gapData.score}% of required skills covered</Text>
      </View>

      {gapData.matching_skills.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>
            <Ionicons name="checkmark-circle-outline" size={16} color={Colors.success} />{" "}
            Skills You Have ({gapData.matching_skills.length})
          </Text>
          <View style={styles.chipRow}>
            {gapData.matching_skills.map((s) => (
              <SkillBadge key={s.skill} skill={s.skill} type="have" level={s.level} />
            ))}
          </View>
        </View>
      )}

      {gapData.gaps.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>
            <Ionicons name="arrow-up-circle-outline" size={16} color={Colors.danger} />{" "}
            Skills to Acquire ({gapData.gaps.length})
          </Text>
          {gapData.roadmap && gapData.roadmap.total_weeks > 0 && (
            <Text style={styles.gapEstimate}>
              Estimated time to close gaps: {gapData.roadmap.total_estimate}
            </Text>
          )}
          {["critical", "important", "helpful"].map((level) => {
            const items = gapData.gaps.filter((g) => g.level === level);
            if (!items.length) return null;
            return (
              <View key={level} style={{ marginBottom: 12 }}>
                <View style={[styles.levelHeader, { backgroundColor: LEVEL_COLOR[level] + "15" }]}>
                  <Text style={[styles.levelLabel, { color: LEVEL_COLOR[level] }]}>{LEVEL_LABEL[level]}</Text>
                </View>
                {items.map((g) => {
                  const resources = gapData.resources[g.skill] || [];
                  return (
                    <View key={g.skill} style={styles.gapItem}>
                      <View style={styles.gapHeader}>
                        <Ionicons name="ellipse" size={8} color={LEVEL_COLOR[level]} />
                        <Text style={styles.gapSkill}>{g.skill}</Text>
                        {g.weeks ? <Text style={styles.gapWeeks}>~{g.weeks}w</Text> : null}
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

      {gapData.ai_advice && (
        <View style={[styles.card, styles.aiCard]}>
          <View style={styles.aiHeader}>
            <Ionicons name="sparkles-outline" size={18} color={Colors.primary} />
            <Text style={styles.aiTitle}>AI Coaching Tips</Text>
          </View>
          <Text style={styles.aiText}>{gapData.ai_advice}</Text>
        </View>
      )}
    </View>
  );
}

/* ---------------- Roadmap tab ---------------- */
function RoadmapTab({ roadmap, extra, personalized }: { roadmap?: Roadmap; extra?: CareerExtra; personalized: boolean }) {
  return (
    <View>
      {roadmap && roadmap.phases.length > 0 ? (
        <View style={[styles.card, styles.aiCard]}>
          <View style={styles.aiHeader}>
            <Ionicons name="map-outline" size={18} color={Colors.primary} />
            <Text style={styles.aiTitle}>{personalized ? "Your Learning Roadmap" : "Learning Roadmap"}</Text>
            <View style={styles.timePill}>
              <Text style={styles.timePillText}>{roadmap.total_estimate}</Text>
            </View>
          </View>
          {roadmap.phases.map((p) => (
            <View key={p.level} style={styles.phaseBlock}>
              <View style={styles.phaseHeader}>
                <Text style={[styles.phaseName, { color: LEVEL_COLOR[p.level] }]}>{p.name}</Text>
                <Text style={styles.phaseEst}>{p.estimate}</Text>
              </View>
              <Text style={styles.phaseBlurb}>{p.blurb}</Text>
              <View style={styles.chipRow}>
                {p.skills.map((s) => (
                  <View key={s} style={styles.phaseChip}>
                    <Text style={styles.phaseChipText}>{s}</Text>
                  </View>
                ))}
              </View>
            </View>
          ))}
          <Text style={styles.estimateNote}>Estimates assume focused self-study; your pace may vary.</Text>
        </View>
      ) : (
        <View style={styles.card}>
          <Text style={styles.hintText}>No roadmap available for this career yet.</Text>
        </View>
      )}

      {extra && extra.job_ladder.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Career Path</Text>
          {extra.job_ladder.map((rung, i) => (
            <View key={rung.title} style={styles.ladderRow}>
              <View style={styles.ladderCol}>
                <View style={styles.ladderDot}>
                  <Text style={styles.ladderNum}>{i + 1}</Text>
                </View>
                {i < extra.job_ladder.length - 1 && <View style={styles.ladderLine} />}
              </View>
              <View style={{ flex: 1, paddingBottom: 14 }}>
                <Text style={styles.ladderTitle}>{rung.title}</Text>
                <Text style={styles.ladderNote}>{rung.note}</Text>
              </View>
            </View>
          ))}
        </View>
      )}
    </View>
  );
}

/* ---------------- Reviews tab ---------------- */
function ReviewsTab(props: any) {
  const {
    avg_rating, rating_count, recent_feedback,
    userRating, setUserRating, comment, setComment, pursuing, setPursuing,
    ratingSubmitted, submittingRating, submitRating, showFeedback, setShowFeedback,
  } = props;
  return (
    <View>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Community Rating</Text>
        {avg_rating != null ? (
          <View style={styles.ratingRow}>
            <StarRating value={avg_rating} readonly size={18} />
            <Text style={styles.ratingMeta}>
              {avg_rating.toFixed(1)} · {rating_count} rating{rating_count !== 1 ? "s" : ""}
            </Text>
          </View>
        ) : (
          <Text style={styles.hintText}>No ratings yet — be the first to rate this career.</Text>
        )}
      </View>

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
            <StarRating value={userRating} onChange={setUserRating} size={32} />
            <TextInput
              style={styles.commentInput}
              placeholder="Share your experience or thoughts (optional)"
              placeholderTextColor={Colors.textMuted}
              value={comment}
              onChangeText={setComment}
              multiline
              numberOfLines={3}
            />
            <TouchableOpacity style={styles.pursuingRow} onPress={() => setPursuing(!pursuing)}>
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

      {recent_feedback.length > 0 && (
        <View style={styles.card}>
          <TouchableOpacity style={styles.feedbackToggle} onPress={() => setShowFeedback(!showFeedback)}>
            <Text style={styles.cardTitle}>Community Feedback ({recent_feedback.length})</Text>
            <Ionicons name={showFeedback ? "chevron-up" : "chevron-down"} size={18} color={Colors.textMuted} />
          </TouchableOpacity>
          {showFeedback &&
            recent_feedback.map((fb: any, i: number) => (
              <View key={i} style={styles.feedbackItem}>
                <View style={styles.feedbackHeader}>
                  <StarRating value={fb.rating} readonly size={14} />
                  {fb.pursuing === 1 && <Text style={styles.pursuingBadge}>Pursuing this career</Text>}
                </View>
                {fb.comment ? <Text style={styles.feedbackComment}>{fb.comment}</Text> : null}
              </View>
            ))}
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  center: { flex: 1, justifyContent: "center", alignItems: "center" },
  header: { backgroundColor: Colors.surface, padding: 18, paddingBottom: 12 },
  headerRow: { flexDirection: "row", alignItems: "flex-start" },
  category: { fontSize: 12, color: Colors.primary, fontWeight: "600", textTransform: "uppercase", marginBottom: 4 },
  title: { fontSize: 21, fontWeight: "800", color: Colors.textPrimary },
  scoreBadge: { backgroundColor: Colors.primary, borderRadius: 12, paddingHorizontal: 14, paddingVertical: 8, alignItems: "center", minWidth: 60 },
  scoreText: { color: "#fff", fontSize: 19, fontWeight: "800" },
  scoreLabel: { color: "rgba(255,255,255,0.8)", fontSize: 10, fontWeight: "600" },
  badgeRow: { flexDirection: "row", flexWrap: "wrap", gap: 8, marginTop: 12 },
  metaBadge: { flexDirection: "row", alignItems: "center", gap: 4, backgroundColor: Colors.primaryLight, borderRadius: 8, paddingHorizontal: 9, paddingVertical: 4 },
  metaBadgeText: { fontSize: 11, color: Colors.primaryDark, fontWeight: "700" },

  tabBar: { flexDirection: "row", backgroundColor: Colors.surface, borderBottomWidth: 1, borderBottomColor: Colors.border },
  tabItem: { flex: 1, flexDirection: "row", alignItems: "center", justifyContent: "center", gap: 5, paddingVertical: 12, borderBottomWidth: 2, borderBottomColor: "transparent" },
  tabItemActive: { borderBottomColor: Colors.primary },
  tabLabel: { fontSize: 12, color: Colors.textMuted, fontWeight: "600" },
  tabLabelActive: { color: Colors.primary },

  card: { backgroundColor: Colors.surface, marginHorizontal: 16, marginTop: 14, borderRadius: 16, padding: 18, borderWidth: 1, borderColor: Colors.border },
  cardTitle: { fontSize: 15, fontWeight: "700", color: Colors.textPrimary, marginBottom: 12 },
  hintText: { fontSize: 13, color: Colors.textMuted, lineHeight: 19 },
  description: { fontSize: 14, color: Colors.textSecondary, lineHeight: 22, marginBottom: 14 },
  metaRow: { flexDirection: "row", gap: 16, marginBottom: 8, flexWrap: "wrap" },
  metaItem: { flexDirection: "row", alignItems: "center", gap: 4 },
  metaMuted: { fontSize: 13, color: Colors.textMuted },
  metaVal: { fontSize: 13, color: Colors.textPrimary, fontWeight: "600" },
  salaryNote: { fontSize: 12, color: Colors.textMuted, fontStyle: "italic", marginBottom: 12 },
  tagRow: { flexDirection: "row", flexWrap: "wrap", gap: 6, marginTop: 4 },
  workTag: { backgroundColor: Colors.primaryLight, borderRadius: 6, paddingHorizontal: 8, paddingVertical: 4 },
  workTagText: { fontSize: 11, color: Colors.primaryDark, fontWeight: "500" },

  ratingRow: { flexDirection: "row", alignItems: "center", gap: 8 },
  ratingMeta: { fontSize: 13, color: Colors.textSecondary },

  progressBar: { height: 10, backgroundColor: Colors.border, borderRadius: 5, overflow: "hidden", marginBottom: 6 },
  progressFill: { height: "100%", backgroundColor: Colors.primary, borderRadius: 5 },
  progressLabel: { fontSize: 12, color: Colors.textSecondary },
  chipRow: { flexDirection: "row", flexWrap: "wrap", gap: 8 },
  levelHeader: { borderRadius: 6, paddingHorizontal: 10, paddingVertical: 4, marginBottom: 8, alignSelf: "flex-start" },
  levelLabel: { fontSize: 11, fontWeight: "700", textTransform: "uppercase", letterSpacing: 0.5 },
  gapItem: { marginBottom: 12 },
  gapHeader: { flexDirection: "row", alignItems: "center", gap: 8, marginBottom: 6 },
  gapSkill: { fontSize: 14, fontWeight: "600", color: Colors.textPrimary },
  gapWeeks: { fontSize: 11, color: Colors.textMuted, fontWeight: "700", marginLeft: "auto" },
  gapEstimate: { fontSize: 12, color: Colors.primary, fontWeight: "700", marginBottom: 12 },

  aiCard: { borderColor: Colors.primaryLight, borderWidth: 1.5 },
  aiHeader: { flexDirection: "row", alignItems: "center", gap: 8, marginBottom: 10 },
  aiTitle: { fontSize: 15, fontWeight: "700", color: Colors.primary },
  aiText: { fontSize: 14, color: Colors.textSecondary, lineHeight: 22 },
  timePill: { marginLeft: "auto", backgroundColor: Colors.primary, borderRadius: 10, paddingHorizontal: 10, paddingVertical: 3 },
  timePillText: { color: "#fff", fontSize: 12, fontWeight: "700" },

  phaseBlock: { borderTopWidth: 1, borderTopColor: Colors.border, paddingTop: 12, marginTop: 4, marginBottom: 4 },
  phaseHeader: { flexDirection: "row", alignItems: "center", justifyContent: "space-between", marginBottom: 4 },
  phaseName: { fontSize: 14, fontWeight: "800", textTransform: "uppercase", letterSpacing: 0.5 },
  phaseEst: { fontSize: 12, color: Colors.textMuted, fontWeight: "700" },
  phaseBlurb: { fontSize: 12, color: Colors.textSecondary, lineHeight: 18, marginBottom: 8 },
  phaseChip: { backgroundColor: Colors.background, borderRadius: 6, paddingHorizontal: 9, paddingVertical: 4, borderWidth: 1, borderColor: Colors.border },
  phaseChipText: { fontSize: 12, color: Colors.textPrimary, fontWeight: "500" },
  estimateNote: { fontSize: 11, color: Colors.textMuted, fontStyle: "italic", marginTop: 8 },

  ladderRow: { flexDirection: "row", gap: 12 },
  ladderCol: { alignItems: "center", width: 26 },
  ladderDot: { width: 26, height: 26, borderRadius: 13, backgroundColor: Colors.primary, alignItems: "center", justifyContent: "center" },
  ladderNum: { color: "#fff", fontSize: 12, fontWeight: "800" },
  ladderLine: { width: 2, flex: 1, backgroundColor: Colors.border, marginTop: 2 },
  ladderTitle: { fontSize: 14, fontWeight: "700", color: Colors.textPrimary },
  ladderNote: { fontSize: 12, color: Colors.textSecondary, marginTop: 2, lineHeight: 17 },

  relatedRow: { flexDirection: "row", alignItems: "center", paddingVertical: 11, borderTopWidth: 1, borderTopColor: Colors.border },
  relatedTitle: { fontSize: 14, fontWeight: "700", color: Colors.textPrimary },
  relatedMeta: { fontSize: 12, color: Colors.textMuted, marginTop: 2 },

  pathRow: { flexDirection: "row", alignItems: "flex-start", gap: 8, marginBottom: 8 },
  pathText: { fontSize: 14, color: Colors.textSecondary, flex: 1 },

  ratePrompt: { fontSize: 14, color: Colors.textSecondary, marginBottom: 14 },
  commentInput: { borderWidth: 1.5, borderColor: Colors.border, borderRadius: 10, padding: 12, marginTop: 14, fontSize: 14, color: Colors.textPrimary, backgroundColor: Colors.background, textAlignVertical: "top", minHeight: 80 },
  pursuingRow: { flexDirection: "row", alignItems: "center", gap: 10, marginTop: 14 },
  checkbox: { width: 22, height: 22, borderWidth: 2, borderColor: Colors.primary, borderRadius: 6, alignItems: "center", justifyContent: "center" },
  checkboxChecked: { backgroundColor: Colors.primary },
  pursuingLabel: { fontSize: 13, color: Colors.textSecondary, flex: 1 },
  submitBtn: { backgroundColor: Colors.primary, borderRadius: 12, paddingVertical: 13, alignItems: "center", marginTop: 14 },
  submitBtnDisabled: { opacity: 0.7 },
  submitBtnText: { color: "#fff", fontSize: 15, fontWeight: "700" },
  thankYou: { alignItems: "center", padding: 20 },
  thankYouText: { fontSize: 16, fontWeight: "700", color: Colors.textPrimary, marginTop: 10 },
  feedbackToggle: { flexDirection: "row", alignItems: "center", justifyContent: "space-between" },
  feedbackItem: { borderTopWidth: 1, borderTopColor: Colors.border, paddingTop: 12, marginTop: 12 },
  feedbackHeader: { flexDirection: "row", alignItems: "center", gap: 10, marginBottom: 6 },
  pursuingBadge: { backgroundColor: Colors.secondaryLight, borderRadius: 6, paddingHorizontal: 8, paddingVertical: 3, fontSize: 11, color: Colors.secondary, fontWeight: "600" },
  feedbackComment: { fontSize: 13, color: Colors.textSecondary, lineHeight: 19 },
});
