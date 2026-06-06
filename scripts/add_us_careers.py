"""Tag existing careers as region IN and add US-based careers (USD, US paths).

Keeps the file UTF-8 clean. Skill names are kept consistent with the Indian
careers so the skill-matching engine works across both regions.
"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


US = [
    {
        "id": "us_software_engineer",
        "title": "Software Engineer",
        "category": "Technology",
        "description": "Design, build, and maintain software applications and systems. One of the highest-demand, best-paid careers in the US, with strong remote-work options. Big Tech, startups, and every industry hire engineers.",
        "salary_range": {"min": 90000, "max": 220000, "currency": "USD/year", "note": "Junior to Senior/Staff Engineer"},
        "growth_outlook": "Strong",
        "work_style": ["Remote-friendly", "Project-based", "Collaborative"],
        "required_skills": [s("Programming", "critical"), s("Python", "important"), s("Problem Solving", "critical"),
                            s("Data Structures & Algorithms", "critical"), s("Git & Version Control", "important"),
                            s("Communication", "important"), s("System Design", "helpful")],
        "entry_paths": ["Bachelor's in Computer Science (or related)", "Coding bootcamp (3-6 months)",
                        "Self-taught + strong project portfolio", "Internships at tech companies"],
        "tags": ["tech", "software", "high-pay", "remote"],
    },
    {
        "id": "us_data_scientist",
        "title": "Data Scientist",
        "category": "Data & Analytics",
        "description": "Turn data into insights and predictive models that drive business decisions. A top-paying, fast-growing US role across tech, finance, healthcare, and retail.",
        "salary_range": {"min": 95000, "max": 200000, "currency": "USD/year", "note": "Analyst to Senior Data Scientist"},
        "growth_outlook": "Strong",
        "work_style": ["Remote-friendly", "Analytical", "Cross-functional"],
        "required_skills": [s("Python", "critical"), s("Statistics", "critical"), s("Machine Learning", "critical"),
                            s("SQL", "important"), s("Data Visualization", "important"), s("Communication", "important"),
                            s("Mathematics", "important")],
        "entry_paths": ["Bachelor's/Master's in Stats, CS, or Math", "Data science bootcamp",
                        "Online certifications (Coursera, DataCamp)", "Portfolio of analysis projects"],
        "tags": ["data", "analytics", "AI", "high-pay"],
    },
    {
        "id": "us_registered_nurse",
        "title": "Registered Nurse (RN)",
        "category": "Healthcare",
        "description": "Provide and coordinate patient care in hospitals, clinics, and homes. A stable, well-paid, in-demand career across the US with severe nationwide shortages and strong job security.",
        "salary_range": {"min": 65000, "max": 130000, "currency": "USD/year", "note": "Staff RN to Specialized/Travel RN"},
        "growth_outlook": "Very Strong",
        "work_style": ["Shift work", "Patient-facing", "Hands-on"],
        "required_skills": [s("Patient Care", "critical"), s("Clinical Skills", "critical"), s("Communication", "critical"),
                            s("Empathy", "important"), s("Attention to Detail", "critical"), s("First Aid", "important"),
                            s("Calm Under Pressure", "important")],
        "entry_paths": ["ADN (2-yr) or BSN (4-yr) degree", "Pass the NCLEX-RN exam",
                        "State nursing license", "Community college nursing programs"],
        "tags": ["healthcare", "nursing", "in-demand", "stable"],
    },
    {
        "id": "us_electrician",
        "title": "Electrician",
        "category": "Trades & Construction",
        "description": "Install, maintain, and repair electrical systems in homes, businesses, and industry. A high-paying skilled trade in the US that you can enter through paid apprenticeship — no college debt required.",
        "salary_range": {"min": 50000, "max": 100000, "currency": "USD/year", "note": "Apprentice to Master Electrician"},
        "growth_outlook": "Strong",
        "work_style": ["Hands-on", "On-site", "Physical"],
        "required_skills": [s("Electrical Wiring", "critical"), s("Blueprint Reading", "important"),
                            s("Problem Solving", "important"), s("Mechanical Aptitude", "important"),
                            s("Safety Procedures", "critical"), s("Mathematics", "helpful")],
        "entry_paths": ["High school diploma / GED", "Paid apprenticeship (IBEW / NECA, 4-5 yrs)",
                        "Trade / technical school", "State journeyman license exam"],
        "tags": ["trades", "skilled-trade", "apprenticeship", "no-degree"],
    },
    {
        "id": "us_accountant_cpa",
        "title": "Accountant / CPA",
        "category": "Finance",
        "description": "Prepare and analyze financial records, taxes, and audits for businesses and individuals. Becoming a licensed CPA significantly boosts pay and opens senior roles across every industry.",
        "salary_range": {"min": 55000, "max": 130000, "currency": "USD/year", "note": "Staff Accountant to CPA / Controller"},
        "growth_outlook": "Stable",
        "work_style": ["Office/remote", "Detail-oriented", "Seasonal peaks"],
        "required_skills": [s("Accounting", "critical"), s("MS Excel", "critical"), s("Attention to Detail", "critical"),
                            s("Financial Analysis", "important"), s("Tax Knowledge", "important"),
                            s("Communication", "important")],
        "entry_paths": ["Bachelor's in Accounting (150 credit hours for CPA)", "Pass the CPA exam",
                        "Internship at accounting firm", "Entry roles at Big 4 / corporate finance"],
        "tags": ["finance", "accounting", "CPA", "stable"],
    },
    {
        "id": "us_financial_analyst",
        "title": "Financial Analyst",
        "category": "Finance",
        "description": "Evaluate investments, budgets, and financial performance to guide business decisions. A strong-paying corporate career with clear paths into banking, corporate finance, and investment management.",
        "salary_range": {"min": 65000, "max": 150000, "currency": "USD/year", "note": "Analyst to Senior / VP"},
        "growth_outlook": "Strong",
        "work_style": ["Office/remote", "Analytical", "Fast-paced"],
        "required_skills": [s("Financial Analysis", "critical"), s("MS Excel", "critical"), s("Mathematics", "important"),
                            s("Data Analysis", "important"), s("Communication", "important"), s("Accounting", "helpful")],
        "entry_paths": ["Bachelor's in Finance, Economics, or Business", "CFA certification (boosts pay)",
                        "Finance internships", "Entry analyst roles at banks/corporates"],
        "tags": ["finance", "analyst", "corporate", "high-pay"],
    },
    {
        "id": "us_truck_driver",
        "title": "Commercial Truck Driver (CDL)",
        "category": "Transport & Logistics",
        "description": "Transport goods across cities and states. A reliable, well-paying career in the US with constant demand and quick entry — many companies pay for your CDL training.",
        "salary_range": {"min": 50000, "max": 90000, "currency": "USD/year", "note": "Company driver to Owner-Operator"},
        "growth_outlook": "Stable",
        "work_style": ["On-the-road", "Independent", "Long hours"],
        "required_skills": [s("Driving", "critical"), s("Safety Procedures", "critical"), s("Navigation", "important"),
                            s("Vehicle Maintenance", "helpful"), s("Time Management", "important")],
        "entry_paths": ["Age 21+ (interstate), clean record", "CDL training school (3-7 weeks)",
                        "Pass CDL written + driving test", "Company-sponsored CDL programs"],
        "tags": ["logistics", "driving", "no-degree", "in-demand"],
    },
    {
        "id": "us_hvac_technician",
        "title": "HVAC Technician",
        "category": "Trades & Construction",
        "description": "Install and repair heating, ventilation, and air-conditioning systems. A recession-resistant skilled trade with strong pay and steady demand year-round across the US.",
        "salary_range": {"min": 48000, "max": 90000, "currency": "USD/year", "note": "Apprentice to Senior Tech"},
        "growth_outlook": "Strong",
        "work_style": ["Hands-on", "On-site", "Physical"],
        "required_skills": [s("Mechanical Aptitude", "critical"), s("Electrical Wiring", "important"),
                            s("Problem Solving", "important"), s("Safety Procedures", "critical"),
                            s("Customer Service", "helpful")],
        "entry_paths": ["High school diploma / GED", "HVAC trade school / certificate (6-24 months)",
                        "Apprenticeship", "EPA 608 certification + state license"],
        "tags": ["trades", "skilled-trade", "apprenticeship", "in-demand"],
    },
    {
        "id": "us_mechanical_engineer",
        "title": "Mechanical Engineer",
        "category": "Technology",
        "description": "Design and build machines, engines, and mechanical systems across automotive, aerospace, energy, and manufacturing. A versatile, well-paid engineering career.",
        "salary_range": {"min": 70000, "max": 140000, "currency": "USD/year", "note": "Junior to Senior Engineer"},
        "growth_outlook": "Stable",
        "work_style": ["Office + lab/field", "Project-based", "Technical"],
        "required_skills": [s("Mechanical Aptitude", "critical"), s("CAD Software", "important"),
                            s("Mathematics", "critical"), s("Physics", "important"), s("Problem Solving", "critical"),
                            s("Project Management", "helpful")],
        "entry_paths": ["Bachelor's in Mechanical Engineering (ABET-accredited)", "FE / PE licensure",
                        "Engineering internships / co-ops", "Entry roles in manufacturing/aerospace"],
        "tags": ["engineering", "mechanical", "design", "stable"],
    },
    {
        "id": "us_teacher",
        "title": "K-12 Teacher",
        "category": "Education & Training",
        "description": "Educate and mentor students in public or private schools. A meaningful, stable career with summers off, strong benefits, and ongoing nationwide demand — especially in STEM and special education.",
        "salary_range": {"min": 45000, "max": 85000, "currency": "USD/year", "note": "New to Experienced Teacher"},
        "growth_outlook": "Stable",
        "work_style": ["In-person", "Structured schedule", "People-facing"],
        "required_skills": [s("Teaching", "critical"), s("Communication", "critical"), s("Patience", "important"),
                            s("Subject Expertise", "critical"), s("Classroom Management", "important"),
                            s("Empathy", "important")],
        "entry_paths": ["Bachelor's degree + teacher prep program", "State teaching license / certification",
                        "Praxis exams", "Alternative certification (Teach for America)"],
        "tags": ["education", "teaching", "stable", "meaningful"],
    },
    {
        "id": "us_marketing_manager",
        "title": "Marketing Manager",
        "category": "Marketing & Sales",
        "description": "Plan and run campaigns that grow brands and drive sales across digital and traditional channels. A creative, strategic, well-paid role in nearly every US company.",
        "salary_range": {"min": 65000, "max": 160000, "currency": "USD/year", "note": "Specialist to Marketing Director"},
        "growth_outlook": "Strong",
        "work_style": ["Remote-friendly", "Creative", "Data-driven"],
        "required_skills": [s("Marketing Strategy", "critical"), s("Communication", "critical"),
                            s("Social Media", "important"), s("Data Analysis", "important"),
                            s("Content Creation", "important"), s("Leadership", "helpful")],
        "entry_paths": ["Bachelor's in Marketing, Business, or Communications", "Digital marketing certifications",
                        "Start in coordinator/specialist roles", "Build a campaign portfolio"],
        "tags": ["marketing", "digital", "creative", "management"],
    },
    {
        "id": "us_police_officer",
        "title": "Police Officer",
        "category": "Government & Public Service",
        "description": "Protect and serve communities, enforce laws, and respond to emergencies. A stable government career with pension benefits, entered through a paid police academy — no degree required in most departments.",
        "salary_range": {"min": 50000, "max": 100000, "currency": "USD/year", "note": "Officer to Sergeant/Detective"},
        "growth_outlook": "Stable",
        "work_style": ["Shift work", "Field", "High-responsibility"],
        "required_skills": [s("Physical Fitness", "critical"), s("Communication", "critical"), s("Integrity", "critical"),
                            s("Quick Decision Making", "important"), s("Conflict Resolution", "important"),
                            s("First Aid", "helpful")],
        "entry_paths": ["High school diploma / GED (some require college)", "Pass written + physical + background checks",
                        "Police academy training (12-24 weeks)", "Field training program"],
        "tags": ["government", "law-enforcement", "no-degree", "pension"],
    },
    {
        "id": "us_pharmacist",
        "title": "Pharmacist",
        "category": "Healthcare",
        "description": "Dispense medications, advise patients, and ensure safe drug use in pharmacies, hospitals, and clinics. A high-paying, trusted healthcare profession across the US.",
        "salary_range": {"min": 110000, "max": 160000, "currency": "USD/year", "note": "Staff to Clinical/Lead Pharmacist"},
        "growth_outlook": "Stable",
        "work_style": ["Patient-facing", "Detail-oriented", "Shift work"],
        "required_skills": [s("Pharmacology", "critical"), s("Attention to Detail", "critical"),
                            s("Patient Care", "important"), s("Communication", "important"), s("Chemistry", "important"),
                            s("Integrity", "important")],
        "entry_paths": ["Pre-pharmacy coursework", "Doctor of Pharmacy (PharmD, 4 yrs)",
                        "Pass NAPLEX + state law exam", "State pharmacist license"],
        "tags": ["healthcare", "pharmacy", "high-pay", "licensed"],
    },
    {
        "id": "us_physical_therapist",
        "title": "Physical Therapist",
        "category": "Healthcare",
        "description": "Help patients recover movement and manage pain after injury, surgery, or illness. A rewarding, well-paid, in-demand healthcare career as the US population ages.",
        "salary_range": {"min": 80000, "max": 110000, "currency": "USD/year", "note": "New grad to Experienced PT"},
        "growth_outlook": "Very Strong",
        "work_style": ["Hands-on", "Patient-facing", "Active"],
        "required_skills": [s("Anatomy Knowledge", "critical"), s("Patient Care", "critical"),
                            s("Communication", "critical"), s("Empathy", "important"), s("Physical Fitness", "important"),
                            s("Problem Solving", "helpful")],
        "entry_paths": ["Bachelor's (any) + prerequisites", "Doctor of Physical Therapy (DPT, 3 yrs)",
                        "Pass the NPTE", "State PT license"],
        "tags": ["healthcare", "therapy", "in-demand", "rewarding"],
    },
    {
        "id": "us_air_traffic_controller",
        "title": "Air Traffic Controller (FAA)",
        "category": "Aviation & Airport",
        "description": "Direct aircraft safely through US airspace and airports. One of the highest-paid jobs you can get without a 4-year degree, hired and trained directly by the FAA. High pressure, high reward.",
        "salary_range": {"min": 90000, "max": 200000, "currency": "USD/year", "note": "Developmental to Certified Professional Controller"},
        "growth_outlook": "Stable",
        "work_style": ["High-pressure", "Shift work", "Control tower"],
        "required_skills": [s("Situational Awareness", "critical"), s("Quick Decision Making", "critical"),
                            s("Communication", "critical"), s("Concentration & Focus", "critical"),
                            s("English Proficiency", "critical"), s("Stress Management", "important")],
        "entry_paths": ["US citizen, under age 31", "Pass FAA ATSA aptitude test",
                        "FAA Academy training (Oklahoma City)", "Or AT-CTI college program / military ATC"],
        "tags": ["aviation", "FAA", "high-pay", "no-degree"],
    },
    {
        "id": "us_commercial_pilot",
        "title": "Commercial Airline Pilot",
        "category": "Aviation & Airport",
        "description": "Fly passengers and cargo for US airlines. A high-paying career with travel benefits, in strong demand due to a nationwide pilot shortage and waves of retirements.",
        "salary_range": {"min": 90000, "max": 350000, "currency": "USD/year", "note": "Regional First Officer to Major Captain"},
        "growth_outlook": "Very Strong",
        "work_style": ["Travel-heavy", "Roster", "High-responsibility"],
        "required_skills": [s("Aircraft Handling", "critical"), s("Aviation Knowledge", "critical"),
                            s("Quick Decision Making", "critical"), s("Situational Awareness", "critical"),
                            s("Communication", "important"), s("Stress Management", "important")],
        "entry_paths": ["FAA Private Pilot License", "Commercial Pilot License + instrument rating",
                        "Build 1,500 hours (ATP requirement)", "Flight school or university aviation program"],
        "tags": ["aviation", "pilot", "FAA", "high-pay"],
    },
    {
        "id": "us_dental_hygienist",
        "title": "Dental Hygienist",
        "category": "Healthcare",
        "description": "Clean teeth, take x-rays, and educate patients on oral health in dental offices. A high-paying healthcare career with great work-life balance, reachable with a 2-3 year degree.",
        "salary_range": {"min": 70000, "max": 100000, "currency": "USD/year", "note": "New to Experienced Hygienist"},
        "growth_outlook": "Strong",
        "work_style": ["Patient-facing", "Part-time friendly", "Hands-on"],
        "required_skills": [s("Patient Care", "critical"), s("Attention to Detail", "critical"),
                            s("Communication", "important"), s("Manual Dexterity", "important"),
                            s("Empathy", "helpful")],
        "entry_paths": ["Associate degree in Dental Hygiene (accredited)", "Pass National Board Dental Hygiene Exam",
                        "Clinical / state board exam", "State hygienist license"],
        "tags": ["healthcare", "dental", "work-life-balance", "licensed"],
    },
    {
        "id": "us_welder",
        "title": "Welder",
        "category": "Trades & Construction",
        "description": "Join metal parts for construction, manufacturing, pipelines, and shipbuilding. A skilled trade with strong pay — specialized welders (underwater, pipeline) can earn six figures.",
        "salary_range": {"min": 45000, "max": 100000, "currency": "USD/year", "note": "Entry to Specialized Welder"},
        "growth_outlook": "Stable",
        "work_style": ["Hands-on", "On-site", "Physical"],
        "required_skills": [s("Welding Techniques", "critical"), s("Mechanical Aptitude", "important"),
                            s("Blueprint Reading", "important"), s("Safety Procedures", "critical"),
                            s("Attention to Detail", "important")],
        "entry_paths": ["High school diploma / GED", "Welding certificate / trade school (6-18 months)",
                        "AWS certification", "Apprenticeship"],
        "tags": ["trades", "welding", "skilled-trade", "no-degree"],
    },
    {
        "id": "us_ux_designer",
        "title": "UX/UI Designer",
        "category": "Design & Creative",
        "description": "Design intuitive, attractive digital products and experiences. A creative, well-paid, remote-friendly tech career bridging design and user research.",
        "salary_range": {"min": 70000, "max": 150000, "currency": "USD/year", "note": "Junior to Senior Designer"},
        "growth_outlook": "Strong",
        "work_style": ["Remote-friendly", "Creative", "Collaborative"],
        "required_skills": [s("UI Design", "critical"), s("User Research", "important"), s("Figma", "important"),
                            s("Prototyping", "important"), s("Communication", "important"), s("Creativity", "critical")],
        "entry_paths": ["Bachelor's in Design/HCI (or self-taught)", "UX bootcamp", "Build a strong portfolio",
                        "Junior designer / internship roles"],
        "tags": ["design", "UX", "tech", "remote"],
    },
    {
        "id": "us_construction_manager",
        "title": "Construction Manager",
        "category": "Trades & Construction",
        "description": "Plan, budget, and oversee construction projects from start to finish. A high-paying leadership role you can reach through experience in the trades or a construction-management degree.",
        "salary_range": {"min": 75000, "max": 160000, "currency": "USD/year", "note": "Assistant to Senior PM"},
        "growth_outlook": "Strong",
        "work_style": ["On-site + office", "Leadership", "Fast-paced"],
        "required_skills": [s("Project Management", "critical"), s("Leadership", "critical"),
                            s("Blueprint Reading", "important"), s("Budgeting", "important"),
                            s("Communication", "critical"), s("Safety Procedures", "important")],
        "entry_paths": ["Bachelor's in Construction Management / Civil Eng (or trades experience)",
                        "Work up from foreman/superintendent", "PMP or OSHA certifications",
                        "On-the-job project experience"],
        "tags": ["construction", "management", "leadership", "high-pay"],
    },
]


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))

    # Tag every existing career as India region (default) if not set.
    tagged = 0
    for c in careers:
        if "region" not in c:
            c["region"] = "IN"
            tagged += 1

    existing = {c["id"] for c in careers}
    added = []
    for c in US:
        if c["id"] in existing:
            print(f"  skip (exists): {c['id']}")
            continue
        c["region"] = "US"
        careers.append(c)
        added.append(c["title"])

    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")

    in_n = sum(1 for c in careers if c.get("region") == "IN")
    us_n = sum(1 for c in careers if c.get("region") == "US")
    print(f"\nTagged {tagged} existing careers as region=IN")
    print(f"Added {len(added)} US careers")
    print(f"Total: {len(careers)}  (IN: {in_n}, US: {us_n})")
    for t in added:
        print(f"  + {t}")


if __name__ == "__main__":
    main()
