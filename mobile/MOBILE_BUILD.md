# CareerCompass — Android/iOS Build Guide

The mobile app is an [Expo](https://expo.dev) (React Native) app using Expo Router,
on **Expo SDK 57** (React Native 0.86, React 19). It is a thin client: every screen
talks to the same FastAPI backend as the website, at `https://careercompass.vigyatri.com`.

| | |
|---|---|
| Display name | CareerCompass |
| Package / bundle id | `com.vigyatri.careercompass` (immutable after the first Play upload) |
| API | `expo.extra.apiUrl` in `app.json` → `https://careercompass.vigyatri.com` |
| Override at build time | `EXPO_PUBLIC_API_URL=https://... eas build ...` |
| Store docs | [`store/PLAY_LISTING.md`](./store/PLAY_LISTING.md) |
| Privacy policy | https://vigyatri.com/careercompass/privacy/ |

Why SDK 57 and not the SDK 51 the app started on: Google Play rejects new apps that
target below Android 15 (API 35) since Aug 2025, and Android 16 (API 36) since Aug 2026.
SDK 51 targets API 34. SDK 57 targets the current requirement.

---

## 1. Prerequisites (one-time)

```bash
npm install -g eas-cli      # or use npx eas-cli@latest below
eas login                   # free Expo account (expo.dev/signup)
```

## 2. Install deps & link the project to EAS

```bash
cd mobile
npm install
eas init                    # creates/links an EAS project, writes extra.eas.projectId
```

## 3. Sanity checks (no device needed)

```bash
npx tsc --noEmit                        # type check
npx expo-doctor                         # 21/21 checks should pass
npx expo export --platform android      # produces a Hermes bundle under dist/
```

The backend endpoints the app depends on are `/api/careers`, `/api/recommend`,
`/api/career/{id}`, `/api/career/{id}/gap`, `/api/rate` and `/api/feedback`. To test
them without production, run the API locally from the repo root:

```bash
pip install -r requirements.txt
cd backend && uvicorn app:app --port 8000
# then start the app with the local API:
cd ../mobile && EXPO_PUBLIC_API_URL=http://<your-LAN-ip>:8000 npx expo start
```

(Use the machine's LAN IP, not `localhost`, so a phone on the same Wi-Fi can reach it.)

## 4. Build the APK (cloud build)

```bash
eas build --platform android --profile preview
```

- `preview` profile (see [`eas.json`](./eas.json)) produces an **APK** for sideloading.
- The build runs on Expo's servers; when done you get a URL to download the `.apk`.
- First build prompts to generate an Android keystore — let EAS manage it.

## 5. Install on a phone

- Open the build URL on the Android device and download the `.apk`, **or**
- `eas build:run -p android` to install the latest build on a connected device/emulator.
- The phone must allow "Install unknown apps" for the browser/file manager.

---

## Profiles in `eas.json`

| Profile | Output | Use for |
|---|---|---|
| `development` | APK + dev client | live-reload debugging on device |
| `preview` | APK | **share with testers** (sideload) |
| `production` | AAB (app bundle) | Google Play submission |

## Going live

Publishing is under the **Vigyatri Solutions LLP** organization account, the same one
used for HinduNaamKaran, so the D-U-N-S / organization setup is done once and shared.
Listing text, data-safety answers and the submit commands are in
[`store/PLAY_LISTING.md`](./store/PLAY_LISTING.md).

**The backend must be up when Google reviews the app.** Every screen fetches from
`careercompass.vigyatri.com`; if the API is down reviewers see an error card on every
screen. Check the site in a browser before you press submit.

## Behaviour worth knowing

- **Timeouts.** Every request aborts after 35 s and shows a friendly message; Cloud Run
  scales to zero, so the first request after idle can take 10-20 s. Explore has a
  "Try again" button; Find shows an inline error.
- **Outlook badges** come from free-text `growth_outlook` — the app shows the headline
  before the first dash and colours it by the strength word (`constants/careerMeta.ts`).
- **Collar filters** mirror the web's eleven work types; keep `COLLAR_FILTERS` and
  `COLLAR_LABEL` in `constants/careerMeta.ts` in sync with `COLLAR_META` in the web app.
- No analytics, ads, auth or on-device storage. `npm audit` findings are all in Expo
  dev tooling; do not run `npm audit fix --force` — it breaks the SDK pin.
