-- CareerBandhu — Supabase schema for user accounts & personalization
-- Run this once in the Supabase SQL Editor (Project → SQL Editor → New query → Run)

-- profiles: one row per user, stores saved skill list for pre-fill on return visits
create table public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  skills jsonb not null default '[]'::jsonb,
  region text default 'IN',
  updated_at timestamptz not null default now()
);

-- bookmarks: saved careers per user ("My saved careers")
create table public.bookmarks (
  user_id uuid not null references auth.users(id) on delete cascade,
  career_id text not null,
  created_at timestamptz not null default now(),
  primary key (user_id, career_id)
);

-- career_progress: learned skills per user per target career (skill-gap progress tracking)
create table public.career_progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  career_id text not null,
  learned_skills jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (user_id, career_id)
);

-- Row Level Security: users can only access their own rows.
-- The FastAPI backend uses the service-role key (bypasses RLS); these policies
-- are defense-in-depth in case the anon/authenticated key is ever used directly.
alter table public.profiles enable row level security;
alter table public.bookmarks enable row level security;
alter table public.career_progress enable row level security;

create policy "Users manage own profile" on public.profiles
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "Users manage own bookmarks" on public.bookmarks
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "Users manage own progress" on public.career_progress
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
