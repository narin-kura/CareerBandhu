"""Add batch 4: Media & Broadcasting (News Anchor, TV Host, RJ, VJ, Modelling, Entertainment)"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # MEDIA & BROADCASTING — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "news_anchor_in",
        "title": "News Anchor / TV News Reader",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Present news bulletins, breaking news, and live news programmes on television. News anchors are the on-air face of news channels — reading scripts, conducting interviews, moderating debates, and often reporting from the field. India has over 400 news channels in multiple languages, creating widespread opportunities.",
        "salary_range": {"min": 25000, "max": 500000, "currency": "INR/month", "note": "Junior anchor (regional) to prime-time anchor (national); varies greatly by channel"},
        "growth_outlook": "Stable — competitive but consistent; regional language channels growing",
        "work_style": ["On-camera", "Fast-paced", "Irregular hours"],
        "required_skills": [
            s("Diction & Voice Clarity", "critical"), s("Communication", "critical"),
            s("Script Reading / Teleprompter", "critical"), s("Current Affairs Knowledge", "critical"),
            s("On-camera Presence", "critical"), s("Interviewing", "important"),
            s("Language Fluency (Hindi/English/Regional)", "critical"),
        ],
        "entry_paths": [
            "Bachelor's or Master's in Journalism, Mass Communication, or English (IIMC, AJK-MCRC JMI, Symbiosis, Manipal)",
            "Voice and diction training; on-camera practice",
            "Start as junior reporter, production assistant, or copy editor at a news channel",
            "Language-specific channels (regional) are a strong entry point",
            "Anchoring courses from journalism institutes or independent trainers",
        ],
        "qualifications": [
            "Bachelor's or Master's in Journalism / Mass Communication (IIMC, AJKMCRC, Symbiosis, Manipal)",
            "Diploma in Broadcast Journalism or Anchoring (private institutes, ACJ Chennai)",
            "Voice & Diction certification (helpful for regional language channels)",
            "IIMC entrance exam for government journalism school admission",
        ],
        "tags": ["news-anchor", "tv", "journalism", "broadcast", "media"],
    },
    {
        "id": "tv_host_in",
        "title": "TV Host / Show Anchor",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Host television programmes — from reality shows, talk shows, game shows, and award ceremonies to lifestyle, travel, and entertainment content on GEC (General Entertainment Channels) and OTT platforms. TV hosts combine personality, spontaneity, and communication skills to engage millions of viewers.",
        "salary_range": {"min": 30000, "max": 2000000, "currency": "INR/month", "note": "Reality show side host to prime-time celebrity host; highly variable"},
        "growth_outlook": "Growing — OTT and GEC producing more non-fiction and hosted content",
        "work_style": ["Creative", "On-camera", "Irregular hours"],
        "required_skills": [
            s("On-camera Presence", "critical"), s("Communication", "critical"),
            s("Spontaneity & Wit", "critical"), s("Audience Engagement", "critical"),
            s("Script Adaptation", "important"), s("Entertainment Knowledge", "helpful"),
            s("Language Fluency", "critical"),
        ],
        "entry_paths": [
            "Background in journalism, acting, performance, or public speaking",
            "Start with smaller productions, web shows, or YouTube before TV",
            "Audition for hosting roles through production houses and talent agencies",
            "Build a visible presence on social media to attract channel attention",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "Bachelor's in Mass Communication / Journalism / Performing Arts (helpful)",
            "Acting or anchoring training from established coaches",
            "Strong showreel of hosting work is the primary credential",
        ],
        "tags": ["tv-host", "anchor", "entertainment", "media", "reality-show"],
    },
    {
        "id": "radio_jockey_in",
        "title": "Radio Jockey (RJ)",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Host radio programmes — playing music, entertaining audiences, discussing current events, conducting listener interactions, and featuring celebrities. RJs are the voice of FM radio stations across India. With 300+ FM stations now, and podcasting growing, voice-based content creation is a strong career avenue.",
        "salary_range": {"min": 20000, "max": 200000, "currency": "INR/month", "note": "Entry RJ (small city FM) to prime-time RJ (metro); top RJs also earn from events"},
        "growth_outlook": "Stable — FM radio steady; podcasting growing as an adjacent opportunity",
        "work_style": ["On-air", "Creative", "Early hours / split shifts"],
        "required_skills": [
            s("Voice & Diction", "critical"), s("Communication", "critical"),
            s("Storytelling", "critical"), s("Music Knowledge", "important"),
            s("Audience Engagement", "critical"), s("Improvisation", "important"),
            s("Script Writing", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Mass Communication, English, or any field",
            "RJ training programs from radio stations (Radio Mirchi, Red FM conduct intern drives)",
            "Voice training and diction coaching",
            "Start at community radio, college radio, or internet radio stations",
            "Audition through radio station open calls and online auditions",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "Bachelor's in Mass Communication / Journalism / English (helpful)",
            "Radio Jockey training certificate (Radio Mirchi Academy, private institutes)",
            "Voice & Diction certification",
            "Strong voice demo reel is the primary hiring criterion",
        ],
        "tags": ["radio", "rj", "fm", "broadcast", "media"],
    },
    {
        "id": "video_jockey_in",
        "title": "Video Jockey (VJ) / Content Host",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Host music video programmes, entertainment shows, and youth-oriented content on music channels (MTV, VH1, Vh1) and digital platforms. The VJ role has expanded significantly into YouTube hosting, Instagram live, and OTT content creator-hosting, making it a growing career for charismatic on-camera personalities.",
        "salary_range": {"min": 25000, "max": 300000, "currency": "INR/month", "note": "Entry VJ to popular digital content host; influencer income supplements"},
        "growth_outlook": "Growing — digital video and creator economy expanding VJ opportunities beyond TV",
        "work_style": ["On-camera", "Creative", "Entertainment-focused"],
        "required_skills": [
            s("On-camera Presence", "critical"), s("Entertainment Knowledge (music, pop culture)", "critical"),
            s("Communication", "critical"), s("Spontaneity", "critical"),
            s("Social Media", "important"), s("Script Adaptation", "important"),
        ],
        "entry_paths": [
            "No strict educational requirement — personality and on-camera skills are key",
            "Build YouTube / Instagram presence with hosted content",
            "Audition for music channels (MTV India, VH1, 9XM) via open calls",
            "Work in event hosting, live shows, and brand activations to build reel",
        ],
        "qualifications": [
            "No mandatory qualification",
            "Bachelor's in Mass Communication / Performing Arts / Film (helpful)",
            "Acting or hosting training from media schools",
            "Strong video reel and social media following are primary credentials",
        ],
        "tags": ["vj", "music-channel", "digital-host", "entertainment", "media"],
    },
    {
        "id": "model_in",
        "title": "Model (Fashion / Commercial / Ramp)",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Represent brands and designers through fashion ramp walks, print advertisements, TV commercials, product endorsements, and digital campaigns. India's modelling industry spans high fashion (FDCI, Lakme Fashion Week), commercial print, regional advertising, and the growing digital creator economy.",
        "salary_range": {"min": 20000, "max": 2000000, "currency": "INR/month", "note": "Entry model (catalogue) to high-fashion ramp model; celebrity endorsements earn crores"},
        "growth_outlook": "Growing — India's fashion, beauty, and D2C advertising market expanding rapidly",
        "work_style": ["Project-based", "Physical", "Travel-heavy"],
        "required_skills": [
            s("Posing & Body Language", "critical"), s("Ramp Walk", "important"),
            s("Physical Fitness & Grooming", "critical"), s("Confidence", "critical"),
            s("Adaptability", "important"), s("Communication", "helpful"),
            s("Social Media Presence", "important"),
        ],
        "entry_paths": [
            "Register with modelling agencies (Elite Model Management India, Toabh, Anima Creative)",
            "Participate in modelling contests and fashion weeks (fresh faces)",
            "Build a professional portfolio with a photographer",
            "Start with catalogue work, regional ads, and e-commerce brands",
            "Social media presence accelerates casting for commercial and digital campaigns",
        ],
        "qualifications": [
            "No formal qualification required",
            "Modelling course / grooming training (FDCI, Fashion Design Council, agencies)",
            "Professional portfolio (composite card) — primary credential for agency registration",
            "Physical requirements vary by category: height (ramp 5'7\"+/5'10\"+), measurements (catalogue flexible)",
        ],
        "tags": ["modelling", "fashion", "ramp", "advertising", "entertainment"],
    },
    {
        "id": "podcast_host_creator_in",
        "title": "Podcast Host / Digital Content Creator",
        "category": "Media & Broadcasting",
        "region": "IN",
        "description": "Create, host, and produce audio or video podcast content on platforms like Spotify, YouTube, JioSaavn, and Audible. India's podcasting market is booming — from true crime, business, and comedy to spirituality, education, and storytelling. Monetisation comes through ads, Spotify deals, Patreon, brand sponsorships, and live events.",
        "salary_range": {"min": 10000, "max": 1000000, "currency": "INR/month", "note": "Highly variable — top Indian podcasters earn ₹10L+ per month through multiple streams"},
        "growth_outlook": "Very strong — India podcast listenership growing 30%+ annually",
        "work_style": ["Creative", "Self-directed", "Remote"],
        "required_skills": [
            s("Content Creation", "critical"), s("Storytelling", "critical"),
            s("Audio / Video Editing", "important"), s("Research", "important"),
            s("Consistency", "critical"), s("Audience Engagement", "critical"),
            s("Marketing", "helpful"),
        ],
        "entry_paths": [
            "Start a podcast on any platform (Spotify, Anchor, Google Podcasts)",
            "Learn basic audio recording and editing (Audacity, GarageBand, Adobe Audition)",
            "Build an audience through consistent content and social media promotion",
            "Monetise: brand deals → Spotify exclusives → premium subscriptions → live events",
        ],
        "qualifications": [
            "No formal qualification required",
            "Journalism / Mass Communication background helpful but not mandatory",
            "Anchor / Spotify creator account setup",
            "Audio production skills (self-taught widely accepted)",
        ],
        "tags": ["podcast", "content-creator", "audio", "digital-media", "creator-economy"],
    },

    # ── MEDIA & BROADCASTING — USA ────────────────────────
    {
        "id": "us_news_anchor",
        "title": "News Anchor / Broadcast Journalist",
        "category": "Media & Broadcasting",
        "region": "US",
        "description": "Present news on local, national, or cable TV networks — from local market stations to CNN, Fox News, NBC, and ABC. Most anchors begin in small markets, hone skills, and move to larger markets over time. A competitive career requiring strong journalism skills, camera presence, and consistent delivery.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "USD/year", "note": "Small market anchor to network anchor; top national anchors earn millions"},
        "growth_outlook": "Declining in traditional broadcast; digital news video growing",
        "work_style": ["On-camera", "Fast-paced", "Irregular hours"],
        "required_skills": [
            s("On-camera Presence", "critical"), s("Journalism", "critical"),
            s("Clear Diction & Vocal Delivery", "critical"), s("Script Writing", "important"),
            s("Breaking News Handling", "critical"), s("Interviewing", "important"),
        ],
        "entry_paths": [
            "BS in Journalism, Broadcasting, or Communications from accredited program",
            "College TV / radio station experience",
            "Start in small markets (markets 150-200+); build reel and move up",
            "SPJ (Society of Professional Journalists) membership",
        ],
        "qualifications": [
            "BS in Journalism / Broadcasting / Communications (ACEJMC-accredited preferred)",
            "Strong on-air demo reel (1-2 minutes) is the primary hiring tool",
            "RTNDA (Radio Television Digital News Association) membership",
            "AP Broadcast Style proficiency",
        ],
        "tags": ["news-anchor", "broadcast", "journalism", "tv", "media"],
    },
    {
        "id": "us_radio_jockey",
        "title": "Radio Host / Disc Jockey (DJ/RJ)",
        "category": "Media & Broadcasting",
        "region": "US",
        "description": "Host radio programmes — playing music, entertaining listeners, sharing commentary, conducting celebrity interviews, and interacting with audiences on terrestrial (AM/FM), satellite (SiriusXM), and internet radio. Radio hosts often build strong local or national audiences and supplement income with live events and podcasting.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "USD/year", "note": "Small market morning show to nationally syndicated host"},
        "growth_outlook": "Declining in traditional terrestrial radio; stable in satellite and digital audio",
        "work_style": ["On-air", "Creative", "Early hours"],
        "required_skills": [
            s("Voice & Diction", "critical"), s("Communication", "critical"),
            s("Music Knowledge", "important"), s("Entertainment / Pop Culture", "important"),
            s("Audience Engagement", "critical"), s("Improvisation", "important"),
        ],
        "entry_paths": [
            "Associate's or Bachelor's in Broadcasting, Communications, or Journalism",
            "College radio station experience",
            "Internship at commercial radio stations",
            "Start in small markets; build to major markets over time",
        ],
        "qualifications": [
            "Associate's / Bachelor's in Broadcasting / Communications (helpful, not mandatory)",
            "FCC Restricted Radiotelephone Operator Permit (for AM/FM transmitter operation)",
            "Strong demo reel / voice sample",
            "NAB (National Association of Broadcasters) membership",
        ],
        "tags": ["radio", "disc-jockey", "broadcast", "entertainment", "media"],
    },
    {
        "id": "us_model",
        "title": "Model (Fashion / Commercial / Digital)",
        "category": "Media & Broadcasting",
        "region": "US",
        "description": "Work as a professional model for fashion designers, luxury brands, commercial advertisers, catalogues, and digital campaigns. The US modelling industry spans high fashion in New York, commercial work in LA and Chicago, and a growing market for diverse and inclusive models for digital-first brands.",
        "salary_range": {"min": 30000, "max": 500000, "currency": "USD/year", "note": "Commercial and plus-size models earn steadily; runway models earn per show + editorials"},
        "growth_outlook": "Stable — digital advertising and inclusive representation expanding commercial modelling",
        "work_style": ["Project-based", "Travel-heavy", "Physical"],
        "required_skills": [
            s("Posing & Body Language", "critical"), s("Professionalism", "critical"),
            s("Physical Fitness & Grooming", "critical"), s("Adaptability", "important"),
            s("Social Media Presence", "important"), s("Runway Walk (for fashion)", "helpful"),
        ],
        "entry_paths": [
            "Register with a modelling agency (Wilhelmina, Ford, IMG Models, Next Models)",
            "Build a professional portfolio with a reputable photographer",
            "Start with test shoots, student fashion shows, and local brand campaigns",
            "Social media following increasingly opens direct brand collaboration",
        ],
        "qualifications": [
            "No formal qualification required",
            "Professional portfolio (comp card with various looks)",
            "Agency representation (for major market bookings)",
            "SAG-AFTRA membership for union commercial shoots",
        ],
        "tags": ["modelling", "fashion", "commercial", "advertising", "entertainment"],
    },
]


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))
    existing = {c["id"] for c in careers}
    added = []
    for c in CAREERS:
        if c["id"] in existing:
            print(f"  skip (exists): {c['id']}")
            continue
        careers.append(c)
        added.append(f"[{c['region']}] {c['title']}")

    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")

    in_n = sum(1 for c in careers if c.get("region") == "IN")
    us_n = sum(1 for c in careers if c.get("region") == "US")
    print(f"\nAdded {len(added)} careers. Total: {len(careers)}  (IN: {in_n}, US: {us_n})")
    for t in added:
        print(f"  + {t}")


if __name__ == "__main__":
    main()
