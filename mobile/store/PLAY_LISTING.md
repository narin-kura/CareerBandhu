# Google Play listing — CareerCompass (Vigyatri Solutions LLP)

Paste-ready content for the Play Console. Character limits are Google's.
Account setup (D-U-N-S, organization registration, service account) is the same as for
HinduNaamKaran — see that repo's `mobile/store/PLAY_LISTING.md`; it is done once per
organization and reused for every app.

---

## Identity

| Field | Value |
|---|---|
| Developer account | **Vigyatri Solutions LLP** (organization account — exempt from the 12-tester rule) |
| App name (≤30) | `CareerCompass` |
| Package name | `com.vigyatri.careercompass` — **cannot change after first upload** |
| Category | Education |
| Tags | Career, Jobs, Skills, Guidance |
| Contact email | info@vigyatrisolutions.com |
| Website | https://careercompass.vigyatri.com |
| Privacy policy URL | https://vigyatri.com/careercompass/privacy/ |
| Price | Free |
| Contains ads | No |
| In-app purchases | No |

## Short description (≤80 chars)

```
Explore 700+ careers, match your skills, and see exactly what to learn next.
```
(76 characters)

## Full description (≤4000 chars)

```
CareerCompass helps students, parents and career switchers find a realistic path — starting from the skills you already have.

FIND YOUR MATCH
Add the skills you know, from Python to plumbing to public speaking. CareerCompass ranks 700+ careers by how well they fit, shows your match score, and tells you which skills would close the gap.

EXPLORE 60+ FIELDS
Browse careers across technology, healthcare, trades, creative work, 3D animation and VFX, 3D printing, agriculture, government, sports, small business and self-employment. Filter by work type (office, hands-on, technical, creative, remote, government and more), by region (India or the US) and by salary.

SEE THE WHOLE PICTURE
Every career shows a plain-language description, salary range, growth outlook, the skills it needs and how important each one is, the ways people actually get into it, and the qualifications that matter. Businesses and self-employment paths include real setup costs and the registrations you need.

PLAN THE NEXT STEP
Open any career to get a phased learning roadmap with time estimates, curated learning resources for each skill gap, and related careers that share your skills.

COMPARE
Put two careers side by side — salary, outlook, skills and entry paths — to decide between them.

COMMUNITY
Rate careers and read what others pursuing the same path have to say. No account needed.

BUILT FOR INDIA AND THE US
Salaries are shown in the right currency for the region, and entry paths reflect how hiring actually works in each country.

HONEST BY DESIGN
Salary and outlook figures are general guidance compiled from public sources, shown as ranges, never as promises. No ads, no tracking, no sign-in.

Made by Vigyatri Solutions LLP. Also on the web at careercompass.vigyatri.com.
```

## Data safety form

The app **does** make network requests, so unlike HinduNaamKaran the answers are not all "No".
Answer from the table below; it matches `hooks/useApi.ts` and the backend handlers for
`/api/rate` and `/api/feedback`.

| Question | Answer | Basis |
|---|---|---|
| Does your app collect or share any of the required user data types? | **Yes** | feedback email + free-text messages are stored |
| Is all of the user data collected by your app encrypted in transit? | **Yes** | HTTPS only (`https://careercompass.vigyatri.com`) |
| Do you provide a way for users to request that their data is deleted? | **Yes** | email info@vigyatrisolutions.com — stated in the privacy policy |

Data types to declare:

| Data type | Collected? | Shared? | Optional? | Purpose |
|---|---|---|---|---|
| Personal info → **Email address** | Yes | No | **Optional** (only if typed into feedback) | App functionality (reply to feedback) |
| Messages → **Other in-app messages** | Yes | No | Optional | App functionality (feedback, rating comments) |
| App activity → **Other user-generated content** | Yes | No | Optional | App functionality (career ratings shown to others) |

Do **not** declare: location, contacts, device IDs, analytics, crash logs, financial info,
health info, photos — the app requests no permissions and bundles no analytics or ads SDK
(`grep -rn "analytics\|firebase\|admob" mobile/app mobile/components` returns nothing).
Skill names sent for matching are ephemeral and not stored, so they are not "collected".

## Content rating questionnaire

The app contains **user-generated content** (rating comments shown to other users) — answer
"Yes" to UGC and note that comments are anonymous, text only, and can be removed on request.
No violence, sexuality, profanity, controlled substances or gambling. Expect **Everyone**
(possibly "Everyone" with a UGC note).

## Graphics

| Asset | Requirement | Status |
|---|---|---|
| App icon | 512×512 PNG | export from `assets/icon.png` (1024²; Play accepts it or downscale) |
| Feature graphic | 1024×500 | `store/feature-graphic-1024x500.png` ✅ |
| Phone screenshots | 2–8, 16:9 to 9:16, ≥320px | **take from the preview APK on a real phone** |

Suggested screenshot sequence: (1) Find Career with a few skill chips and results,
(2) Explore with the category pills and a filter open, (3) a career detail on the Skills tab
showing Must Have / Important badges, (4) the Roadmap tab, (5) Compare.

---

## Backend dependency — read before submitting

This app is only as available as `https://careercompass.vigyatri.com`. Google's reviewers
will open the app; if the API is down they will see the "server unavailable" card on every
screen and may reject the build as broken. **Confirm the site loads in a browser the same
day you submit.** As of 2026-09-17 the Cloud Run service is down because GCP billing is
disabled — restore billing first.

## Build and submit

```bash
cd mobile
eas login
eas build --platform android --profile preview      # APK to sideload and screenshot
eas build --platform android --profile production   # .aab for Play
eas submit --platform android                       # Internal testing track, draft
```

`eas.json` targets the **internal** track as a **draft**. Review the draft in the Console,
add screenshots and the listing text above, then promote to Production yourself.

Without a service account key at `mobile/play-service-account.json`, skip `eas submit`
and upload the `.aab` by hand under Release → Production → Create new release.
