"""Batch: Architecture & Urban Planning, Energy & Utilities, Food Science & Nutrition, Publishing & Writing"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # ARCHITECTURE & URBAN PLANNING — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "architect_in",
        "title": "Architect",
        "category": "Architecture & Urban Planning",
        "region": "IN",
        "description": "Design buildings, complexes, interiors, and urban spaces — balancing aesthetics, functionality, safety, and sustainability. Registered architects in India are governed by the Council of Architecture (CoA). Practice areas include residential, commercial, hospitality, industrial, healthcare, and heritage conservation architecture. Indian architecture is booming with smart cities, PMAY housing, and premium real estate projects.",
        "salary_range": {"min": 30000, "max": 500000, "currency": "INR/month", "note": "Junior architect at a firm to principal / partner at a leading studio (Morphogenesis, RSP, HCP)"},
        "growth_outlook": "Strong — India's construction sector expected to become the world's 3rd largest by 2030",
        "work_style": ["Creative", "Design-intensive", "Client-facing"],
        "required_skills": [
            s("Architectural Design & Drafting", "critical"), s("AutoCAD & Revit (BIM)", "critical"),
            s("3D Visualisation (SketchUp, 3ds Max, Lumion)", "important"), s("Building Codes & NBC (National Building Code)", "critical"),
            s("Site Supervision", "important"), s("Client Communication", "critical"),
        ],
        "entry_paths": [
            "Pass NATA (National Aptitude Test in Architecture) and JEE Paper 2 for architecture college admission",
            "Complete B.Arch (5-year degree) from a CoA-approved college",
            "Register with CoA (Council of Architecture) after B.Arch — mandatory to use the title 'Architect'",
            "Work in a design studio for 3-5 years before setting up an independent practice",
        ],
        "qualifications": [
            "B.Arch from a CoA-recognised institution (5-year degree)",
            "Council of Architecture (CoA) registration (mandatory to practise as an architect)",
            "M.Arch for specialisation (sustainable design, urban design, conservation architecture)",
            "IGBC AP (Accredited Professional) or GRIHA (Green Rating for Integrated Habitat Assessment) for sustainable architecture",
        ],
        "tags": ["architect", "architecture", "design", "bim", "urban"],
    },
    {
        "id": "urban_planner_in",
        "title": "Urban Planner / Town Planner",
        "category": "Architecture & Urban Planning",
        "region": "IN",
        "description": "Plan and design land use, infrastructure, transportation, and public spaces for cities, towns, and regions. Urban planners work with municipal corporations, state urban development authorities (DDA, MMRDA, BBMP), central agencies (TERI, NIUA), consultancy firms (Deloitte, McKinsey Urban Practice), and international organisations (UN-Habitat). India's Smart Cities Mission and AMRUT programme have created significant demand.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "INR/month", "note": "Junior planner at a private consultancy to senior planner / chief town planner in a state authority"},
        "growth_outlook": "Strong — Smart Cities Mission, Metro projects, and rapid urbanisation driving planning demand",
        "work_style": ["Analytical", "GIS-intensive", "Government / Consultancy"],
        "required_skills": [
            s("Land Use Planning & Zoning", "critical"), s("GIS & Spatial Analysis (ArcGIS, QGIS)", "critical"),
            s("Urban Economics & Demographics", "important"), s("Participatory Planning", "important"),
            s("Transport Planning", "important"), s("Master Plan Preparation", "critical"),
        ],
        "entry_paths": [
            "B.Arch or B.Plan → M.Plan (Master of Planning) from SPA Delhi, IIT Kharagpur, CEPT Ahmedabad, or TISS",
            "Join urban development authorities (DDA, MMRDA, GDA) through UPSC / state PSC exams",
            "Work at private urban consultancy firms (RITES, Deloitte, McKinsey Urban) or NGOs (WRI India, ITDP)",
            "International career path: UN-Habitat, World Bank Urban practice (requires strong academic credentials)",
        ],
        "qualifications": [
            "M.Plan (Master of Planning) from SPA Delhi, IIT, or CEPT — the standard professional qualification",
            "B.Arch + M.Plan or B.Plan + M.Plan pathway",
            "Town & Country Planners registration (RTPI India equivalent — ITPI membership)",
            "GIS certifications (ESRI ArcGIS, QGIS) — strong practical value",
        ],
        "tags": ["urban-planning", "town-planning", "gis", "smart-city", "infrastructure"],
    },
    {
        "id": "landscape_architect_in",
        "title": "Landscape Architect / Landscape Designer",
        "category": "Architecture & Urban Planning",
        "region": "IN",
        "description": "Design outdoor environments — parks, gardens, green corridors, public plazas, resort landscapes, and campus grounds. India's growing premium real estate, hospitality, and smart city sectors have increased demand for landscape professionals. Large projects include Navi Mumbai greening, Delhi's Central Vista, Hyderabad's urban forests, and private resort design across hill stations.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior designer at a landscape firm to principal partner or independent consultant for luxury real estate"},
        "growth_outlook": "Growing — urban greening mandates, premium real estate, and resort tourism driving demand",
        "work_style": ["Creative", "Outdoor + Office", "Design-intensive"],
        "required_skills": [
            s("Landscape Design & Planting Knowledge", "critical"), s("AutoCAD & SketchUp", "critical"),
            s("Horticulture & Plant Science", "important"), s("Sustainable Drainage & Water Management", "important"),
            s("Site Analysis & Grading", "critical"), s("3D Visualisation", "important"),
        ],
        "entry_paths": [
            "B.L.Arch (Bachelor of Landscape Architecture) from SPA Delhi, CEPT, or Chandigarh College of Architecture",
            "B.Arch + M.Arch in Landscape Design as a cross-qualification path",
            "Join a landscape architecture firm (Studio Terra, SiteWorks, Design Cell) as a junior designer",
            "Build a portfolio of residential garden and campus projects",
        ],
        "qualifications": [
            "B.L.Arch or M.L.Arch from an ISOLA (Indian Society of Landscape Architects) recognised institution",
            "ISOLA membership (Indian Society of Landscape Architects)",
            "IGBC Landscape AP certification for sustainable landscape design",
        ],
        "tags": ["landscape-architect", "garden-design", "urban-green", "environment", "outdoor"],
    },

    # ─── ARCHITECTURE — USA ───────────────────────────────
    {
        "id": "us_architect",
        "title": "Architect",
        "category": "Architecture & Urban Planning",
        "region": "US",
        "description": "Design buildings, interiors, and urban environments for residential, commercial, institutional, and public use. US architects are licensed by state boards through the ARE (Architectural Registration Examination). Major firms include SOM, Gensler, HOK, Perkins & Will, and thousands of boutique practices. Sustainable design (LEED) and healthcare architecture are strong growth specialisations.",
        "salary_range": {"min": 65000, "max": 200000, "currency": "USD/year", "note": "Intern architect to principal / partner at a major firm; independent practice scales with portfolio"},
        "growth_outlook": "Stable — BLS projects 5% growth; sustainable design and healthcare driving demand",
        "work_style": ["Creative", "Design-intensive", "Client-facing"],
        "required_skills": [
            s("Architectural Design", "critical"), s("Revit & BIM", "critical"),
            s("AutoCAD & SketchUp", "critical"), s("Building Codes (IBC)", "critical"),
            s("Project Management", "important"), s("Sustainable Design (LEED)", "important"),
        ],
        "entry_paths": [
            "B.Arch or M.Arch from NAAB-accredited programme",
            "Complete AXP (Architectural Experience Program) — 3,740 hours of supervised experience",
            "Pass the ARE (Architect Registration Examination) — 6 divisions",
            "Gain LEED AP accreditation for sustainable design specialisation",
        ],
        "qualifications": [
            "B.Arch or M.Arch from NAAB-accredited institution",
            "State architect licence (via ARE completion + AXP hours)",
            "LEED AP BD+C, ID+C, or O+M (for sustainable architecture specialisation)",
            "AIA (American Institute of Architects) membership",
        ],
        "tags": ["architect", "leed", "bim", "revit", "design"],
    },

    # ══════════════════════════════════════════════════════
    # ENERGY & UTILITIES — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "petroleum_engineer_in",
        "title": "Petroleum Engineer / Oil & Gas Engineer",
        "category": "Energy & Utilities",
        "region": "IN",
        "description": "Develop methods for extracting oil and natural gas from the earth, design drilling equipment, oversee production operations, and ensure safe reservoir management. India's key employers include ONGC, Oil India, Cairn Energy India, GAIL, and BPCL. The offshore industry (Mumbai High, Krishna-Godavari basin) is the primary employment zone, with ONGC alone employing thousands of petroleum engineers.",
        "salary_range": {"min": 60000, "max": 400000, "currency": "INR/month", "note": "Graduate Engineer Trainee at ONGC to senior engineer or expatriate offshore engineer"},
        "growth_outlook": "Stable — India's oil demand growing; diversifying to natural gas and LNG infrastructure",
        "work_style": ["Technical", "Outdoor / Offshore", "Shift-based"],
        "required_skills": [
            s("Reservoir Engineering & Geology Basics", "critical"), s("Drilling Engineering", "critical"),
            s("Production & Well Completion", "critical"), s("Petroleum Simulation Software (PETREL, ECLIPSE)", "important"),
            s("Safety Protocols (HSEE, IADC)", "critical"), s("Data Interpretation", "important"),
        ],
        "entry_paths": [
            "B.Tech in Petroleum Engineering from IIT (ISM) Dhanbad, UPES Dehradun, MIT Manipal, or BITS Pilani",
            "GATE petroleum engineering score for ONGC / OIL recruitment",
            "Join ONGC, OIL, or GAIL as a Graduate Engineer Trainee",
            "Work with private upstream operators (Cairn, HMEL, Shell India) or oilfield services (Halliburton, Schlumberger India)",
        ],
        "qualifications": [
            "B.Tech in Petroleum Engineering from IIT Dhanbad or UPES (most recognised for this stream)",
            "GATE score in Petroleum Engineering for PSU recruitment",
            "SPE (Society of Petroleum Engineers) membership",
            "M.Tech in Petroleum Engineering for senior reservoir or drilling roles",
        ],
        "tags": ["petroleum", "oil-gas", "ongc", "drilling", "reservoir"],
    },
    {
        "id": "solar_energy_engineer_in",
        "title": "Solar Energy Engineer / Renewable Energy Specialist",
        "category": "Energy & Utilities",
        "region": "IN",
        "description": "Design, install, commission, and manage solar photovoltaic (PV) and solar thermal energy systems for residential rooftops, commercial buildings, industrial plants, and utility-scale solar parks. India is targeting 500 GW of renewable energy by 2030 — solar is the fastest-growing energy sector in the country. Players include NTPC Renewables, Adani Green, Tata Power Solar, ReNew Power, and SECI.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "INR/month", "note": "Junior design engineer at an EPC company to senior project manager at Adani Green or NTPC Renewables"},
        "growth_outlook": "Excellent — India's solar capacity tripling every 5 years; NTPC, Adani, ReNew all on massive hiring sprees",
        "work_style": ["Technical", "Field + Office", "Project-based"],
        "required_skills": [
            s("Solar PV System Design (PVsyst, Helioscope)", "critical"), s("Electrical Engineering Fundamentals", "critical"),
            s("Grid Integration & Power Electronics", "important"), s("Energy Yield Analysis", "critical"),
            s("Site Assessment & Solar Irradiance", "important"), s("Project Management", "important"),
        ],
        "entry_paths": [
            "B.Tech in Electrical, Electronics, or Mechanical Engineering",
            "Specialise in renewable energy through M.Tech (IIT, MNIT, TERI School of Advanced Studies)",
            "Short certification courses in solar PV (NIWE, TERI, ISES — Indian Section)",
            "Join EPC firms (Jakson, SunSource Energy, Greenko) or developers (Adani Green, ReNew) as a junior engineer",
        ],
        "qualifications": [
            "B.Tech in Electrical, Electronics, or Mechanical Engineering",
            "M.Tech in Renewable Energy / Power Systems (IIT Roorkee, MNIT, TERI SAS)",
            "Certified Solar PV Installer / Designer (NIWE, TERI, MNRE approved bodies)",
            "BEE (Bureau of Energy Efficiency) Certified Energy Manager (CEM) for energy management roles",
        ],
        "tags": ["solar", "renewable-energy", "pv-design", "green-energy", "ntpc"],
    },
    {
        "id": "power_plant_operator_in",
        "title": "Power Plant Operator / Control Room Engineer",
        "category": "Energy & Utilities",
        "region": "IN",
        "description": "Operate and monitor thermal, hydro, nuclear, gas, or renewable power plants — ensuring safe and efficient electricity generation. NTPC, TATA Power, CESC, Adani Power, and state DISCOMs are major employers. Control room operators monitor turbines, boilers, generators, and safety systems. Senior operators become plant managers or shift supervisors.",
        "salary_range": {"min": 30000, "max": 150000, "currency": "INR/month", "note": "Junior operator trainee at a state power utility to shift in-charge at an NTPC or Adani thermal plant"},
        "growth_outlook": "Stable — thermal plants declining slowly; new renewable plants need operators too",
        "work_style": ["Shift-based", "Technical", "Control room / Plant floor"],
        "required_skills": [
            s("Electrical & Mechanical Systems Knowledge", "critical"), s("DCS / SCADA Operation", "critical"),
            s("Turbine & Boiler Operation", "critical"), s("Plant Safety Protocols", "critical"),
            s("Shift Logging & Reporting", "important"), s("Fault Identification", "critical"),
        ],
        "entry_paths": [
            "Diploma in Electrical, Mechanical, or Instrumentation Engineering (polytechnic)",
            "Recruit through NTPC, TATA Power, Adani Power Graduate Apprenticeship / Diploma Trainee programmes",
            "Qualify NTPC Executive Trainee (GET) exam for B.Tech holders",
            "Progress from apprentice trainee → junior engineer → assistant shift in-charge",
        ],
        "qualifications": [
            "Diploma or B.Tech in Electrical / Mechanical / Instrumentation Engineering",
            "NTPC / TATA Power / Adani Power internal certifications (provided during training)",
            "CEA (Central Electricity Authority) operator certification for licensed control room operation",
        ],
        "tags": ["power-plant", "electricity", "ntpc", "operator", "energy"],
    },

    # ══════════════════════════════════════════════════════
    # FOOD SCIENCE & NUTRITION — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "dietitian_nutritionist_in",
        "title": "Dietitian / Clinical Nutritionist",
        "category": "Food Science & Nutrition",
        "region": "IN",
        "description": "Advise individuals and groups on diet and nutrition to manage health conditions, improve athletic performance, or achieve wellness goals. Hospital dietitians work in clinical settings managing patients with diabetes, kidney disease, and post-surgical recovery. Sports nutritionists work with athletes. Wellness nutritionists serve the growing corporate wellness market. Online nutrition coaching is a fast-growing independent practice.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior clinical dietitian in a hospital to head of nutrition at a corporate hospital chain or independent online nutritionist"},
        "growth_outlook": "Strong — rising health awareness, diabetes & lifestyle disease burden, and sports nutrition growing",
        "work_style": ["Clinical / Consulting", "Client-facing", "Office or online"],
        "required_skills": [
            s("Clinical Nutrition & Therapeutic Diets", "critical"), s("Nutritional Assessment", "critical"),
            s("Diet Planning & Counselling", "critical"), s("Knowledge of Food Composition", "important"),
            s("Communication & Behaviour Change Coaching", "critical"), s("Research & Evidence-Based Practice", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Food Science & Nutrition, Home Science, or Dietetics (BSc / BSc Home Science)",
            "Master's in Clinical Nutrition & Dietetics or Food Science (MSc)",
            "Internship at a tertiary care hospital (AIIMS, Fortis, Apollo) for clinical experience",
            "Register with IDA (Indian Dietetic Association) for professional recognition",
        ],
        "qualifications": [
            "BSc in Food Science & Nutrition / Home Science / Dietetics",
            "MSc / PG Diploma in Dietetics / Clinical Nutrition (AIIMS, IGNOU, SNDT, Amity)",
            "RD (Registered Dietitian) credential from IDA (Indian Dietetic Association)",
        ],
        "tags": ["dietitian", "nutritionist", "clinical-nutrition", "diet", "wellness"],
    },
    {
        "id": "food_technologist_in",
        "title": "Food Technologist / Food Scientist",
        "category": "Food Science & Nutrition",
        "region": "IN",
        "description": "Develop, test, and improve food products — from formulation and processing to packaging and shelf-life extension. India's food processing industry is the world's 5th largest and growing rapidly, with companies like ITC, Nestlé India, Hindustan Unilever Foods, Britannia, and dairy cooperatives (Amul, Mother Dairy) employing thousands of food technologists. FSSAI regulatory compliance is a key responsibility.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior technologist at a food manufacturing plant to R&D head at a major FMCG food brand"},
        "growth_outlook": "Strong — India's food processing sector targeted at 25% of food production value by 2025; government incentive-backed",
        "work_style": ["Laboratory-based", "Manufacturing", "R&D"],
        "required_skills": [
            s("Food Processing & Preservation Technology", "critical"), s("Product Development & Formulation", "critical"),
            s("Quality Control & HACCP", "critical"), s("FSSAI Regulations", "critical"),
            s("Sensory Evaluation", "important"), s("Packaging Technology", "helpful"),
        ],
        "entry_paths": [
            "B.Tech or BSc in Food Technology / Food Science from NIT, CFTRI, UICT, SRM, or state agricultural universities",
            "M.Tech / MSc in Food Technology for R&D and senior product development roles",
            "Join a food FMCG company (Nestlé, ITC, Britannia, Amul) as a quality / production / R&D trainee",
            "CFTRI (Central Food Technological Research Institute, Mysuru) short-term industry courses for skill upgrades",
        ],
        "qualifications": [
            "B.Tech in Food Technology from NIT or CFTRI-affiliated institute",
            "M.Tech / MSc in Food Science & Technology",
            "FSSAI Food Safety Supervisor Certification",
            "FSSC 22000 / HACCP Lead Auditor certification for QA management roles",
        ],
        "tags": ["food-technology", "food-science", "fssai", "r-and-d", "food-processing"],
    },

    # ─── FOOD SCIENCE — USA ───────────────────────────────
    {
        "id": "us_registered_dietitian",
        "title": "Registered Dietitian Nutritionist (RDN)",
        "category": "Food Science & Nutrition",
        "region": "US",
        "description": "Provide evidence-based nutrition counselling and dietary therapy to patients, clients, and communities. RDNs work in hospitals, long-term care, public health, schools, corporate wellness, private practice, and sports organisations. The Academy of Nutrition and Dietetics (AND) governs the RDN credential, which requires an accredited master's degree, supervised practice, and a national registration examination.",
        "salary_range": {"min": 55000, "max": 120000, "currency": "USD/year", "note": "Clinical RDN in a hospital to private practice dietitian or sports nutritionist for pro teams"},
        "growth_outlook": "Good — BLS projects 7% growth 2022-2032; telehealth expanding access to dietetic services",
        "work_style": ["Clinical / Consulting", "Client-facing", "Office or remote"],
        "required_skills": [
            s("Medical Nutrition Therapy (MNT)", "critical"), s("Nutritional Assessment (ADIME process)", "critical"),
            s("Diet Planning & Counselling", "critical"), s("Motivational Interviewing", "important"),
            s("Electronic Health Records (EHR)", "important"), s("Evidence-Based Research", "important"),
        ],
        "entry_paths": [
            "Complete an ACEND-accredited Master's in Dietetics (now required since 2024 for RDN eligibility)",
            "Complete 1,000+ hours of supervised practice through ACEND-accredited programme",
            "Pass the CDR National Registration Examination for Dietitian Nutritionists",
            "Obtain state licensure (required in most states)",
        ],
        "qualifications": [
            "Master's in Dietetics or Nutrition from ACEND-accredited programme",
            "RDN credential from CDR (Commission on Dietetic Registration)",
            "State Dietitian Licence (required in most states)",
            "Board Certification (CSSD for sports dietetics, CSO for oncology nutrition)",
        ],
        "tags": ["dietitian", "rdn", "clinical-nutrition", "sports-nutrition", "telehealth"],
    },

    # ══════════════════════════════════════════════════════
    # PUBLISHING & WRITING — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "author_writer_in",
        "title": "Author / Novelist / Poet",
        "category": "Publishing & Writing",
        "region": "IN",
        "description": "Write and publish books — fiction, non-fiction, poetry, short stories, and children's literature — in English, Hindi, and regional languages. India's publishing industry is growing, led by HarperCollins India, Penguin Random House India, Rupa Publications, and a thriving regional language market. Self-publishing (Amazon KDP, Notion Press) has democratised authorship. Successful authors supplement income with speaking, workshops, and content writing.",
        "salary_range": {"min": 10000, "max": 500000, "currency": "INR/month", "note": "Part-time author with advance + royalties to full-time bestselling author (Chetan Bhagat scale); highly variable"},
        "growth_outlook": "Growing — audiobooks, ebooks, and self-publishing platforms expanding the market",
        "work_style": ["Creative", "Self-directed", "Freelance / Independent"],
        "required_skills": [
            s("Writing & Storytelling", "critical"), s("Narrative Structure", "critical"),
            s("Research & Fact-Checking", "important"), s("Editing & Revision", "critical"),
            s("Publishing Industry Knowledge", "helpful"), s("Social Media & Author Platform Building", "important"),
        ],
        "entry_paths": [
            "Read extensively and write consistently — the only universal prerequisite",
            "Complete creative writing programmes (JNU, Ashoka, Amity) or online courses (Coursera, Gotham Writers Workshop)",
            "Submit short stories to literary magazines and anthologies to build a publishing track record",
            "Approach literary agents (Jacaranda, The Book Bakers) or publishers directly with a manuscript query",
        ],
        "qualifications": [
            "No mandatory degree — writing quality is the credential",
            "BA/MA in English Literature, Creative Writing, or Journalism (helpful foundation)",
            "Creative Writing certificate programmes from IGNOU or private writing schools",
        ],
        "tags": ["author", "writer", "publishing", "fiction", "books"],
    },
    {
        "id": "technical_writer_in",
        "title": "Technical Writer / Documentation Specialist",
        "category": "Publishing & Writing",
        "region": "IN",
        "description": "Create clear, accurate documentation for software products, APIs, hardware manuals, medical devices, and industrial equipment. India's tech industry employs thousands of technical writers — Bangalore, Pune, and Hyderabad are the largest hubs. Technical writers work closely with engineering teams and are essential in software, IT services, healthcare tech, and manufacturing. Remote and freelance opportunities are abundant.",
        "salary_range": {"min": 35000, "max": 250000, "currency": "INR/month", "note": "Junior technical writer at a product company to senior writer / documentation lead at a major tech firm (Infosys, SAP, Microsoft India)"},
        "growth_outlook": "Strong — API documentation, DevOps runbooks, and SaaS product documentation in high demand",
        "work_style": ["Writing-intensive", "Collaborative", "Office / Remote"],
        "required_skills": [
            s("Technical Communication & Plain English Writing", "critical"), s("Documentation Tools (Confluence, DITA, MadCap Flare)", "critical"),
            s("Understanding of Software Development / APIs", "important"), s("User Research & Information Architecture", "important"),
            s("Markdown & Static Site Generators (Docusaurus, GitBook)", "helpful"), s("Version Control (Git) basics", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in English, Journalism, Mass Communication, or Engineering",
            "Take a dedicated Technical Writing course (Henry Harvin, Cherryleaf, Google Technical Writing Fundamentals on Coursera — free)",
            "Build a portfolio of sample docs: API documentation, user guides, or release notes from open-source projects",
            "Apply to tech product companies (startups, SaaS, IT services) for junior technical writer roles",
        ],
        "qualifications": [
            "BA/BSc in English, Journalism, Mass Communication, or a technical field",
            "Google Technical Writing Fundamentals (free Coursera course — widely recognised)",
            "STC (Society for Technical Communication) certification",
            "DITA XML / MadCap Flare certification for specialised content authoring systems",
        ],
        "tags": ["technical-writer", "documentation", "api-docs", "saas", "content"],
    },
    {
        "id": "content_strategist_ux_writer_in",
        "title": "UX Writer / Content Strategist",
        "category": "Publishing & Writing",
        "region": "IN",
        "description": "Craft the words, labels, tooltips, error messages, onboarding flows, and microcopy inside digital products — apps, websites, and SaaS platforms. UX writing is one of the fastest-growing writing careers in India's booming product and startup ecosystem (Swiggy, Zomato, Nykaa, PhonePe, Groww). Content strategists plan the broader content ecosystem — tone of voice, information architecture, and content operations.",
        "salary_range": {"min": 50000, "max": 350000, "currency": "INR/month", "note": "Junior UX writer at a startup to senior content designer at Swiggy, Zomato, or a FAANG India office"},
        "growth_outlook": "Excellent — product design teams in India increasingly hiring dedicated UX writers; demand far outstrips supply",
        "work_style": ["Writing", "Design-adjacent", "Collaborative", "Remote-friendly"],
        "required_skills": [
            s("Microcopy & Interface Writing", "critical"), s("User Empathy & UX Research Basics", "critical"),
            s("Figma collaboration", "important"), s("Information Architecture", "important"),
            s("Brand Voice & Tone Guidelines", "important"), s("A/B Testing & Content Metrics", "helpful"),
        ],
        "entry_paths": [
            "Background in English, Journalism, Product Management, or Design",
            "Study UX writing through Google UX Design Certificate (Coursera), UX Writing Hub, or Coursera specialisations",
            "Build a portfolio of before/after UX copy critiques and product writing samples",
            "Join a startup or product company as a content writer and transition to UX writing",
        ],
        "qualifications": [
            "BA in English, Journalism, Communications, or Design",
            "Google UX Design Certificate (Coursera — covers UX writing fundamentals)",
            "UX Writing Hub Fundamentals Certificate (industry-recognised)",
            "No mandatory degree — portfolio and demonstrated craft are primary credentials",
        ],
        "tags": ["ux-writer", "content-strategy", "microcopy", "product-design", "writing"],
    },

    # ─── WRITING — USA ────────────────────────────────────
    {
        "id": "us_technical_writer",
        "title": "Technical Writer / Documentation Engineer",
        "category": "Publishing & Writing",
        "region": "US",
        "description": "Create software documentation, API reference guides, help centres, hardware manuals, regulatory submissions, and internal wikis for tech companies, SaaS platforms, healthcare devices, and aerospace/defence firms. Technical writing is a stable, remote-friendly profession. 'Documentation Engineer' and 'Developer Advocate' are emerging senior titles that combine technical writing with coding.",
        "salary_range": {"min": 65000, "max": 160000, "currency": "USD/year", "note": "Junior writer at a mid-market SaaS company to senior documentation engineer at Google, Stripe, or Twilio"},
        "growth_outlook": "Stable — BLS projects 4% growth; API docs and DevRel (developer relations) driving premium salaries",
        "work_style": ["Writing-intensive", "Remote-friendly", "Collaborative"],
        "required_skills": [
            s("Technical Communication", "critical"), s("Docs-as-Code (Markdown, Git, CI/CD publishing)", "important"),
            s("API Documentation (OpenAPI / Swagger)", "important"), s("Structured Authoring (DITA, XML)", "helpful"),
            s("Developer Empathy", "critical"), s("Information Architecture", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Technical Communication, English, Journalism, or Engineering",
            "Complete Google Technical Writing Fundamentals (free on Coursera)",
            "Build a portfolio: document an open-source project, write API tutorials, contribute to open-source docs",
            "Apply to tech companies; target startups for faster growth and broader scope",
        ],
        "qualifications": [
            "Bachelor's in Technical Communication, English, or a technical field",
            "STC Certified Technical Professional (CPTC)",
            "Google Technical Writing certification (widely recognised)",
            "API documentation specialisation (Stoplight, Swagger / OpenAPI tooling knowledge)",
        ],
        "tags": ["technical-writer", "api-docs", "developer-relations", "saas", "documentation"],
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
