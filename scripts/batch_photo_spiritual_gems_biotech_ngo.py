"""Batch: Photography & Visual Media, Spiritual & Religious, Gemology & Jewelry,
Biotechnology & Pharma R&D, NGO & Development, Library & Information Science"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # PHOTOGRAPHY & VISUAL MEDIA — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "photographer_in",
        "title": "Professional Photographer",
        "category": "Photography & Visual Media",
        "region": "IN",
        "description": "Capture images for weddings, corporate events, editorial features, advertising, travel, wildlife, and documentary projects. India's photography market is growing rapidly — weddings alone generate hundreds of crores for photographers annually. Digital platforms (Instagram, Behance, Unsplash) have opened global markets. Specialisations include wedding, fashion, food, wildlife, architecture, and aerial (drone) photography.",
        "salary_range": {"min": 25000, "max": 500000, "currency": "INR/month", "note": "Junior event photographer to top-tier wedding or fashion photographer; award-winning fine art photographers earn far more"},
        "growth_outlook": "Growing — content marketing, social media, and OTT content are driving demand for quality visual storytelling",
        "work_style": ["Creative", "Field-based", "Freelance / Project-based"],
        "required_skills": [
            s("Camera Operation & Exposure Control", "critical"), s("Composition & Lighting", "critical"),
            s("Photo Editing (Lightroom, Photoshop)", "critical"), s("Colour Grading", "important"),
            s("Client Communication & Art Direction", "important"), s("Equipment Management", "important"),
        ],
        "entry_paths": [
            "Develop skills through photography courses (Delhi School of Photography, Lightroom Academy, Nikon School, online MOOC)",
            "Assist established photographers on shoots — the fastest learning path",
            "Build a portfolio on Instagram and Behance to attract clients",
            "Specialise early (wedding, wildlife, food) for focused portfolio building",
        ],
        "qualifications": [
            "Diploma / Certificate in Photography from FTII, Symbiosis, AAFT, or private photo schools",
            "BA Visual Arts / Mass Communication (helpful for editorial and advertising photography)",
            "No formal degree required if portfolio is strong — this is a portfolio-first profession",
        ],
        "tags": ["photography", "wedding", "editorial", "lightroom", "visual"],
    },
    {
        "id": "videographer_editor_in",
        "title": "Videographer / Video Editor",
        "category": "Photography & Visual Media",
        "region": "IN",
        "description": "Shoot and edit video content for weddings, corporate communications, advertising, YouTube, OTT platforms, documentaries, and social media. India's booming creator economy — 500 million+ internet users, Reels, YouTube Shorts — has created enormous demand for video production professionals. Video editors can work freelance, in production houses, or at advertising agencies and OTT platforms.",
        "salary_range": {"min": 20000, "max": 300000, "currency": "INR/month", "note": "Junior editor at a wedding film company to senior motion graphics / VFX editor at an OTT production house"},
        "growth_outlook": "Very strong — India's video content market growing 25%+ annually; OTT, YouTube, and Reels driving demand",
        "work_style": ["Creative", "Studio / Remote", "Project-based"],
        "required_skills": [
            s("Video Shooting & Camera Work", "critical"), s("Video Editing (Premiere Pro, DaVinci Resolve, Final Cut)", "critical"),
            s("Colour Grading", "important"), s("Motion Graphics (After Effects)", "important"),
            s("Sound Design & Audio Sync", "helpful"), s("Storytelling & Narrative Editing", "critical"),
        ],
        "entry_paths": [
            "Learn video editing through YouTube tutorials or structured courses (Arena Animation, MAAC, Udemy)",
            "Build a YouTube channel or create sample edit reels to demonstrate skills",
            "Assist a director of photography or video production company",
            "Intern at a digital content agency or OTT production house",
        ],
        "qualifications": [
            "Diploma / Certificate in Film Production or Video Editing (FTII, Whistling Woods, Arena Animation)",
            "BSc / BM in Mass Communication / Visual Media (helpful for broadcast)",
            "Adobe Certified Professional — Premiere Pro (optional but credentialises skill)",
            "DaVinci Resolve Certified Trainer programme (for colour grading specialisation)",
        ],
        "tags": ["videography", "video-editing", "premiere-pro", "content-creator", "ott"],
    },

    # ══════════════════════════════════════════════════════
    # SPIRITUAL & RELIGIOUS — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "pandit_priest_in",
        "title": "Pandit / Priest / Pujari",
        "category": "Spiritual & Religious",
        "region": "IN",
        "description": "Perform religious ceremonies, rituals, and pujas for individuals, families, and communities — including weddings (vivah), funerals (antyesti), housewarming (griha pravesh), and daily temple worship. Temple priests serve in temples managed by trusts and state endowment boards. Event pandits serve at homes and function venues. The profession passes through families (hereditary) or formal Agama-shastra (temple ritual science) training.",
        "salary_range": {"min": 15000, "max": 300000, "currency": "INR/month", "note": "Daily puja priest at a small temple to head priest of a major temple trust or in-demand wedding pandit in a metro city"},
        "growth_outlook": "Stable — culturally embedded role with consistent demand; ceremonial services industry growing with rising incomes",
        "work_style": ["Service-based", "Ritual-intensive", "Early hours"],
        "required_skills": [
            s("Vedic Mantra Recitation (Sanskrit)", "critical"), s("Ritual Procedure Knowledge (Agama Shastra or Grihya Sutras)", "critical"),
            s("Jyotish (Vedic Astrology basics for muhurta)", "important"),
            s("Communication with Devotees / Families", "important"),
            s("Sanskrit Language", "critical"), s("Ritual Materials & Samagri Knowledge", "important"),
        ],
        "entry_paths": [
            "Hereditary learning under a family elder or gurukul system from childhood",
            "Vedic studies at a pathasala (Vedic school) — Gurukul Kangri, Sringeri, Kanchi Math affiliated institutions",
            "Sanskrit Vibhag studies (Samskrit Pathasala, government Sanskrit universities)",
            "Register with temple trust or become an independent pandit for household ceremonies",
        ],
        "qualifications": [
            "Vedic Pandit certificate from a recognised pathasala or Vedic university (Sampurnanand Sanskrit Vishwavidyalaya, SVDU)",
            "Government Sanskrit University degrees (Shastri, Acharya) for academic + ritual career",
            "Agamashastram certification for temple priests in South Indian traditions",
        ],
        "tags": ["pandit", "priest", "temple", "ritual", "vedic"],
    },
    {
        "id": "astrologer_vastu_in",
        "title": "Astrologer / Vastu Consultant",
        "category": "Spiritual & Religious",
        "region": "IN",
        "description": "Provide Jyotish (Vedic astrology) readings — natal chart (kundali) analysis, muhurta (auspicious timing), compatibility (kundali Milan), and remedies — or Vastu Shastra consultancy for homes, offices, and commercial buildings. India's astrology and Vastu market is worth thousands of crores and growing with social media platforms, YouTube channels, and matrimony portals integrating astrology. Online consultations have made this a remote-first career.",
        "salary_range": {"min": 15000, "max": 500000, "currency": "INR/month", "note": "Part-time local astrologer to celebrity astrologer with a YouTube channel and paid membership; consultancy fees vary widely"},
        "growth_outlook": "Growing — digital astrology platforms, apps, and social media have massively expanded the client base",
        "work_style": ["Consulting", "Online / Remote", "Self-employed"],
        "required_skills": [
            s("Vedic Astrology (Jyotish) — Parashari or Jaimini system", "critical"),
            s("Kundali Preparation & Chart Analysis", "critical"), s("Vastu Shastra (for Vastu track)", "critical"),
            s("Sanskrit basics for classical texts", "helpful"), s("Communication & Empathy", "critical"),
            s("Digital Content Creation (for YouTube / social reach)", "helpful"),
        ],
        "entry_paths": [
            "Study Jyotish under a guru (traditional guru-shishya path) or formal university programme",
            "Enrol in Jyotish courses from BHU (Banaras Hindu University), Bharatiya Vidya Bhavan, or online platforms (Astro-Vision, Saptarishis)",
            "Start with local consultations and build online presence (YouTube, Instagram, WhatsApp groups)",
            "Join platforms like AstroTalk, Astroyogi, or Ganeshaspeaks for online consultations",
        ],
        "qualifications": [
            "Jyotish Alankar / Jyotish Visharad / Jyotish Acharya from Bharatiya Vidya Bhavan or BHU",
            "MA in Jyotish from a Sanskrit university (Sampurnanand, Sringeri)",
            "No formal degree required for private practice — reputation and track record are the real credential",
        ],
        "tags": ["astrology", "jyotish", "vastu", "spiritual", "consulting"],
    },
    {
        "id": "meditation_teacher_in",
        "title": "Meditation & Mindfulness Teacher",
        "category": "Spiritual & Religious",
        "region": "IN",
        "description": "Teach meditation, mindfulness, and stress-management practices to individuals, corporate groups, schools, and wellness retreats. India is the birthplace of meditation traditions — Vipassana, Transcendental Meditation, Sahaja Yoga — and a global leader in meditation teacher training. Corporate wellness programmes now regularly include mindfulness sessions, and digital platforms (Headspace, Calm, Inner Circle India) are creating new opportunities.",
        "salary_range": {"min": 20000, "max": 300000, "currency": "INR/month", "note": "Local meditation teacher to corporate mindfulness consultant or online programme creator with global students"},
        "growth_outlook": "Excellent — global wellness industry exceeding $5 trillion; corporate mindfulness a fast-growing segment",
        "work_style": ["Teaching", "Flexible", "Remote-friendly", "Self-employed"],
        "required_skills": [
            s("Meditation Practice & Tradition Knowledge", "critical"), s("Teaching Methodology", "critical"),
            s("Breath & Body Awareness Techniques", "critical"), s("Communication & Group Facilitation", "critical"),
            s("Trauma-Sensitive Instruction", "important"), s("Online Course Creation (helpful)", "helpful"),
        ],
        "entry_paths": [
            "Establish a personal meditation practice over several years under a qualified teacher",
            "Complete a formal teacher training: Vipassana (Dhamma.org), TM (Maharishi University), MBSR (Mindfulness-Based Stress Reduction, Jon Kabat-Zinn tradition)",
            "Obtain a 300-hour Yoga & Meditation Teacher Training certificate",
            "Build a corporate wellness offering or launch an online course on Udemy/Teachable",
        ],
        "qualifications": [
            "MBSR (Mindfulness-Based Stress Reduction) Teacher Training from the Centre for Mindfulness or an authorised trainer",
            "Vipassana meditation course completion + assistant teacher training (dhamma.org)",
            "200/300-hour Yoga & Meditation TT (Yoga Alliance registered schools)",
            "No formal government degree required — lineage and training credentials are the trust signals",
        ],
        "tags": ["meditation", "mindfulness", "yoga", "wellness", "corporate-wellness"],
    },

    # ══════════════════════════════════════════════════════
    # GEMOLOGY & JEWELRY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "gemologist_in",
        "title": "Gemologist / Diamond Grader",
        "category": "Gemology & Jewelry",
        "region": "IN",
        "description": "Identify, evaluate, and grade gemstones and diamonds using spectroscopic and optical instruments. India is the world's largest diamond cutting and polishing hub — Surat alone processes 90% of the world's rough diamonds. Gemologists work for diamond manufacturers (Kiran Gems, KGK, Surat diamond factories), jewellery retailers (Tanishq, Kalyan, Malabar), gem labs (GIA India, IGI, SGL), and as independent appraisers.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior grader at a Surat diamond unit to senior gemologist at a premier jewellery house or certified gem lab"},
        "growth_outlook": "Stable — India's diamond and coloured stone trade globally significant; lab-grown diamond segment adding new jobs",
        "work_style": ["Laboratory-based", "Precise", "Detail-intensive"],
        "required_skills": [
            s("Gemological Identification Techniques", "critical"), s("Diamond Grading (4Cs: cut, colour, clarity, carat)", "critical"),
            s("Gemological Instruments (loupe, refractometer, spectrometer)", "critical"),
            s("Gem Certification Report Writing", "important"), s("Coloured Stone Knowledge", "important"),
        ],
        "entry_paths": [
            "Complete the GIA GG (Graduate Gemologist) programme — the global gold standard",
            "Study at IGI (International Gemological Institute) India, SGL (Solitaire Gemmological Laboratory), or IDC",
            "Join a diamond factory in Surat for practical grading experience",
            "Work at a gem testing lab (GIA India, IGI Mumbai) for certification and appraisal roles",
        ],
        "qualifications": [
            "GIA GG (Graduate Gemologist) — International standard (GIA Mumbai campus available)",
            "FGA (Fellow of the Gemmological Association of Great Britain) — UK standard recognised globally",
            "IGI Diploma in Diamond Grading or Diamond and Coloured Stone Specialist",
            "Jewellery Design degree (NID, NIFT) for design + gemology crossover roles",
        ],
        "tags": ["gemology", "diamond", "gemstone", "gia", "surat"],
    },
    {
        "id": "goldsmith_jewelry_maker_in",
        "title": "Goldsmith / Jewellery Artisan",
        "category": "Gemology & Jewelry",
        "region": "IN",
        "description": "Craft fine jewellery from precious metals (gold, silver, platinum) and gemstones using traditional and modern bench techniques. India is the world's second-largest jewellery market. Skilled goldsmiths (karigars) work in jewellery ateliers, luxury brand workshops (Titan, Kalyan, Senco), handmade jewellery studios, and as independent craftspeople. Demand for traditional Indian craft techniques (Kundan, Meenakari, Filigree, Temple jewellery) is growing globally.",
        "salary_range": {"min": 20000, "max": 150000, "currency": "INR/month", "note": "Apprentice goldsmith to master karigar at a luxury jewellery atelier or independent studio owner"},
        "growth_outlook": "Stable — growing artisan jewellery segment and global demand for Indian crafts; skilled karigars rare and valued",
        "work_style": ["Hands-on", "Craft-intensive", "Workshop-based"],
        "required_skills": [
            s("Metal Working (sawing, filing, soldering)", "critical"), s("Stone Setting", "critical"),
            s("Casting & Wax Carving", "important"), s("Finishing & Polishing", "critical"),
            s("Jewellery Design Drawing", "helpful"), s("Traditional Indian Techniques (Kundan, Meenakari)", "important"),
        ],
        "entry_paths": [
            "Traditional apprenticeship under a master karigar (goldsmith) — most common entry path",
            "Diploma / Certificate in Jewellery Design & Manufacturing from GIA India, IDC, or NIFT",
            "Join a jewellery manufacturing unit in Jaipur, Hyderabad, Thrissur, or Surat for hands-on training",
            "Start with silver jewellery and build up to gold / gemstone-set pieces",
        ],
        "qualifications": [
            "Diploma in Jewellery Design & Manufacturing (GIA India, IDC, NIFT, state polytechnics)",
            "National Skill Qualification Framework (NSQF) Jewellery Sector Skill Council certification",
            "GIA Graduate Gemologist (GG) for gemstone-setting specialisation",
        ],
        "tags": ["goldsmith", "jewellery", "karigar", "crafts", "gold"],
    },

    # ══════════════════════════════════════════════════════
    # BIOTECHNOLOGY & PHARMA R&D — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "biochemist_researcher_in",
        "title": "Biochemist / Molecular Biologist",
        "category": "Biotechnology & Pharma R&D",
        "region": "IN",
        "description": "Conduct research on biological molecules — proteins, DNA, enzymes, and metabolites — to advance medical science, develop drugs, create diagnostics, and understand disease mechanisms. India's biotech sector includes over 5,000 firms and a fast-growing biopharma industry (Biocon, Serum Institute, Sun Pharma R&D). Top research institutes include NCBS Bengaluru, CCMB Hyderabad, IISc, and IITs.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "INR/month", "note": "Junior research fellow at an academic institute to principal scientist at Biocon, Dr. Reddy's, or Cipla R&D"},
        "growth_outlook": "Strong — India's biotech sector growing 15%+ annually; post-COVID vaccine industry investment sustained",
        "work_style": ["Laboratory-based", "Research-intensive", "Analytical"],
        "required_skills": [
            s("Molecular Biology Techniques (PCR, gel electrophoresis, Western blot)", "critical"),
            s("Cell Culture & Assay Development", "important"), s("ELISA & Immunoassay", "important"),
            s("Bioinformatics Basics", "helpful"), s("Lab Documentation (Good Laboratory Practice)", "critical"),
            s("Data Analysis (R, GraphPad Prism)", "important"),
        ],
        "entry_paths": [
            "BSc in Biochemistry, Microbiology, or Biotechnology → MSc in same field",
            "Qualify CSIR-JRF or DBT-JRF fellowship to work at premier labs (CCMB, NCBS, TIFR)",
            "PhD from IISc, IIT, or NCBS for academic research or senior industry R&D roles",
            "Join Biocon, Serum Institute, or Cipla R&D as a research scientist (post MSc / PhD)",
        ],
        "qualifications": [
            "BSc / MSc in Biochemistry, Biotechnology, Microbiology, or Molecular Biology",
            "CSIR-JRF or DBT-JRF (Joint Research Fellowship) for PhD and national lab research",
            "PhD in Biochemistry / Molecular Biology / Biotechnology from IISc, IIT, or TIFR",
        ],
        "tags": ["biochemist", "molecular-biology", "biotech", "pharma-r-and-d", "research"],
    },
    {
        "id": "clinical_research_associate_in",
        "title": "Clinical Research Associate (CRA) / Clinical Trial Manager",
        "category": "Biotechnology & Pharma R&D",
        "region": "IN",
        "description": "Monitor and manage clinical trials of new drugs, medical devices, and vaccines — ensuring they are conducted in accordance with GCP (Good Clinical Practice) guidelines and regulatory requirements (CDSCO, ICH, FDA). India's clinical research industry employs thousands of CRAs at global CROs (Covance, IQVIA, Syneos Health) and Indian pharma companies (Cipla, Sun Pharma, Lupin). CRA roles require extensive travel to trial sites.",
        "salary_range": {"min": 35000, "max": 250000, "currency": "INR/month", "note": "Junior CRA at a CRO to Senior CRA or Clinical Trial Manager at a global pharma company"},
        "growth_outlook": "Strong — India's clinical trial industry growing as a global destination; post-COVID regulatory reforms opening new trials",
        "work_style": ["Field-based (site visits)", "Regulatory-intensive", "Travel-heavy"],
        "required_skills": [
            s("GCP (Good Clinical Practice) Guidelines", "critical"), s("ICH Guidelines & CDSCO Regulations", "critical"),
            s("Source Data Verification (SDV)", "critical"), s("Clinical Trial Management Systems (Medidata, Veeva)", "important"),
            s("Protocol Compliance Monitoring", "critical"), s("Communication & Site Management", "critical"),
        ],
        "entry_paths": [
            "BSc / MSc in Life Sciences, Pharmacy, Nursing, or Medicine",
            "Obtain a PG Diploma or Certificate in Clinical Research (PGDCR) from organisations like IQVIA Academy, ACRES, or university programmes",
            "Join a CRO (Contract Research Organisation) as a clinical research trainee",
            "Complete ICH-GCP training and certification (mandatory for the role)",
        ],
        "qualifications": [
            "BSc / MSc / B.Pharm / M.Pharm / MBBS in a life sciences or clinical field",
            "PGDCR (Post Graduate Diploma in Clinical Research) from IGNOU, ACTS, or IQVIA Academy",
            "ICH-GCP Certificate (mandatory) + CDSCO awareness training",
            "ACRP CCRC / SOCRA CCRP certification (valued for senior CRA and global roles)",
        ],
        "tags": ["clinical-research", "cra", "gcp", "pharma", "clinical-trials"],
    },

    # ══════════════════════════════════════════════════════
    # NGO & DEVELOPMENT — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "ngo_project_manager_in",
        "title": "NGO Programme Manager / Development Professional",
        "category": "NGO & Development",
        "region": "IN",
        "description": "Design, implement, monitor, and evaluate development programmes in areas such as education, health, livelihoods, women's empowerment, environment, and governance. India has over 3 million NGOs employing millions of development professionals. Key sectors: WASH (water/sanitation), rural livelihoods, child nutrition (POSHAN), disability inclusion, and climate resilience. Bilateral donors (USAID, DFID), UN agencies, and Indian CSR funds are the primary funding sources.",
        "salary_range": {"min": 30000, "max": 250000, "currency": "INR/month", "note": "Entry programme coordinator at a small NGO to Country Director or Programme Head at an INGO (CRS, HelpAge, Oxfam)"},
        "growth_outlook": "Stable — CSR mandate (Companies Act 2013) sustaining funding; international development aid flowing into India",
        "work_style": ["Field + Office", "Community-facing", "Reporting-intensive"],
        "required_skills": [
            s("Project Cycle Management (PCM)", "critical"), s("M&E (Monitoring, Evaluation & Learning)", "critical"),
            s("Proposal Writing & Grant Management", "critical"), s("Community Engagement", "critical"),
            s("Data Collection & Analysis", "important"), s("Donor Reporting (USAID, UN, CSR)", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Social Work, Development Studies, Economics, or Public Policy",
            "Master's in Social Work (MSW), Development Studies, or Public Policy (TISS, JNU, IRMA, XLRI)",
            "Join a small grassroots NGO as a field coordinator to gain ground-level experience",
            "Build up to mid-size INGOs (Plan India, World Vision, CRY) and eventually large INGOs or UN agencies",
        ],
        "qualifications": [
            "MA in Development Studies / Social Work (TISS Mumbai or Hyderabad — premier institutions)",
            "MSW (Master of Social Work) from a recognised university",
            "PGDM in Rural Management (IRMA — Institute of Rural Management Anand)",
            "Project Management Professional (PMP) or PRINCE2 (valued for large programme roles)",
        ],
        "tags": ["ngo", "development", "social-work", "programme-manager", "csr"],
    },
    {
        "id": "social_entrepreneur_in",
        "title": "Social Entrepreneur / Impact Startup Founder",
        "category": "NGO & Development",
        "region": "IN",
        "description": "Build organisations that create measurable social or environmental impact while being financially sustainable. India's social enterprise ecosystem is vibrant — Pratham, Akanksha, Teach For India, Gram Vaani, Rang De, and hundreds of Ashoka Fellows are examples. Impact investors (Omidyar Network, Elevar Equity, Acumen, Unitus Capital) fund social ventures. The B Corp, CIC, and Section 8 company structures allow hybrid models.",
        "salary_range": {"min": 20000, "max": 500000, "currency": "INR/month", "note": "Bootstrapped founder (often modest early salary) to well-funded social startup CEO with market-rate compensation"},
        "growth_outlook": "Growing — Impact investing in India growing rapidly; SEBI SSIR (Social Stock Exchange) adding new capital access routes",
        "work_style": ["Entrepreneurial", "Multi-disciplinary", "Community + Investor-facing"],
        "required_skills": [
            s("Problem Identification & Theory of Change", "critical"), s("Business Model Development", "critical"),
            s("Fundraising & Impact Investor Communication", "critical"), s("Team Building & Leadership", "critical"),
            s("Impact Measurement (SROI, IRIS+)", "important"), s("Community Co-creation", "important"),
        ],
        "entry_paths": [
            "Work at an existing social enterprise or NGO to understand the landscape",
            "Programmes: Ashoka Fellowship, Echoing Green Fellowship, Villgro, Dasra Social Impact, Nudge Foundation",
            "Social impact MBA programmes: TISS, XLRI, IRMA, Ashoka University, ISB Center for Business and Society",
            "Register as a Section 8 company (non-profit), social cooperative, or for-profit with impact mission",
        ],
        "qualifications": [
            "No mandatory degree — demonstrated social impact and organisational building are the credentials",
            "MBA from TISS, XLRI, IRMA, or ISB (Social Enterprise track)",
            "Ashoka, Echoing Green, or Skoll Fellowship (prestigious signal in the impact ecosystem)",
            "Certified B Corp status for the organisation (demonstrates impact commitment to investors)",
        ],
        "tags": ["social-entrepreneurship", "impact", "startup", "ngo", "b-corp"],
    },

    # ══════════════════════════════════════════════════════
    # LIBRARY & INFORMATION SCIENCE — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "librarian_in",
        "title": "Librarian / Information Professional",
        "category": "Library & Information Science",
        "region": "IN",
        "description": "Manage collections of books, digital resources, journals, and archives in public libraries, university libraries, school libraries, corporate libraries, and government information centres. India has a network of over 60,000 public libraries managed by state governments. University libraries at IITs, IIMs, and central universities are significant employers. Digital librarians managing online repositories and information systems are a growing specialisation.",
        "salary_range": {"min": 25000, "max": 150000, "currency": "INR/month", "note": "School / public library assistant to Chief Librarian of a central university or IIT"},
        "growth_outlook": "Stable — digital transformation of libraries creating new roles in knowledge management and e-resources",
        "work_style": ["Administrative", "Knowledge-management", "Quiet office"],
        "required_skills": [
            s("Library Classification (Dewey Decimal, Colon Classification)", "critical"),
            s("Cataloguing & Metadata (MARC, Dublin Core)", "critical"),
            s("Library Management Systems (Koha, SOUL)", "critical"),
            s("Reference & Information Services", "important"),
            s("Digital Resource Management & Database Searching", "important"),
        ],
        "entry_paths": [
            "BLISc (Bachelor of Library and Information Science) followed by MLISc",
            "Apply to government library posts through SSC, state PSC, and UGC NET",
            "UGC NET in Library & Information Science for university librarian and lecturer roles",
            "Join corporate or law firm library for higher salaries in the private sector",
        ],
        "qualifications": [
            "BLISc + MLISc (Master of Library & Information Science) from a UGC-recognised university",
            "UGC NET in Library & Information Science (required for university librarian posts)",
            "PhD in Library & Information Science for academic and research library leadership",
        ],
        "tags": ["librarian", "library-science", "information", "knowledge-management", "university"],
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
