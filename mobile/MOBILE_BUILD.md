# CareerCompass — Android App Build Guide

The mobile app is an [Expo](https://expo.dev) (React Native) app using Expo Router.
This guide gets you from source to an **installable Android APK** that testers can
sideload, using **EAS Build** (Expo's cloud build service — no Android Studio needed).

---

## 0. One value you MUST set first

Open [`app.json`](./app.json) and replace the API URL placeholder with the real
**Cloud Run** URL of the CareerBandhu backend:

```json
"extra": {
  "apiUrl": "https://REPLACE-WITH-CAREERBANDHU-CLOUD-RUN-URL"
}
```

Get the URL from **GCP Console → Cloud Run → `careerbandhu` → URL** (or from the
"Show service URL" step of the last `Deploy to Cloud Run (GCP)` GitHub Action run).
It looks like `https://careerbandhu-xxxxxxxxxx-uc.a.run.app`.

> The app does **not** use the Hugging Face Space for its API — Cloud Run only.
> You can also override per-build with the `EXPO_PUBLIC_API_URL` env var.

---

## 1. Prerequisites (one-time)

```bash
npm install -g eas-cli      # or use npx eas-cli@latest below
eas login                   # sign in with your free Expo account (expo.dev/signup)
```

## 2. Install deps & link the project to EAS

```bash
cd mobile
npm install
eas init                    # creates/links an EAS project, writes extra.eas.projectId
```

## 3. Build the APK (cloud build)

```bash
eas build --platform android --profile preview
```

- `preview` profile (see [`eas.json`](./eas.json)) produces an **APK** for internal
  distribution.
- The build runs on Expo's servers; when done you get a URL to download the `.apk`.
- First build also prompts to generate an Android Keystore — let EAS manage it (just
  press Enter / "yes").

## 4. Install on a phone

- Open the build URL on the Android device and download the `.apk`, **or**
- `eas build:run -p android` to install the latest build to a connected device/emulator.
- The phone must allow "Install unknown apps" for the browser/file manager.

---

## Profiles in `eas.json`

| Profile | Output | Use for |
|---|---|---|
| `development` | APK + dev client | live-reload debugging on device |
| `preview` | APK | **share with testers** (sideload) |
| `production` | AAB (app bundle) | Google Play submission |

## Later: publish to Google Play

1. Pay the one-time **$25** Google Play developer registration.
2. `eas build --platform android --profile production` (produces an `.aab`).
3. `eas submit --platform android` (uploads to Play Console), or upload the `.aab`
   manually in the Play Console.

## Quick local preview (no build)

```bash
cd mobile
npx expo start          # scan the QR with Expo Go (expo.dev/go) on your phone
```

Set `EXPO_PUBLIC_API_URL` to the Cloud Run URL when running locally if you want it to
hit production data:

```bash
EXPO_PUBLIC_API_URL=https://<cloud-run-url> npx expo start
```
