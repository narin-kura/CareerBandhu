import urllib.request, json, time

TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # set via env: export GITHUB_TOKEN=...
REPO  = "narin-kura/CareerBandhu"
BASE  = f"https://api.github.com/repos/{REPO}"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.github+json",
}

def api(method, path, body=None):
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(f"{BASE}{path}", data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())

issues = [
    # Phase 1 - Testing Setup
    (1, ["testing","infra"],   "Install Node.js and set up local dev environment",
     "Install Node.js LTS from nodejs.org, then `cd mobile && npm install`. Required before any Expo commands work."),
    (1, ["testing","mobile"],  "Run Expo app locally and test in web browser",
     "Run `npx expo start --web` inside `mobile/`. Verify the Find Career, Explore, and About tabs load correctly."),
    (1, ["testing","mobile"],  "Test Expo app on Android device via Expo Go",
     "Install Expo Go on an Android phone. Scan the QR code from `npx expo start`. Test all screens on a real device."),
    (1, ["testing","mobile"],  "Test Expo app on iOS device via Expo Go",
     "Install Expo Go on an iPhone. Scan the QR code. Verify layout renders correctly on iOS."),
    (1, ["testing","backend"], "Test FastAPI backend locally",
     "Run `cd backend && pip install -r requirements.txt && python app.py`. Hit http://localhost:8000/docs to verify all endpoints."),
    (1, ["testing","backend"], "Verify HF Spaces deployment is live",
     "Check https://knnarin-careerbandhu.hf.space returns API status. Test /api/careers and /api/recommend endpoints."),
    (1, ["testing","mobile"],  "Connect Expo app to live HF Spaces API",
     "Set EXPO_PUBLIC_API_URL=https://knnarin-careerbandhu.hf.space in mobile/.env and test the full flow on a real device."),
    (1, ["testing"],           "End-to-end test: skills to career to rating",
     "Full journey: add 5 skills, see recommendations, open a career, run gap analysis, submit a rating. Verify data saves in DB."),

    # Phase 2 - Mobile Polish
    (2, ["mobile"],  "Design and add app icon and splash screen",
     "Create a CareerBandhu icon (1024x1024) and splash screen (2048x2048) with indigo brand color. Place in mobile/assets/."),
    (2, ["mobile"],  "Add skeleton loading states for career cards",
     "Replace ActivityIndicator spinners with animated skeleton placeholders while career data loads."),
    (2, ["mobile"],  "Add empty state illustrations",
     "Add friendly empty states when no careers match, no skills added yet, or no community ratings exist."),
    (2, ["mobile"],  "Test and fix layout on small screens (5-inch phones)",
     "Test on 360x640dp viewport. Fix any text overflow, button clipping, or card layout issues."),
    (2, ["mobile"],  "Add haptic feedback for key interactions",
     "Add light haptic feedback when a skill chip is added/removed and when a star rating is selected. Use expo-haptics."),
    (2, ["mobile"],  "Handle network errors and offline state gracefully",
     "Show a user-friendly error message when the API is unreachable. Add a retry button."),
    (2, ["mobile"],  "Add skill autocomplete suggestions from API",
     "When typing in the skill input, call /api/skills to filter and suggest matching skills in a dropdown."),

    # Phase 3 - Content Expansion
    (3, ["content"], "Add 15 more careers covering trades and vocational fields",
     "Add: Electrician, Plumber, Chef, Paramedic, Civil Engineer, Mechanical Engineer, Pharmacist, Journalist, Social Worker, Architect, Interior Designer, Event Manager, Real Estate Agent, Pilot, Marine Engineer."),
    (3, ["content"], "Add South Asia specific career paths",
     "Add careers common in India/Nepal/Sri Lanka: CA (Chartered Accountant), UPSC Officer, Ayurvedic Doctor, Textile Designer."),
    (3, ["content"], "Add salary data in INR for Indian market",
     "Add INR salary ranges alongside USD for all careers. Source from Glassdoor India and Naukri salary data."),
    (3, ["content"], "Expand learning resources with Indian institutes",
     "Add resources from IITs, NIIT, Coursera India, NPTEL, Swayam, and other Indian platforms for each skill gap."),
    (3, ["content"], "Add career progression ladder (junior to senior)",
     "For each career, add a progression field showing the typical 5-year career ladder (e.g. Junior Dev -> Mid -> Senior -> Architect)."),
    (3, ["content"], "Add regional language proficiency as a skill",
     "Add Tamil, Hindi, Telugu, Kannada, Bengali as skills that unlock relevant regional career recommendations."),

    # Phase 4 - App Store Preparation
    (4, ["app-store","mobile"], "Create Google Play Developer account",
     "Register at play.google.com/console. One-time $25 fee. Required for publishing to Android."),
    (4, ["app-store","mobile"], "Create Apple Developer account",
     "Register at developer.apple.com. Annual $99/year fee. Required for TestFlight and App Store."),
    (4, ["app-store","infra"],  "Set up Expo EAS for cloud builds",
     "Run `npm install -g eas-cli && eas login && eas build:configure` inside mobile/. Configure eas.json for production builds."),
    (4, ["app-store","mobile"], "Build Android AAB for Play Store via EAS",
     "Run `eas build --platform android --profile production`. Download the .aab for Play Store submission."),
    (4, ["app-store","mobile"], "Build iOS IPA for TestFlight via EAS",
     "Run `eas build --platform ios --profile production`. Submit to TestFlight for internal testing."),
    (4, ["app-store"],          "Write Google Play Store listing",
     "Write short description (80 chars), full description (4000 chars), category: Education. Prepare 8 screenshots and a feature graphic."),
    (4, ["app-store"],          "Write Apple App Store listing",
     "Write title, subtitle, description, keywords. Prepare screenshots for iPhone 6.5-inch and iPad 12.9-inch."),
    (4, ["app-store","mobile"], "Take and prepare all store screenshots",
     "Use the Expo simulator to capture: Hero, Skill Input, Career Results, Career Detail, Gap Analysis, Rating screen."),

    # Phase 5 - Web Launch
    (5, ["web"],         "Export Expo web build",
     "Run `npx expo export --platform web` inside mobile/. Output goes to dist/. Verify it loads correctly."),
    (5, ["web","infra"], "Deploy web build to Vercel",
     "Create a Vercel project, set root to mobile/, build command to `npx expo export --platform web`, output dir to `dist/`."),
    (5, ["web"],         "Set EXPO_PUBLIC_API_URL environment variable on Vercel",
     "In Vercel project settings -> Environment Variables -> add EXPO_PUBLIC_API_URL=https://knnarin-careerbandhu.hf.space"),
    (5, ["web"],         "Register domain careerbandhu.com",
     "Register careerbandhu.com on Namecheap or GoDaddy (~$10/year). Point DNS to Vercel."),
    (5, ["web"],         "Add SEO meta tags and Open Graph images",
     "Add title, description, og:image, og:title, twitter:card meta tags. Create a 1200x630 OG image with the CareerBandhu brand."),
    (5, ["web"],         "Set up Google Analytics on web build",
     "Add GA4 tracking. Track key events: skill_submitted, career_viewed, rating_submitted."),

    # Phase 6 - Backend Production
    (6, ["backend","infra"], "Migrate SQLite to Supabase PostgreSQL",
     "Create a free Supabase project. Update backend/app.py to use psycopg2. Ratings will persist across HF Space restarts."),
    (6, ["backend"],         "Set ANTHROPIC_API_KEY in HF Spaces secrets",
     "HF Space settings -> Variables and secrets -> add ANTHROPIC_API_KEY. Enables AI coaching tips in gap analysis."),
    (6, ["backend","infra"], "Add API rate limiting to prevent abuse",
     "Add slowapi rate limiting to /api/recommend and /api/rate. Limit to 30 req/min per IP."),
    (6, ["backend","infra"], "Set up error monitoring with Sentry",
     "Add sentry-sdk to requirements.txt. Wrap FastAPI app with Sentry. Set SENTRY_DSN as HF Space secret."),
    (6, ["backend"],         "Add pagination to careers and ratings endpoints",
     "Support ?page=1&limit=20 query params on /api/careers and /api/career/{id} feedback."),
    (6, ["backend"],         "Write API integration tests",
     "Create tests/test_api.py using pytest and httpx. Cover recommend, gap, rating submission, and edge cases."),

    # Phase 7 - Public Launch
    (7, ["launch"],           "Recruit 20 beta testers",
     "Share the Expo Go QR code or TestFlight link with students, parents, and career changers. Collect structured feedback."),
    (7, ["launch"],           "Create feedback form for beta users",
     "Set up a Google Form for beta feedback: Was the career match accurate? Was the gap analysis useful? What is missing?"),
    (7, ["launch"],           "Fix top 5 issues from beta feedback",
     "Triage feedback, prioritize top 5 issues, fix and release before public launch."),
    (7, ["launch","web"],     "Create marketing landing page",
     "Build careerbandhu.com with: headline, 3 feature highlights, app store buttons, screenshot gallery."),
    (7, ["launch"],           "Set up social media accounts",
     "Create Instagram @careerbandhu, LinkedIn page, Twitter @careerbandhu. Post launch content."),
    (7, ["launch","app-store"], "Submit to Google Play open testing",
     "Promote from internal to open testing on Play Console. Share the opt-in link publicly."),
    (7, ["launch","app-store"], "Submit to Apple App Store for review",
     "Submit production build for App Store review. Allow 2-7 days for Apple review process."),
    (7, ["launch"],           "Launch on Product Hunt",
     "Schedule Product Hunt launch. Prepare tagline, description, GIF demo, and gallery. Notify your network on launch day."),
    (7, ["launch"],           "Write launch story on LinkedIn and Medium",
     "Write the origin story: from loka-bandhuv (2013 idea) to CareerBandhu (2026 launch). Publish to build audience."),
]

total = 0
for ms_num, labels, title, body in issues:
    payload = {"title": title, "body": body, "labels": labels, "milestone": ms_num}
    r = api("POST", "/issues", payload)
    num = r.get("number")
    if num:
        print(f"  #{num} [Phase {ms_num}] {title[:65]}")
        total += 1
    else:
        print(f"  ERROR: {r}")
    time.sleep(0.25)

print(f"\nDone. Created {total} issues.")
