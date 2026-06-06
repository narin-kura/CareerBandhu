"""Batch: Legal & Justice, Real Estate & Property, Insurance & Actuarial"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # LEGAL & JUSTICE — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "advocate_in",
        "title": "Advocate / Lawyer",
        "category": "Legal & Justice",
        "region": "IN",
        "description": "Represent clients in courts, tribunals, and legal proceedings; provide legal advice and draft contracts, petitions, and legal opinions. India has over 1.5 million registered advocates practising in areas including criminal, civil, family, corporate, tax, and constitutional law. Junior advocates typically apprentice under seniors in the first few years.",
        "salary_range": {"min": 20000, "max": 1000000, "currency": "INR/month", "note": "Junior advocate in small town to senior counsel in High Court or Supreme Court"},
        "growth_outlook": "Stable — consistent demand across courts, corporates, and NGOs",
        "work_style": ["Client-facing", "Research-intensive", "Court appearances"],
        "required_skills": [
            s("Legal Research", "critical"), s("Drafting & Documentation", "critical"),
            s("Argumentation & Advocacy", "critical"), s("Case Analysis", "critical"),
            s("Communication", "critical"), s("Negotiation", "important"),
            s("Knowledge of Indian Law (IPC, CPC, CrPC, Evidence Act)", "critical"),
        ],
        "entry_paths": [
            "Complete LLB (3-year post-graduation) or integrated BA LLB / BBA LLB (5-year after 12th)",
            "Write CLAT for admission to National Law Schools (NLUs) — the most prestigious route",
            "Enrol with the State Bar Council — mandatory before practising in any court",
            "Apprentice under a senior advocate for 1-2 years to learn court craft",
            "Start in a law firm (litigation, corporate, or dispute resolution team) as a junior associate",
        ],
        "qualifications": [
            "LLB degree (3-year) or 5-year integrated LLB from NLU or Bar Council-recognised law school",
            "State Bar Council enrolment (mandatory for practice)",
            "AIBE (All India Bar Examination) — required to appear in court independently",
            "LLM (optional) for specialisation in constitutional, corporate, IP, or international law",
        ],
        "tags": ["law", "advocate", "court", "litigation", "legal"],
    },
    {
        "id": "district_judge_in",
        "title": "District Judge / Civil Judge / Magistrate",
        "category": "Legal & Justice",
        "region": "IN",
        "description": "Preside over district-level civil and criminal courts, hear cases, and deliver judgments. Judicial officers are recruited through State Judicial Service examinations (PCS-J) conducted by High Courts. They form the backbone of India's justice delivery system — the first point of formal adjudication for millions of citizens.",
        "salary_range": {"min": 70000, "max": 260000, "currency": "INR/month", "note": "Civil Judge / Junior Division to District Judge (Principal); 7th Pay Commission scales"},
        "growth_outlook": "Stable — high judicial vacancies across states; good promotion track within judiciary",
        "work_style": ["Court-based", "Formal", "Analytical", "Government"],
        "required_skills": [
            s("Indian Law (IPC, CrPC, CPC, Evidence Act, Constitution)", "critical"),
            s("Judgment Writing", "critical"), s("Case Management", "critical"),
            s("Impartiality & Judicial Temperament", "critical"), s("Legal Research", "critical"),
        ],
        "entry_paths": [
            "Complete an LLB degree (minimum qualification for the exam)",
            "Appear for the State Judicial Service Examination (PCS-J / HJS) conducted by the state High Court",
            "Some High Courts recruit directly to District Judge grade (requiring 7 years of advocate experience)",
            "Promotion from Civil Judge to District Judge through departmental exams and seniority",
        ],
        "qualifications": [
            "LLB from a Bar Council-recognised institution",
            "State Judicial Service Exam (conducted by High Court of each state)",
            "Minimum 7 years of practice as advocate (for direct District Judge recruitment in some states)",
        ],
        "tags": ["judiciary", "judge", "magistrate", "court", "government"],
    },
    {
        "id": "company_secretary_in",
        "title": "Company Secretary (CS)",
        "category": "Legal & Justice",
        "region": "IN",
        "description": "Ensure corporate legal and regulatory compliance — conducting board meetings, filing ROC / SEBI forms, advising on corporate governance, and acting as the statutory compliance officer. CS professionals are governed by ICSI and are mandatory for all listed companies and large unlisted companies under the Companies Act 2013.",
        "salary_range": {"min": 40000, "max": 500000, "currency": "INR/month", "note": "Entry CS in an SME to Group Company Secretary of a listed conglomerate"},
        "growth_outlook": "Good — increasing compliance burden under Companies Act 2013 and SEBI regulations driving demand",
        "work_style": ["Office-based", "Compliance-driven", "Detail-oriented"],
        "required_skills": [
            s("Corporate Law & Companies Act 2013", "critical"), s("SEBI & Securities Law", "important"),
            s("Board Meeting & Secretarial Audit", "critical"), s("MCA/ROC Statutory Filing", "critical"),
            s("Contract Drafting", "important"), s("Communication", "important"),
        ],
        "entry_paths": [
            "Enrol in ICSI CS Foundation Programme after 10+2",
            "Progress through Executive and Professional examinations",
            "Complete mandatory 15-month training — company training or CS firm articleship",
            "Join listed companies, law firms, or secretarial firms after passing CS Professional exam",
        ],
        "qualifications": [
            "CS qualification from ICSI (Foundation → Executive → Professional — three exam stages)",
            "15-month training (mandatory before ICSI associateship)",
            "ACS (Associate Member) or FCS (Fellow Member) of ICSI",
        ],
        "tags": ["company-secretary", "corporate-law", "compliance", "icsi", "governance"],
    },
    {
        "id": "paralegal_in",
        "title": "Paralegal / Legal Process Outsourcing Professional",
        "category": "Legal & Justice",
        "region": "IN",
        "description": "Support lawyers and legal departments with research, drafting, case management, and document review. The Legal Process Outsourcing (LPO) industry in India is a $3-billion sector — firms like Integreon, UnitedLex, and Pangea3 employ thousands of legal professionals who serve US, UK, and Australian law firms remotely. A paralegal role can grow into an LPO team lead or in-house legal position.",
        "salary_range": {"min": 20000, "max": 100000, "currency": "INR/month", "note": "Entry legal assistant in LPO to senior paralegal or team lead in law firm"},
        "growth_outlook": "Growing — India's LPO sector expanding with global demand for cost-effective legal services",
        "work_style": ["Office-based", "Research-intensive", "Deadline-driven"],
        "required_skills": [
            s("Legal Research", "critical"), s("Document Drafting & Review", "critical"),
            s("Case File Management", "important"), s("MS Word & Legal Software", "important"),
            s("Communication in English", "critical"), s("Attention to Detail", "critical"),
        ],
        "entry_paths": [
            "Obtain an LLB or diploma in legal studies from a recognised institution",
            "Apply to LPO companies (Integreon, Pangea3, Cyril Amarchand Mangaldas support arms)",
            "Pursue a paralegal certificate from NALSAR, TISS, or a private institute",
            "Join law firm's support team as a legal executive and progress to paralegal",
        ],
        "qualifications": [
            "LLB degree (preferred) or BA in Legal Studies",
            "Diploma / Certificate in Paralegal Studies (NALSAR, TISS, private institutes)",
            "No Bar Council enrolment needed — paralegals cannot appear in court independently",
        ],
        "tags": ["paralegal", "legal-assistant", "lpo", "law-firm", "legal-research"],
    },

    # ─── LEGAL & JUSTICE — USA ───────────────────────────
    {
        "id": "us_attorney",
        "title": "Attorney / Lawyer",
        "category": "Legal & Justice",
        "region": "US",
        "description": "Represent clients in federal and state courts, provide legal counsel, draft contracts, and advise on regulatory compliance. The US has over 1.3 million licensed attorneys practising across litigation, corporate law, criminal defence, immigration, intellectual property, family law, and public interest law.",
        "salary_range": {"min": 60000, "max": 500000, "currency": "USD/year", "note": "Public defender / solo practitioner to BigLaw partner; varies enormously by specialisation and market"},
        "growth_outlook": "Stable — consistent demand in litigation, corporate, and regulatory practice",
        "work_style": ["Client-facing", "Research-intensive", "Court / Boardroom"],
        "required_skills": [
            s("Legal Research (Westlaw / LexisNexis)", "critical"), s("Brief & Memo Writing", "critical"),
            s("Oral Advocacy", "critical"), s("Case Strategy", "critical"),
            s("Negotiation", "critical"), s("Contract Drafting", "important"),
        ],
        "entry_paths": [
            "Earn a bachelor's degree (any major) → sit LSAT → attend ABA-accredited law school (JD — 3 years)",
            "Pursue summer associate programmes at law firms during law school",
            "Pass the State Bar Examination of the state you wish to practise in",
            "A federal or state judicial clerkship after JD is prestigious and builds a strong foundation",
        ],
        "qualifications": [
            "Juris Doctor (JD) from ABA-accredited law school",
            "State Bar Examination (Uniform Bar Exam used in most states)",
            "Multistate Professional Responsibility Examination (MPRE)",
            "LLM (optional) for specialisation — tax law, international law, IP",
        ],
        "tags": ["attorney", "lawyer", "litigation", "corporate-law", "legal"],
    },
    {
        "id": "us_paralegal",
        "title": "Paralegal / Legal Assistant",
        "category": "Legal & Justice",
        "region": "US",
        "description": "Support attorneys with legal research, drafting documents, organising case files, and managing client communications. Paralegals work in law firms, government agencies, corporate legal departments, and non-profits. NALA and NFPA certifications boost earning potential. IP and corporate paralegals are among the highest paid.",
        "salary_range": {"min": 38000, "max": 90000, "currency": "USD/year", "note": "Legal secretary to senior paralegal in BigLaw; IP and corporate paralegals earn more"},
        "growth_outlook": "Good — firms rely on paralegals to reduce attorney billing costs",
        "work_style": ["Office-based", "Research-intensive", "Detail-oriented"],
        "required_skills": [
            s("Legal Research", "critical"), s("Document Management", "critical"),
            s("Drafting Motions & Contracts", "important"), s("Case Management Software", "important"),
            s("Communication", "important"), s("Attention to Detail", "critical"),
        ],
        "entry_paths": [
            "Earn an AAS or bachelor's in Paralegal Studies from an ABA-approved programme",
            "Complete a certificate in Paralegal Studies (many community colleges offer them)",
            "Enter as a legal secretary and work up to paralegal with experience",
            "Obtain NALA CP (Certified Paralegal) or NFPA PACE certification",
        ],
        "qualifications": [
            "Associate's / Bachelor's in Paralegal Studies or related field",
            "ABA-approved paralegal certificate (most respected credential)",
            "NALA Certified Paralegal (CP) or NFPA PACE certification (optional but valued)",
        ],
        "tags": ["paralegal", "legal-assistant", "law-firm", "legal-research", "legal"],
    },

    # ══════════════════════════════════════════════════════
    # REAL ESTATE & PROPERTY — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "real_estate_agent_in",
        "title": "Real Estate Agent / Property Broker",
        "category": "Real Estate & Property",
        "region": "IN",
        "description": "Facilitate the buying, selling, and renting of residential and commercial properties. India's real estate sector employs millions and is growing rapidly with urbanisation, PMAY affordable housing, and smart city projects. RERA registration (post-2016 Act) is mandatory for brokers in most states. Digital platforms like 99acres, MagicBricks, and NoBroker are reshaping the industry.",
        "salary_range": {"min": 20000, "max": 500000, "currency": "INR/month", "note": "Entry agent (base + small commission) to senior independent broker — strongly commission-driven"},
        "growth_outlook": "Strong — India's real estate sector growing at 6-8% annually; Tier 2/3 cities booming",
        "work_style": ["Field-based", "Commission-driven", "Client-facing"],
        "required_skills": [
            s("Sales & Negotiation", "critical"), s("Local Property Market Knowledge", "critical"),
            s("Client Relationship Management", "critical"), s("Communication", "critical"),
            s("RERA & Legal Basics (stamp duty, registration)", "important"),
            s("Digital Listings & PropTech Platforms", "important"),
        ],
        "entry_paths": [
            "Register under RERA in your state (mandatory for brokers)",
            "Join an established real estate firm (Anarock, JLL, CBRE, local developers) as a trainee agent",
            "Build local market knowledge and a network of property owners and buyers",
            "Take up a franchise with RE/MAX India, Century 21 India, or similar brands",
            "Work on digital platforms (NoBroker, 99acres) as a listed verified agent",
        ],
        "qualifications": [
            "No mandatory formal qualification — 12th pass is the minimum",
            "RERA registration (mandatory in most states under RERA Act 2016)",
            "Certificate in Real Estate Management (NAREDCO or CREDAI institutes)",
            "Bachelor's in Business or Architecture (advantageous for commercial real estate)",
        ],
        "tags": ["real-estate", "property", "broker", "rera", "sales"],
    },
    {
        "id": "property_valuer_in",
        "title": "Property Valuer / Real Estate Appraiser",
        "category": "Real Estate & Property",
        "region": "IN",
        "description": "Assess the market value of land and buildings for sale, mortgage, taxation, insurance, and legal proceedings. Registered Valuers are governed by IBBI under the Insolvency & Bankruptcy Code. Banks, NBFCs, courts, and government bodies rely on certified valuers. Specialisations include residential, commercial, industrial, and agricultural property.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "INR/month", "note": "Junior valuer to empanelled bank valuer with multiple clients; fee-based practice at senior levels"},
        "growth_outlook": "Good — growing banking, NBFC, and insolvency sector demand for certified valuers",
        "work_style": ["Field + Office", "Analytical", "Report-writing"],
        "required_skills": [
            s("Property Market Analysis", "critical"), s("Valuation Methodologies (Cost, Income, Comparison)", "critical"),
            s("Valuation Report Writing", "critical"), s("Registration & Stamp Act knowledge", "important"),
            s("MS Excel & Valuation Models", "important"), s("Site Inspection", "critical"),
        ],
        "entry_paths": [
            "Obtain a degree in Civil Engineering, Architecture, or Commerce",
            "Pass the IBBI Registered Valuer Examination (category-wise: Land & Building, Plant & Machinery, Securities)",
            "Work with senior panel valuers of banks (SBI, HDFC, LIC Housing) to gain experience",
            "Join a valuation firm (JLL, Knight Frank, Cushman & Wakefield) for structured training",
        ],
        "qualifications": [
            "Bachelor's in Civil Engineering, Architecture, or relevant technical field",
            "IBBI Registered Valuer (Land & Building) — mandatory examination",
            "IOV (Institution of Valuers) membership or RICS accreditation (optional, adds credibility)",
        ],
        "tags": ["valuer", "appraiser", "property", "real-estate", "banking"],
    },

    # ─── REAL ESTATE — USA ───────────────────────────────
    {
        "id": "us_real_estate_agent",
        "title": "Real Estate Agent / Realtor",
        "category": "Real Estate & Property",
        "region": "US",
        "description": "Help clients buy, sell, and rent residential and commercial properties. Licensed by the state and often members of the National Association of Realtors (NAR), agents work in one of the largest service industries in the US. Top agents in competitive markets like NYC, LA, and Miami earn millions in annual commissions.",
        "salary_range": {"min": 40000, "max": 300000, "currency": "USD/year", "note": "Commission-only; median ~$55k but top performers earn $200k+"},
        "growth_outlook": "Stable — cyclical with interest rates but long-term demand remains strong",
        "work_style": ["Field-based", "Commission-driven", "Flexible hours"],
        "required_skills": [
            s("Sales & Negotiation", "critical"), s("Local Market Knowledge", "critical"),
            s("Client Relationship Management", "critical"), s("Contract Knowledge", "important"),
            s("Digital Marketing (Zillow, Realtor.com, MLS)", "important"), s("Communication", "critical"),
        ],
        "entry_paths": [
            "Complete state-required pre-licensing coursework (40-150 hours depending on state)",
            "Pass the state Real Estate License Exam",
            "Work under a licensed broker for 1-3 years (required in most states before independent practice)",
            "Join the NAR to become a Realtor and access MLS listings",
            "Earn a Broker's License after experience for independent practice or agency ownership",
        ],
        "qualifications": [
            "State Real Estate Salesperson License (exam + pre-licensing coursework)",
            "High school diploma minimum; college degree increasingly common",
            "NAR Realtor membership (for MLS access)",
            "State Broker's License (to operate an independent agency)",
        ],
        "tags": ["realtor", "real-estate", "property", "sales", "housing"],
    },
    {
        "id": "us_property_manager",
        "title": "Property Manager",
        "category": "Real Estate & Property",
        "region": "US",
        "description": "Oversee the daily operation of residential apartment complexes, commercial buildings, or industrial properties on behalf of owners. Responsibilities include tenant screening, lease management, maintenance coordination, financial reporting, and Fair Housing compliance. Property managers work for REITs, large management companies, or independently.",
        "salary_range": {"min": 45000, "max": 120000, "currency": "USD/year", "note": "On-site apartment manager to portfolio director for a large REIT; CAM certification boosts pay"},
        "growth_outlook": "Good — growing rental market and rise of institutional landlords expanding demand",
        "work_style": ["Office + Field", "Administrative", "Tenant-facing"],
        "required_skills": [
            s("Tenant Relations", "critical"), s("Lease Management", "critical"),
            s("Budgeting & Financial Reporting", "important"), s("Maintenance Coordination", "critical"),
            s("Property Management Software (AppFolio, Yardi)", "important"),
            s("Fair Housing Law Knowledge", "critical"),
        ],
        "entry_paths": [
            "Start as a leasing consultant or assistant property manager",
            "Earn a CPM (Certified Property Manager) from the Institute of Real Estate Management (IREM)",
            "CAM (Certified Apartment Manager) credential for residential management",
            "Work for a major property management company (Greystar, Lincoln Property, AvalonBay) for structured growth",
        ],
        "qualifications": [
            "Bachelor's in Business, Real Estate, or related field (preferred, not always required)",
            "State real estate licence (required in many states for leasing and management roles)",
            "CPM from IREM or CAM from NAAEI (National Apartment Association)",
        ],
        "tags": ["property-manager", "real-estate", "leasing", "facilities", "management"],
    },

    # ══════════════════════════════════════════════════════
    # INSURANCE & ACTUARIAL — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "insurance_advisor_in",
        "title": "Insurance Advisor / LIC Agent",
        "category": "Insurance & Actuarial",
        "region": "IN",
        "description": "Sell life insurance, health insurance, and investment-linked policies to individuals and businesses. India's insurance penetration is ~4% — well below the global average — creating enormous growth headroom. LIC, SBI Life, HDFC Life, ICICI Prudential, and 20+ private players license hundreds of thousands of advisors through IRDAI.",
        "salary_range": {"min": 10000, "max": 300000, "currency": "INR/month", "note": "Commission-based; top advisors earning over ₹3L/month; private insurers often offer a base + commission"},
        "growth_outlook": "Very strong — insurance penetration growing fast with rising middle class and digital distribution",
        "work_style": ["Field-based", "Commission-driven", "Relationship-based"],
        "required_skills": [
            s("Sales & Persuasion", "critical"), s("Product Knowledge (Life, Health, Term, ULIP)", "critical"),
            s("Client Relationship Management", "critical"), s("Communication", "critical"),
            s("Basic Financial Planning", "important"), s("Persistence & Follow-up", "critical"),
        ],
        "entry_paths": [
            "Pass the IRDAI Agent Exam (after mandatory 15-hour pre-licensing training)",
            "Get sponsored by an insurance company (LIC office, HDFC Life, ICICI Prudential, etc.)",
            "Become a POSP (Point of Salesperson) through a web aggregator (Policybazaar, Coverfox)",
            "Work up to Corporate Agent or Insurance Broker after experience",
        ],
        "qualifications": [
            "Minimum 10th pass (12th preferred); no degree required for IRDAI agent licence",
            "IRDAI Agent Licence (mandatory — after 15-hour training + online exam)",
            "CFP (Certified Financial Planner) for advanced financial advisory (optional but valued)",
        ],
        "tags": ["insurance", "lic", "agent", "life-insurance", "sales"],
    },
    {
        "id": "actuary_in",
        "title": "Actuary",
        "category": "Insurance & Actuarial",
        "region": "IN",
        "description": "Analyse financial risks using advanced mathematics, statistics, and financial theory — primarily for insurance pricing, reserve estimation, pension management, and investment risk. India has a critical shortage of qualified actuaries; IAI (Institute of Actuaries of India) governs the profession. Actuaries are among the highest-paid professionals in financial services.",
        "salary_range": {"min": 80000, "max": 1000000, "currency": "INR/month", "note": "Student actuary (a few exams passed) to Fellow Actuary (FIAI) at top insurer or consulting firm"},
        "growth_outlook": "Excellent — critical shortage of actuaries; IRDAI mandates qualified actuaries in all insurance companies",
        "work_style": ["Office-based", "Analytical", "Quantitative"],
        "required_skills": [
            s("Statistics & Probability", "critical"), s("Financial Mathematics", "critical"),
            s("Risk Modelling", "critical"), s("Actuarial Software (Prophet, MG-ALFA)", "critical"),
            s("R or Python", "important"), s("Communication of Risk to Non-Technical Audiences", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Mathematics, Statistics, Actuarial Science, or Economics",
            "Register with IAI and begin the exam series (CT / CA / ST papers)",
            "Join an insurance company or actuarial consulting firm (Milliman, Willis Towers Watson, Deloitte) as student actuary",
            "Progress through Core Technical → Core Applications → Specialist papers to Fellowship",
        ],
        "qualifications": [
            "Fellow of IAI (FIAI) — requires passing ~15 actuarial exams over several years",
            "Associateship (AIAI) available after partial exam completion and work experience",
            "Bachelor's in Mathematics / Statistics / Actuarial Science (prerequisite)",
        ],
        "tags": ["actuary", "insurance", "risk", "finance", "mathematics"],
    },
    {
        "id": "insurance_surveyor_in",
        "title": "Insurance Surveyor / Loss Assessor",
        "category": "Insurance & Actuarial",
        "region": "IN",
        "description": "Investigate insurance claims — visiting accident sites, fire damage locations, marine cargo losses, or factory damage — to determine the extent of loss and recommend settlement amounts. Licensed by IRDAI, surveyors are independent professionals who work with all non-life insurers on claims above ₹50,000. A high-demand, self-employed profession with growth tied to India's expanding insurance market.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "INR/month", "note": "Fee-based per survey; motor and engineering specialists with large panel rosters earn well"},
        "growth_outlook": "Stable — mandatory under non-life insurance regulations; demand grows with insurance penetration",
        "work_style": ["Field-based", "Analytical", "Independent / Self-employed"],
        "required_skills": [
            s("Damage Assessment", "critical"), s("Survey Report Writing", "critical"),
            s("Engineering / Technical Knowledge (category-specific)", "critical"),
            s("Insurance Policy Interpretation", "important"), s("Negotiation", "important"),
            s("Photography & Documentation", "critical"),
        ],
        "entry_paths": [
            "Obtain an engineering degree or relevant technical qualification (mechanical, electrical, civil)",
            "Pass the IRDAI Surveyor & Loss Assessor Examination (conducted category-wise)",
            "Work under a licensed senior surveyor to gain field experience",
            "Build a panel of insurance companies and develop a specialisation (motor, fire, marine)",
        ],
        "qualifications": [
            "BE/B.Tech in Mechanical, Electrical, Civil, or relevant engineering field",
            "IRDAI Surveyor & Loss Assessor Licence (mandatory — category-specific exams)",
            "Associate of Insurance Institute of India (A.III.) — optional but valued",
        ],
        "tags": ["insurance-surveyor", "loss-assessor", "claims", "irdai", "non-life"],
    },

    # ─── INSURANCE — USA ─────────────────────────────────
    {
        "id": "us_insurance_agent",
        "title": "Insurance Agent / Broker",
        "category": "Insurance & Actuarial",
        "region": "US",
        "description": "Sell and service life, health, property, casualty, and speciality insurance products for individuals and businesses. Agents represent a single insurer; brokers work across multiple carriers. Licensed by each state, insurance professionals operate in one of the US's largest service industries — a sector generating over $1.3 trillion in premiums annually.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "USD/year", "note": "Base + commission; independent commercial P&C brokers and top life agents earn $150k+"},
        "growth_outlook": "Stable — cyber, climate risk, and healthcare driving new policy categories",
        "work_style": ["Client-facing", "Commission-driven", "Office or field"],
        "required_skills": [
            s("Sales & Persuasion", "critical"), s("Product Knowledge (Life, P&C, Health)", "critical"),
            s("Client Relationship Management", "critical"), s("Risk Assessment", "important"),
            s("Communication", "critical"), s("CRM Software", "helpful"),
        ],
        "entry_paths": [
            "Complete state pre-licensing coursework and pass the state licensing exam (Life & Health, or P&C — separate licences)",
            "Start at a captive agency (State Farm, Allstate, Farmers) for training support and salary base",
            "Transition to the independent or broker model after building a book of business",
            "Earn the CPCU (Chartered Property Casualty Underwriter) designation for commercial lines growth",
        ],
        "qualifications": [
            "State Insurance Licence (Life & Health and / or Property & Casualty)",
            "High school diploma minimum; bachelor's degree preferred by larger employers",
            "CPCU, CLU (Chartered Life Underwriter), or ChFC for specialisation and advancement",
        ],
        "tags": ["insurance", "broker", "agent", "life-insurance", "p-and-c"],
    },
    {
        "id": "us_actuary",
        "title": "Actuary",
        "category": "Insurance & Actuarial",
        "region": "US",
        "description": "Use mathematical and statistical methods to assess and manage financial risk for insurance companies, pension funds, healthcare organisations, and investment firms. The US Bureau of Labor Statistics consistently ranks Actuary among the top 5 best jobs in America. Fellowship with CAS (casualty) or SOA (life/health/pension) is the gold standard credential.",
        "salary_range": {"min": 80000, "max": 250000, "currency": "USD/year", "note": "Entry actuarial analyst to Fellow Actuary (FCAS/FSA) at major insurer, reinsurer, or consulting firm"},
        "growth_outlook": "Excellent — BLS projects 23% growth 2021-2031; one of the fastest-growing professions",
        "work_style": ["Office-based", "Analytical", "Quantitative"],
        "required_skills": [
            s("Statistics & Probability", "critical"), s("Financial Mathematics", "critical"),
            s("Actuarial Modelling (Prophet, AXIS)", "important"), s("R or Python", "important"),
            s("Communication of Risk to Non-Technical Audiences", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Actuarial Science, Mathematics, or Statistics",
            "Pass initial SOA or CAS preliminary exams while at university or early in career",
            "Join an insurer, reinsurer, or consulting firm as an actuarial analyst",
            "Progress through exam series: SOA (P → FM → IFM → LTAM/STAM → ASA → FSA) or CAS (Exam 1-9 → ACAS → FCAS)",
        ],
        "qualifications": [
            "FSA (Fellow of Society of Actuaries) for life/health/pension",
            "FCAS (Fellow of Casualty Actuarial Society) for property/casualty",
            "Bachelor's in Actuarial Science, Mathematics, or Statistics",
        ],
        "tags": ["actuary", "insurance", "risk", "mathematics", "finance"],
    },
    {
        "id": "us_claims_adjuster",
        "title": "Claims Adjuster / Claims Examiner",
        "category": "Insurance & Actuarial",
        "region": "US",
        "description": "Investigate insurance claims — interviewing claimants, inspecting property damage, reviewing medical reports, and determining fair settlement amounts. Adjusters work as staff adjusters (insurer employees), independent adjusters (contractors), or public adjusters (who represent policyholders). Catastrophe adjusters deploy to disaster zones for surge pay and rapid experience.",
        "salary_range": {"min": 45000, "max": 100000, "currency": "USD/year", "note": "Entry desk adjuster to senior CAT adjuster or complex commercial claims specialist"},
        "growth_outlook": "Stable — natural disasters and litigation driving sustained demand for experienced adjusters",
        "work_style": ["Field + Office", "Investigative", "Case-based"],
        "required_skills": [
            s("Claims Investigation", "critical"), s("Insurance Policy Interpretation", "critical"),
            s("Xactimate Damage Estimation Software", "critical"), s("Negotiation", "important"),
            s("Report Writing", "critical"), s("Attention to Detail", "critical"),
        ],
        "entry_paths": [
            "Obtain a state adjuster licence (required in most states)",
            "Start as a desk adjuster at a major insurer (State Farm, Allstate, Liberty Mutual)",
            "Get Xactimate training (the industry-standard property damage estimation tool)",
            "Work CAT events as an independent adjuster for surge income and rapid experience",
        ],
        "qualifications": [
            "State Claims Adjuster Licence (exam-based; requirements vary by state)",
            "Bachelor's degree helpful but not always required",
            "AIC (Associate in Claims) or CPCU designation for advancement",
            "Xactimate Level 1 or Level 2 certification for property claims",
        ],
        "tags": ["claims", "adjuster", "insurance", "property-damage", "investigation"],
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
