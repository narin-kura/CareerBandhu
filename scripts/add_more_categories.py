"""Add 5 new categories: Arts & Crafts, Language & Diplomacy,
Trading & Commodities, Medical Supplies & Distribution, Manufacturing & Production"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # ARTS & CRAFTS — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "fine_artist_in",
        "title": "Fine Artist / Painter",
        "category": "Arts & Crafts",
        "region": "IN",
        "description": "Create original works of art — paintings, drawings, mixed media — for galleries, collectors, commissions, and exhibitions. Fine artists in India find opportunity through government cultural grants (Lalit Kala Akademi), art fairs (India Art Fair), digital platforms, and art education. Income is variable but the field is growing as art collecting and appreciation expands in India.",
        "salary_range": {"min": 15000, "max": 500000, "currency": "INR/month", "note": "Highly variable; teaching + commissions + grants + exhibitions"},
        "growth_outlook": "Growing — art market and digital sales platforms expanding artist reach",
        "work_style": ["Creative", "Self-directed", "Studio-based"],
        "required_skills": [
            s("Drawing & Painting", "critical"), s("Colour Theory", "critical"),
            s("Creative Vision", "critical"), s("Art History Knowledge", "helpful"),
            s("Portfolio Development", "important"), s("Digital Marketing", "helpful"),
        ],
        "entry_paths": [
            "Bachelor of Fine Arts (BFA) from government art colleges (JJ School of Art Mumbai, Faculty of Fine Arts Baroda, Delhi College of Art)",
            "Master of Fine Arts (MFA) for deeper specialisation",
            "Build portfolio; submit to galleries, art fairs, and online platforms (Saatchi Art, Artsy)",
            "Apply for Lalit Kala Akademi grants and artist residencies",
            "Supplement income through art workshops, commissions, and art education",
        ],
        "qualifications": [
            "BFA — Bachelor of Fine Arts (5 years; JJ School of Art, Faculty of Fine Arts Baroda, Delhi College of Art)",
            "MFA — Master of Fine Arts (for advanced specialisation and teaching)",
            "Lalit Kala Akademi fellowship / national awards (recognition, not mandatory)",
            "NET / SET for college-level teaching positions",
        ],
        "tags": ["fine-art", "painting", "creative", "gallery", "artist"],
    },
    {
        "id": "sculptor_ceramics_in",
        "title": "Sculptor & Ceramic Artist",
        "category": "Arts & Crafts",
        "region": "IN",
        "description": "Create three-dimensional art works in clay, stone, metal, wood, or mixed media for galleries, public installations, architecture, and collectors. Ceramic artists additionally produce functional and decorative pottery. India has rich traditions in sculpture and pottery across regions — from Moradabad brassware to Khurja ceramics.",
        "salary_range": {"min": 15000, "max": 300000, "currency": "INR/month", "note": "Teaching + commissions + exports + residencies"},
        "growth_outlook": "Stable — growing interest in handmade, artisan objects and public art",
        "work_style": ["Creative", "Hands-on", "Studio-based"],
        "required_skills": [
            s("Sculpture Techniques", "critical"), s("Clay / Pottery / Ceramics", "important"),
            s("Material Knowledge", "critical"), s("Creative Vision", "critical"),
            s("3D Spatial Thinking", "important"), s("Portfolio Development", "important"),
        ],
        "entry_paths": [
            "BFA with sculpture or applied arts specialisation",
            "Train at ceramics studios, craft schools, or under master artisans",
            "Government craft board training programs (state khadi/handloom/ceramic boards)",
            "Build portfolio; exhibit at craft fairs, art galleries, and online platforms",
        ],
        "qualifications": [
            "BFA in Sculpture or Applied Arts (government art colleges)",
            "Diploma in Ceramics / Pottery from state craft institutes",
            "MFA for academic and advanced practice",
            "PM Vishwakarma recognition for traditional artisans",
        ],
        "tags": ["sculpture", "ceramics", "pottery", "craft", "fine-art"],
    },
    {
        "id": "jewellery_designer_in",
        "title": "Jewellery Designer",
        "category": "Arts & Crafts",
        "region": "IN",
        "description": "Design and create jewellery pieces — from traditional gold and gemstone designs to contemporary fashion jewellery. India is the world's largest jewellery market. Jewellery designers work with manufacturers, retail brands (Tanishq, Malabar), boutique studios, export houses, and as independent artisans.",
        "salary_range": {"min": 25000, "max": 300000, "currency": "INR/month", "note": "Designer to creative director; own label scales significantly"},
        "growth_outlook": "Strong — India's jewellery exports growing; domestic premium segment expanding",
        "work_style": ["Creative", "Detail-oriented", "Studio-based"],
        "required_skills": [
            s("Jewellery Design", "critical"), s("Gemology basics", "important"),
            s("CAD for Jewellery (Rhinoceros, Matrix, JewelCAD)", "important"),
            s("Material Knowledge (metals, stones)", "critical"),
            s("Sketching", "critical"), s("Craftsmanship", "important"),
        ],
        "entry_paths": [
            "Diploma or Degree in Jewellery Design (NIFT, GIA India, JD Institute, SNDT)",
            "Gemology courses (GIA, Gem & Jewellery Export Promotion Council)",
            "Apprenticeship with established jewellery manufacturers or designers",
            "Build portfolio; work with jewellery brands or set up own label",
        ],
        "qualifications": [
            "Diploma / Degree in Jewellery Design (NIFT, GIA India, JD Institute of Fashion)",
            "GIA (Gemological Institute of America) Graduate Gemologist — for gemology specialisation",
            "GJEPC (Gem & Jewellery Export Promotion Council) certification",
            "CAD software proficiency: Rhinoceros / Matrix / JewelCAD",
        ],
        "tags": ["jewellery", "design", "craft", "export", "luxury"],
    },
    {
        "id": "textile_artist_in",
        "title": "Textile & Fabric Artist",
        "category": "Arts & Crafts",
        "region": "IN",
        "description": "Create art and functional objects through weaving, dyeing, embroidery, block printing, and fabric manipulation. India's textile traditions — Banarasi silk, Kantha, Phulkari, Kalamkari, Ajrakh — are globally acclaimed. Textile artists work in fashion, home decor, galleries, craft exports, and cultural preservation.",
        "salary_range": {"min": 20000, "max": 250000, "currency": "INR/month", "note": "Weaver to design head or own brand; export scales income"},
        "growth_outlook": "Growing — handloom revival, sustainable fashion, and cultural export demand",
        "work_style": ["Creative", "Hands-on", "Craft-focused"],
        "required_skills": [
            s("Textile Techniques (weaving, dyeing, printing)", "critical"),
            s("Colour Theory", "important"), s("Design", "critical"),
            s("Material Knowledge", "critical"), s("Cultural Textile Heritage", "helpful"),
            s("Pattern Making", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's / Diploma in Textile Design (NIFT, NID, IIAD, state polytechnics)",
            "Train under master weavers or at weaver service centres (Government)",
            "National Handloom Development Programme (NHDP) training",
            "Sell through craft cooperatives, own label, or online (Craft Village, Etsy)",
        ],
        "qualifications": [
            "Bachelor's / Diploma in Textile Design (NIFT, NID, state polytechnics)",
            "National Handloom Development Programme (NHDP) certification",
            "Weavers Service Centre training (government, free for weavers)",
            "PM Vishwakarma Yojana recognition for traditional weavers",
        ],
        "tags": ["textile", "weaving", "handloom", "craft", "design"],
    },
    {
        "id": "us_studio_craft_artist",
        "title": "Studio Craft Artist",
        "category": "Arts & Crafts",
        "region": "US",
        "description": "Create handmade objects — pottery, glass, metalwork, woodwork, fibre art, jewellery — as both fine art and functional craft. American craft artists sell through galleries, craft fairs (American Craft Council), Etsy, and studio sales. Many supplement income through teaching workshops or artist residencies.",
        "salary_range": {"min": 30000, "max": 100000, "currency": "USD/year", "note": "Highly variable; galleries + teaching + commissions + fairs"},
        "growth_outlook": "Stable — handmade goods market growing; craft tourism and workshops flourishing",
        "work_style": ["Creative", "Self-directed", "Studio-based"],
        "required_skills": [
            s("Craft Mastery (pottery / glassblowing / metalsmithing / woodwork)", "critical"),
            s("Creative Vision", "critical"), s("Business basics", "important"),
            s("Portfolio Development", "important"), s("Marketing & Etsy / online sales", "helpful"),
        ],
        "entry_paths": [
            "BFA in Craft, Studio Art, or Fine Arts (RISD, Cranbrook, Alfred University for ceramics)",
            "MFA for teaching positions at universities and art schools",
            "Apprenticeship / residency at craft centres",
            "Build sales through American Craft Council fairs, Etsy, galleries",
        ],
        "qualifications": [
            "BFA or MFA in Studio Art, Craft, or Fine Arts (RISD, Cranbrook, Alfred, MICA)",
            "No mandatory credential — strong portfolio and exhibition record",
            "Artist residency credentials (Haystack, Penland, Arrowmont — prestigious in the field)",
            "NEA (National Endowment for the Arts) grants for recognition",
        ],
        "tags": ["craft", "studio-art", "pottery", "handmade", "fine-art"],
    },

    # ══════════════════════════════════════════════════════
    # LANGUAGE & DIPLOMACY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "translator_interpreter_in",
        "title": "Translator / Interpreter",
        "category": "Language & Diplomacy",
        "region": "IN",
        "description": "Convert written text (translation) or spoken language (interpretation) between languages — enabling communication across government, business, courts, hospitals, and international organisations. India's multilingual environment and growing global business presence create strong demand for translators in languages including English, French, German, Spanish, Arabic, Chinese, and Japanese.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Freelance per-word/hour to senior govt translator; UN/EU pays premium"},
        "growth_outlook": "Strong — globalisation, BPO, legal, and diplomatic demand growing",
        "work_style": ["Remote-friendly", "Detail-oriented", "Research-driven"],
        "required_skills": [
            s("Fluency in 2+ Languages", "critical"), s("Writing Precision", "critical"),
            s("Cultural Knowledge", "important"), s("Research", "important"),
            s("Subject Matter Expertise", "helpful"), s("CAT Tools (SDL Trados, memoQ)", "helpful"),
        ],
        "entry_paths": [
            "BA or MA in Linguistics, Foreign Language, or Translation Studies (JNU, Hyderabad Central University, BHU)",
            "Certifications from Central Translation Bureau or language institutes (Alliance Française, Goethe Institut, British Council)",
            "Freelance on ProZ, Translators Café, or with corporates, courts, and hospitals",
            "Government: Ministry of External Affairs, Doordarshan, Lok Sabha Secretariat",
        ],
        "qualifications": [
            "BA / MA in Foreign Language, Linguistics, or Translation Studies",
            "Language Proficiency Certificate: DELF (French), Goethe Zertifikat (German), JLPT (Japanese), HSK (Chinese)",
            "Central Translation Bureau (CTB) empanelment for government translation work",
            "ATA (American Translators Association) certification for international work",
        ],
        "tags": ["translation", "language", "interpretation", "multilingual", "linguistics"],
    },
    {
        "id": "ifs_officer_in",
        "title": "Indian Foreign Service (IFS) Officer",
        "category": "Language & Diplomacy",
        "region": "IN",
        "description": "Represent India's interests abroad as a diplomat — managing bilateral relations, trade negotiations, consular services, and cultural diplomacy from Indian embassies and consulates worldwide. IFS is one of the most prestigious civil services in India, requiring clearing the UPSC Civil Services Examination.",
        "salary_range": {"min": 75000, "max": 250000, "currency": "INR/month", "note": "Plus overseas allowances, accommodation, and perquisites — effective package 2-4x base"},
        "growth_outlook": "Stable — fixed cadre; highly competitive but prestigious lifetime career",
        "work_style": ["International travel", "Diplomatic", "High-responsibility"],
        "required_skills": [
            s("Foreign Languages", "critical"), s("Communication", "critical"),
            s("Negotiation", "critical"), s("General Knowledge & Current Affairs", "critical"),
            s("Writing & Report Drafting", "important"), s("Cultural Sensitivity", "important"),
            s("Leadership", "important"),
        ],
        "entry_paths": [
            "Bachelor's degree in any discipline from a recognised university",
            "Clear UPSC Civil Services Examination (Prelims → Mains → Personality Test)",
            "Rank high enough to qualify for IFS allocation (typically top 100-150 ranks)",
            "Foreign Service Institute training in New Delhi + language training",
        ],
        "qualifications": [
            "Bachelor's degree (any discipline) from a recognised university",
            "UPSC Civil Services Examination — IFS allocation based on rank and preference",
            "Foreign Service Institute (FSI) training (post-selection, mandatory)",
            "Mandatory foreign language training (Arabic, French, Russian, Chinese, etc.)",
        ],
        "tags": ["ifs", "upsc", "diplomacy", "foreign-service", "government"],
    },
    {
        "id": "conference_interpreter_in",
        "title": "Conference Interpreter",
        "category": "Language & Diplomacy",
        "region": "IN",
        "description": "Provide simultaneous or consecutive interpretation at high-level conferences, government summits, UN events, business meetings, and international forums. One of the most intellectually demanding language careers — interpreters work in real-time, often for international organisations, the Government of India, and multinational corporations.",
        "salary_range": {"min": 50000, "max": 500000, "currency": "INR/month", "note": "Freelance per-day rates for senior conference interpreters can be very high"},
        "growth_outlook": "Stable — high skill barrier keeps supply low; demand steady from GOI and corporates",
        "work_style": ["High-pressure", "Travel", "Freelance or contracted"],
        "required_skills": [
            s("Simultaneous Interpretation", "critical"), s("Fluency in 3+ Languages", "critical"),
            s("Active Listening & Memory", "critical"), s("Quick Thinking", "critical"),
            s("Subject Matter Expertise", "important"), s("Stress Management", "important"),
        ],
        "entry_paths": [
            "MA or Postgraduate Diploma in Conference Interpretation (JNU, Hyderabad, IIFT)",
            "Train at AIIC-recognised programmes (International Association of Conference Interpreters)",
            "Intern at government bodies (Lok Sabha, Rajya Sabha, MEA) or international organisations",
            "Build client base with corporates, UN agencies, and diplomatic missions in India",
        ],
        "qualifications": [
            "MA or PG Diploma in Conference Interpretation or Translation",
            "AIIC membership (International Association of Conference Interpreters — career gold standard)",
            "UN language examination (for UN Secretariat / agency interpreter positions)",
            "Minimum 2 working languages + 1 passive language for most conference roles",
        ],
        "tags": ["interpretation", "conference", "diplomacy", "language", "multilingual"],
    },

    # ── LANGUAGE & DIPLOMACY — USA ────────────────────────
    {
        "id": "us_foreign_service_officer",
        "title": "US Foreign Service Officer (Diplomat)",
        "category": "Language & Diplomacy",
        "region": "US",
        "description": "Represent the United States abroad through diplomacy, consular services, trade advocacy, and public affairs at US embassies and consulates worldwide. Entry via the highly competitive Foreign Service Officer Test (FSOT). One of the most prestigious government careers in the US.",
        "salary_range": {"min": 55000, "max": 150000, "currency": "USD/year", "note": "Plus overseas differentials, housing allowance — effective total significantly higher"},
        "growth_outlook": "Stable — Foreign Service has fixed hiring quotas; competitive but prestigious",
        "work_style": ["International travel", "Diplomatic", "High-responsibility"],
        "required_skills": [
            s("Communication", "critical"), s("Negotiation", "critical"),
            s("Foreign Language Proficiency", "important"), s("Critical Thinking", "critical"),
            s("Cultural Sensitivity", "critical"), s("Leadership", "important"),
        ],
        "entry_paths": [
            "Bachelor's degree in any field (International Relations, Political Science, Languages popular)",
            "Pass FSOT — Foreign Service Officer Test (written exam)",
            "Qualify Qualifications Evaluation Panel (QEP), Oral Assessment, and Security Clearance",
            "Foreign Service Institute language and diplomatic training (post-appointment)",
        ],
        "qualifications": [
            "Bachelor's degree (any discipline) — required for FSOT eligibility",
            "FSOT — Foreign Service Officer Test + Oral Assessment (State Dept selection process)",
            "Top Secret security clearance (mandatory)",
            "Foreign language proficiency (language-designated positions — additional pay for proficiency)",
        ],
        "tags": ["diplomacy", "foreign-service", "fsot", "state-department", "government"],
    },
    {
        "id": "us_interpreter_translator",
        "title": "Interpreter / Translator",
        "category": "Language & Diplomacy",
        "region": "US",
        "description": "Convert spoken or written content between languages for courts, hospitals, government agencies, schools, corporations, and international organisations. Spanish, Mandarin, Arabic, French, and Russian are top languages in demand. Medical and legal interpreting are among the highest-paying specialisations.",
        "salary_range": {"min": 45000, "max": 100000, "currency": "USD/year", "note": "Court-certified and medical interpreters earn premium rates"},
        "growth_outlook": "Strong — BLS projects 20% growth; immigration and globalisation driving demand",
        "work_style": ["Remote-friendly", "Flexible", "Specialisation-driven"],
        "required_skills": [
            s("Fluency in 2+ Languages", "critical"), s("Writing Precision", "critical"),
            s("Cultural Knowledge", "important"), s("Subject Matter Expertise", "important"),
            s("CAT Tools (SDL Trados, memoQ)", "helpful"), s("Simultaneous Interpretation", "helpful"),
        ],
        "entry_paths": [
            "BA in Languages, Linguistics, or Translation Studies",
            "ATA (American Translators Association) certification for professional credibility",
            "Court Interpreter certification (federal or state) for legal work",
            "CMI certification (Certified Medical Interpreter) for healthcare work",
            "Freelance through ProZ, Translators Café, or agency contracts",
        ],
        "qualifications": [
            "BA in Linguistics, Foreign Language, or Translation (preferred)",
            "ATA Certification (American Translators Association — industry gold standard)",
            "Federal Court Interpreter Certification or State Court certification",
            "CMI — Certified Medical Interpreter (for healthcare settings)",
        ],
        "tags": ["translation", "interpretation", "language", "legal", "medical"],
    },

    # ══════════════════════════════════════════════════════
    # TRADING & COMMODITIES — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "commodity_trader_in",
        "title": "Commodity Trader",
        "category": "Trading & Commodities",
        "region": "IN",
        "description": "Trade commodities — agricultural products (wheat, cotton, spices), metals (gold, silver, copper), and energy (crude oil, natural gas) — on MCX (Multi Commodity Exchange) and NCDEX. Commodity traders work at brokerage firms, commodity houses, importers/exporters, or as proprietary traders.",
        "salary_range": {"min": 40000, "max": 500000, "currency": "INR/month", "note": "Fixed salary + trading P&L; top traders earn significantly more"},
        "growth_outlook": "Strong — commodity markets growing with India's trade and manufacturing expansion",
        "work_style": ["Fast-paced", "Analytical", "High-pressure"],
        "required_skills": [
            s("Market Analysis", "critical"), s("Risk Management", "critical"),
            s("Commodity Knowledge", "critical"), s("Financial Modelling", "important"),
            s("Trading Platforms (MCX, NCDEX)", "important"), s("Economics", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Commerce, Economics, Finance, or Agriculture",
            "NISM (National Institute of Securities Markets) certifications — Commodity Derivatives",
            "Join commodity brokerage firms, trading companies, or agri-businesses",
            "SEBI-registered research analyst or trading desk career path",
        ],
        "qualifications": [
            "Bachelor's in Commerce, Economics, or Finance",
            "NISM Series-XVII: Commodity Derivatives certification (SEBI-mandated for trading roles)",
            "SEBI Research Analyst Registration (for publishing commodity reports)",
            "MBA Finance or CFA for senior trading/research roles",
        ],
        "tags": ["commodity", "trading", "mcx", "ncdex", "finance"],
    },
    {
        "id": "import_export_consultant_in",
        "title": "Import-Export Trade Consultant",
        "category": "Trading & Commodities",
        "region": "IN",
        "description": "Advise businesses on international trade — including customs documentation, import-export licensing, trade regulations, HS codes, DGFT policies, foreign exchange compliance, and logistics. Critical for SMEs and manufacturers looking to export or source globally. High demand given India's growing trade volumes.",
        "salary_range": {"min": 35000, "max": 300000, "currency": "INR/month", "note": "Salaried or independent consultant; fee-based for senior experts"},
        "growth_outlook": "Strong — India's export push and PLI scheme driving more businesses into international trade",
        "work_style": ["Advisory", "Detail-oriented", "Client-facing"],
        "required_skills": [
            s("International Trade Regulations", "critical"), s("Customs & DGFT Procedures", "critical"),
            s("Documentation", "critical"), s("FEMA & Foreign Exchange", "important"),
            s("Logistics Knowledge", "important"), s("Communication", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Commerce, Economics, or International Business",
            "Diploma in Export Management (IIFT, IIBM, Export Promotion Councils)",
            "DGFT (Directorate General of Foreign Trade) processes and IEC (Import-Export Code) registration",
            "Work at freight forwarders, customs brokers, or export houses",
        ],
        "qualifications": [
            "Bachelor's in Commerce / Economics / International Business",
            "Diploma in Export Management (IIFT New Delhi, Indian Institute of Foreign Trade)",
            "IEC — Importer Exporter Code (mandatory for any export/import business)",
            "CHA — Customs House Agent license (for customs clearance professionals)",
        ],
        "tags": ["import-export", "trade", "customs", "dgft", "international-business"],
    },
    {
        "id": "stockbroker_in",
        "title": "Stock Broker / Equity Dealer",
        "category": "Trading & Commodities",
        "region": "IN",
        "description": "Execute buy and sell orders for clients or proprietary books on the NSE and BSE. Stock brokers advise retail and institutional clients on equity investments, manage trading accounts, and analyse markets. The profession spans discount broking (Zerodha, Groww model) to full-service advisory.",
        "salary_range": {"min": 30000, "max": 400000, "currency": "INR/month", "note": "Fixed + brokerage commission; top brokers and advisors earn substantially more"},
        "growth_outlook": "Strong — India's retail investor base growing rapidly; equity market expanding",
        "work_style": ["Fast-paced", "Client-facing", "Analytical"],
        "required_skills": [
            s("Equity Research", "important"), s("Market Analysis", "critical"),
            s("Client Communication", "critical"), s("SEBI Regulations", "critical"),
            s("Financial Modelling", "helpful"), s("Risk Management", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Commerce, Finance, or Economics",
            "NISM certifications (mandatory for SEBI-regulated activities)",
            "Join brokerage firms, investment banks, or trading desks",
            "SEBI-registered Investment Adviser or Research Analyst for advisory roles",
        ],
        "qualifications": [
            "Bachelor's in Commerce / Finance / Economics",
            "NISM Series-VIII: Equity Derivatives (mandatory for F&O trading)",
            "NISM Series-VII: Securities Operations and Risk Management",
            "SEBI Research Analyst Registration (for publishing equity recommendations)",
            "NSE/BSE Sub-Broker Registration",
        ],
        "tags": ["stockbroker", "equity", "nse", "bse", "trading"],
    },
    {
        "id": "forex_analyst_in",
        "title": "Forex Analyst / Currency Risk Manager",
        "category": "Trading & Commodities",
        "region": "IN",
        "description": "Analyse foreign exchange markets, forecast currency movements, and help businesses manage forex exposure and risk. Forex professionals work at banks (treasury divisions), corporates (hedging import/export risks), forex brokers, and financial research firms. RBI regulations govern India's forex market.",
        "salary_range": {"min": 50000, "max": 400000, "currency": "INR/month", "note": "Bank treasury to senior forex risk manager"},
        "growth_outlook": "Growing — India's growing import-export base creates forex risk management demand",
        "work_style": ["Analytical", "High-pressure", "Research-driven"],
        "required_skills": [
            s("Forex Market Knowledge", "critical"), s("Technical Analysis", "important"),
            s("Fundamental Analysis", "important"), s("Risk Management", "critical"),
            s("FEMA (Foreign Exchange Management Act)", "important"),
            s("Bloomberg / Reuters terminals", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Finance, Economics, or Commerce",
            "MBA Finance or CFA for research and senior treasury roles",
            "Join bank treasury departments or corporate forex desks",
            "FEDAI (Foreign Exchange Dealers Association of India) courses",
        ],
        "qualifications": [
            "Bachelor's in Finance / Economics",
            "MBA Finance or CFA (CFA Institute) for senior roles",
            "FEDAI forex dealer courses (Foreign Exchange Dealers Association of India)",
            "NISM certifications for SEBI-regulated advisory activities",
        ],
        "tags": ["forex", "currency", "treasury", "risk-management", "finance"],
    },

    # ── TRADING & COMMODITIES — USA ───────────────────────
    {
        "id": "us_commodities_trader",
        "title": "Commodities Trader",
        "category": "Trading & Commodities",
        "region": "US",
        "description": "Trade futures and options on agricultural commodities, energy (oil, gas, electricity), and metals (gold, silver, copper) on CME Group (Chicago Mercantile Exchange) and ICE. Traders work at commodity houses (Cargill, ADM), investment banks, hedge funds, or as proprietary traders.",
        "salary_range": {"min": 80000, "max": 500000, "currency": "USD/year", "note": "Base + substantial P&L-based bonus; top traders earn millions"},
        "growth_outlook": "Stable — commodity markets essential; algorithmic trading changing the landscape",
        "work_style": ["Fast-paced", "High-pressure", "Quantitative"],
        "required_skills": [
            s("Market Analysis", "critical"), s("Risk Management", "critical"),
            s("Quantitative Skills", "important"), s("Commodity Knowledge", "critical"),
            s("Bloomberg / Reuters", "important"), s("Programming (Python)", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Finance, Economics, Mathematics, or Engineering",
            "Series 3 — National Commodity Futures Examination (FINRA, mandatory for commodity advisors)",
            "Trading internship at commodity houses, banks, or hedge funds",
            "CTA — Commodity Trading Advisor registration with CFTC",
        ],
        "qualifications": [
            "Bachelor's in Finance / Economics / Math / Engineering",
            "Series 3 — National Commodity Futures Examination (FINRA-required)",
            "CTA — Commodity Trading Advisor registration (CFTC, for managing client funds)",
            "NFA membership (National Futures Association) for compliance",
        ],
        "tags": ["commodities", "futures", "trading", "cme", "finance"],
    },
    {
        "id": "us_trade_advisor",
        "title": "International Trade Advisor",
        "category": "Trading & Commodities",
        "region": "US",
        "description": "Guide companies through the complexities of US import/export regulations, tariff classification, trade compliance, customs law, and international trade agreements. Trade advisors work at law firms, customs brokerages, Big 4 consulting practices, freight forwarders, and as independent consultants.",
        "salary_range": {"min": 65000, "max": 150000, "currency": "USD/year", "note": "Trade compliance specialist to senior trade attorney / director"},
        "growth_outlook": "Strong — tariff volatility, supply chain restructuring, and trade compliance demand growing",
        "work_style": ["Advisory", "Detail-oriented", "Client-facing"],
        "required_skills": [
            s("US Customs & Trade Regulations (CBP, BIS, OFAC)", "critical"),
            s("Tariff Classification (HTS Codes)", "critical"),
            s("Import/Export Documentation", "critical"),
            s("Trade Agreement Knowledge (USMCA, FTAs)", "important"),
            s("Compliance & Risk Management", "important"), s("Communication", "important"),
        ],
        "entry_paths": [
            "Bachelor's in International Business, Supply Chain, or Law",
            "Licensed Customs Broker (LCB) exam (CBP — US Customs and Border Protection)",
            "Certified Export Specialist (CES) from NASBITE",
            "Work at customs brokerages, Big 4 trade practice, or corporate compliance teams",
        ],
        "qualifications": [
            "Bachelor's in International Business / Supply Chain / Law",
            "Licensed Customs Broker (LCB) — CBP national exam",
            "CES — Certified Export Specialist (NASBITE International)",
            "CUSECO or NCBFAA broker certification",
            "JD with Trade Law specialisation for attorney-level advisory",
        ],
        "tags": ["trade", "customs", "international-business", "compliance", "export"],
    },

    # ══════════════════════════════════════════════════════
    # MEDICAL SUPPLIES & DISTRIBUTION — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "medical_equipment_rep_in",
        "title": "Medical Equipment Sales Representative",
        "category": "Medical Supplies & Distribution",
        "region": "IN",
        "description": "Sell and demonstrate medical devices and equipment — from diagnostic machines (MRI, CT, ultrasound) and surgical instruments to hospital beds and ICU equipment — to hospitals, clinics, and laboratories. One of India's fastest-growing sales careers as healthcare infrastructure expands rapidly.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "INR/month", "note": "Fixed + sales commission; top reps in capital equipment earn high commissions"},
        "growth_outlook": "Very strong — India's healthcare infrastructure investment growing significantly",
        "work_style": ["Field-based", "Travel-heavy", "Client-facing"],
        "required_skills": [
            s("Medical Device Knowledge", "critical"), s("Sales", "critical"),
            s("Communication", "critical"), s("Relationship Building", "critical"),
            s("Basic Clinical Knowledge", "important"), s("Negotiation", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Biomedical Engineering, Life Sciences, Pharmacy, or B.Sc",
            "Some companies accept any science/commerce graduate with training",
            "Product training provided by medical device companies",
            "Work at Indian or multinational med-tech companies (GE Healthcare, Siemens Healthineers, Philips, local OEMs)",
        ],
        "qualifications": [
            "Bachelor's in Biomedical Engineering / Pharmacy / Life Sciences / B.Sc",
            "No specific licence required; company product training is mandatory",
            "CDSCO (Central Drugs Standard Control Organisation) knowledge for regulated devices",
            "MBA Marketing for sales management / senior commercial roles",
        ],
        "tags": ["medical-devices", "sales", "healthcare", "meditec", "hospital"],
    },
    {
        "id": "pharma_sales_rep_in",
        "title": "Pharmaceutical Sales Representative (MR)",
        "category": "Medical Supplies & Distribution",
        "region": "IN",
        "description": "Promote and sell prescription and OTC pharmaceutical products to doctors, hospitals, and pharmacies as a Medical Representative (MR). The pharmaceutical industry is one of India's largest employers of science graduates. India is the pharmacy of the world — the role is stable, well-structured, and offers strong growth into management.",
        "salary_range": {"min": 25000, "max": 120000, "currency": "INR/month", "note": "MR to District Manager; CTC includes allowances and incentives"},
        "growth_outlook": "Strong — India's pharma industry growing steadily; rural healthcare expansion",
        "work_style": ["Field-based", "Travel", "Client-facing"],
        "required_skills": [
            s("Pharmaceutical Product Knowledge", "critical"), s("Sales", "critical"),
            s("Communication", "critical"), s("Relationship Building", "critical"),
            s("Basic Medical / Clinical Knowledge", "important"), s("Territory Management", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Pharmacy (B.Pharm), Life Sciences, or B.Sc",
            "Company training programs on products and detailing skills",
            "Join pharma companies (Sun Pharma, Cipla, Dr. Reddy's, Lupin, MNCs)",
            "Progress: MR → Senior MR → Area Sales Manager → Regional Manager",
        ],
        "qualifications": [
            "B.Pharm or B.Sc in Life Sciences (Biology, Chemistry, Microbiology)",
            "Some companies accept any graduate and train internally",
            "CDSCO Drug Representative knowledge (for scheduled drug promotion)",
            "MBA Pharma / Healthcare Management for management-track roles",
        ],
        "tags": ["pharma", "medical-rep", "sales", "healthcare", "drugs"],
    },
    {
        "id": "hospital_supply_manager_in",
        "title": "Hospital Supply Chain & Materials Manager",
        "category": "Medical Supplies & Distribution",
        "region": "IN",
        "description": "Manage procurement, storage, and distribution of medical supplies, pharmaceuticals, surgical items, and equipment within hospitals and healthcare systems. A critical backend role that directly impacts patient care quality and hospital operational efficiency.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "INR/month", "note": "Materials manager to Supply Chain Director in hospital chains"},
        "growth_outlook": "Strong — hospital chain expansion and healthcare infrastructure investment",
        "work_style": ["Operations", "Detail-oriented", "Cross-functional"],
        "required_skills": [
            s("Procurement & Inventory Management", "critical"), s("Healthcare Supply Knowledge", "critical"),
            s("Vendor Management", "important"), s("ERP / HMS Systems", "important"),
            s("Quality & Compliance", "important"), s("Budgeting", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Hospital Administration, Pharmacy, Supply Chain, or Commerce",
            "MBA in Hospital Administration or Supply Chain Management",
            "Work in hospital administration, materials department, or pharma distribution",
            "Join hospital chains (Apollo, Fortis, Narayana Health) or government hospitals",
        ],
        "qualifications": [
            "Bachelor's in Hospital Administration / Pharmacy / Supply Chain",
            "MBA in Hospital Administration or Healthcare Management",
            "Diploma in Materials Management (IIMM — Indian Institute of Materials Management)",
            "APICS CSCP or CPSM certification for advanced supply chain roles",
        ],
        "tags": ["supply-chain", "hospital", "procurement", "healthcare", "operations"],
    },
    {
        "id": "medical_distributor_in",
        "title": "Medical Supplies Distributor / Dealer",
        "category": "Medical Supplies & Distribution",
        "region": "IN",
        "description": "Own and operate a business distributing medical supplies, equipment, surgical goods, diagnostic kits, or pharmaceuticals to hospitals, clinics, laboratories, and pharmacies. A growing entrepreneurial opportunity as India's healthcare market expands into tier-2 and tier-3 cities. Investment: ₹5L – ₹50L depending on product category.",
        "salary_range": {"min": 40000, "max": 1000000, "currency": "INR/month", "note": "Business profit — scalable with territory and product range"},
        "growth_outlook": "Very strong — healthcare infrastructure building in non-metro India",
        "work_style": ["Self-employed", "Operations", "Relationship-driven"],
        "required_skills": [
            s("Business Management", "critical"), s("Sales & Relationship Building", "critical"),
            s("Inventory Management", "important"), s("Medical / Pharma Knowledge", "important"),
            s("Financial Management", "important"), s("Logistics", "helpful"),
        ],
        "entry_paths": [
            "Drug License from State Drug Controller (mandatory for pharma distribution)",
            "GST registration and business entity setup",
            "Tie up with pharma companies or medical device OEMs as authorised distributor",
            "Background in pharma sales (MR) or healthcare business is helpful",
        ],
        "qualifications": [
            "Drug License — Form 20/21 for retail / wholesale pharma distribution (State Drug Controller)",
            "GST Registration (mandatory)",
            "B.Pharm or D.Pharm required for drug wholesale/retail licenses",
            "MSME / Udyam Registration (for government supply tenders)",
        ],
        "tags": ["medical-distribution", "pharma", "entrepreneurship", "healthcare", "business"],
    },

    # ── MEDICAL SUPPLIES & DISTRIBUTION — USA ─────────────
    {
        "id": "us_medical_device_sales",
        "title": "Medical Device Sales Representative",
        "category": "Medical Supplies & Distribution",
        "region": "US",
        "description": "Sell medical devices — from surgical instruments and implants to imaging equipment and hospital IT systems — to hospitals, surgeons, and medical centres. One of the highest-paying sales careers in the US, with substantial base + commission structure. Surgical reps often observe live procedures.",
        "salary_range": {"min": 80000, "max": 200000, "currency": "USD/year", "note": "Base + commission + bonus; top surgical device reps earn $300k+"},
        "growth_outlook": "Strong — US healthcare spending growing; device innovation driving new product launches",
        "work_style": ["Field-based", "High-pressure", "Relationship-driven"],
        "required_skills": [
            s("Sales", "critical"), s("Medical Device Knowledge", "critical"),
            s("Relationship Building", "critical"), s("Clinical Knowledge", "important"),
            s("Negotiation", "important"), s("Territory Management", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Biology, Biomedical Engineering, Kinesiology, or Business",
            "Medical device companies train new reps extensively on products",
            "Start as sales associate or clinical specialist at device companies",
            "Experience as physical therapist, athletic trainer, or nurse often provides entry path",
        ],
        "qualifications": [
            "Bachelor's degree (Life Sciences, Biomedical Engineering, Business — no strict requirement)",
            "No FDA licence required for most reps; company product certification mandatory",
            "NAMSR (National Association of Medical Sales Representatives) certification",
            "MBA for sales management and commercial leadership tracks",
        ],
        "tags": ["medical-devices", "sales", "healthcare", "medtech", "hospital"],
    },
    {
        "id": "us_healthcare_supply_chain",
        "title": "Healthcare Supply Chain Manager",
        "category": "Medical Supplies & Distribution",
        "region": "US",
        "description": "Oversee procurement, logistics, and distribution of medical supplies, drugs, and equipment across hospital systems. Healthcare supply chain professionals ensure clinical teams always have what they need — while managing costs, vendor contracts, and regulatory compliance in one of the US economy's largest and most regulated sectors.",
        "salary_range": {"min": 75000, "max": 150000, "currency": "USD/year", "note": "Supply chain analyst to VP of Supply Chain at hospital system"},
        "growth_outlook": "Strong — post-COVID supply chain resilience investment; hospital system consolidation",
        "work_style": ["Operations", "Cross-functional", "Analytical"],
        "required_skills": [
            s("Supply Chain Management", "critical"), s("Healthcare Procurement", "critical"),
            s("Vendor Management", "important"), s("ERP / Supply Chain software", "important"),
            s("Data Analysis", "important"), s("Compliance (GPO, FDA, Joint Commission)", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Supply Chain, Healthcare Administration, Business, or Logistics",
            "MBA or MHA (Master of Health Administration) for leadership roles",
            "APICS CSCP (Certified Supply Chain Professional) certification",
            "Work at hospital GPOs, IDNs, or healthcare distributors (McKesson, Cardinal Health)",
        ],
        "qualifications": [
            "Bachelor's in Supply Chain / Healthcare Administration / Business",
            "MBA or MHA for director-level and above roles",
            "APICS CSCP — Certified Supply Chain Professional (industry credential)",
            "AHRMM CMRP — Certified Materials and Resource Professional (healthcare-specific)",
        ],
        "tags": ["supply-chain", "healthcare", "procurement", "hospital", "operations"],
    },

    # ══════════════════════════════════════════════════════
    # MANUFACTURING & PRODUCTION — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "manufacturing_engineer_in",
        "title": "Manufacturing Engineer",
        "category": "Manufacturing & Production",
        "region": "IN",
        "description": "Design, optimise, and manage manufacturing processes, production lines, and factory systems to produce goods efficiently and with high quality. Manufacturing engineers work across sectors — auto, electronics, FMCG, aerospace, pharma, and defence. India's PLI scheme is driving massive manufacturing investment.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "INR/month", "note": "Junior engineer to senior manufacturing / process engineer"},
        "growth_outlook": "Very strong — Make in India, PLI schemes, and China+1 strategy driving investment",
        "work_style": ["Plant-based", "Technical", "Problem-solving"],
        "required_skills": [
            s("Manufacturing Processes", "critical"), s("Lean Manufacturing", "important"),
            s("CAD / SolidWorks / AutoCAD", "important"), s("Quality Management", "important"),
            s("Problem Solving", "critical"), s("Production Planning", "helpful"),
            s("ERP (SAP / Oracle)", "helpful"),
        ],
        "entry_paths": [
            "B.E. / B.Tech in Mechanical, Production, Industrial, or Manufacturing Engineering",
            "Internships in manufacturing plants during degree",
            "Entry roles: Graduate Engineer Trainee (GET) in manufacturing companies",
            "Work up: GET → Engineer → Senior Engineer → Asst Manager → Manager",
        ],
        "qualifications": [
            "B.E. / B.Tech in Mechanical / Production / Industrial Engineering (AICTE-recognised)",
            "M.Tech for specialisation and senior technical roles",
            "Six Sigma Green Belt / Black Belt (Lean and quality management)",
            "SAP PP (Production Planning) module certification (helpful for ERP-driven environments)",
        ],
        "tags": ["manufacturing", "engineering", "production", "lean", "make-in-india"],
    },
    {
        "id": "production_manager_in",
        "title": "Production Manager",
        "category": "Manufacturing & Production",
        "region": "IN",
        "description": "Plan, coordinate, and oversee all manufacturing activities to meet production targets on time, within budget, and to quality standards. Production managers are the operational backbone of factories — managing people, machines, materials, and schedules simultaneously.",
        "salary_range": {"min": 60000, "max": 300000, "currency": "INR/month", "note": "Production supervisor to plant head / General Manager"},
        "growth_outlook": "Strong — every manufacturing unit needs production management professionals",
        "work_style": ["Operational", "Leadership", "Plant-based"],
        "required_skills": [
            s("Production Planning & Scheduling", "critical"), s("Leadership", "critical"),
            s("Quality Management", "important"), s("Lean / Kaizen / 5S", "important"),
            s("Cost Management", "important"), s("ERP Systems", "helpful"),
            s("Problem Solving", "critical"),
        ],
        "entry_paths": [
            "B.E./B.Tech in Mechanical, Production, or Industrial Engineering",
            "Start as production engineer or floor supervisor",
            "MBA Operations for fast-track management roles",
            "Relevant experience across auto, FMCG, pharma, or electronics manufacturing",
        ],
        "qualifications": [
            "B.E. / B.Tech in Mechanical / Production / Industrial Engineering",
            "MBA Operations or PG Diploma in Production / Industrial Management",
            "Six Sigma Black Belt for process improvement leadership",
            "Certified Production and Inventory Management (CPIM — APICS)",
        ],
        "tags": ["production", "manufacturing", "operations", "management", "factory"],
    },
    {
        "id": "qc_engineer_in",
        "title": "Quality Control / Quality Assurance Engineer",
        "category": "Manufacturing & Production",
        "region": "IN",
        "description": "Ensure products meet quality standards through inspection, testing, process audits, and root cause analysis. QC/QA engineers work in every manufacturing sector — automotive (IATF 16949), pharma (GMP), food (FSSAI), electronics (IPC), and aerospace (AS9100). The role is critical for exports and customer satisfaction.",
        "salary_range": {"min": 35000, "max": 180000, "currency": "INR/month", "note": "QC Inspector to Senior QA Manager"},
        "growth_outlook": "Strong — quality compliance essential for export markets and PLI-linked production",
        "work_style": ["Detail-oriented", "Analytical", "Plant-based"],
        "required_skills": [
            s("Quality Management Systems (ISO 9001, IATF 16949, GMP)", "critical"),
            s("Inspection & Testing Techniques", "critical"), s("Root Cause Analysis", "important"),
            s("Statistical Process Control (SPC)", "important"),
            s("Documentation", "important"), s("Measurement Tools (CMM, gauges)", "helpful"),
        ],
        "entry_paths": [
            "B.E./B.Tech in Mechanical, Production, or relevant engineering",
            "ISO Lead Auditor / Internal Auditor training",
            "Entry: Quality Inspector or QA trainee in manufacturing plants",
            "Industry certifications: Six Sigma, ISO, sector-specific (IATF, GMP, IPC)",
        ],
        "qualifications": [
            "B.E. / B.Tech in Mechanical / Production / Electronics Engineering",
            "ISO 9001 Lead Auditor certification",
            "Six Sigma Green Belt or Black Belt",
            "IATF 16949 Internal Auditor (for automotive), GMP (for pharma), IPC (for electronics)",
        ],
        "tags": ["quality", "qc", "qa", "manufacturing", "iso"],
    },
    {
        "id": "industrial_engineer_in",
        "title": "Industrial Engineer",
        "category": "Manufacturing & Production",
        "region": "IN",
        "description": "Optimise complex systems — people, machines, materials, information, and energy — to eliminate waste and improve efficiency. Industrial engineers use techniques like time-motion study, line balancing, capacity planning, and simulation to make factories and operations run better.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "INR/month", "note": "IE trainee to Senior Industrial Engineering Manager"},
        "growth_outlook": "Strong — automation, lean adoption, and global competitiveness driving demand",
        "work_style": ["Analytical", "Plant-based", "Cross-functional"],
        "required_skills": [
            s("Industrial Engineering techniques (time study, line balancing)", "critical"),
            s("Lean Manufacturing / Toyota Production System", "critical"),
            s("Process Mapping & Value Stream Mapping", "important"),
            s("Data Analysis", "important"), s("AutoCAD / Plant Layout", "helpful"),
            s("Ergonomics", "helpful"),
        ],
        "entry_paths": [
            "B.E./B.Tech in Industrial Engineering, Production Engineering, or Mechanical",
            "Internships in IE departments of manufacturing companies",
            "Entry: Industrial Engineering trainee or Methods Engineer",
            "Specialise in Lean, Six Sigma, simulation, or automation",
        ],
        "qualifications": [
            "B.E. / B.Tech in Industrial / Production / Mechanical Engineering",
            "M.Tech in Industrial Engineering for research and senior roles",
            "Six Sigma Black Belt + Lean Expert certification",
            "CPIM (Certified in Production and Inventory Management — APICS)",
        ],
        "tags": ["industrial-engineering", "lean", "manufacturing", "efficiency", "operations"],
    },
    {
        "id": "automation_robotics_engineer_in",
        "title": "Automation & Robotics Engineer",
        "category": "Manufacturing & Production",
        "region": "IN",
        "description": "Design, program, and maintain automated manufacturing systems — PLCs, SCADA, robotic arms, conveyor systems, and smart factory technologies. Automation engineers are among the most in-demand professionals in Indian manufacturing as Industry 4.0 adoption accelerates across auto, electronics, and FMCG.",
        "salary_range": {"min": 50000, "max": 250000, "currency": "INR/month", "note": "Junior automation engineer to senior automation/robotics lead"},
        "growth_outlook": "Very strong — Industry 4.0, EV manufacturing, and electronics PLI driving automation investment",
        "work_style": ["Technical", "Plant-based", "Problem-solving"],
        "required_skills": [
            s("PLC Programming (Siemens, Allen-Bradley)", "critical"),
            s("SCADA / HMI Systems", "critical"), s("Robotics (ABB, FANUC, KUKA)", "important"),
            s("Electrical / Control Systems", "critical"), s("Automation Design", "important"),
            s("Python / C for automation scripting", "helpful"),
        ],
        "entry_paths": [
            "B.E./B.Tech in Electrical, Electronics, Mechatronics, or Instrumentation Engineering",
            "Diploma in Automation / PLC-SCADA (government ITIs, NTTF, private institutes)",
            "PLC/SCADA certifications from Siemens, Rockwell, Schneider",
            "Entry at machine builders, system integrators, or automotive OEMs",
        ],
        "qualifications": [
            "B.E. / B.Tech in Electrical / Electronics / Mechatronics / Instrumentation",
            "Diploma in Automation / PLC-SCADA (NTTF, CIPET, state polytechnics)",
            "Siemens SINUMERIK / SIMATIC or Allen-Bradley ControlLogix certification",
            "FANUC or ABB Robotics programming certification",
        ],
        "tags": ["automation", "robotics", "plc", "scada", "industry4"],
    },

    # ── MANUFACTURING & PRODUCTION — USA ─────────────────
    {
        "id": "us_manufacturing_engineer",
        "title": "Manufacturing Engineer",
        "category": "Manufacturing & Production",
        "region": "US",
        "description": "Design, implement, and improve manufacturing processes and production systems across the US industrial base — from automotive and aerospace to electronics, defence, and medical devices. Manufacturing engineers are central to America's reshoring push and remain in strong demand.",
        "salary_range": {"min": 70000, "max": 120000, "currency": "USD/year", "note": "Entry to senior manufacturing engineer; management roles pay more"},
        "growth_outlook": "Strong — reshoring, CHIPS Act, IRA, and defence investment creating new manufacturing jobs",
        "work_style": ["Plant-based", "Technical", "Problem-solving"],
        "required_skills": [
            s("Manufacturing Processes", "critical"), s("Lean / Six Sigma", "important"),
            s("CAD (SolidWorks / NX / CATIA)", "important"), s("GD&T", "important"),
            s("Quality Management", "important"), s("ERP (SAP / Oracle)", "helpful"),
        ],
        "entry_paths": [
            "BS in Mechanical, Industrial, Manufacturing, or Materials Engineering",
            "Co-op or internship at manufacturing companies during degree",
            "Entry: Manufacturing Engineer I at automotive, aerospace, or electronics OEMs",
            "SME (Society of Manufacturing Engineers) membership for networking and certifications",
        ],
        "qualifications": [
            "BS in Mechanical / Industrial / Manufacturing Engineering (ABET-accredited)",
            "PE (Professional Engineer) licence for senior engineering sign-off roles",
            "Six Sigma Green Belt / Black Belt (ASQ certification)",
            "SME Certified Manufacturing Engineer (CMfgE)",
        ],
        "tags": ["manufacturing", "engineering", "lean", "aerospace", "automotive"],
    },
    {
        "id": "us_industrial_engineer",
        "title": "Industrial Engineer",
        "category": "Manufacturing & Production",
        "region": "US",
        "description": "Optimise production systems, supply chains, and operational workflows using engineering principles, data analysis, and process improvement methods. Industrial engineers work across manufacturing, logistics, healthcare, and technology companies — one of the most versatile engineering disciplines in the US.",
        "salary_range": {"min": 70000, "max": 110000, "currency": "USD/year", "note": "Entry IE to senior Industrial Engineer or operations manager"},
        "growth_outlook": "Strong — BLS projects steady demand; IE skills valuable in non-manufacturing sectors too",
        "work_style": ["Analytical", "Cross-functional", "Problem-solving"],
        "required_skills": [
            s("Industrial Engineering techniques", "critical"), s("Lean / Six Sigma", "critical"),
            s("Data Analysis", "important"), s("Process Simulation (Arena, AnyLogic)", "helpful"),
            s("Supply Chain Knowledge", "important"), s("Ergonomics", "helpful"),
        ],
        "entry_paths": [
            "BS in Industrial Engineering from ABET-accredited university",
            "Internship / co-op at manufacturing or logistics companies",
            "Entry roles at automotive OEMs, Amazon fulfilment, healthcare systems",
            "IISE (Institute of Industrial and Systems Engineers) membership",
        ],
        "qualifications": [
            "BS in Industrial Engineering (ABET-accredited — Stanford, Georgia Tech, Penn State, Purdue)",
            "PE licence (Professional Engineer) for senior roles",
            "Six Sigma Black Belt (ASQ — American Society for Quality)",
            "Lean Expert or CPIM (APICS) for operations specialisation",
        ],
        "tags": ["industrial-engineering", "lean", "operations", "logistics", "manufacturing"],
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
