"""Add qualifications field to all 118 careers in careers.json."""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"

QUALS = {
    # ── Technology (IN) ────────────────────────────────────────────────
    "software_engineer": [
        "Bachelor's in CS / IT / Software Engineering (preferred)",
        "Coding bootcamp + strong project portfolio accepted",
        "Cloud certifications (AWS / GCP / Azure) — optional but valued",
    ],
    "data_scientist": [
        "Bachelor's in Statistics, Math, CS, or related field",
        "Master's or PhD preferred for research / senior roles",
        "Kaggle / Google Data Analytics certification (supplementary)",
    ],
    "ml_engineer": [
        "Bachelor's / Master's in CS, Math, or AI",
        "Strong foundation in linear algebra, calculus, and statistics",
        "Relevant ML certifications (deeplearning.ai, Coursera) — supplementary",
    ],
    "devops_engineer": [
        "Bachelor's in CS / IT (preferred)",
        "AWS DevOps / GCP / Azure DevOps certification",
        "Linux Foundation certifications (LFCS, CKA) — preferred",
    ],
    "cloud_architect": [
        "Bachelor's in CS or IT",
        "AWS Solutions Architect Professional / GCP Professional Cloud Architect / Azure Expert certification",
    ],
    "cybersecurity_analyst": [
        "Bachelor's in CS, IT, or Cybersecurity",
        "CompTIA Security+ (entry level)",
        "CEH — Certified Ethical Hacker or CISSP for senior roles",
    ],
    "full_stack_developer": [
        "Bachelor's in CS / IT (preferred) or accredited coding bootcamp",
        "Portfolio of deployed full-stack projects",
    ],
    "mobile_app_developer": [
        "Bachelor's in CS / IT (preferred)",
        "Published apps on Play Store / App Store (often outweighs degree)",
        "Google / Apple developer program membership",
    ],
    "ux_ui_designer": [
        "Bachelor's in Design, HCI, or Visual Communication (preferred)",
        "Google UX Design Certificate (Coursera) — widely accepted",
        "Strong portfolio in Figma / Adobe XD mandatory",
    ],
    "product_manager": [
        "Bachelor's degree (any discipline)",
        "MBA preferred for senior / Director-level roles",
        "AIPMM CPM or Pragmatic Institute certifications",
    ],
    "data_analyst": [
        "Bachelor's in Statistics, Math, Economics, or CS",
        "Microsoft / Google Data Analytics certification",
        "SQL, Excel, Tableau / Power BI proficiency",
    ],
    "business_analyst": [
        "Bachelor's in Business, IT, or related field",
        "CBAP — Certified Business Analysis Professional (IIBA)",
        "PMI-PBA — Professional in Business Analysis",
    ],
    "project_manager": [
        "Bachelor's degree (any discipline)",
        "PMP — Project Management Professional (PMI)",
        "PRINCE2 or Agile / Scrum (CSM) certification",
    ],
    "digital_marketing_manager": [
        "Bachelor's in Marketing, Communications, or any field",
        "Google Analytics & Ads certifications",
        "HubSpot, Meta Blueprint, or SEMrush certifications",
    ],
    "financial_analyst": [
        "Bachelor's in Finance, Accounting, or Economics",
        "CFA — Chartered Financial Analyst (CFA Institute) — preferred",
        "FRM for risk-focused roles",
    ],
    "accountant": [
        "B.Com or Bachelor's in Accounting / Finance",
        "CA (ICAI) for senior statutory roles in India",
        "CMA / ACCA for management / international accounting",
    ],
    "hr_manager": [
        "Bachelor's in HR, Business, or Psychology",
        "MBA in HR preferred for senior roles",
        "SHRM-CP / PHR certification",
    ],
    "graphic_designer": [
        "Bachelor's in Graphic Design, Visual Arts, or Fine Arts",
        "Adobe Certified Professional (Photoshop / Illustrator)",
        "Portfolio of published / client work is mandatory",
    ],
    "content_writer": [
        "Bachelor's in English, Journalism, Communications, or any field",
        "Strong writing portfolio across formats",
        "SEO / content marketing certifications (optional)",
    ],
    "video_producer": [
        "Bachelor's in Film, Media Production, or Communications (preferred)",
        "Adobe Premiere / Final Cut Pro proficiency",
        "Showreel / portfolio of produced content",
    ],
    "teacher_educator": [
        "Bachelor's in the subject of specialization",
        "B.Ed — Bachelor of Education (mandatory for school teaching)",
        "CTET / State TET (mandatory for government schools in India)",
        "NET / SET for college-level teaching",
    ],
    "corporate_trainer": [
        "Bachelor's degree (any discipline)",
        "MBA / Postgraduate in HRD or L&D (preferred)",
        "Certified Training Professional (CTP) or ATD-CPLP",
    ],
    "operations_manager": [
        "Bachelor's in Business, Engineering, or Operations Management",
        "MBA preferred for senior / VP roles",
        "Six Sigma Green or Black Belt (valued)",
    ],
    "sales_manager": [
        "Bachelor's degree (any discipline)",
        "MBA in Marketing / Sales (preferred for corporate ladder)",
        "Relevant industry certifications (SalesForce, HubSpot CRM)",
    ],
    "healthcare_administrator": [
        "Bachelor's in Healthcare Administration, Business, or Public Health",
        "MHA or MBA (Healthcare) for senior roles",
    ],
    "data_engineer": [
        "Bachelor's in CS, Engineering, or related field",
        "Cloud certifications: AWS Data Analytics / GCP Data Engineer",
        "Apache Spark / Kafka knowledge (certifications optional)",
    ],
    "game_developer": [
        "Bachelor's in CS, Game Design, or Software Engineering",
        "Unity Certified Associate / Unreal certification (optional)",
        "Published game portfolio on itch.io / Steam",
    ],
    "bi_developer": [
        "Bachelor's in CS, Data Science, or Business",
        "Microsoft Power BI Data Analyst Associate certification",
        "Tableau Desktop Specialist certification",
    ],
    "investment_analyst": [
        "Bachelor's in Finance, Economics, or Business",
        "CFA Level I (minimum) — CFA charterholder preferred",
        "NISM certifications for securities market roles (India)",
    ],
    "supply_chain_manager": [
        "Bachelor's in Supply Chain, Logistics, Engineering, or Business",
        "APICS CPIM — Certified in Production & Inventory Management",
        "APICS CSCP — Certified Supply Chain Professional",
    ],
    "content_strategist": [
        "Bachelor's in Marketing, Communications, or Journalism",
        "HubSpot Content Marketing certification",
        "SEO certifications (Moz, SEMrush, Google)",
    ],
    "instructional_designer": [
        "Bachelor's in Education, Instructional Design, or related",
        "Master's in Instructional Technology preferred for academia",
        "ATD CPTD or eLearning Guild certification",
    ],
    # ── Trades & Construction ───────────────────────────────────────────
    "electrician": [
        "ITI — Industrial Training Institute in Electrician trade (2 years)",
        "Wireman License from State Electrical Inspectorate (mandatory)",
        "CITS — Craft Instructor Training Scheme (for supervisory / training roles)",
    ],
    "plumber": [
        "ITI in Plumbing trade (2 years)",
        "Apprenticeship under a licensed plumber",
        "Contractor / Trade License for independent work",
    ],
    "carpenter": [
        "ITI in Carpentry trade (2 years) or apprenticeship",
        "Diploma in Interior Design / Furniture Design (optional)",
    ],
    "auto_mechanic": [
        "ITI in Automobile or Motor Vehicle Mechanic (2 years)",
        "Diploma in Automobile Engineering (optional but valued)",
        "OEM training certifications (Maruti, Toyota, etc.) for dealerships",
    ],
    "welder": [
        "ITI in Welding (1-2 years)",
        "CSWIP / AWS Certified Welder for premium / export roles",
        "ASME / API certifications for pressure vessel / pipeline work",
    ],
    "civil_engineer": [
        "B.E. / B.Tech in Civil Engineering (mandatory)",
        "M.Tech for research or senior design roles",
        "State Council of Engineering registration",
        "UPSC Engineering Services (IES) for government roles",
    ],
    # ── Healthcare ──────────────────────────────────────────────────────
    "nurse": [
        "B.Sc Nursing (4 years) or GNM — General Nursing & Midwifery (3.5 years)",
        "State Nursing Council registration (mandatory)",
        "NCLEX-RN for international nursing (USA / Canada / UK)",
    ],
    "anaesthesiologist": [
        "MBBS — 5.5 years (MCI / NMC recognized college)",
        "MD / DNB in Anaesthesiology (3 years post-MBBS)",
        "NMC registration mandatory to practice",
    ],
    "pharmacist": [
        "B.Pharm — Bachelor of Pharmacy (4 years) or D.Pharm (2 years)",
        "State Pharmacy Council registration (mandatory)",
        "M.Pharm for research / quality control roles",
    ],
    "physiotherapist": [
        "BPT — Bachelor of Physiotherapy (4.5 years)",
        "State Physiotherapy Council registration (mandatory)",
        "MPT — Master of Physiotherapy for specialist / senior roles",
    ],
    "ayurvedic_doctor": [
        "BAMS — Bachelor of Ayurvedic Medicine and Surgery (5.5 years)",
        "State Ayurveda Council registration (mandatory to practice)",
        "MD (Ayurveda) for specialist and academic roles",
    ],
    # ── Food & Hospitality ──────────────────────────────────────────────
    "chef": [
        "Diploma / Degree in Culinary Arts or Hotel Management (IHM / state polytechnic)",
        "Craft Certificate in Food Production (NCHMCT/IHM)",
        "No formal qualification needed for self-employment / small food business",
    ],
    "hotel_manager": [
        "BHM — Bachelor of Hotel Management (3-4 years, NCHMCT affiliated)",
        "MBA in Hospitality Management for GM / senior roles",
    ],
    "baker": [
        "Certificate / Diploma in Bakery & Confectionery (IHM / State Polytechnic)",
        "NCHMCT short-term bakery programs",
        "Portfolio of products (for freelance / own bakery setup)",
    ],
    # ── Beauty & Wellness ───────────────────────────────────────────────
    "hair_stylist": [
        "Cosmetology / Hairdressing Diploma (VLCC, Lakme Academy, PIVOT POINT)",
        "State-recognized vocational certificate in beauty & wellness",
        "International: City & Guilds or CIDESCO certification (for premium salons)",
    ],
    "fitness_trainer": [
        "Diploma in Fitness and Nutrition (government polytechnic or recognized institute)",
        "ACSM / ACE / NASM / ISSA Certified Personal Trainer",
        "CPR / AED certification (mandatory)",
    ],
    "yoga_instructor": [
        "200-hour Yoga Teacher Training (RYT-200, Yoga Alliance registered)",
        "Certification from AYUSH Ministry or QCI-accredited yoga schools",
        "Advanced: 500-hour RYT for studios or specialized teaching",
    ],
    # ── Fashion & Apparel ───────────────────────────────────────────────
    "fashion_designer": [
        "B.Des in Fashion Design (NIFT / NID / Pearl Academy or equivalent)",
        "Diploma in Fashion Design (3 years) from state polytechnic",
        "Portfolio of design collections mandatory for employment",
    ],
    "tailor": [
        "ITI in Dress Making / Sewing Technology (1-2 years)",
        "Short-term vocational certificate from state polytechnic",
        "No formal qualification required for independent tailoring",
    ],
    # ── Transport & Logistics ───────────────────────────────────────────
    "commercial_driver": [
        "Class 10 pass (minimum)",
        "HMV / HGV Driving License from RTO (mandatory)",
        "HAZMAT endorsement for hazardous goods transport",
        "Passenger Transport endorsement for buses / taxis",
    ],
    "logistics_manager": [
        "Bachelor's in Logistics, Supply Chain, or Business Administration",
        "APICS CPIM / CSCP or CILT certification (preferred)",
    ],
    # ── Agriculture & Farming ───────────────────────────────────────────
    "progressive_farmer": [
        "No formal qualification required for self-employed farming",
        "Diploma in Agriculture (preferred, improves techniques & loan access)",
        "Krishi Vigyan Kendra (KVK) or state agriculture university training",
    ],
    "agricultural_officer": [
        "B.Sc Agriculture (mandatory)",
        "State Agricultural Service Exam or UPSC for central services",
        "M.Sc Agriculture / Ph.D for research and senior posts",
    ],
    # ── Arts & Performance ──────────────────────────────────────────────
    "photographer": [
        "Diploma / Degree in Photography (FTII, NID, or equivalent)",
        "Portfolio-driven field — no formal qualification mandatory",
        "Adobe Lightroom / Photoshop proficiency",
    ],
    "musician": [
        "Diploma / Degree in Music or Performing Arts (preferred)",
        "Guru-Shishya training for classical streams",
        "Recording portfolio / live performance experience mandatory",
    ],
    "actor": [
        "Diploma in Performing Arts / Acting (NSD, FTII, or film institutes)",
        "Acting workshops and method acting courses (short-term accepted)",
        "Showreel / stage experience essential",
    ],
    # ── Government & Public Service ─────────────────────────────────────
    "civil_servant_ias": [
        "Bachelor's degree in any discipline (mandatory)",
        "UPSC Civil Services Examination — Prelims + Mains + Personality Test",
        "Age limit: 21-32 years (General); relaxations for OBC / SC / ST",
    ],
    "bank_officer": [
        "Graduation in any discipline (mandatory)",
        "IBPS PO Exam (Prelims + Mains + Interview) or SBI PO Exam",
        "IBPS Specialist Officer (SO) Exam for technical / IT cadre",
    ],
    "police_officer": [
        "Class 12 for constable level; Graduation for ASI / SI / DSP",
        "State Police Service Exam or UPSC IPS for gazetted ranks",
        "Physical fitness and medical standards mandatory at all ranks",
    ],
    "railway_officer": [
        "B.Tech / B.E. for Group A (IRSE, IRSS, IRTS) and technical cadre",
        "Graduation for Group B and administrative cadre",
        "UPSC Engineering Services Exam or UPSC Civil Services (IRS/IRTS)",
    ],
    # ── Retail & Commerce ───────────────────────────────────────────────
    "retail_manager": [
        "Bachelor's in Retail Management, Business, or Marketing",
        "MBA / PGDM preferred for chain retail / brand management roles",
    ],
    # ── Social Work & Community ─────────────────────────────────────────
    "social_worker": [
        "BSW — Bachelor of Social Work (UGC-recognized, mandatory for formal sector)",
        "MSW — Master of Social Work for senior / specialized / policy roles",
        "Certification from reputed NGOs or TISS for niche domains",
    ],
    # ── Media & Journalism ──────────────────────────────────────────────
    "journalist": [
        "BJMC — Bachelor of Journalism & Mass Communication",
        "Bachelor's in English / Political Science also widely accepted",
        "Published internship / portfolio of articles essential",
        "PCI press card for practicing journalists",
    ],
    # ── Aviation & Airport ──────────────────────────────────────────────
    "air_traffic_controller": [
        "Bachelor's in Physics / Math / Electronics or B.Tech (preferred)",
        "DGCA ATC License (mandatory)",
        "AAI ATC Recruitment Exam (Airports Authority of India)",
        "Medical fitness as per DGCA requirements",
    ],
    "commercial_pilot": [
        "Class 12 with Physics + Math (mandatory)",
        "CPL — Commercial Pilot License (DGCA)",
        "Minimum 200 flying hours (for CPL issuance)",
        "DGCA Class 1 Medical Certificate",
    ],
    "cabin_crew": [
        "Class 12 pass (minimum qualification)",
        "Aviation Hospitality Diploma (preferred by most airlines)",
        "Airline-specific cabin crew training (mandatory on joining)",
        "DGCA approved first-aid and safety certifications",
    ],
    "aircraft_maintenance_engineer": [
        "Class 12 with Physics + Math (mandatory)",
        "AME License — DGCA Category A / B1 / B2",
        "AME course from DGCA-approved institute (3-4 years)",
        "Type Rating on specific aircraft models",
    ],
    "airport_ground_staff": [
        "Class 12 pass (minimum)",
        "Diploma in Airport / Ground Operations Management (preferred)",
        "BCAS security training (mandatory on joining)",
    ],
    "airport_manager": [
        "Bachelor's in Aviation Management, Business, or Engineering",
        "MBA in Aviation Management (preferred for senior roles)",
        "IATA Diploma in Airport Operations",
    ],
    "customs_officer": [
        "Bachelor's degree in any discipline",
        "UPSC IRS (Customs & Central Excise) Exam for Group A officers",
        "SSC CGL Exam for Inspector-level posts",
    ],
    # ── Defence & Armed Forces ──────────────────────────────────────────
    "army_officer": [
        "NDA route: Class 12 + NDA Entrance Exam (UPSC) + SSB Interview",
        "CDS route: Graduation + UPSC CDS Exam + SSB Interview",
        "TES / TGC for engineering graduates (direct commission)",
        "Medical fitness as per Army standards mandatory",
    ],
    "navy_officer": [
        "NDA route: Class 12 (Physics + Math) + NDA Exam + SSB Interview",
        "CDSE route: B.Tech / Graduation + UPSC CDS + SSB Interview",
        "Executive / Technical / Pilot branches — different educational requirements",
        "Medical fitness as per Naval standards mandatory",
    ],
    "air_force_officer": [
        "NDA route: Class 12 (Physics + Math) + NDA Exam + SSB + PABT",
        "AFCAT: Graduation + Air Force Common Admission Test + SSB",
        "B.Tech for technical / engineering branches",
        "Medical fitness including vision standards mandatory",
    ],
    "agniveer": [
        "Class 10 pass (minimum for most categories)",
        "Class 12 or ITI for technical categories",
        "Age: 17.5 to 21 years",
        "Agnipath Scheme written exam + physical fitness test + medical",
    ],
    # ── Maritime & Shipping ─────────────────────────────────────────────
    "merchant_navy_officer": [
        "Class 12 with Physics + Math + Chemistry",
        "B.Sc Nautical Science or B.Tech Marine Engineering (DGS-approved, 4 years)",
        "STCW Basic Safety Training certificates (mandatory)",
        "Pre-Sea Training from DGS-approved institute",
    ],
    "port_operations": [
        "Bachelor's in Port Management, Logistics, Civil, or Mechanical Engineering",
        "Diploma in Port & Shipping Management (preferred)",
        "IAME / ICSM course certifications",
    ],
    # ── Railways ────────────────────────────────────────────────────────
    "loco_pilot": [
        "Class 10 + ITI in Mechanical / Electrical / Electronics (for ALP)",
        "Class 12 / Diploma in Engineering (for Loco Pilot)",
        "RRB ALP Exam — Railway Recruitment Board",
        "Railway Medical fitness standard (vision requirements)",
    ],
    "station_master": [
        "Class 12 or Graduation (depending on level / grade)",
        "RRB Station Master Recruitment Exam",
        "Railway Medical standards must be met",
    ],
    # ── Science & Research ──────────────────────────────────────────────
    "research_scientist": [
        "M.Sc or B.Tech in the relevant field (minimum)",
        "PhD — mandatory for independent research positions",
        "GATE / CSIR-UGC NET / JEST qualifying exam for public institutions",
    ],
    "space_scientist": [
        "B.Tech / M.Tech in Aerospace, Mechanical, Electronics, or M.Sc Physics",
        "ISRO ICRB Exam — Centralised Recruitment for Scientists / Engineers",
        "GATE score often required for entry-level ISRO recruitment",
    ],
    "defence_scientist_drdo": [
        "B.Tech or M.Sc in the relevant discipline",
        "DRDO SET — Scientist Entry Test or GATE",
        "PhD preferred for Scientist D and above grades",
    ],
    # ── Finance (IN) ────────────────────────────────────────────────────
    "chartered_accountant": [
        "Class 12 (any stream) for Foundation route",
        "ICAI CA Foundation → Intermediate → Final exams",
        "3-year Articleship under a practicing CA",
        "Membership with ICAI (awarded after passing Final & completing articleship)",
    ],
    "investment_banker_in": [
        "Bachelor's in Finance / Commerce / Economics / Engineering",
        "MBA (Finance) from top B-school or CFA designation",
        "Internship at investment bank / boutique (highly valued)",
    ],
    "company_secretary": [
        "Class 12 (any stream) for CSEET entry",
        "ICSI CSEET → Executive Programme → Professional Programme",
        "Practical Training (15-21 months under CS / company)",
        "Membership with ICSI (post exams + training)",
    ],
    "stock_broker_in": [
        "Graduation in any discipline",
        "NISM Series VIII — Equity Derivatives Certification (mandatory)",
        "NISM Series X-A — Investment Adviser (for advisory roles)",
        "SEBI registration for acting as a broker / adviser",
    ],
    "bank_clerk_in": [
        "Graduation in any discipline (mandatory)",
        "IBPS Clerk Exam (Prelims + Mains) or SBI Clerk Exam",
        "Local / official language proficiency test",
    ],
    "insurance_advisor_in": [
        "Class 10 / 12 pass (minimum)",
        "IRDAI Agent Training — 50-hour pre-licensing training",
        "IC-38 IRDAI Licensing Exam (mandatory to sell insurance)",
    ],
    "actuary_in": [
        "Class 12 with strong Mathematics / Statistics",
        "IAI ACET — Actuarial Common Entrance Test",
        "Series of IAI actuarial exams (CT / CA series — 15 exams total for Fellow)",
    ],
    "financial_advisor_in": [
        "Graduation in any discipline",
        "NISM Series X-A (Investment Adviser Module) or CFP certification",
        "SEBI RIA (Registered Investment Adviser) registration for independent practice",
    ],
    # ── Finance (US) ────────────────────────────────────────────────────
    "us_investment_banker": [
        "Bachelor's in Finance, Economics, or Business (target school preferred)",
        "MBA from top business school (for career switchers / promotion to VP+)",
        "FINRA Series 7 & Series 63 licenses (obtained on the job)",
    ],
    "us_actuary": [
        "Bachelor's in Actuarial Science, Mathematics, or Statistics",
        "SOA or CAS actuarial exams (Associate designation, then Fellow)",
        "VEE credits in Economics, Accounting, and Mathematical Statistics",
    ],
    "us_financial_advisor": [
        "Bachelor's degree (Finance or Business preferred)",
        "FINRA Series 7 & Series 66 licenses (mandatory)",
        "CFP — Certified Financial Planner designation (strongly preferred)",
    ],
    "us_loan_officer": [
        "High school diploma (minimum); Bachelor's preferred by employers",
        "NMLS — Mortgage Loan Originator License (state-specific, mandatory)",
        "SAFE Act compliance and continuing education requirements",
    ],
    "us_underwriter": [
        "Bachelor's in Finance, Business, or Mathematics",
        "CPCU — Chartered Property Casualty Underwriter (preferred)",
        "AU — Associate in Underwriting designation",
    ],
    "us_auditor": [
        "Bachelor's in Accounting (150 credit hours required for CPA in most states)",
        "CPA — Certified Public Accountant (state board exam, mandatory for signing audits)",
        "CIA — Certified Internal Auditor (for internal audit / compliance roles)",
    ],
    "us_personal_banker": [
        "High school diploma / GED (minimum)",
        "Associate's or Bachelor's degree (preferred by major banks)",
        "On-the-job bank training and product certification provided by employer",
    ],
    # ── US Other ────────────────────────────────────────────────────────
    "us_software_engineer": [
        "Bachelor's in CS, Software Engineering, or related (preferred)",
        "Coding bootcamp + strong portfolio widely accepted",
        "AWS / GCP / Azure certifications (optional but valued)",
    ],
    "us_data_scientist": [
        "Bachelor's in Statistics, CS, or Math (minimum)",
        "Master's or PhD preferred for research / senior roles",
        "Kaggle / Google / Coursera Data Science certificates (supplementary)",
    ],
    "us_registered_nurse": [
        "ADN — Associate Degree in Nursing (2 years) or BSN — Bachelor of Science in Nursing (4 years)",
        "NCLEX-RN — National Council Licensure Examination (mandatory)",
        "State RN License (mandatory to practice)",
        "BSN increasingly required by hospitals and Magnet facilities",
    ],
    "us_electrician": [
        "High school diploma + 4-5 year Apprenticeship (IBEW or NECA-affiliated)",
        "Journeyman Electrician License (state-specific, mandatory)",
        "Master Electrician License (required to own a contracting business)",
    ],
    "us_accountant_cpa": [
        "Bachelor's in Accounting (150 credit hours required for CPA in most states)",
        "CPA — Certified Public Accountant (Uniform CPA Exam, AICPA)",
        "CMA — Certified Management Accountant (optional, for industry roles)",
    ],
    "us_financial_analyst": [
        "Bachelor's in Finance, Economics, or Business",
        "CFA — Chartered Financial Analyst Level I–III (CFA Institute)",
        "FINRA Series 7 / 66 licenses for sell-side roles",
    ],
    "us_truck_driver": [
        "High school diploma / GED",
        "CDL — Commercial Driver's License Class A (mandatory for long-haul)",
        "DOT medical certificate (mandatory, renewed every 2 years)",
        "HAZMAT endorsement for hazardous materials transport",
    ],
    "us_hvac_technician": [
        "High school diploma + 6-month to 2-year HVAC certificate or Associate's degree",
        "EPA Section 608 Certification (legally mandatory for refrigerant handling)",
        "NATE — North American Technician Excellence certification (employer-preferred)",
    ],
    "us_mechanical_engineer": [
        "Bachelor's in Mechanical Engineering (ABET-accredited program)",
        "FE Exam — Fundamentals of Engineering (entry to PE licensure path)",
        "PE — Professional Engineer License (required to stamp designs for public projects)",
    ],
    "us_teacher": [
        "Bachelor's in Education or subject specialization",
        "State Teaching License / Credential (mandatory, varies by state)",
        "Praxis I & II exams (required in most states)",
        "Master's degree (required for tenure / higher salary in many districts)",
    ],
    "us_marketing_manager": [
        "Bachelor's in Marketing, Business, or Communications",
        "MBA preferred for Director / VP level roles",
        "Google Analytics, HubSpot, or Meta Blueprint certifications",
    ],
    "us_police_officer": [
        "High school diploma / GED (minimum); many departments prefer Associate's or Bachelor's",
        "POST — Police Officer Standards and Training academy (mandatory)",
        "Physical fitness test, background check, and polygraph",
        "Psychological evaluation",
    ],
    "us_pharmacist": [
        "PharmD — Doctor of Pharmacy (4-year accredited graduate program)",
        "NAPLEX — North American Pharmacist Licensure Examination (mandatory)",
        "MPJE — Multistate Pharmacy Jurisprudence Examination",
        "State Pharmacy License (mandatory to practice)",
    ],
    "us_physical_therapist": [
        "DPT — Doctor of Physical Therapy (3-year accredited graduate program)",
        "NPTE — National Physical Therapy Examination (mandatory)",
        "State Physical Therapy License (mandatory to practice)",
    ],
    "us_air_traffic_controller": [
        "Bachelor's degree or completion of FAA-approved AT-CTI program",
        "US citizenship (mandatory)",
        "FAA Academy training in Oklahoma City (mandatory, ~5 months)",
        "FAA Air Traffic Controller Certificate (CPC designation)",
    ],
    "us_commercial_pilot": [
        "High school diploma / GED (minimum)",
        "FAA Commercial Pilot Certificate (CPL)",
        "Instrument Rating + Multi-Engine Rating",
        "ATP — Airline Transport Pilot Certificate (required for airline First Officer)",
        "FAA Class 1 Medical Certificate",
    ],
    "us_dental_hygienist": [
        "Associate's in Dental Hygiene (2 years) or Bachelor's",
        "NBDHE — National Board Dental Hygiene Examination (mandatory)",
        "State Dental Hygiene License (mandatory to practice)",
    ],
    "us_welder": [
        "High school diploma + vocational / trade school (6 months – 2 years)",
        "AWS CW — Certified Welder (American Welding Society)",
        "API / ASME certifications for pipeline and pressure vessel work",
    ],
    "us_ux_designer": [
        "Bachelor's in Design, HCI, or related (preferred)",
        "Google UX Design Certificate (Coursera — widely accepted)",
        "Portfolio of UX case studies (often more important than degree)",
    ],
    "us_construction_manager": [
        "Bachelor's in Construction Management, Civil Engineering, or Architecture",
        "CCM — Certified Construction Manager (CMAA)",
        "OSHA 30-hour Construction Safety Certification (strongly preferred)",
    ],
}


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))
    updated = 0
    missing = []
    for c in careers:
        cid = c["id"]
        if cid in QUALS:
            c["qualifications"] = QUALS[cid]
            updated += 1
        else:
            missing.append(cid)

    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Updated {updated} careers with qualifications.")
    if missing:
        print(f"WARNING — {len(missing)} careers missing qualifications data:")
        for m in missing:
            print(f"  - {m}")


if __name__ == "__main__":
    main()
