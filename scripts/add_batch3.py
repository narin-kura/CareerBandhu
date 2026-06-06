"""Add batch 3: Supply Chain & Logistics, Cottage Industries, Education Support, Banking & Lending, Admin & Front Desk"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # SUPPLY CHAIN & LOGISTICS
    # ══════════════════════════════════════════════════════
    {
        "id": "supply_chain_analyst_in",
        "title": "Supply Chain Analyst",
        "category": "Supply Chain & Logistics",
        "region": "IN",
        "description": "Analyse and optimise the flow of goods, information, and money across the supply chain — from raw material sourcing to final delivery. Supply chain analysts work at FMCG, e-commerce, manufacturing, retail, and logistics companies. One of the fastest-growing career areas as India's logistics sector modernises.",
        "salary_range": {"min": 35000, "max": 150000, "currency": "INR/month", "note": "Analyst to Supply Chain Manager; e-commerce pays premium"},
        "growth_outlook": "Very strong — PM Gati Shakti, logistics parks, and e-commerce growth driving demand",
        "work_style": ["Analytical", "Data-driven", "Cross-functional"],
        "required_skills": [
            s("Supply Chain Analytics", "critical"), s("Excel / Power BI / SQL", "important"),
            s("Inventory Management", "critical"), s("ERP (SAP / Oracle)", "important"),
            s("Demand Forecasting", "important"), s("Vendor Management", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Supply Chain, Logistics, Commerce, or Engineering",
            "MBA in Supply Chain / Operations Management",
            "APICS CSCP or CPIM certification",
            "Entry at FMCG companies, e-commerce (Flipkart, Meesho), or 3PL firms",
        ],
        "qualifications": [
            "Bachelor's in Supply Chain / Logistics / Commerce / Engineering",
            "MBA in Supply Chain or Operations Management (IIM, SCMHRD, LSCM preferred)",
            "APICS CSCP — Certified Supply Chain Professional",
            "APICS CPIM — Certified in Production and Inventory Management",
        ],
        "tags": ["supply-chain", "logistics", "analytics", "operations", "ecommerce"],
    },
    {
        "id": "logistics_manager_in",
        "title": "Logistics & Distribution Manager",
        "category": "Supply Chain & Logistics",
        "region": "IN",
        "description": "Manage the transportation, warehousing, and distribution of goods — ensuring timely and cost-efficient delivery. Logistics managers work at 3PL companies (DHL, Mahindra Logistics), FMCG brands, e-commerce players, and manufacturing firms. India's logistics sector is growing rapidly with government infrastructure investments.",
        "salary_range": {"min": 50000, "max": 250000, "currency": "INR/month", "note": "Logistics exec to Supply Chain Director"},
        "growth_outlook": "Very strong — India logistics sector growing 10%+ annually; PM Gati Shakti",
        "work_style": ["Operational", "Fast-paced", "Multi-location"],
        "required_skills": [
            s("Fleet & Warehouse Management", "critical"), s("Route Optimisation", "important"),
            s("Vendor & Carrier Management", "critical"), s("ERP / WMS systems", "important"),
            s("Cost Management", "important"), s("Team Leadership", "critical"),
        ],
        "entry_paths": [
            "Bachelor's in Logistics, Supply Chain, Commerce, or Engineering",
            "MBA Operations or PG Diploma in Logistics & Supply Chain",
            "Start as logistics coordinator / dispatch executive in 3PL or FMCG",
            "Progress: Coordinator → Executive → Asst Manager → Logistics Manager",
        ],
        "qualifications": [
            "Bachelor's in Logistics / Supply Chain / Commerce / Engineering",
            "MBA Operations or PG Diploma in Logistics (IIMM, NIFM, SCMHRD)",
            "IIMM — Indian Institute of Materials Management certifications",
            "Certified Logistics Professional (CLP) from IIMM",
        ],
        "tags": ["logistics", "distribution", "warehouse", "3pl", "supply-chain"],
    },
    {
        "id": "freight_forwarder_in",
        "title": "Freight Forwarder / Customs Broker",
        "category": "Supply Chain & Logistics",
        "region": "IN",
        "description": "Arrange the shipment of goods internationally — handling documentation, customs clearance, freight booking, and compliance on behalf of importers and exporters. Freight forwarders are the lubricant of global trade. Strong demand from India's growing import-export sector.",
        "salary_range": {"min": 25000, "max": 150000, "currency": "INR/month", "note": "Operations exec to senior freight broker or own freight agency"},
        "growth_outlook": "Strong — India's trade volume growing; freight forwarding is essential infrastructure",
        "work_style": ["Detail-oriented", "Client-facing", "Deadline-driven"],
        "required_skills": [
            s("Import-Export Documentation", "critical"), s("Customs Procedures (DGFT, ICEGATE)", "critical"),
            s("Incoterms Knowledge", "important"), s("Freight Negotiation", "important"),
            s("Communication", "critical"), s("Logistics Software", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Commerce, International Business, or Logistics",
            "CHA (Customs House Agent) licence from CBIC (mandatory for customs clearance)",
            "Join freight forwarding companies (DHL, Kuehne+Nagel, DB Schenker, local players)",
            "IATA Cargo Agent certification for air freight",
        ],
        "qualifications": [
            "Bachelor's in Commerce / International Business / Logistics",
            "CHA — Customs House Agent Licence (CBIC, mandatory for customs clearance work)",
            "IATA Cargo Agent certification (for air freight operations)",
            "FIATA Diploma in Freight Management (international credential)",
        ],
        "tags": ["freight", "customs", "logistics", "import-export", "shipping"],
    },
    {
        "id": "us_supply_chain_manager",
        "title": "Supply Chain Manager",
        "category": "Supply Chain & Logistics",
        "region": "US",
        "description": "Lead end-to-end supply chain operations — procurement, inventory, warehousing, and distribution — for manufacturing, retail, e-commerce, or technology companies. One of the most in-demand management roles in the US as companies invest in supply chain resilience post-COVID.",
        "salary_range": {"min": 80000, "max": 140000, "currency": "USD/year", "note": "Supply chain analyst to director; FAANG and Fortune 500 pay premium"},
        "growth_outlook": "Very strong — BLS projects 28% growth for logisticians; supply chain resilience top priority",
        "work_style": ["Analytical", "Cross-functional", "Leadership"],
        "required_skills": [
            s("Supply Chain Strategy", "critical"), s("ERP (SAP / Oracle)", "important"),
            s("Data Analysis", "important"), s("Supplier Management", "critical"),
            s("Demand Planning", "important"), s("Team Leadership", "critical"),
        ],
        "entry_paths": [
            "BS in Supply Chain Management, Industrial Engineering, or Business",
            "MBA with Supply Chain concentration for senior roles",
            "APICS CSCP or CPIM certification",
            "Entry: Supply Chain Analyst at large retailer, manufacturer, or tech company",
        ],
        "qualifications": [
            "BS in Supply Chain, Operations, Industrial Engineering, or Business",
            "MBA with Supply Chain specialisation (Michigan Ross, Michigan State, ASU preferred)",
            "APICS CSCP — Certified Supply Chain Professional",
            "Six Sigma Green/Black Belt for process improvement roles",
        ],
        "tags": ["supply-chain", "logistics", "operations", "procurement", "management"],
    },

    # ══════════════════════════════════════════════════════
    # COTTAGE & SMALL-SCALE MANUFACTURING
    # ══════════════════════════════════════════════════════
    {
        "id": "soap_cosmetics_manufacturer",
        "title": "Soap & Cosmetics Manufacturer (Cottage Industry)",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Produce handmade soaps, shampoos, skincare, and personal care products from home or a small unit. One of India's most accessible cottage industry businesses — startup costs are low (₹50,000–₹3,00,000), demand is strong (natural/organic trend), and products can be sold online, through salons, or via wholesale. Government MSME and Khadi schemes provide training and grants.",
        "salary_range": {"min": 15000, "max": 300000, "currency": "INR/month", "note": "Scales with brand building and distribution reach"},
        "growth_outlook": "Very strong — natural and organic personal care booming; D2C brands thriving",
        "work_style": ["Self-employed", "Creative", "Home/small-unit based"],
        "required_skills": [
            s("Formulation & Chemistry basics", "critical"), s("Quality Control", "critical"),
            s("Packaging & Labelling", "important"), s("Digital Marketing", "important"),
            s("Business basics", "important"), s("Creativity", "helpful"),
        ],
        "entry_paths": [
            "Learn soap/cosmetics formulation through courses (CIMAP, NIFTEM, CIPET, online)",
            "Obtain CDSCO Cosmetics Manufacturing Licence (mandatory for selling cosmetics)",
            "MSME/Udyam registration + GST (for scale)",
            "Sell via Amazon, Meesho, local pharmacies, salons, and own D2C website",
        ],
        "qualifications": [
            "No formal degree required",
            "CDSCO Cosmetics Manufacturing Licence (mandatory under Drugs & Cosmetics Act)",
            "Soap/cosmetics formulation training (CIMAP Lucknow, NIFTEM, CIPET, state institutes)",
            "BIS certification for specific categories (optional but boosts credibility)",
            "MSME / Udyam Registration + FSSAI if any food-grade ingredients used",
        ],
        "tags": ["soap", "cosmetics", "cottage-industry", "msme", "d2c"],
    },
    {
        "id": "garment_manufacturer_in",
        "title": "Garment / Apparel Manufacturer (MSME)",
        "category": "Entrepreneurship & MSME",
        "region": "IN",
        "description": "Set up a small garment manufacturing unit producing readymade clothes, uniforms, traditional wear, or fashion items. India is the world's 2nd largest textiles exporter and the garment sector employs millions. Small units can start with 5-10 sewing machines (₹2L-₹10L investment) and grow through job work for larger brands or direct retail/export.",
        "salary_range": {"min": 30000, "max": 500000, "currency": "INR/month", "note": "Profit after costs; scales with order volume and brand positioning"},
        "growth_outlook": "Strong — India's textile PLI scheme and China+1 strategy boosting garment orders",
        "work_style": ["Self-employed", "Operations-heavy", "Labour management"],
        "required_skills": [
            s("Garment Construction & Sewing", "critical"), s("Quality Control", "critical"),
            s("Pattern Making basics", "important"), s("Operations Management", "important"),
            s("Vendor & Labour Management", "important"), s("Costing", "helpful"),
        ],
        "entry_paths": [
            "NIFT / ITI / state textile board garment manufacturing courses",
            "Start as job-work unit for established brands or exporters",
            "Udyam (MSME) registration + GST + Factory Licence (if >10 workers with power)",
            "Apply for TUFS (Technology Upgradation Fund Scheme) for machinery subsidies",
        ],
        "qualifications": [
            "ITI in Sewing Technology or Garment making (1 year)",
            "Diploma in Garment Manufacturing (NIFT, state textile institutes)",
            "Factory Licence under Factories Act (if employing 10+ workers with power)",
            "Udyam / MSME Registration for government scheme access",
        ],
        "tags": ["garment", "apparel", "textile", "msme", "manufacturing"],
    },
    {
        "id": "plant_nursery_owner",
        "title": "Plant Nursery Owner / Horticulturist",
        "category": "Agriculture & Farming",
        "region": "IN",
        "description": "Grow and sell plants, saplings, seeds, and gardening products through a nursery — supplying home gardeners, landscape contractors, municipal authorities, and urban farming enthusiasts. India's urban gardening boom, government green initiatives, and landscape industry growth make plant nurseries a strong small business opportunity. Investment: ₹1L – ₹10L.",
        "salary_range": {"min": 20000, "max": 300000, "currency": "INR/month", "note": "Seasonal variability; scale through landscape contracts and online sales"},
        "growth_outlook": "Strong — urban gardening trend + government afforestation contracts growing",
        "work_style": ["Outdoor", "Self-employed", "Physically active"],
        "required_skills": [
            s("Horticulture & Plant Knowledge", "critical"), s("Plant Propagation", "critical"),
            s("Pest & Disease Management", "important"), s("Business basics", "important"),
            s("Customer Service", "important"), s("Soil & Irrigation knowledge", "helpful"),
        ],
        "entry_paths": [
            "B.Sc or Diploma in Horticulture or Agriculture",
            "State Agriculture Department nursery training programs (often free)",
            "National Horticulture Mission (NHM) schemes provide subsidies for nursery setup",
            "Start with a small plot; supply local landscapers, housing societies, and municipal tenders",
        ],
        "qualifications": [
            "B.Sc in Horticulture or Agriculture (SAU — State Agricultural Universities)",
            "Diploma in Horticulture (state agriculture polytechnics — 2 years)",
            "National Horticulture Mission (NHM) registration for subsidy access",
            "State nursery registration / licence (varies by state)",
        ],
        "tags": ["nursery", "horticulture", "plants", "agriculture", "entrepreneurship"],
    },
    {
        "id": "us_nursery_horticulturist",
        "title": "Nursery Worker / Horticulturist",
        "category": "Agriculture & Farming",
        "region": "US",
        "description": "Grow, cultivate, and sell plants, shrubs, trees, and seedlings in retail nurseries, wholesale growing operations, or botanical gardens. The US nursery and floriculture industry generates $20B+ annually. Roles range from nursery worker and grower to horticulture manager and landscape designer.",
        "salary_range": {"min": 35000, "max": 80000, "currency": "USD/year", "note": "Nursery worker to head grower or nursery owner"},
        "growth_outlook": "Stable — home gardening boomed post-COVID; landscape industry growing steadily",
        "work_style": ["Outdoor", "Physically active", "Seasonal variation"],
        "required_skills": [
            s("Plant Knowledge & Identification", "critical"), s("Plant Propagation", "critical"),
            s("Pest & Disease Management", "important"), s("Irrigation Systems", "helpful"),
            s("Customer Service (retail)", "helpful"), s("Physical Fitness", "important"),
        ],
        "entry_paths": [
            "AAS or BS in Horticulture from community college or university",
            "On-the-job training at retail nurseries (Home Depot Garden Center, local nurseries)",
            "Pursue Certified Professional Horticulturist (CPH) credential from ANLA",
            "Advance to head grower, nursery manager, or own business",
        ],
        "qualifications": [
            "AAS or BS in Horticulture / Plant Science",
            "CPH — Certified Professional Horticulturist (ANLA — American Nursery & Landscape Association)",
            "State Pesticide Applicator Licence (for chemical pest management)",
            "Certified Nursery Professional (CNP) for retail roles",
        ],
        "tags": ["nursery", "horticulture", "plants", "landscape", "agriculture"],
    },

    # ══════════════════════════════════════════════════════
    # BANKING & LENDING
    # ══════════════════════════════════════════════════════
    {
        "id": "loan_officer_in",
        "title": "Loan Officer / Credit Manager",
        "category": "Finance",
        "region": "IN",
        "description": "Evaluate, process, and approve loan applications for individuals and businesses — including home loans, business loans, personal loans, vehicle loans, and agricultural credit. Loan officers work in banks (PSU and private), NBFCs, microfinance institutions, and HFCs (Housing Finance Companies). A stable, growing career as India's credit penetration expands.",
        "salary_range": {"min": 25000, "max": 150000, "currency": "INR/month", "note": "Branch loan officer to Credit Head; NBFCs and private banks pay more"},
        "growth_outlook": "Strong — India's formalisation of credit and financial inclusion driving loan officer demand",
        "work_style": ["Client-facing", "Analytical", "Field & office"],
        "required_skills": [
            s("Credit Analysis", "critical"), s("Financial Statement Analysis", "critical"),
            s("Communication", "critical"), s("Risk Assessment", "important"),
            s("KYC & Compliance", "important"), s("Loan Documentation", "important"),
            s("MS Excel", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in Commerce, Finance, Economics, or Banking",
            "JAIIB / CAIIB from IIBF (Indian Institute of Banking and Finance) for banking roles",
            "Enter as Probationary Officer (PO) via IBPS exam (PSU banks) or bank-specific exams",
            "Join NBFCs, HFCs, or MFIs directly (often hire commerce graduates)",
        ],
        "qualifications": [
            "Bachelor's in Commerce / Finance / Economics",
            "JAIIB — Junior Associate of Indian Institute of Bankers (IIBF)",
            "CAIIB — Certified Associate of Indian Institute of Bankers (for senior roles)",
            "IBPS PO / SBI PO exam for public sector bank officer positions",
            "MBA Finance for commercial banking and credit management roles",
        ],
        "tags": ["loan", "banking", "credit", "finance", "nbfc"],
    },
    {
        "id": "us_loan_officer",
        "title": "Loan Officer",
        "category": "Finance",
        "region": "US",
        "description": "Help individuals and businesses secure loans — including mortgages, auto loans, personal loans, and SBA business loans. Loan officers work at banks, credit unions, and mortgage companies. Mortgage loan officers are among the highest-earning professionals in financial services, with strong commission potential.",
        "salary_range": {"min": 55000, "max": 150000, "currency": "USD/year", "note": "Salary or commission-based; top mortgage LOs earn $200k+"},
        "growth_outlook": "Stable — mortgage volume tied to housing market; consumer lending steady",
        "work_style": ["Client-facing", "Sales-oriented", "Deadline-driven"],
        "required_skills": [
            s("Credit Analysis", "critical"), s("Mortgage / Loan Knowledge", "critical"),
            s("Sales", "important"), s("Communication", "critical"),
            s("Regulatory Compliance (RESPA, TILA, HMDA)", "important"),
            s("Loan Origination Software (Encompass, Calyx)", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Finance, Business, or Economics (preferred, not mandatory)",
            "NMLS — Nationwide Multistate Licensing System registration (mandatory for mortgage LOs)",
            "SAFE Act — 20-hour pre-licensing education + state exam for mortgage",
            "Start as loan processor or junior LO; progress to senior LO or branch manager",
        ],
        "qualifications": [
            "Bachelor's in Finance / Business / Economics (preferred)",
            "NMLS Registration — Nationwide Multistate Licensing System (mandatory for mortgage LOs)",
            "SAFE Act Pre-Licensing Education (20 hours) + state mortgage exam",
            "Series 6 or Series 7 (FINRA) for investment product cross-selling",
        ],
        "tags": ["loan-officer", "mortgage", "banking", "finance", "credit"],
    },

    # ══════════════════════════════════════════════════════
    # EDUCATION SUPPORT
    # ══════════════════════════════════════════════════════
    {
        "id": "teaching_assistant_in",
        "title": "Teaching Assistant / Academic Support",
        "category": "Education & Training",
        "region": "IN",
        "description": "Support classroom teachers and professors by assisting with instruction, student assessment, lab sessions, tutoring, and administrative tasks. Teaching assistants work in schools, colleges, universities, special education centres, and coaching institutes. Also a key stepping stone to a full teaching or academic career.",
        "salary_range": {"min": 12000, "max": 60000, "currency": "INR/month", "note": "School TA to university research/teaching assistant (UGC stipend)"},
        "growth_outlook": "Stable — education sector expanding; inclusive education creating more support roles",
        "work_style": ["Student-facing", "Supportive", "Structured"],
        "required_skills": [
            s("Subject Knowledge", "critical"), s("Communication", "critical"),
            s("Patience", "critical"), s("Classroom Management", "important"),
            s("Assessment & Feedback", "important"), s("Documentation", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's degree in any subject (same subject as teaching area preferred)",
            "B.Ed for school teaching assistant roles (in states where required)",
            "UGC-NET / JRF for university Teaching Assistant / Research Fellow positions",
            "Apply at coaching institutes, special schools, international schools, or universities",
        ],
        "qualifications": [
            "Bachelor's degree (any relevant discipline)",
            "B.Ed (for school assistant teacher positions in government schools)",
            "UGC-NET / JRF (for university teaching assistantship / research fellowship)",
            "CTET / State TET for government school eligibility",
        ],
        "tags": ["teaching", "education", "assistant", "school", "university"],
    },
    {
        "id": "us_teaching_assistant",
        "title": "Teaching Assistant / Paraprofessional",
        "category": "Education & Training",
        "region": "US",
        "description": "Support classroom teachers in K-12 schools or higher education — helping students with instruction, assessments, special needs support, and classroom management. Paraprofessionals (paras) in special education are a particularly large and growing employment category. Also the primary path for graduate students in universities.",
        "salary_range": {"min": 28000, "max": 55000, "currency": "USD/year", "note": "K-12 para to graduate teaching assistant (with tuition waiver)"},
        "growth_outlook": "Stable — special education paras in strong demand; graduate TAs tied to university enrollment",
        "work_style": ["Student-facing", "Supportive", "Structured"],
        "required_skills": [
            s("Subject Knowledge", "important"), s("Communication", "critical"),
            s("Patience & Empathy", "critical"), s("Classroom Management", "important"),
            s("Differentiated Instruction", "helpful"), s("Behaviour Management", "helpful"),
        ],
        "entry_paths": [
            "Associate's degree or 60+ college credit hours (NCLB HQP requirement for Title I schools)",
            "State paraprofessional certification or ParaPro Assessment",
            "Bachelor's + enroll in graduate school for university TA position",
            "Apply at public school districts, charter schools, or universities",
        ],
        "qualifications": [
            "Associate's degree or 60 college credit hours (NCLB-compliant districts)",
            "ParaPro Assessment (ETS) — many districts require this",
            "State paraprofessional certification (varies by state)",
            "Special Education paraprofessional training (autism, ABA basics, behaviour management)",
        ],
        "tags": ["teaching-assistant", "para", "education", "school", "special-education"],
    },

    # ══════════════════════════════════════════════════════
    # ADMIN & FRONT DESK
    # ══════════════════════════════════════════════════════
    {
        "id": "front_desk_receptionist_in",
        "title": "Front Desk Executive / Receptionist",
        "category": "Business & Management",
        "region": "IN",
        "description": "Serve as the first point of contact for visitors, clients, and callers at hospitals, hotels, corporate offices, clinics, coworking spaces, and government offices. Front desk roles combine communication, coordination, and administrative skills. A strong entry-level career with clear pathways into administration, hospitality, and office management.",
        "salary_range": {"min": 15000, "max": 50000, "currency": "INR/month", "note": "Entry-level; hospitality and corporate offices pay higher"},
        "growth_outlook": "Stable — required in virtually every organisation; hospitality sector growing",
        "work_style": ["Customer-facing", "Structured", "On-site"],
        "required_skills": [
            s("Communication", "critical"), s("Customer Service", "critical"),
            s("Computer Skills (MS Office)", "important"), s("Multitasking", "important"),
            s("Telephone Etiquette", "critical"), s("Professional Appearance", "important"),
            s("Data Entry", "helpful"),
        ],
        "entry_paths": [
            "12th pass or any Bachelor's degree",
            "Diploma in Office Management, Hospitality, or Computer Applications",
            "Apply at hospitals, hotels, corporate offices, clinics, and coworking spaces",
            "Progress to Office Administrator, Executive Assistant, or Hotel Front Office Manager",
        ],
        "qualifications": [
            "12th pass minimum (Bachelor's degree preferred for corporate roles)",
            "Diploma in Office Management / Hospitality / BCA / BA",
            "MS Office proficiency (Word, Excel, Outlook)",
            "Hotel Management course (IHM) for hospitality front desk roles",
        ],
        "tags": ["front-desk", "receptionist", "admin", "customer-service", "hospitality"],
    },
    {
        "id": "office_administrator_in",
        "title": "Office Administrator / Administrative Executive",
        "category": "Business & Management",
        "region": "IN",
        "description": "Keep offices running smoothly — managing schedules, correspondence, facilities, vendor coordination, travel arrangements, and records. Office administrators are essential in every organisation from startups and NGOs to large corporations and government departments. A versatile career with strong job security.",
        "salary_range": {"min": 20000, "max": 80000, "currency": "INR/month", "note": "Admin Executive to Office Manager / Executive Assistant to Director"},
        "growth_outlook": "Stable — every organisation needs administrative professionals",
        "work_style": ["Organised", "On-site", "Multi-role"],
        "required_skills": [
            s("MS Office (Word, Excel, Outlook, PowerPoint)", "critical"),
            s("Communication", "critical"), s("Organisation & Planning", "critical"),
            s("Multitasking", "critical"), s("Record Management", "important"),
            s("Vendor Coordination", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's in any discipline (Commerce, BCA, BA)",
            "Diploma in Office Administration, Secretarial Practice, or Computer Applications",
            "Entry as admin executive / office assistant; grow to senior admin roles",
            "Specialize: Executive Assistant, HR Admin, or Facilities Manager",
        ],
        "qualifications": [
            "Bachelor's degree (any discipline; Commerce or BCA preferred)",
            "Diploma in Secretarial Practice / Office Administration",
            "MS Office / Tally certification",
            "Company Secretary (CS Foundation) for corporate secretarial specialisation",
        ],
        "tags": ["admin", "office-management", "executive-assistant", "administration", "operations"],
    },
    {
        "id": "us_receptionist_admin",
        "title": "Receptionist / Administrative Assistant",
        "category": "Business & Management",
        "region": "US",
        "description": "Manage front desk operations, phone lines, scheduling, and administrative tasks at offices, medical practices, law firms, hotels, and clinics. One of the largest employment categories in the US, offering entry to many industries. Medical receptionists and legal administrative assistants earn premium rates.",
        "salary_range": {"min": 32000, "max": 55000, "currency": "USD/year", "note": "Medical and legal admin assistants earn higher; executive assistants earn 60k+"},
        "growth_outlook": "Stable — steady demand across industries; automation affecting some routine tasks",
        "work_style": ["Customer-facing", "Organised", "On-site"],
        "required_skills": [
            s("Communication", "critical"), s("MS Office / Google Workspace", "critical"),
            s("Customer Service", "critical"), s("Scheduling (Calendly, Outlook)", "important"),
            s("Multitasking", "important"), s("Confidentiality", "important"),
        ],
        "entry_paths": [
            "High school diploma or associate's degree",
            "Microsoft Office Specialist (MOS) certification strengthens resume",
            "Apply at medical offices, law firms, corporate HQs, or hotels",
            "Advance to Executive Assistant, Office Manager, or HR Admin",
        ],
        "qualifications": [
            "High school diploma or GED (minimum)",
            "Associate's degree in Business Administration or Office Technology (preferred)",
            "Microsoft Office Specialist (MOS) certification",
            "Medical Administrative Assistant certification (NCCT or AAMA) for healthcare front desk",
        ],
        "tags": ["receptionist", "admin", "front-desk", "office", "customer-service"],
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
