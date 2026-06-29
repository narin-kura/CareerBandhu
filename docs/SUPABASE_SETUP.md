# Supabase Setup (Accounts & Personalization)

CareerBandhu uses [Supabase](https://supabase.com) for user accounts (email/password
+ Google sign-in) and to store personalization data (saved skill profile,
bookmarked careers, skill-gap progress). Free tier is sufficient.

## 1. Create the project

1. Sign in at [supabase.com](https://supabase.com), create a new project named
   `careerbandhu` (pick a region close to your users, e.g. `ap-south-1` for India).
2. Wait for provisioning to finish (~2 min).

## 2. Collect credentials (Project Settings → API)

| Value | Where to find it | Sensitivity |
|---|---|---|
| `SUPABASE_URL` | Project Settings → API → "Project URL" | Public |
| `SUPABASE_ANON_KEY` | Project Settings → API → "Project API keys" → `anon` `public` | Public |
| `SUPABASE_SERVICE_KEY` | Project Settings → API → "Project API keys" → `service_role` | **Secret — backend only** |

The backend verifies access tokens against the project's public JWKS endpoint
(`{SUPABASE_URL}/auth/v1/.well-known/jwks.json`) — no separate JWT secret is
needed.

## 3. Run the schema

Open SQL Editor → New query → paste the contents of
[`backend/data/supabase_schema.sql`](../backend/data/supabase_schema.sql) → Run.

This creates `profiles`, `bookmarks`, and `career_progress` tables with RLS enabled.

## 4. Enable Google sign-in

1. In [Google Cloud Console](https://console.cloud.google.com/apis/credentials),
   create an OAuth 2.0 Client ID (type: **Web application**).
2. Add this Authorized redirect URI (replace `<project-ref>` with your Supabase
   project ref, visible in the project URL):
   ```
   https://<project-ref>.supabase.co/auth/v1/callback
   ```
3. Copy the generated **Client ID** and **Client Secret**.
4. In Supabase: Authentication → Providers → Google → paste Client ID/Secret →
   Enable.

## 5. Configure redirect URLs

Authentication → URL Configuration:
- **Site URL**: `https://careercompass.vigyatri.com` (production — GCP Cloud Run)
- **Redirect URLs** (add all of these):
  - `http://localhost:8000` (local web dev)
  - `https://careercompass.vigyatri.com` (production custom domain)
  - `https://careerbandhu-h5axc6napq-uc.a.run.app` (GCP Cloud Run direct)
  - `https://knnarin-careerbandhu.hf.space` (HF Spaces — test/staging)
  - `careerbandhu://auth/callback` (mobile deep link)

> **Production is GCP Cloud Run; HF Spaces is the test environment.** Google OAuth
> only redirects back to URLs registered above, so the production domain MUST be the
> Site URL or sign-in breaks for real users.

## 6. Set environment variables

The backend reads these 3 env vars (see `backend/auth.py`). The app boots fine
without them — personalization endpoints just return `503` and `/api/config`
reports `auth_enabled: false`.

- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_KEY`

**Local dev**: export them in your shell or a `.env` file (gitignored) before
running `python backend/app.py` / `uvicorn`.

**Hugging Face Spaces**: Space → Settings → "Variables and secrets" → add all 3
(the service key as a "Secret", the URL/anon key can be "Variables").
No workflow change needed — `deploy-hf.yml` is a plain `git push`, and HF
injects configured values as container env vars automatically.

**GCP Cloud Run**: create secrets in Secret Manager and extend the
`--set-secrets` flag in `.github/workflows/deploy-gcp.yml`:

```bash
echo -n "<value>" | gcloud secrets create supabase-url --data-file=- --project=project-f281922f-0040-402f-b61
echo -n "<value>" | gcloud secrets create supabase-anon-key --data-file=- --project=project-f281922f-0040-402f-b61
echo -n "<value>" | gcloud secrets create supabase-service-key --data-file=- --project=project-f281922f-0040-402f-b61
```

> Windows users: see [[feedback_windows_secrets]] — don't use `echo -n` in
> PowerShell, it corrupts the secret. Use Cloud Shell, or `Out-File -NoNewline`.

**Mobile (Expo)**: set `EXPO_PUBLIC_SUPABASE_URL` and
`EXPO_PUBLIC_SUPABASE_ANON_KEY` in `mobile/.env` (gitignored) for local dev,
and in your EAS Build environment for production builds.
