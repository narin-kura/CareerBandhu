"""Batch: Sports & Athletics, Music Industry, Gaming & Esports"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # SPORTS & ATHLETICS — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "cricketer_in",
        "title": "Cricketer (Professional)",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Compete at state, national, or franchise level in India's most popular sport. The pathway runs from school and club cricket → district teams → Ranji Trophy (domestic first-class) → IPL (franchise T20 league) → Indian national team. IPL has made cricket a highly lucrative profession even below the international level. Coaches, academies, and state cricket associations support the development pipeline.",
        "salary_range": {"min": 20000, "max": 5000000, "currency": "INR/month", "note": "State contract player to IPL franchise player (IPL auction price crores); international players earn far more"},
        "growth_outlook": "Stable — IPL and domestic tournaments provide income; highly competitive",
        "work_style": ["Physical", "Team-based", "Travel-heavy"],
        "required_skills": [
            s("Batting / Bowling / Wicket-keeping (specialisation)", "critical"),
            s("Fielding & Athletic Fitness", "critical"), s("Mental Toughness", "critical"),
            s("Game Situation Awareness", "critical"), s("Team Communication", "important"),
            s("Discipline & Consistent Practice", "critical"),
        ],
        "entry_paths": [
            "Join a cricket academy from a young age (6-15 years) under a qualified coach",
            "Represent school and district teams in BCCI Under-16 / Under-19 tournaments",
            "Play in state Ranji Trophy squad — the gateway to national selection",
            "Perform consistently to attract IPL franchise scouts or state selectors",
            "Alternatively: become a cricket coach (NCA Level 1 / Level 2) after playing career",
        ],
        "qualifications": [
            "No formal academic degree required for playing",
            "BCCI registration with State Cricket Association (mandatory for domestic matches)",
            "NCA (National Cricket Academy, Bengaluru) coaching programmes for post-playing career",
        ],
        "tags": ["cricket", "ipl", "sports", "athlete", "ranji"],
    },
    {
        "id": "kabaddi_player_in",
        "title": "Kabaddi Player / Pro Kabaddi Athlete",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Compete professionally in India's indigenous contact sport, which has seen a massive revival through the Pro Kabaddi League (PKL). PKL teams auction players for lakhs to crores annually. At the national level, the Indian kabaddi team is dominant at Asian Games and Asian Kabaddi Championships. The sport is rooted in rural India but now has urban academies and corporate sponsorship.",
        "salary_range": {"min": 10000, "max": 500000, "currency": "INR/month", "note": "Junior state player to PKL auction player (₹50L+ per season at the top)"},
        "growth_outlook": "Growing — PKL driving monetisation; school kabaddi programmes expanding feeder base",
        "work_style": ["Physical", "Team-based", "Competitive"],
        "required_skills": [
            s("Raiding Techniques", "critical"), s("Defensive Tackles", "critical"),
            s("Physical Strength & Stamina", "critical"), s("Breath Control", "critical"),
            s("Game Awareness & Strategy", "important"), s("Agility", "critical"),
        ],
        "entry_paths": [
            "Join a school or district kabaddi academy",
            "Represent district and state teams in national championships",
            "Get scouted for the Pro Kabaddi League trials (PKL holds annual draft and trials)",
            "Build visibility through national-level tournaments to attract team franchises",
        ],
        "qualifications": [
            "No formal degree required",
            "State and national kabaddi federation registration",
            "Physical fitness certifications (helpful for professional contracts)",
        ],
        "tags": ["kabaddi", "pkl", "sports", "athlete", "contact-sport"],
    },
    {
        "id": "badminton_player_in",
        "title": "Badminton Player (Professional)",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Compete nationally and internationally in singles or doubles events. India has produced world-class badminton players including PV Sindhu, Saina Nehwal, Kidambi Srikanth, and Satwiksairaj Rankireddy. The Premier Badminton League (PBL) provides a domestic franchise league on the lines of IPL. SAI (Sports Authority of India) provides scholarships and training centres for elite players.",
        "salary_range": {"min": 30000, "max": 1000000, "currency": "INR/month", "note": "State junior player to PBL franchise / national team player with BWF ranking income and endorsements"},
        "growth_outlook": "Growing — India's badminton ecosystem maturing; Olympics focus driving investment",
        "work_style": ["Physical", "Individual / Doubles pairs", "Travel-heavy"],
        "required_skills": [
            s("Technical Shot-Making (smash, drop, net play)", "critical"),
            s("Footwork & Agility", "critical"), s("Physical Fitness & Endurance", "critical"),
            s("Match Tactics & Mental Game", "critical"), s("Serve & Return Strategies", "critical"),
        ],
        "entry_paths": [
            "Enrol in a SAI or state badminton academy from an early age",
            "Compete in BAI (Badminton Association of India) junior tournaments",
            "Aim for SAI/TOPS scholarship for elite training under national coaches",
            "Compete in BWF-sanctioned international tournaments for world ranking",
        ],
        "qualifications": [
            "BAI (Badminton Association of India) player registration",
            "SAI National Academy selection for elite pathway",
            "BWF Player ID for international circuit",
        ],
        "tags": ["badminton", "pbl", "sports", "athlete", "olympics"],
    },
    {
        "id": "sports_coach_in",
        "title": "Sports Coach / Athletic Trainer",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Train and develop athletes in a specific sport — from school-level programmes and district academies to professional franchise and national team coaching. India's sport ecosystem is growing with SAI's TOPS (Target Olympic Podium Scheme), state sports academies, SGFI school leagues, and private academies across cricket, football, badminton, athletics, and more.",
        "salary_range": {"min": 25000, "max": 500000, "currency": "INR/month", "note": "School or district-level coach to head coach of IPL / national franchise"},
        "growth_outlook": "Growing — India investing heavily in sports development ahead of 2028 and 2032 Olympics",
        "work_style": ["Physical", "Mentoring", "Early hours"],
        "required_skills": [
            s("Sport-Specific Technical Knowledge", "critical"), s("Athlete Development Methodology", "critical"),
            s("Communication & Motivation", "critical"), s("Performance Analysis", "important"),
            s("Injury Prevention Basics", "important"), s("Planning & Periodisation", "important"),
        ],
        "entry_paths": [
            "Pursue a Bachelor's in Physical Education (BPEd) or Sports Science (NIS, LNIPE, Amity)",
            "Obtain NIS (National Institute of Sports, Patiala) coaching diploma in your sport",
            "Start coaching at school or club level to build experience",
            "Work up to SAI Sports Authority of India or state association head coach positions",
        ],
        "qualifications": [
            "BPEd / MPEd from a recognised institution (LNIPE, Amity, state sports universities)",
            "NIS (National Institute of Sports) Coaching Diploma — gold standard for Indian sports coaches",
            "Sport-specific federation coaching certification (BCCI, BAI, AFI, etc.)",
        ],
        "tags": ["coach", "sports", "athletic-training", "academy", "fitness"],
    },
    {
        "id": "personal_trainer_in",
        "title": "Personal Fitness Trainer / Gym Trainer",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Design and deliver personalised fitness programmes for clients in gyms, homes, or online. India's fitness industry is booming — gym chains (Cult.fit, Gold's Gym, Anytime Fitness), boutique studios, and digital fitness platforms (Cure.fit, Fittr) have created massive demand for certified trainers. Specialisations include weight training, yoga, CrossFit, HIIT, and rehabilitation fitness.",
        "salary_range": {"min": 20000, "max": 200000, "currency": "INR/month", "note": "Junior gym trainer to celebrity personal trainer or online fitness entrepreneur"},
        "growth_outlook": "Strong — India's fitness industry growing 25%+ annually post-pandemic",
        "work_style": ["Physical", "Client-facing", "Flexible hours"],
        "required_skills": [
            s("Exercise Science & Programming", "critical"), s("Nutrition Basics", "important"),
            s("Client Assessment & Goal Setting", "critical"), s("Communication & Motivation", "critical"),
            s("Anatomy & Physiology", "critical"), s("First Aid / CPR", "important"),
        ],
        "entry_paths": [
            "Obtain a CPT (Certified Personal Trainer) certification from ACE, NASM, ISSA, ACSM, or NCSF",
            "Complete an Indian certification: INFS, IFT (Indian Fitness Training Academy), or K11 Fitness Academy",
            "Join a gym as a junior trainer; build a client base and specialise",
            "Build social media presence and move to online coaching for scale",
        ],
        "qualifications": [
            "CPT certification from NASM, ACE, ISSA, or Indian equivalent (INFS, IFT, K11)",
            "Bachelor's in Physical Education, Sports Science, or Kinesiology (advantageous)",
            "CPR / First Aid certification (required by most gyms)",
        ],
        "tags": ["fitness", "personal-trainer", "gym", "wellness", "strength-training"],
    },
    {
        "id": "yoga_instructor_in",
        "title": "Yoga Instructor / Yoga Therapist",
        "category": "Sports & Athletics",
        "region": "IN",
        "description": "Teach traditional and modern yoga practices to individuals and groups in studios, schools, corporate wellness programmes, and retreats. India is the birthplace of yoga and a global hub for yoga education. Yoga Alliance registered schools proliferate nationwide. International demand for Indian-certified yoga teachers is enormous — many instructors build global careers teaching online or abroad.",
        "salary_range": {"min": 15000, "max": 200000, "currency": "INR/month", "note": "Local studio instructor to running own yoga school or international retreats; online courses create passive income"},
        "growth_outlook": "Excellent — global yoga market growing rapidly; India's soft power makes Indian yoga teachers highly sought internationally",
        "work_style": ["Physical", "Teaching", "Flexible / Self-employed"],
        "required_skills": [
            s("Asana Practice & Alignment", "critical"), s("Pranayama & Breathwork", "critical"),
            s("Teaching Methodology", "critical"), s("Anatomy & Physiology for Yoga", "important"),
            s("Meditation & Mindfulness", "important"), s("Communication", "critical"),
        ],
        "entry_paths": [
            "Complete a 200-hour Yoga Teacher Training (YTT) from a Yoga Alliance-registered school",
            "Progress to 300-hour or 500-hour advanced training",
            "Teach at a local studio while building experience and an online following",
            "Specialise in yoga therapy (for rehabilitation), prenatal yoga, kids' yoga, or corporate wellness",
        ],
        "qualifications": [
            "200-hour YTT (Yoga Teacher Training) from Yoga Alliance-registered school",
            "Yoga Alliance RYT-200 or RYT-500 registration (recognised internationally)",
            "MDNIY (Morarji Desai National Institute of Yoga) diploma — government-recognised",
            "300-hour advanced TT or C-IAYT (Certified International Association of Yoga Therapists) for yoga therapy",
        ],
        "tags": ["yoga", "wellness", "instructor", "mindfulness", "health"],
    },

    # ─── SPORTS — USA ─────────────────────────────────────
    {
        "id": "us_personal_trainer",
        "title": "Personal Trainer / Fitness Coach",
        "category": "Sports & Athletics",
        "region": "US",
        "description": "Design and deliver personalised fitness programmes for clients in gyms, studios, homes, and online platforms. The US fitness industry exceeds $35 billion annually and employs over 300,000 personal trainers. Specialisations include strength and conditioning, corrective exercise, sports performance, weight loss, and online coaching. Top trainers build six-figure coaching businesses.",
        "salary_range": {"min": 35000, "max": 120000, "currency": "USD/year", "note": "Gym floor trainer to elite private trainer; online coaching can far exceed these figures"},
        "growth_outlook": "Good — BLS projects 14% job growth 2022-2032; online fitness accelerating",
        "work_style": ["Physical", "Client-facing", "Flexible hours"],
        "required_skills": [
            s("Exercise Programming", "critical"), s("Anatomy & Physiology", "critical"),
            s("Nutrition Basics", "important"), s("Client Assessment & Goal Setting", "critical"),
            s("Communication & Motivation", "critical"), s("CPR / AED", "critical"),
        ],
        "entry_paths": [
            "Earn NASM, ACE, ACSM, or NSCA-CPT certification (nationally recognised)",
            "Get CPR / AED certified (required by most gyms)",
            "Start at a commercial gym (Planet Fitness, Equinox, LA Fitness) as a floor trainer",
            "Build an online coaching brand through social media and platforms like Trainerize or TrueCoach",
        ],
        "qualifications": [
            "NASM CPT, ACE CPT, ACSM-CPT, or NSCA CSCS certification",
            "CPR / AED certification (mandatory for employment)",
            "Bachelor's in Kinesiology, Exercise Science, or Sports Management (advantageous)",
        ],
        "tags": ["personal-trainer", "fitness", "gym", "wellness", "coaching"],
    },
    {
        "id": "us_sports_coach",
        "title": "Sports Coach / Athletic Director",
        "category": "Sports & Athletics",
        "region": "US",
        "description": "Coach amateur, collegiate, or professional athletes in a specific sport. High school coaches double as teachers; college coaches are full-time with multi-million dollar salaries at major programmes; professional coaches earn the highest. NFL, NBA, MLB, NHL, MLS, and Olympics pipeline coaches are the pinnacle — but the majority of coaches work in schools and community programmes.",
        "salary_range": {"min": 35000, "max": 500000, "currency": "USD/year", "note": "High school coach (often with teacher salary) to Division I / professional head coach; top NFL/NBA head coaches earn $5M+"},
        "growth_outlook": "Stable — steady demand at school, college, and community levels",
        "work_style": ["Physical", "Mentoring", "Irregular hours / Travel"],
        "required_skills": [
            s("Sport-Specific Technical Expertise", "critical"), s("Athlete Development", "critical"),
            s("Leadership & Motivation", "critical"), s("Game Strategy & Film Study", "important"),
            s("Recruitment (college level)", "important"), s("Communication", "critical"),
        ],
        "entry_paths": [
            "Play sport at a high level (collegiate or professional) — the most common pathway",
            "Earn a bachelor's in Physical Education, Kinesiology, or a relevant sport science",
            "Get state coaching certification or NSCA CSCS for strength & conditioning",
            "Start as an assistant coach and work up to head coach at school or college level",
        ],
        "qualifications": [
            "Bachelor's in Physical Education, Kinesiology, or related field",
            "State coaching certification (required for high school coaches in most states)",
            "NSCA CSCS (Certified Strength and Conditioning Specialist) for collegiate and pro levels",
            "First Aid / CPR certification (universally required)",
        ],
        "tags": ["coach", "sports", "athletics", "collegiate", "nfl-nba"],
    },

    # ══════════════════════════════════════════════════════
    # MUSIC INDUSTRY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "musician_vocalist_in",
        "title": "Musician / Vocalist (Classical & Playback)",
        "category": "Music Industry",
        "region": "IN",
        "description": "Perform as a vocalist or instrumentalist in classical (Hindustani or Carnatic), film (playback singing), pop, folk, or devotional music. Bollywood playback singing and Carnatic / Hindustani classical concerts are two distinct career streams. The digital era has opened Spotify, YouTube music, Instagram Reels, and brand deals as income streams for independent artists. Earning potential is enormous at the top but highly variable.",
        "salary_range": {"min": 15000, "max": 5000000, "currency": "INR/month", "note": "Local event musician to A-list Bollywood playback singer or classical maestro; digital royalties supplement"},
        "growth_outlook": "Growing — streaming platforms (Spotify, Gaana, JioSaavn) and YouTube creating new income paths for independent artists",
        "work_style": ["Creative", "Performance-based", "Self-directed"],
        "required_skills": [
            s("Vocal Training / Instrumental Proficiency", "critical"), s("Sur (pitch) & Taal (rhythm)", "critical"),
            s("Raga Knowledge (for classical)", "critical"), s("Recording Studio Etiquette", "important"),
            s("Music Theory", "important"), s("Performance & Stage Presence", "critical"),
        ],
        "entry_paths": [
            "Begin classical vocal or instrumental training from childhood under a guru (guru-shishya parampara)",
            "Enrol in a formal music programme (BM / MMus at Gandharva Mahavidyalaya, Prayag Sangeet Samiti, or university music departments)",
            "Pursue playback singing by networking with music directors and recording studios in Mumbai",
            "Build an audience on YouTube, Instagram, and Spotify as an independent artist",
            "Perform at sabhas (classical concerts), mehfils, and corporate events for regular income",
        ],
        "qualifications": [
            "Sangeet Visharad or Sangeet Alankar (classical music diploma — Gandharva, Prayag, Bhatkhande)",
            "BM / BMus from a university or music college",
            "ABRSM Grade exams (for Western music / instruments)",
            "No formal qualification required to pursue independent / digital music career",
        ],
        "tags": ["music", "singer", "vocalist", "classical", "bollywood"],
    },
    {
        "id": "music_producer_in",
        "title": "Music Producer / Composer",
        "category": "Music Industry",
        "region": "IN",
        "description": "Compose original music and produce audio tracks for Bollywood films, web series (Netflix, Prime Video), ads, independent artists, and content creators. Modern music production is largely software-driven — using DAWs (Digital Audio Workstations) like FL Studio, Ableton, and Logic Pro. India's film music industry is one of the world's largest, and the independent music scene on streaming platforms is growing rapidly.",
        "salary_range": {"min": 30000, "max": 2000000, "currency": "INR/month", "note": "Junior composer / jingle maker to A-list Bollywood composer (AR Rahman, Pritam level — worth crores)"},
        "growth_outlook": "Growing — OTT, YouTube content, gaming, and advertising creating massive demand for original music",
        "work_style": ["Creative", "Studio-based", "Freelance / Project-based"],
        "required_skills": [
            s("DAW Proficiency (FL Studio, Ableton, Logic Pro)", "critical"),
            s("Music Theory & Composition", "critical"), s("Sound Design & Mixing", "critical"),
            s("MIDI Programming", "important"), s("Client Brief Interpretation", "important"),
            s("Ear Training", "critical"),
        ],
        "entry_paths": [
            "Learn music production through formal courses (Swarnabhoomi Academy, True School of Music, Mumbai) or online (Coursera, Berklee Online)",
            "Build a portfolio of original compositions and beats — share on SoundCloud, Instagram, YouTube",
            "Assist established music directors in Bollywood or independent music studios",
            "Score for short films, ads, YouTube channels to build reel and network",
        ],
        "qualifications": [
            "Diploma or degree in Music Production / Audio Engineering (True School, Swarnabhoomi, or online platforms)",
            "No formal degree required if portfolio is strong — industry is portfolio-first",
            "ABRSM / Trinity Grade 8 theory (helpful foundation for formal music knowledge)",
        ],
        "tags": ["music-producer", "composer", "bollywood", "daw", "audio"],
    },
    {
        "id": "sound_engineer_in",
        "title": "Sound Engineer / Audio Engineer",
        "category": "Music Industry",
        "region": "IN",
        "description": "Record, mix, and master audio for music albums, films, TV shows, advertisements, and live events. Sound engineers work in recording studios, film production houses, broadcast channels, and as live sound engineers at concerts and events. Dolby Atmos and spatial audio for streaming platforms are growing specialisations. India's largest studios are in Mumbai, Chennai, and Hyderabad.",
        "salary_range": {"min": 25000, "max": 300000, "currency": "INR/month", "note": "Studio assistant engineer to chief mixing engineer for film or top recording studio; live sound engineers vary by event size"},
        "growth_outlook": "Stable — film, OTT, and live events sustaining steady demand; Dolby/spatial audio a growing niche",
        "work_style": ["Studio-based", "Technical", "Irregular hours"],
        "required_skills": [
            s("DAW Proficiency (Pro Tools, Logic, Nuendo)", "critical"),
            s("Microphone Placement & Recording Techniques", "critical"),
            s("Mixing & Mastering", "critical"), s("Signal Chain & Studio Gear", "critical"),
            s("Acoustic Treatment Knowledge", "important"), s("Communication with Artists", "important"),
        ],
        "entry_paths": [
            "Obtain a diploma or degree in Audio Engineering or Sound Design",
            "Join a recording studio as a studio assistant / intern",
            "Work under an experienced mixing engineer for 2-3 years before solo mixing",
            "Specialise in live sound for events to build a parallel income stream",
        ],
        "qualifications": [
            "Diploma in Audio Engineering / Sound Design (SAE Institute India, Swarnabhoomi, Furtados School of Music, Berklee India Exchange)",
            "Pro Tools operator certification (Avid Pro Tools — industry standard certification)",
            "Dolby Atmos for Music production certificate (growing in demand for streaming)",
        ],
        "tags": ["sound-engineer", "audio", "mixing", "recording-studio", "film"],
    },

    # ─── MUSIC — USA ──────────────────────────────────────
    {
        "id": "us_music_producer",
        "title": "Music Producer / Recording Artist",
        "category": "Music Industry",
        "region": "US",
        "description": "Create, arrange, and produce music for record labels, streaming platforms, film soundtracks, video games, and advertising. The US music industry generates over $15 billion annually. Producers work with artists in studios, remotely, or independently releasing their own music. Streaming royalties, sync licensing (placing music in film/TV/ads), and live performance are the main income streams.",
        "salary_range": {"min": 40000, "max": 500000, "currency": "USD/year", "note": "Staff producer at a smaller label to platinum-hit independent producer; sync licences can generate significant passive income"},
        "growth_outlook": "Stable — streaming growth sustaining; sync licensing booming with content explosion on Netflix, Amazon, Disney+",
        "work_style": ["Creative", "Studio-based", "Freelance / Project-based"],
        "required_skills": [
            s("DAW Proficiency (Pro Tools, Ableton, Logic)", "critical"),
            s("Music Theory & Arrangement", "critical"), s("Sound Design & Mixing", "critical"),
            s("Artist Direction & Communication", "important"), s("Music Business Knowledge", "important"),
        ],
        "entry_paths": [
            "Earn a degree in Music Production / Audio Engineering (Berklee, Full Sail, SAE, NYU)",
            "Or self-teach with online resources and build a portfolio of tracks",
            "Network by assisting in established studios and collaborating with independent artists",
            "Place music in films, ads, and shows (sync licensing) for steady royalty income",
        ],
        "qualifications": [
            "Bachelor's in Music Production, Audio Engineering, or Music Business (Berklee, Full Sail, NYU)",
            "No formal degree required if portfolio is strong — industry values catalogue over credentials",
            "Pro Tools certification (Avid — widely recognised for studio work)",
        ],
        "tags": ["music-producer", "audio", "daw", "recording", "sync-licensing"],
    },

    # ══════════════════════════════════════════════════════
    # GAMING & ESPORTS — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "game_developer_in",
        "title": "Game Developer (Mobile / PC / Console)",
        "category": "Gaming & Esports",
        "region": "IN",
        "description": "Design and build video games for mobile (Android / iOS), PC, or console platforms. India's gaming industry is the second-fastest growing in the world — with companies like Nazara, Junglee Games, nCore Games, and dozens of studios hiring Unity and Unreal developers. Mobile gaming dominates, but PC/console studios (with global publishers) are growing. Game developers specialise as programmers, artists, designers, or audio engineers.",
        "salary_range": {"min": 40000, "max": 400000, "currency": "INR/month", "note": "Junior developer at a mid-sized studio to senior engineer at Nazara or a global publisher's India office"},
        "growth_outlook": "Very strong — India gaming market projected to reach $7B by 2026; mobile-first expansion rapid",
        "work_style": ["Technical", "Creative", "Team-based"],
        "required_skills": [
            s("Unity or Unreal Engine", "critical"), s("Programming (C# or C++)", "critical"),
            s("Game Design Principles", "important"), s("3D Math & Physics", "important"),
            s("Version Control (Git)", "critical"), s("Problem Solving", "critical"),
        ],
        "entry_paths": [
            "Bachelor's in Computer Science, IT, or Game Development (Manipal, MIT Pune, Srishti Manipal, MAAC)",
            "Self-study Unity / Unreal + build a portfolio of prototype games on itch.io and GitHub",
            "Join a game jam (Global Game Jam, Ludum Dare) to build prototypes and network",
            "Apply to studios (Nazara, Dhruva Interactive, nCore, 99Games) as junior developer with portfolio",
        ],
        "qualifications": [
            "Bachelor's in Computer Science, IT, or Game Design",
            "Unity Certified Associate or Unity Certified Professional certification",
            "Unreal Engine certification from Epic Games Online Learning (for UE projects)",
        ],
        "tags": ["game-dev", "unity", "unreal", "mobile-gaming", "gaming"],
    },
    {
        "id": "esports_player_in",
        "title": "Esports Player / Pro Gamer",
        "category": "Gaming & Esports",
        "region": "IN",
        "description": "Compete professionally in multiplayer video games — BGMI (Battlegrounds Mobile India), Free Fire, Valorant, CS2, DOTA 2, and mobile games — for prize money, team salaries, and brand sponsorships. India's esports ecosystem is growing rapidly with ESFed recognition, ESports Federation of India, and investment from brands like Paytm, Moto, and MPL. Star players earn through salaries, streaming, and brand deals.",
        "salary_range": {"min": 15000, "max": 500000, "currency": "INR/month", "note": "Entry team player to top BGMI or Valorant pro with salary + streaming income + brand deals"},
        "growth_outlook": "Growing — India's esports industry growing 50%+ annually; BGMI and Valorant tournaments multiplying",
        "work_style": ["Digital", "Competitive", "Team-based", "Online"],
        "required_skills": [
            s("Game Mastery (specific title)", "critical"), s("Game Sense & Strategy", "critical"),
            s("Team Communication", "critical"), s("Mental Resilience", "critical"),
            s("Reflexes & Reaction Time", "critical"), s("Streaming & Content Creation", "helpful"),
        ],
        "entry_paths": [
            "Reach top ranks in your game (Immortal/Radiant in Valorant, Conqueror in BGMI)",
            "Join an open team or amateur tournament circuit to build a track record",
            "Apply to esports organisations (S8UL, Team XO, Orangutan, GodLike) for trials",
            "Build a streaming audience on YouTube / Twitch alongside playing career",
        ],
        "qualifications": [
            "No formal qualification required",
            "In-game ranking (top 1-5% in ranked matches is typically the entry threshold for pro trials)",
            "ESFed-registered player ID for official Indian esports competitions",
        ],
        "tags": ["esports", "pro-gamer", "bgmi", "valorant", "streaming"],
    },
    {
        "id": "game_designer_in",
        "title": "Game Designer / UX Designer (Games)",
        "category": "Gaming & Esports",
        "region": "IN",
        "description": "Design the rules, mechanics, levels, narrative, and player experience of a video game. Game designers bridge creative vision and technical implementation, working closely with programmers and artists. India's growing game studios need designers who understand mobile game monetisation (IAP, ad models), player psychology, and Indian cultural context for India-first game designs.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "INR/month", "note": "Junior designer at a mobile studio to lead game designer at a funded startup or global studio"},
        "growth_outlook": "Strong — India's mobile game design talent in demand locally and globally",
        "work_style": ["Creative", "Collaborative", "Iterative"],
        "required_skills": [
            s("Game Mechanics & Systems Design", "critical"), s("Level Design", "important"),
            s("Player Psychology & Engagement", "critical"), s("Prototyping (Figma, Unity)", "important"),
            s("Documentation (GDD — Game Design Document)", "critical"), s("Monetisation Design", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Game Design, Interaction Design, or Computer Science (Srishti Manipal, MIT ID, MAAC)",
            "Build a portfolio of game design documents and prototype games",
            "Play and analyse a wide variety of games critically — understand what makes mechanics work",
            "Start as a junior designer at a mobile game studio and specialise (level design, narrative, economy)",
        ],
        "qualifications": [
            "Bachelor's in Game Design, UX Design, or Computer Science",
            "Unity / Unreal prototyping skills (self-taught or from online platforms)",
            "Online game design courses from Coursera (CalArts), edX (MIT), or Udemy",
        ],
        "tags": ["game-design", "ux", "level-design", "gaming", "mobile-games"],
    },

    # ─── GAMING — USA ─────────────────────────────────────
    {
        "id": "us_game_developer",
        "title": "Game Developer / Software Engineer (Games)",
        "category": "Gaming & Esports",
        "region": "US",
        "description": "Build video games for console, PC, mobile, and VR platforms. The US is the world's largest game market — with studios like Blizzard, Naughty Dog, Rockstar, and EA employing thousands of engineers. Specialisations include gameplay programming, engine development, AI, graphics engineering, and tools programming. Indie game development is also a viable path through Steam and Epic's self-publishing tools.",
        "salary_range": {"min": 80000, "max": 250000, "currency": "USD/year", "note": "Junior developer at a mid-sized studio to senior engineer at AAA studios like EA, Activision, or Naughty Dog"},
        "growth_outlook": "Good — US gaming market exceeding $60B; mobile, cloud gaming, and VR expanding",
        "work_style": ["Technical", "Creative", "Team-based"],
        "required_skills": [
            s("C++ or C# Programming", "critical"), s("Unreal Engine or Unity", "critical"),
            s("Algorithms & Data Structures", "critical"), s("Game Physics & Math", "important"),
            s("Version Control (Perforce or Git)", "critical"), s("Debugging & Profiling", "critical"),
        ],
        "entry_paths": [
            "Bachelor's in Computer Science, Game Development, or Software Engineering (Full Sail, DigiPen, USC, CMU)",
            "Build a strong portfolio: two or three polished game projects hosted on GitHub and itch.io",
            "Contribute to open-source game projects or create game mods for popular engines",
            "Apply to AAA studios, indie publishers, or game-adjacent tech (Unity, Epic Games) for junior roles",
        ],
        "qualifications": [
            "Bachelor's in Computer Science, Game Development, or Software Engineering",
            "Unity Certified Professional or Unreal Engine certification",
            "Strong portfolio of shipped or prototype games (GitHub + playable builds)",
        ],
        "tags": ["game-dev", "unity", "unreal", "c-plus-plus", "gaming"],
    },
    {
        "id": "us_esports_coach",
        "title": "Esports Coach / Analyst",
        "category": "Gaming & Esports",
        "region": "US",
        "description": "Develop, analyse, and coach competitive esports teams in games like League of Legends, CS2, Valorant, and Rocket League. Collegiate esports programmes at over 100 US universities have created structured coaching roles. Professional organisations in LCS (League of Legends), CDL (Call of Duty), OWL (Overwatch), and VCT (Valorant Champions Tour) hire full coaching staffs. Analysts break down opponent data; coaches run team strategy and mental performance.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "USD/year", "note": "Collegiate assistant coach to head coach of a professional LCS or CDL franchise"},
        "growth_outlook": "Growing — collegiate esports expanding rapidly; professional league rosters demand structured coaching staff",
        "work_style": ["Digital", "Analytical", "Team-based", "Remote / LAN"],
        "required_skills": [
            s("Deep Game Knowledge (specific title)", "critical"), s("Data & Video Analysis", "critical"),
            s("Team Communication & Psychology", "critical"), s("Strategy & Draft / Meta Understanding", "critical"),
            s("Coaching Methodology", "important"), s("Performance Analytics Tools", "helpful"),
        ],
        "entry_paths": [
            "Reach a high competitive rank in the target game (challenger/radiant level)",
            "Coach amateur or university teams to build a track record",
            "Apply to Collegiate Esports leagues (NACE, NASEF) for university team coaching positions",
            "Network within the esports ecosystem through events, Discord communities, and league portals",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "High competitive rank in the game you coach (demonstrable)",
            "Esports management certificate from NACE Scholastic or Coursera esports programmes",
            "A coaching portfolio: documented results from teams coached",
        ],
        "tags": ["esports", "coach", "gaming", "valorant", "collegiate"],
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
