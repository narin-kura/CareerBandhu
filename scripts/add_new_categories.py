"""Add 5 new categories: Mythology & Culture, Film & Entertainment,
Animation Industry, Mental Health & Therapy, Entrepreneurship & MSME"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # MYTHOLOGY & CULTURE
    # ══════════════════════════════════════════════════════
    {
        "id": "mythologist_in",
        "title": "Mythologist & Cultural Researcher",
        "category": "Mythology & Culture",
        "region": "IN",
        "description": "Study, interpret, and communicate India's rich mythological traditions — from the Vedas, Puranas, and epics to folk traditions and regional lore. Mythologists work as authors, speakers, media consultants, academics, and cultural advisors for films, brands, and museums.",
        "salary_range": {"min": 30000, "max": 300000, "currency": "INR/month", "note": "Author/speaker income varies widely; academic roles ₹50k+"},
        "growth_outlook": "Growing — mythology content is booming on social media, OTT, and publishing",
        "work_style": ["Research-driven", "Creative", "Remote-friendly"],
        "required_skills": [
            s("Indian Mythology & Epics", "critical"), s("Research", "critical"),
            s("Writing & Storytelling", "critical"), s("Public Speaking", "important"),
            s("Sanskrit / Ancient Languages", "helpful"), s("Teaching", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in History, Sanskrit, Philosophy, or Religious Studies",
            "Master's / PhD in Indology, Comparative Religion, or Cultural Studies",
            "Build a public following through books, podcasts, YouTube, or speaking",
            "Consult for films, OTT, and brands needing cultural/mythological accuracy",
        ],
        "qualifications": [
            "Bachelor's in History / Sanskrit / Philosophy / Religious Studies",
            "MA or PhD in Indology, Comparative Religion, or Cultural Studies (preferred)",
            "NET / SET for academic teaching positions",
        ],
        "tags": ["mythology", "culture", "research", "writing", "academia"],
    },
    {
        "id": "heritage_museum_professional",
        "title": "Heritage & Museum Professional",
        "category": "Mythology & Culture",
        "region": "IN",
        "description": "Preserve, curate, and communicate India's historical and cultural heritage through museums, archaeological sites, archives, and cultural institutions. Roles include museum curator, archaeologist, conservator, and heritage tourism specialist.",
        "salary_range": {"min": 30000, "max": 150000, "currency": "INR/month", "note": "Government curator to private museum director"},
        "growth_outlook": "Stable — growing heritage tourism and government investment in culture",
        "work_style": ["Research-driven", "Field & office", "Public engagement"],
        "required_skills": [
            s("Cultural Knowledge", "critical"), s("Research", "critical"),
            s("Documentation", "important"), s("Communication", "important"),
            s("Archaeology / Conservation basics", "helpful"), s("Photography", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in History, Archaeology, Museology, or Fine Arts",
            "MA in Museology or Archaeology (NMI / Baroda / JNU / Hyderabad University)",
            "Internship at ASI (Archaeological Survey of India) or state museums",
            "Government: UPSC / State PSC museum services; Private: cultural foundations",
        ],
        "qualifications": [
            "Bachelor's in History / Archaeology / Fine Arts / Museology",
            "MA in Museology or Archaeology (National Museum Institute preferred)",
            "ASI (Archaeological Survey of India) training programs",
            "UPSC / State PSC exam for government heritage department posts",
        ],
        "tags": ["heritage", "museum", "archaeology", "culture", "preservation"],
    },

    {
        "id": "archaeologist_in",
        "title": "Archaeologist",
        "category": "Mythology & Culture",
        "region": "IN",
        "description": "Excavate and study physical remains of past civilisations — ancient cities, temples, artefacts, and burial sites — to reconstruct India's history. Archaeologists work with the Archaeological Survey of India (ASI), universities, state archaeology departments, and international research projects.",
        "salary_range": {"min": 30000, "max": 100000, "currency": "INR/month", "note": "State/ASI scale; senior/project archaeologists earn more"},
        "growth_outlook": "Stable — ASI, state depts, and university research positions; heritage tourism growing",
        "work_style": ["Fieldwork & research", "Physical", "Academic"],
        "required_skills": [
            s("Excavation Techniques", "critical"), s("Artefact Analysis", "critical"),
            s("Research", "critical"), s("Report Writing", "important"),
            s("Historical Knowledge", "critical"), s("GIS / Mapping", "helpful"),
            s("Photography & Documentation", "helpful"),
        ],
        "entry_paths": [
            "BA in History or Archaeology (3 years)",
            "MA in Archaeology (universities: DU, JNU, BHU, Deccan College Pune)",
            "PhD for academic and senior research roles",
            "ASI recruitment through UPSC / SSC exams for government archaeologist posts",
            "Fieldwork internships with ASI or university excavation projects",
        ],
        "qualifications": [
            "MA in Archaeology (Deccan College Pune, JNU, BHU, DU — top institutions)",
            "PhD for academic / senior research positions",
            "UPSC / SSC exam for ASI (Archaeological Survey of India) government posts",
            "NET / SET for university teaching positions",
        ],
        "tags": ["archaeology", "heritage", "culture", "asi", "history"],
    },
    {
        "id": "us_archaeologist",
        "title": "Archaeologist",
        "category": "Mythology & Culture",
        "region": "US",
        "description": "Investigate past cultures through excavation, artefact analysis, and historical research. US archaeologists work in Cultural Resource Management (CRM — the largest employer), academia, federal agencies (NPS, BLM, Army Corps), and museums. CRM archaeology supports construction and land development projects.",
        "salary_range": {"min": 45000, "max": 90000, "currency": "USD/year", "note": "CRM field tech to senior project archaeologist; faculty varies"},
        "growth_outlook": "Stable — CRM is steady; federal and academic opportunities competitive",
        "work_style": ["Fieldwork & lab", "Research", "Outdoor"],
        "required_skills": [
            s("Excavation Techniques", "critical"), s("Artefact Analysis", "critical"),
            s("Research", "critical"), s("Technical Report Writing", "critical"),
            s("GIS / GPS / Mapping", "important"), s("Section 106 / NHPA compliance", "helpful"),
        ],
        "entry_paths": [
            "BA in Anthropology or Archaeology",
            "Field school experience (mandatory for most CRM jobs)",
            "MA or PhD for senior project management and academic roles",
            "Register with SAA (Society for American Archaeology)",
            "RPA — Register of Professional Archaeologists for senior credentials",
        ],
        "qualifications": [
            "BA in Anthropology / Archaeology + field school (entry-level CRM)",
            "MA or PhD in Anthropology / Archaeology (for senior and academic roles)",
            "RPA — Register of Professional Archaeologists (professional credential)",
            "36 CFR Part 63 qualification standards for federal agency positions",
        ],
        "tags": ["archaeology", "crm", "anthropology", "heritage", "federal"],
    },

    # ══════════════════════════════════════════════════════
    # FILM & ENTERTAINMENT — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "film_director_in",
        "title": "Film Director",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Lead the creative vision of a film — guiding actors, cinematographers, and the entire crew from script to screen. India has one of the world's largest film industries (Bollywood, Tollywood, Kollywood, etc.), offering opportunities across languages and formats including OTT originals.",
        "salary_range": {"min": 50000, "max": 2000000, "currency": "INR/month", "note": "Assistant director to established director; huge variance"},
        "growth_outlook": "Strong — OTT boom creating massive demand for directors across languages",
        "work_style": ["Creative", "High-pressure", "Project-based"],
        "required_skills": [
            s("Storytelling", "critical"), s("Leadership", "critical"),
            s("Creative Vision", "critical"), s("Communication", "critical"),
            s("Script Analysis", "important"), s("Production Management", "important"),
            s("Knowledge of Cinema", "important"),
        ],
        "entry_paths": [
            "Film school: FTII (Pune), Satyajit Ray Film Institute, or private institutes",
            "Begin as an assistant director (AD) on sets — most common route",
            "Build short films / web series independently",
            "Transition from acting, writing, or other film departments",
        ],
        "qualifications": [
            "Diploma / Degree in Film Direction (FTII, SRFTI, Whistling Woods, LV Prasad)",
            "No mandatory qualification — strong portfolio of short films / ADs widely accepted",
            "FTII / SRFTI entrance exam for government film institutes",
        ],
        "tags": ["film", "bollywood", "ott", "creative", "director"],
    },
    {
        "id": "screenwriter_in",
        "title": "Screenwriter / Story Writer",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Craft the stories, dialogues, and scripts that power India's vast film and OTT industry. From feature films and web series to ad films and documentaries, skilled screenwriters are in strong demand as OTT platforms hunger for compelling original content.",
        "salary_range": {"min": 40000, "max": 500000, "currency": "INR/month", "note": "Freelance dialogue writer to credited feature film writer"},
        "growth_outlook": "Strong — OTT platforms driving unprecedented demand for original scripts",
        "work_style": ["Creative", "Remote-friendly", "Deadline-driven"],
        "required_skills": [
            s("Creative Writing", "critical"), s("Storytelling", "critical"),
            s("Character Development", "critical"), s("Dialogue Writing", "critical"),
            s("Script Formatting", "important"), s("Research", "helpful"),
        ],
        "entry_paths": [
            "Write spec scripts and short films to build a portfolio",
            "Join scriptwriting workshops (FTII, Film Companion, Screenplay Studio India)",
            "Assist established writers; join writers' rooms on OTT productions",
            "Transition from journalism, fiction writing, or theatre",
        ],
        "qualifications": [
            "Bachelor's in English / Creative Writing / Journalism (preferred, not mandatory)",
            "Screenplay writing certificate courses (FTII, Whistling Woods)",
            "Published portfolio of scripts or produced work is the real credential",
        ],
        "tags": ["screenwriting", "film", "ott", "creative", "writing"],
    },
    {
        "id": "cinematographer_in",
        "title": "Cinematographer / Director of Photography",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Shape the visual language of a film — controlling camera, lighting, composition, and color to bring a director's vision to life. The DoP (Director of Photography) is one of the most creative and technically demanding roles in filmmaking.",
        "salary_range": {"min": 50000, "max": 1000000, "currency": "INR/month", "note": "Camera assistant to established DoP; project-based income"},
        "growth_outlook": "Strong — growing OTT, ad film, and documentary sectors",
        "work_style": ["Creative", "Physical", "Project-based"],
        "required_skills": [
            s("Camera Operation", "critical"), s("Lighting Design", "critical"),
            s("Visual Storytelling", "critical"), s("Color Grading", "important"),
            s("Technical Equipment Knowledge", "important"), s("Creativity", "critical"),
        ],
        "entry_paths": [
            "Film school: FTII / SRFTI cinematography specialization",
            "Start as camera assistant / clapper loader / focus puller",
            "Shoot short films, music videos, and ads to build a reel",
            "Progress from camera department: AC → Camera Operator → DoP",
        ],
        "qualifications": [
            "Diploma / Degree in Cinematography (FTII, SRFTI, Whistling Woods)",
            "No mandatory degree — strong showreel and camera department experience accepted",
            "FTII / SRFTI entrance exam for government film schools",
        ],
        "tags": ["cinematography", "film", "camera", "creative", "dop"],
    },
    {
        "id": "film_editor_in",
        "title": "Film Editor",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Shape the final story of a film by assembling footage, pacing scenes, and collaborating with the director to craft the definitive cut. Film editors work on features, documentaries, web series, and ad films — often called the 'invisible director'.",
        "salary_range": {"min": 40000, "max": 500000, "currency": "INR/month", "note": "Editing assistant to senior film editor"},
        "growth_outlook": "Strong — OTT content boom creating abundant editing work",
        "work_style": ["Detailed", "Remote-friendly", "Creative"],
        "required_skills": [
            s("Video Editing", "critical"), s("Storytelling", "critical"),
            s("Premiere Pro / Avid / DaVinci Resolve", "critical"),
            s("Sound Design basics", "important"), s("Color Grading basics", "helpful"),
            s("Attention to Detail", "critical"),
        ],
        "entry_paths": [
            "Film school editing department (FTII, SRFTI, Whistling Woods)",
            "Start as an editing assistant on productions",
            "Edit short films, YouTube content, and web series independently",
            "Learn Avid / Premiere / DaVinci through online courses and self-practice",
        ],
        "qualifications": [
            "Diploma / Degree in Film Editing (FTII, SRFTI or equivalent)",
            "Self-taught + strong portfolio of edited work widely accepted",
            "Avid Media Composer or Adobe Premiere Pro certification (optional)",
        ],
        "tags": ["film", "editing", "post-production", "ott", "creative"],
    },
    {
        "id": "vfx_artist_in",
        "title": "VFX / Visual Effects Artist",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Create the visual magic that transforms ordinary footage into extraordinary cinema — from CGI creatures and digital environments to matte paintings and motion graphics. India's VFX industry services both Bollywood and Hollywood productions.",
        "salary_range": {"min": 35000, "max": 400000, "currency": "INR/month", "note": "Junior VFX artist to senior compositor / CG supervisor"},
        "growth_outlook": "Very strong — Indian VFX studios servicing global productions",
        "work_style": ["Technical & creative", "Studio-based", "Project deadlines"],
        "required_skills": [
            s("3D Modeling / Animation", "important"), s("Compositing", "critical"),
            s("After Effects / Nuke", "critical"), s("Maya / Houdini / Blender", "important"),
            s("Color Science", "helpful"), s("Attention to Detail", "critical"),
        ],
        "entry_paths": [
            "Diploma / Degree in VFX or Animation (Arena, MAAC, DSK Supinfocom, MAAC)",
            "Learn through online courses (Udemy, fxphd, CGMA)",
            "Build a demo reel and apply to VFX studios (Prana, DQ Entertainment, DNEG India)",
            "Start in junior/tracking roles and grow to compositing or CG supervision",
        ],
        "qualifications": [
            "Diploma / Degree in VFX, Animation, or Computer Graphics",
            "Arena Animation / MAAC / DQ Supinfocom certification programs",
            "Strong VFX demo reel is the primary credential for employment",
        ],
        "tags": ["vfx", "animation", "film", "visual-effects", "cgi"],
    },
    {
        "id": "film_producer_in",
        "title": "Film Producer",
        "category": "Film & Entertainment",
        "region": "IN",
        "description": "Bring a film from concept to screen by managing financing, assembling the team, overseeing production, and driving distribution. Producers are the business architects of cinema — they manage budgets, negotiate deals, and make the film financially viable.",
        "salary_range": {"min": 60000, "max": 3000000, "currency": "INR/month", "note": "Associate producer to independent producer; highly variable"},
        "growth_outlook": "Strong — OTT and regional cinema expansion creating new production opportunities",
        "work_style": ["High-pressure", "Networking-heavy", "Project-based"],
        "required_skills": [
            s("Project Management", "critical"), s("Financial Management", "critical"),
            s("Networking", "critical"), s("Communication", "critical"),
            s("Negotiation", "important"), s("Knowledge of Cinema", "important"),
            s("Leadership", "important"),
        ],
        "entry_paths": [
            "Film school production management programs",
            "Start as a production assistant or associate producer",
            "Enter from business / finance background and partner with creative talent",
            "Self-produce short films / web series to build credibility",
        ],
        "qualifications": [
            "Bachelor's in Film Production, Business, or any field",
            "MBA (optional but useful for large-scale production companies)",
            "Film production certification (Whistling Woods, FTII production course)",
            "No mandatory qualification — track record of produced content is the credential",
        ],
        "tags": ["film", "production", "entertainment", "business", "bollywood"],
    },

    # ══════════════════════════════════════════════════════
    # FILM & ENTERTAINMENT — USA
    # ══════════════════════════════════════════════════════
    {
        "id": "us_film_director",
        "title": "Film Director",
        "category": "Film & Entertainment",
        "region": "US",
        "description": "Lead the creative and artistic vision of a film or TV project in one of the world's most competitive entertainment markets. US directors work across Hollywood features, independent cinema, streaming originals (Netflix, HBO, Amazon), and commercials.",
        "salary_range": {"min": 80000, "max": 500000, "currency": "USD/year", "note": "Indie director to mid-tier studio director; A-list directors earn millions"},
        "growth_outlook": "Strong — streaming platforms commissioning more original content than ever",
        "work_style": ["Creative", "High-pressure", "Project-based"],
        "required_skills": [
            s("Storytelling", "critical"), s("Leadership", "critical"),
            s("Creative Vision", "critical"), s("Communication", "critical"),
            s("Script Analysis", "important"), s("Production Management", "important"),
        ],
        "entry_paths": [
            "BFA / MFA in Film Direction from accredited film school (USC, NYU Tisch, AFI)",
            "Start as a production assistant or assistant director in the industry",
            "Direct short films, festival submissions, and branded content",
            "DGA — Directors Guild of America membership for union film sets",
        ],
        "qualifications": [
            "BFA or MFA in Film Directing (USC School of Cinematic Arts, NYU Tisch, AFI)",
            "No mandatory degree — strong portfolio of directed work widely accepted",
            "DGA membership (Directors Guild of America) for studio productions",
        ],
        "tags": ["film", "hollywood", "streaming", "creative", "director"],
    },
    {
        "id": "us_screenwriter",
        "title": "Screenwriter",
        "category": "Film & Entertainment",
        "region": "US",
        "description": "Write the scripts that become Hollywood films, TV series, and streaming originals. The WGA (Writers Guild of America) represents thousands of working writers. Breaking in is competitive but the rewards — both creative and financial — are significant.",
        "salary_range": {"min": 60000, "max": 300000, "currency": "USD/year", "note": "Staff TV writer to feature screenwriter; WGA minimums guaranteed"},
        "growth_outlook": "Strong — streaming platforms run constant writers' room demand",
        "work_style": ["Creative", "Remote-friendly", "Deadline-driven"],
        "required_skills": [
            s("Creative Writing", "critical"), s("Storytelling", "critical"),
            s("Character Development", "critical"), s("Dialogue Writing", "critical"),
            s("Script Formatting (Final Draft)", "important"), s("Pitching", "important"),
        ],
        "entry_paths": [
            "BA or MFA in Screenwriting or Creative Writing",
            "Write spec scripts and enter competitions (Nicholl Fellowship, Austin Film Festival)",
            "Work as a writer's assistant or script reader to break into writers' rooms",
            "WGA registration and eventually membership",
        ],
        "qualifications": [
            "BA / MFA in Screenwriting or Creative Writing (USC, NYU, AFI)",
            "No mandatory degree — produced credits and competition wins matter more",
            "WGA — Writers Guild of America membership (union productions)",
            "Final Draft software proficiency (industry standard)",
        ],
        "tags": ["screenwriting", "hollywood", "tv", "streaming", "writing"],
    },

    # ══════════════════════════════════════════════════════
    # ANIMATION INDUSTRY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "animator_2d_in",
        "title": "2D Animator",
        "category": "Animation Industry",
        "region": "IN",
        "description": "Create frame-by-frame or rigged 2D animation for films, TV series, educational content, advertisements, and YouTube channels. India is a global outsourcing hub for 2D animation, and domestic studios are producing acclaimed original content for platforms like Disney+, Netflix, and Doordarshan.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior animator to senior/lead animator; freelance rates vary"},
        "growth_outlook": "Strong — India's animation outsourcing + growing domestic OTT content market",
        "work_style": ["Creative", "Studio-based", "Deadline-driven"],
        "required_skills": [
            s("2D Animation Principles", "critical"), s("Toon Boom Harmony / Adobe Animate", "critical"),
            s("Character Design", "important"), s("Timing & Spacing", "critical"),
            s("Storyboarding", "helpful"), s("Drawing / Illustration", "important"),
        ],
        "entry_paths": [
            "Diploma or Degree in Animation (Arena, MAAC, Frameboxx, NIFT, NID)",
            "Build a demo reel of animated character scenes",
            "Apply to animation studios (Cosmos-Maya, Prana Studios, Green Gold)",
            "Freelance on YouTube, edtech platforms, and ad agencies to build client base",
        ],
        "qualifications": [
            "Diploma / Degree in Animation or Multimedia (Arena Animation, MAAC, Frameboxx)",
            "No mandatory qualification — strong animation reel is the real credential",
            "Toon Boom Harmony or Adobe Animate proficiency (industry standard)",
        ],
        "tags": ["animation", "2d", "creative", "ott", "film"],
    },
    {
        "id": "animator_3d_in",
        "title": "3D Character Animator",
        "category": "Animation Industry",
        "region": "IN",
        "description": "Bring 3D characters to life through movement, performance, and emotion in films, games, and advertisements. India's 3D animation sector services major global studios and is growing its own IP. Strong demand from gaming companies, VFX pipelines, and OTT productions.",
        "salary_range": {"min": 35000, "max": 400000, "currency": "INR/month", "note": "Junior to senior character animator or animation director"},
        "growth_outlook": "Very strong — gaming, OTT, and VFX driving 3D animation demand",
        "work_style": ["Creative & technical", "Studio-based", "Collaborative"],
        "required_skills": [
            s("Maya / Blender Animation", "critical"), s("12 Principles of Animation", "critical"),
            s("Character Rigging basics", "helpful"), s("Motion Capture editing", "helpful"),
            s("Timing & Weight", "critical"), s("Storytelling through movement", "important"),
        ],
        "entry_paths": [
            "Diploma / Degree in 3D Animation (MAAC, Frameboxx, Arena, DSK Supinfocom)",
            "Master Maya or Blender animation through online courses (Animation Mentor, iAnimate)",
            "Build a character animation reel (walk cycles, dialogue shots, body mechanics)",
            "Apply to VFX/animation studios or game companies (Ubisoft India, EA Sports India)",
        ],
        "qualifications": [
            "Diploma / Degree in 3D Animation or VFX",
            "Maya Certified Professional or Blender proficiency",
            "Strong animation demo reel (12 principles demonstrated)",
            "Animation Mentor or iAnimate certification (internationally recognised, optional)",
        ],
        "tags": ["animation", "3d", "maya", "blender", "gaming"],
    },
    {
        "id": "storyboard_artist_in",
        "title": "Storyboard Artist",
        "category": "Animation Industry",
        "region": "IN",
        "description": "Visualise scripts as sequential drawings that guide directors, animators, and cinematographers. Storyboard artists are essential in animation studios, ad agencies, film production houses, and game cinematics. A fast-growing role as India's animation and ad industry expands.",
        "salary_range": {"min": 30000, "max": 250000, "currency": "INR/month", "note": "Freelance per-episode to senior storyboard artist"},
        "growth_outlook": "Strong — every animation series and ad campaign needs storyboards",
        "work_style": ["Creative", "Remote-friendly", "Collaborative"],
        "required_skills": [
            s("Drawing", "critical"), s("Visual Storytelling", "critical"),
            s("Film Grammar (shot types, angles)", "critical"),
            s("Adobe Photoshop / Storyboard Pro", "important"),
            s("Speed and productivity", "important"), s("Communication", "helpful"),
        ],
        "entry_paths": [
            "Fine arts or animation degree with strong drawing skills",
            "Learn film grammar, shot composition, and storyboarding software",
            "Build a portfolio of storyboard samples for different genres",
            "Work in animation studios, ad agencies, or as a freelance storyboard artist",
        ],
        "qualifications": [
            "Diploma / Degree in Fine Arts, Animation, or Film",
            "No mandatory credential — strong drawing portfolio and story sense are key",
            "Toon Boom Storyboard Pro proficiency (industry standard)",
        ],
        "tags": ["storyboard", "animation", "film", "creative", "illustration"],
    },
    {
        "id": "motion_graphics_designer_in",
        "title": "Motion Graphics Designer",
        "category": "Animation Industry",
        "region": "IN",
        "description": "Create animated graphics, text, infographics, and visual effects for broadcast TV, YouTube, OTT title sequences, apps, and corporate presentations. One of the most in-demand animation-adjacent careers with strong job market across media, advertising, and tech.",
        "salary_range": {"min": 30000, "max": 250000, "currency": "INR/month", "note": "Junior designer to senior motion designer; freelance scales well"},
        "growth_outlook": "Very strong — every brand, media company, and app needs motion graphics",
        "work_style": ["Creative", "Remote-friendly", "Deadline-driven"],
        "required_skills": [
            s("Adobe After Effects", "critical"), s("Motion Design Principles", "critical"),
            s("Adobe Premiere Pro", "important"), s("Illustrator / Photoshop", "important"),
            s("Typography", "helpful"), s("3D (Cinema 4D / Blender)", "helpful"),
        ],
        "entry_paths": [
            "Learn After Effects through online courses (School of Motion, YouTube, Udemy)",
            "Build a motion design reel with diverse projects (logo animations, explainers, title cards)",
            "Work with ad agencies, media houses, YouTube creators, or startups",
            "Freelance through platforms like Fiverr, Upwork, and direct client acquisition",
        ],
        "qualifications": [
            "Diploma / Degree in Animation, Graphic Design, or Multimedia (preferred, not mandatory)",
            "After Effects proficiency — self-taught + portfolio widely accepted",
            "School of Motion, Motion Design School or similar course completion (helpful)",
        ],
        "tags": ["motion-graphics", "after-effects", "animation", "creative", "design"],
    },
    {
        "id": "animation_director_in",
        "title": "Animation Director",
        "category": "Animation Industry",
        "region": "IN",
        "description": "Lead the creative vision of an animated series or film — guiding animators, story artists, and production teams to ensure visual consistency, quality, and artistic coherence. Animation directors typically have 10+ years of experience across multiple animation disciplines.",
        "salary_range": {"min": 100000, "max": 800000, "currency": "INR/month", "note": "Senior role; leads major studio productions"},
        "growth_outlook": "Growing — OTT investment in original Indian animation driving senior talent demand",
        "work_style": ["Leadership", "Creative", "High-responsibility"],
        "required_skills": [
            s("Animation Expertise", "critical"), s("Creative Vision", "critical"),
            s("Leadership", "critical"), s("Communication", "critical"),
            s("Storyboarding", "important"), s("Production Management", "important"),
            s("Script Analysis", "important"),
        ],
        "entry_paths": [
            "Established career as animator or story artist (10+ years)",
            "Progress through roles: animator → lead animator → sequence supervisor → director",
            "Build leadership track record on animated series or shorts",
            "Typically promoted internally at animation studios",
        ],
        "qualifications": [
            "Degree in Animation (FTII, DSK Supinfocom, NID, Symbiosis) — usually already held",
            "10+ years of animation industry experience",
            "Production credits on animated features or series",
        ],
        "tags": ["animation", "director", "leadership", "creative", "studio"],
    },

    # ── ANIMATION INDUSTRY — USA ──────────────────────────
    {
        "id": "us_animator_3d",
        "title": "3D Animator",
        "category": "Animation Industry",
        "region": "US",
        "description": "Animate characters, creatures, and objects in 3D for feature films, TV series, games, and commercials. The US is home to the world's top animation studios — Disney, Pixar, DreamWorks, Laika, and major game companies. Competition is fierce but the career is deeply rewarding.",
        "salary_range": {"min": 65000, "max": 130000, "currency": "USD/year", "note": "Junior animator (feature) to senior animator; leads earn more"},
        "growth_outlook": "Strong — streaming and gaming maintaining strong demand for 3D animation talent",
        "work_style": ["Creative & technical", "Studio-based", "Collaborative"],
        "required_skills": [
            s("Maya / Blender / Houdini", "critical"), s("12 Principles of Animation", "critical"),
            s("Character Performance", "critical"), s("Motion Capture editing", "helpful"),
            s("Rigging basics", "helpful"), s("Portfolio presentation", "important"),
        ],
        "entry_paths": [
            "BFA in Animation from accredited school (CalArts, SVA, Ringling, SCAD)",
            "Complete Animation Mentor, iAnimate, or AnimSchool online programs",
            "Build a strong character animation reel and apply to studios",
            "Entry via games, VFX, or commercials; transition to features over time",
        ],
        "qualifications": [
            "BFA in Animation from accredited program (CalArts, Ringling, SCAD, SVA)",
            "Animation Mentor / iAnimate / AnimSchool completion (respected industry credentials)",
            "Strong demo reel — the primary hiring criterion at all studios",
            "IATSE union membership for major studio productions",
        ],
        "tags": ["animation", "3d", "pixar", "disney", "gaming"],
    },
    {
        "id": "us_motion_graphics",
        "title": "Motion Graphics Designer",
        "category": "Animation Industry",
        "region": "US",
        "description": "Design and animate visual content for broadcast, streaming, advertising, and digital media. Motion graphics is one of the most versatile and hirable animation skillsets in the US — studios, ad agencies, tech companies, and media brands all hire motion designers.",
        "salary_range": {"min": 60000, "max": 110000, "currency": "USD/year", "note": "Junior designer to senior motion designer"},
        "growth_outlook": "Strong — digital content explosion keeping demand consistently high",
        "work_style": ["Creative", "Remote-friendly", "Client-driven"],
        "required_skills": [
            s("Adobe After Effects", "critical"), s("Motion Design Principles", "critical"),
            s("Cinema 4D / Blender", "important"), s("Illustrator / Photoshop", "important"),
            s("Typography", "important"), s("Client Communication", "helpful"),
        ],
        "entry_paths": [
            "BFA in Graphic Design, Motion Design, or related (preferred)",
            "School of Motion, Motion Design School, or Domestika online programs",
            "Build reel: logo animation, explainer videos, broadcast design, title sequences",
            "Freelance or work at ad agencies, broadcast studios, or in-house brand teams",
        ],
        "qualifications": [
            "BFA in Motion Design, Graphic Design, or Animation (preferred, not mandatory)",
            "School of Motion or equivalent course completion (industry recognised)",
            "Adobe Creative Cloud proficiency — After Effects + Premiere + Illustrator",
            "Strong portfolio across multiple styles and industries",
        ],
        "tags": ["motion-graphics", "after-effects", "broadcast", "creative", "design"],
    },

    # ══════════════════════════════════════════════════════
    # MENTAL HEALTH & THERAPY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "speech_therapist_in",
        "title": "Speech-Language Pathologist",
        "category": "Mental Health & Therapy",
        "region": "IN",
        "description": "Assess and treat communication disorders, speech impediments, language delays, and swallowing difficulties in children and adults. SLPs work in hospitals, schools, rehabilitation centres, private clinics, and via teletherapy — a rapidly growing field in India.",
        "salary_range": {"min": 25000, "max": 120000, "currency": "INR/month", "note": "Fresher to senior clinical SLP or private practice"},
        "growth_outlook": "Strong — awareness of speech disorders growing, shortage of trained SLPs",
        "work_style": ["Patient-facing", "Clinical", "Compassionate"],
        "required_skills": [
            s("Speech & Language Assessment", "critical"), s("Patient Care", "critical"),
            s("Communication", "critical"), s("Empathy", "critical"),
            s("Report Writing", "important"), s("Child Development Knowledge", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Audiology and Speech-Language Pathology (BASLP — 4 years)",
            "Master's in Speech-Language Pathology (MASLP — 2 years)",
            "RCI — Rehabilitation Council of India registration (mandatory to practice)",
            "Internship in hospitals, schools, and rehabilitation centres",
        ],
        "qualifications": [
            "BASLP — Bachelor of Audiology and Speech-Language Pathology (4 years)",
            "MASLP — Master's (preferred for clinical / senior roles)",
            "RCI registration (Rehabilitation Council of India) — mandatory to practice legally",
        ],
        "tags": ["speech-therapy", "healthcare", "therapy", "rci", "clinical"],
    },
    {
        "id": "occupational_therapist_in",
        "title": "Occupational Therapist",
        "category": "Mental Health & Therapy",
        "region": "IN",
        "description": "Help individuals with physical, developmental, or mental health challenges regain independence in daily life activities — from children with autism and developmental delays to adults recovering from injury or stroke. OTs work in hospitals, schools, NGOs, and private clinics.",
        "salary_range": {"min": 25000, "max": 100000, "currency": "INR/month", "note": "Fresher to senior OT or private practice"},
        "growth_outlook": "Growing — increasing awareness of autism, neurorehabilitation, and disability rights",
        "work_style": ["Patient-facing", "Hands-on", "Compassionate"],
        "required_skills": [
            s("Occupational Therapy Assessment", "critical"), s("Patient Care", "critical"),
            s("Empathy", "critical"), s("Activity Planning", "important"),
            s("Communication", "important"), s("Child Development Knowledge", "important"),
        ],
        "entry_paths": [
            "BOT — Bachelor of Occupational Therapy (4.5 years, RCI-recognized institutes)",
            "MOT — Master of Occupational Therapy (2 years, for specialization)",
            "RCI registration (mandatory to practice)",
            "Clinical internship in hospitals, schools, and rehabilitation settings",
        ],
        "qualifications": [
            "BOT — Bachelor of Occupational Therapy (4.5 years)",
            "MOT — Master of Occupational Therapy (preferred for specialization)",
            "RCI — Rehabilitation Council of India registration (mandatory)",
        ],
        "tags": ["occupational-therapy", "healthcare", "therapy", "rci", "rehabilitation"],
    },
    {
        "id": "psychologist_in",
        "title": "Psychologist / Counseling Professional",
        "category": "Mental Health & Therapy",
        "region": "IN",
        "description": "Assess, diagnose, and treat mental health conditions — or provide counseling and emotional support for personal growth. India faces a massive shortage of mental health professionals; psychologists work in hospitals, schools, corporates, NGOs, and private practice, with growing acceptance of therapy.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "INR/month", "note": "School counselor to senior clinical psychologist or private practice"},
        "growth_outlook": "Very strong — mental health awareness is surging in India post-COVID",
        "work_style": ["Patient-facing", "Empathetic", "Research / Clinical"],
        "required_skills": [
            s("Psychological Assessment", "critical"), s("Counseling", "critical"),
            s("Empathy", "critical"), s("Active Listening", "critical"),
            s("Ethics & Confidentiality", "critical"), s("Research", "helpful"),
        ],
        "entry_paths": [
            "BA/BSc in Psychology (3 years)",
            "MA/MSc in Clinical, Counseling, or Applied Psychology (2 years)",
            "M.Phil in Clinical Psychology (RCI-mandated for clinical practice)",
            "PhD for research and academic roles",
        ],
        "qualifications": [
            "BA/BSc in Psychology (foundation)",
            "MA/MSc in Clinical or Counseling Psychology (minimum for practice)",
            "M.Phil in Clinical Psychology (RCI-mandated for clinical psychologist title)",
            "RCI or RPS registration for clinical practice",
        ],
        "tags": ["psychology", "mental-health", "counseling", "therapy", "clinical"],
    },
    {
        "id": "aba_therapist_in",
        "title": "ABA Therapist / Behavior Analyst",
        "category": "Mental Health & Therapy",
        "region": "IN",
        "description": "Apply Applied Behavior Analysis (ABA) to help children with autism and developmental disabilities build communication, social, and life skills. A rapidly growing profession in India as awareness of autism increases and more families seek structured early intervention.",
        "salary_range": {"min": 20000, "max": 80000, "currency": "INR/month", "note": "Therapist to senior behavior analyst or clinic supervisor"},
        "growth_outlook": "Very strong — autism diagnosis rates rising, ABA therapist shortage in India",
        "work_style": ["Patient-facing", "Structured", "Compassionate"],
        "required_skills": [
            s("ABA Principles", "critical"), s("Behavior Assessment", "critical"),
            s("Data Collection & Analysis", "critical"), s("Patient Care", "critical"),
            s("Empathy", "critical"), s("Communication", "important"),
            s("Child Development Knowledge", "important"),
        ],
        "entry_paths": [
            "Degree in Psychology, Special Education, or Allied Health",
            "ABA training programs (RBT training — 40 hours minimum)",
            "RBT — Registered Behavior Technician certification for entry-level work",
            "BCBA / BCaBA for senior analyst and supervisory roles (international credential)",
        ],
        "qualifications": [
            "Bachelor's in Psychology, Special Education, or Allied Health Sciences",
            "RBT — Registered Behavior Technician (40-hour training, exam)",
            "BCaBA or BCBA certification for supervisory / senior roles (international standard)",
            "RCI registration for special education related practice (India)",
        ],
        "tags": ["aba", "autism", "behavior-analysis", "therapy", "special-education"],
    },

    # ══════════════════════════════════════════════════════
    # MENTAL HEALTH & THERAPY — USA
    # ══════════════════════════════════════════════════════
    {
        "id": "us_speech_therapist",
        "title": "Speech-Language Pathologist (SLP)",
        "category": "Mental Health & Therapy",
        "region": "US",
        "description": "Diagnose and treat communication, language, voice, and swallowing disorders across all ages. One of the most in-demand healthcare careers in the US — SLPs work in hospitals, schools, early intervention, SNFs, and telehealth. Consistently ranked among the best healthcare careers.",
        "salary_range": {"min": 70000, "max": 110000, "currency": "USD/year", "note": "CF year to senior/private practice SLP"},
        "growth_outlook": "Very strong — BLS projects 19% growth, well above average",
        "work_style": ["Patient-facing", "Clinical", "Compassionate"],
        "required_skills": [
            s("Speech & Language Assessment", "critical"), s("Patient Care", "critical"),
            s("Communication", "critical"), s("Empathy", "critical"),
            s("Report Writing & Documentation", "important"), s("Evidence-Based Practice", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Communication Sciences and Disorders (CSD) or related",
            "Master's in Speech-Language Pathology (MS/MA-SLP — ASHA-accredited, mandatory)",
            "Clinical Fellowship Year (CF — 9 months supervised practice)",
            "State SLP License + CCC-SLP (Certificate of Clinical Competence from ASHA)",
        ],
        "qualifications": [
            "Master's in Speech-Language Pathology from ASHA-accredited program (mandatory)",
            "CCC-SLP — Certificate of Clinical Competence (ASHA) after CF year",
            "State SLP License (mandatory, varies by state)",
            "Clinical Fellowship Year (supervised post-degree practice)",
        ],
        "tags": ["speech-therapy", "healthcare", "slp", "asha", "clinical"],
    },
    {
        "id": "us_occupational_therapist",
        "title": "Occupational Therapist (OT)",
        "category": "Mental Health & Therapy",
        "region": "US",
        "description": "Help patients of all ages regain the ability to perform meaningful daily activities after injury, illness, or disability. OTs work in hospitals, schools, pediatric clinics, SNFs, and home health — one of the most versatile and in-demand allied health professions in the US.",
        "salary_range": {"min": 75000, "max": 100000, "currency": "USD/year", "note": "Entry OT to senior/hand therapy specialist"},
        "growth_outlook": "Strong — BLS projects 12% growth",
        "work_style": ["Patient-facing", "Hands-on", "Compassionate"],
        "required_skills": [
            s("OT Assessment & Intervention", "critical"), s("Patient Care", "critical"),
            s("Empathy", "critical"), s("Activity Analysis", "important"),
            s("Documentation", "important"), s("Evidence-Based Practice", "important"),
        ],
        "entry_paths": [
            "Bachelor's pre-requisites in biology, psychology, and anatomy",
            "Master's in OT (MOT) or Doctorate (OTD) from ACOTE-accredited program",
            "NBCOT — National Board for Certification in OT exam (mandatory)",
            "State OT License (mandatory)",
        ],
        "qualifications": [
            "Master's (MOT) or Doctorate (OTD) in Occupational Therapy — ACOTE accredited (mandatory)",
            "NBCOT — Occupational Therapist Registered (OTR) certification exam",
            "State OT License (mandatory to practice)",
            "Specialty certifications: COTA, CHT (Certified Hand Therapist) for advanced practice",
        ],
        "tags": ["occupational-therapy", "healthcare", "ot", "nbcot", "clinical"],
    },
    {
        "id": "us_bcba",
        "title": "BCBA — Board Certified Behavior Analyst",
        "category": "Mental Health & Therapy",
        "region": "US",
        "description": "Apply the science of Applied Behavior Analysis (ABA) to assess, design, and supervise behavior intervention programs — primarily for individuals with autism spectrum disorder (ASD). BCBAs are among the most in-demand healthcare professionals in the US, with a severe national shortage.",
        "salary_range": {"min": 65000, "max": 110000, "currency": "USD/year", "note": "BCBA to senior/clinic director level"},
        "growth_outlook": "Very strong — ABA therapy mandated by insurance in most US states; chronic shortage",
        "work_style": ["Supervisory", "Data-driven", "Clinical"],
        "required_skills": [
            s("ABA Principles", "critical"), s("Behavior Assessment (FBA/VB-MAPP)", "critical"),
            s("Data Analysis", "critical"), s("RBT Supervision", "critical"),
            s("Communication", "important"), s("Ethics", "critical"),
            s("Program Development", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Psychology, Education, or related field",
            "Master's degree with BACB-verified coursework (required for BCBA exam)",
            "2,000 hours supervised fieldwork experience",
            "Pass the BCBA exam (Behavior Analyst Certification Board)",
        ],
        "qualifications": [
            "Master's degree with BACB-verified coursework sequence",
            "2,000 hours supervised fieldwork (or 1,500 concentrated hours)",
            "BCBA Exam — Behavior Analyst Certification Board (pass required)",
            "State licensure as LABA or equivalent (required in most states)",
        ],
        "tags": ["bcba", "aba", "autism", "behavior-analysis", "healthcare"],
    },
    {
        "id": "us_psychologist",
        "title": "Licensed Psychologist",
        "category": "Mental Health & Therapy",
        "region": "US",
        "description": "Assess, diagnose, and treat mental, emotional, and behavioral health conditions. Psychologists work in private practice, hospitals, schools, community mental health centers, and VA facilities. The path is long but the career is deeply impactful and well-compensated.",
        "salary_range": {"min": 80000, "max": 130000, "currency": "USD/year", "note": "Postdoctoral fellow to senior/private practice psychologist"},
        "growth_outlook": "Strong — mental health demand surging post-COVID",
        "work_style": ["Patient-facing", "Empathetic", "Research / Clinical"],
        "required_skills": [
            s("Psychological Assessment", "critical"), s("Therapy / Counseling", "critical"),
            s("Empathy", "critical"), s("Active Listening", "critical"),
            s("Ethics & Confidentiality", "critical"), s("Research", "important"),
            s("Documentation", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Psychology",
            "PhD or PsyD in Clinical or Counseling Psychology (APA-accredited)",
            "1-2 year predoctoral internship (APA-accredited)",
            "Postdoctoral supervised hours (varies by state)",
            "State Psychologist License (mandatory to practice independently)",
        ],
        "qualifications": [
            "PhD or PsyD in Clinical / Counseling Psychology (APA-accredited program, 4-7 years)",
            "APA-accredited predoctoral internship (mandatory)",
            "Postdoctoral supervised experience (1-2 years, state-specific)",
            "State Psychologist License — EPPP exam (Examination for Professional Practice in Psychology)",
        ],
        "tags": ["psychology", "mental-health", "therapy", "clinical", "private-practice"],
    },

    # ══════════════════════════════════════════════════════
    # ENTREPRENEURSHIP & MSME — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "street_food_entrepreneur",
        "title": "Street Food / Tiffin Service Entrepreneur",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Start your own food business with low investment — from a street food stall or cart to a home tiffin service or food delivery brand. One of India's most accessible entrepreneurial paths requiring culinary skill, location sense, and customer service. Investment: ₹20,000 – ₹2,00,000.",
        "salary_range": {"min": 15000, "max": 150000, "currency": "INR/month", "note": "Profit depends on location, volume, and menu — scalable"},
        "growth_outlook": "Strong — food delivery apps & Zomato/Swiggy expanding market reach",
        "work_style": ["Self-employed", "Physical", "Customer-facing"],
        "required_skills": [
            s("Cooking", "critical"), s("Customer Service", "critical"),
            s("Basic Accounting", "important"), s("Food Safety & Hygiene", "critical"),
            s("Sales", "important"), s("Physical Fitness", "helpful"),
        ],
        "entry_paths": [
            "Learn cooking skills through family, apprenticeship, or short culinary courses",
            "Start with a home tiffin service (lowest investment, no rent needed)",
            "Register as a food vendor / get FSSAI Food License (mandatory)",
            "Scale up: cart → small shop → cloud kitchen → franchise",
        ],
        "qualifications": [
            "No formal qualification required",
            "FSSAI Food Safety License (mandatory for any food business)",
            "Short culinary / food safety courses from state polytechnics or NSDC",
            "Optional: NHM Diploma in Food Production",
        ],
        "tags": ["entrepreneurship", "food", "small-business", "self-employed", "low-investment"],
    },
    {
        "id": "handicraft_entrepreneur",
        "title": "Handicraft & Artisan Business Owner",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Turn traditional craftsmanship — pottery, weaving, embroidery, woodwork, jewelry, leather goods — into a thriving business. Sell locally, through exhibitions, or online via Amazon Karigar, Etsy, and Meesho. Government schemes like PM Vishwakarma offer funding and training. Investment: ₹50,000 – ₹5,00,000.",
        "salary_range": {"min": 15000, "max": 200000, "currency": "INR/month", "note": "Highly variable — export and online channels significantly boost income"},
        "growth_outlook": "Growing — handmade and artisan products booming domestically and in exports",
        "work_style": ["Creative", "Self-employed", "Flexible"],
        "required_skills": [
            s("Craft Skills", "critical"), s("Creativity", "critical"),
            s("Sales", "important"), s("Basic Accounting", "important"),
            s("Digital Marketing", "helpful"), s("Design", "helpful"),
        ],
        "entry_paths": [
            "Learn craft from family tradition or government design institutes (NID, NIFT, state craft boards)",
            "Register with MSME / Udyam portal for government scheme benefits",
            "Apply for PM Vishwakarma Yojana for tool upgrades and training",
            "Sell through local markets → craft fairs → Amazon Karigar / Etsy / own website",
        ],
        "qualifications": [
            "No formal qualification required — craft mastery is the credential",
            "MSME / Udyam Registration (for government scheme access)",
            "PM Vishwakarma Yojana recognition (for traditional artisans)",
            "Optional: Diploma from state craft board or NID/NIFT short courses",
        ],
        "tags": ["handicraft", "artisan", "msme", "entrepreneurship", "self-employed"],
    },
    {
        "id": "cloud_kitchen_entrepreneur",
        "title": "Cloud Kitchen / Home Bakery Entrepreneur",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Run a delivery-only food business from a rented kitchen or even your home — no dine-in costs, lower overheads, and access to Swiggy/Zomato's built-in customer base. Cloud kitchens are the fastest-growing food business format in India. Investment: ₹2,00,000 – ₹10,00,000.",
        "salary_range": {"min": 30000, "max": 500000, "currency": "INR/month", "note": "Profitable cloud kitchens generate ₹1L-₹5L+ with multiple brands"},
        "growth_outlook": "Very strong — cloud kitchen market in India growing 30%+ annually",
        "work_style": ["Self-employed", "Operations-heavy", "Scalable"],
        "required_skills": [
            s("Cooking", "critical"), s("Operations Management", "critical"),
            s("Digital Marketing", "important"), s("Financial Management", "important"),
            s("Customer Service", "important"), s("Food Safety & Hygiene", "critical"),
        ],
        "entry_paths": [
            "Get FSSAI license and local municipal permissions",
            "List on Swiggy, Zomato, and direct WhatsApp ordering",
            "Start with 1-2 focused menus; add more brands as demand grows",
            "Use government MUDRA loan / PM SVANidhi scheme for initial funding",
        ],
        "qualifications": [
            "No formal qualification required",
            "FSSAI Food Safety License (mandatory)",
            "GST registration (for businesses above ₹20L turnover)",
            "FSSAI FoSCoS online training (recommended)",
        ],
        "tags": ["cloud-kitchen", "food", "entrepreneurship", "swiggy", "zomato"],
    },
    {
        "id": "franchise_owner_in",
        "title": "Franchise Business Owner",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Own and operate a proven business model under an established brand — from fast food (Subway, Domino's, Amul) and education (BYJU's, Kumon) to retail and healthcare. Franchising reduces startup risk significantly. Investment ranges from ₹5 lakhs (small kiosk) to ₹50 lakhs+ (full restaurant/store).",
        "salary_range": {"min": 30000, "max": 1000000, "currency": "INR/month", "note": "Returns depend on brand, location, and operating efficiency"},
        "growth_outlook": "Strong — India's franchise industry growing 30%+ annually",
        "work_style": ["Self-employed", "Customer-facing", "Operations-driven"],
        "required_skills": [
            s("Business Management", "critical"), s("Customer Service", "critical"),
            s("Financial Management", "important"), s("Leadership", "important"),
            s("Sales", "important"), s("Operations Management", "important"),
        ],
        "entry_paths": [
            "Research franchise opportunities on FranchiseIndia.com, BizConnect",
            "Evaluate brands: franchise fee, royalty %, territory rights, support",
            "Arrange funding: own savings, bank loan, SIDBI scheme",
            "Sign franchise agreement and complete brand training program",
        ],
        "qualifications": [
            "No formal qualification required",
            "Business or retail management experience (preferred)",
            "Bank / NBFC loan eligibility based on creditworthiness",
            "Franchisor training program (mandatory on signing)",
        ],
        "tags": ["franchise", "business", "entrepreneurship", "investment", "retail"],
    },
    {
        "id": "msme_manufacturer",
        "title": "Small Manufacturing / MSME Business Owner",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Set up a small manufacturing unit producing everyday goods — from agarbatti, candles, and paper bags to garments, steel furniture, or food processing. India's MSME sector is the backbone of the economy. Government offers subsidies, loans, and infrastructure support. Investment: ₹10,00,000 – ₹1 crore+ depending on product.",
        "salary_range": {"min": 30000, "max": 2000000, "currency": "INR/month", "note": "Profit after operational costs; varies enormously by product and scale"},
        "growth_outlook": "Strong — Make in India, PLI schemes, and export opportunities growing",
        "work_style": ["Self-employed", "Operational", "Leadership-heavy"],
        "required_skills": [
            s("Operations Management", "critical"), s("Financial Management", "critical"),
            s("Leadership", "important"), s("Sales & Marketing", "important"),
            s("Technical Knowledge (product-specific)", "important"),
            s("Accounting", "helpful"), s("Supply Chain basics", "helpful"),
        ],
        "entry_paths": [
            "Register business: proprietorship / partnership / Pvt Ltd",
            "Udyam (MSME) Registration (enables access to govt schemes, loans)",
            "Apply for PMEGP, MUDRA, SIDBI, or bank loans for capital",
            "Source machinery, raw materials, and set up unit in industrial area or home",
            "Obtain product-specific licenses (BIS, FSSAI, pollution clearance)",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "Udyam / MSME Registration (mandatory for government benefits)",
            "Product-specific licenses: BIS, FSSAI, PCB clearance (as applicable)",
            "ITI / Diploma in relevant trade (improves technical quality and credibility)",
        ],
        "tags": ["manufacturing", "msme", "entrepreneurship", "make-in-india", "small-business"],
    },
    {
        "id": "ecommerce_entrepreneur",
        "title": "E-commerce / Online Reseller Entrepreneur",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Build an online retail business selling products through Amazon, Flipkart, Meesho, or your own website — with or without holding inventory (dropshipping). One of the most accessible business models today, startable with as little as ₹50,000 from home. Investment: ₹50,000 – ₹5,00,000.",
        "salary_range": {"min": 15000, "max": 500000, "currency": "INR/month", "note": "Returns depend on niche, margins, and marketing investment"},
        "growth_outlook": "Very strong — Indian e-commerce growing 25%+ annually",
        "work_style": ["Self-employed", "Remote", "Flexible"],
        "required_skills": [
            s("Digital Marketing", "critical"), s("Product Sourcing", "critical"),
            s("Customer Service", "important"), s("MS Excel / Accounting basics", "important"),
            s("Photography", "helpful"), s("Communication", "helpful"),
        ],
        "entry_paths": [
            "Choose a product niche and source from manufacturers (IndiaMart, Alibaba)",
            "Register on Amazon Seller, Flipkart Seller, or Meesho",
            "Get GST registration (mandatory for marketplace sellers)",
            "Run ads (Amazon PPC, Meta Ads) and grow organically through reviews",
            "Scale: add SKUs → own website (Shopify / WooCommerce) → private label",
        ],
        "qualifications": [
            "No formal qualification required",
            "GST Registration (mandatory for marketplace selling)",
            "MSME / Udyam Registration (optional but unlocks benefits)",
            "Digital marketing certifications (Google, Meta) — optional but helpful",
        ],
        "tags": ["ecommerce", "online-business", "entrepreneurship", "amazon", "flipkart"],
    },

    # ══════════════════════════════════════════════════════
    # ENTREPRENEURSHIP & MSME — USA
    # ══════════════════════════════════════════════════════
    {
        "id": "us_small_business_owner",
        "title": "Small Business Owner",
        "category": "Entrepreneurship & MSME",
        "region": "US",
        "description": "Start and run your own business — from a food truck, cleaning service, landscaping company, or boutique retail store to a skilled trade service. The US has strong infrastructure for small businesses through the SBA (Small Business Administration). Investment: $5,000 – $100,000+ depending on type.",
        "salary_range": {"min": 40000, "max": 300000, "currency": "USD/year", "note": "Highly variable; profitable small businesses often out-earn corporate salaries"},
        "growth_outlook": "Stable — small businesses form the backbone of the US economy",
        "work_style": ["Self-employed", "Multi-role", "Risk-tolerant"],
        "required_skills": [
            s("Business Management", "critical"), s("Financial Management", "critical"),
            s("Customer Service", "critical"), s("Sales & Marketing", "important"),
            s("Leadership", "important"), s("Problem Solving", "important"),
        ],
        "entry_paths": [
            "Register business: LLC or Sole Proprietorship (most common)",
            "Get EIN (Employer Identification Number) from IRS",
            "Explore SBA loans, SCORE mentorship, and local small business grants",
            "Obtain product/service-specific licenses and insurance",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "LLC / Sole Proprietorship registration with state",
            "EIN from IRS (mandatory for banking and taxes)",
            "Industry-specific licenses (food handler, contractor, cosmetology, etc.)",
            "SBA training programs (free at score.org)",
        ],
        "tags": ["small-business", "entrepreneurship", "self-employed", "sba", "startup"],
    },
    {
        "id": "us_franchise_owner",
        "title": "Franchise Owner",
        "category": "Entrepreneurship & MSME",
        "region": "US",
        "description": "Invest in a proven brand and business system — from McDonald's, Subway, and Dunkin' to service franchises like Anytime Fitness, Kumon, or ServiceMaster. Franchising is one of the most reliable paths to business ownership. Investment ranges from $50,000 to $1M+ depending on the brand.",
        "salary_range": {"min": 60000, "max": 500000, "currency": "USD/year", "note": "Highly variable; multi-unit franchise owners can earn $500k+"},
        "growth_outlook": "Stable — franchise industry generates $800B+ in GDP",
        "work_style": ["Self-employed", "Operations-driven", "Customer-facing"],
        "required_skills": [
            s("Business Management", "critical"), s("Customer Service", "critical"),
            s("Financial Management", "critical"), s("Leadership", "important"),
            s("Sales", "important"), s("Operations Management", "important"),
        ],
        "entry_paths": [
            "Research franchises on FranConnect, Franchise Direct, or IFA (International Franchise Association)",
            "Review FDD — Franchise Disclosure Document (legally required)",
            "Secure financing: SBA 7(a) loan, franchisor financing, or ROBS (401k funding)",
            "Complete franchisor training and open your location",
        ],
        "qualifications": [
            "No mandatory formal qualification",
            "Business or management experience (preferred by major franchisors)",
            "SBA loan qualification (credit score 680+, liquid assets typically 20-30% of investment)",
            "Franchisor approval and training program completion",
        ],
        "tags": ["franchise", "business", "entrepreneurship", "investment", "self-employed"],
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
