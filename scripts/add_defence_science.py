"""Add defence, maritime/merchant-navy, railways, and science/research careers (India)."""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


NEW = [
    # ---------------- Defence & Armed Forces ----------------
    {
        "id": "army_officer",
        "title": "Indian Army Officer",
        "category": "Defence & Armed Forces",
        "description": "Lead soldiers and serve the nation in the Indian Army. A prestigious, disciplined career with authority, adventure, lifelong benefits, and immense respect. Entered young through NDA or after graduation via CDS/SSC.",
        "salary_range": {"min": 56000, "max": 200000, "currency": "INR/month", "note": "Lieutenant to senior ranks + allowances"},
        "growth_outlook": "Stable — prestigious government service",
        "work_style": ["Disciplined", "Leadership", "Field postings"],
        "required_skills": [s("Physical Fitness", "critical"), s("Leadership", "critical"), s("Discipline", "critical"),
                            s("Quick Decision Making", "important"), s("Mental Toughness", "critical"),
                            s("Teamwork", "important"), s("General Knowledge", "important")],
        "entry_paths": ["Class 12 + NDA exam (UPSC)", "Graduation + CDS exam (UPSC)",
                        "SSB interview + medical", "Officers Training Academy / IMA / OTA"],
        "tags": ["defence", "army", "officer", "government"],
    },
    {
        "id": "navy_officer",
        "title": "Indian Navy Officer",
        "category": "Defence & Armed Forces",
        "description": "Command ships, submarines, and naval aircraft protecting India's seas. A technically rich, adventurous officer career with global exposure, sea time, and strong benefits.",
        "salary_range": {"min": 56000, "max": 200000, "currency": "INR/month", "note": "Sub-Lieutenant to senior ranks + allowances"},
        "growth_outlook": "Stable — prestigious government service",
        "work_style": ["Sea + shore", "Technical", "Leadership"],
        "required_skills": [s("Physical Fitness", "critical"), s("Leadership", "critical"), s("Discipline", "critical"),
                            s("Mathematics", "important"), s("Mental Toughness", "critical"), s("Teamwork", "important"),
                            s("Technical Aptitude", "important")],
        "entry_paths": ["Class 12 (PCM) + NDA exam", "Graduation + CDS / INET exam",
                        "SSB interview + medical", "Indian Naval Academy training"],
        "tags": ["defence", "navy", "officer", "government"],
    },
    {
        "id": "air_force_officer",
        "title": "Indian Air Force Officer / Fighter Pilot",
        "category": "Defence & Armed Forces",
        "description": "Fly fighter jets or lead technical and ground operations in the Indian Air Force. One of the most aspirational careers in India — fly cutting-edge aircraft, serve the nation, and earn deep respect.",
        "salary_range": {"min": 56000, "max": 200000, "currency": "INR/month", "note": "Flying Officer to senior ranks + flying allowance"},
        "growth_outlook": "Stable — prestigious government service",
        "work_style": ["High-pressure", "Technical", "Adventure"],
        "required_skills": [s("Physical Fitness", "critical"), s("Quick Decision Making", "critical"),
                            s("Aircraft Handling", "important"), s("Discipline", "critical"), s("Mathematics", "important"),
                            s("Mental Toughness", "critical"), s("Situational Awareness", "important")],
        "entry_paths": ["Class 12 (PCM) + NDA exam", "Graduation + AFCAT exam",
                        "SSB interview + pilot aptitude (CPSS) + medical", "Air Force Academy training"],
        "tags": ["defence", "air-force", "pilot", "government"],
    },
    {
        "id": "agniveer",
        "title": "Agniveer (Armed Forces Soldier/Sailor/Airman)",
        "category": "Defence & Armed Forces",
        "description": "Serve in the Army, Navy, or Air Force as an Agniveer under the Agnipath scheme. A direct route to wear the uniform after school, with training, discipline, a service package, and skills for life after service.",
        "salary_range": {"min": 30000, "max": 40000, "currency": "INR/month", "note": "Includes Seva Nidhi package"},
        "growth_outlook": "Stable — direct armed-forces entry",
        "work_style": ["Disciplined", "Physical", "Field"],
        "required_skills": [s("Physical Fitness", "critical"), s("Discipline", "critical"), s("Mental Toughness", "important"),
                            s("Teamwork", "important"), s("General Knowledge", "helpful")],
        "entry_paths": ["Class 10 / 12 (role dependent)", "Agnipath online exam",
                        "Physical fitness test + medical", "Service-specific training"],
        "tags": ["defence", "agniveer", "no-degree", "government"],
    },
    # ---------------- Maritime & Shipping ----------------
    {
        "id": "merchant_navy_officer",
        "title": "Merchant Navy Officer (Deck / Marine Engineer)",
        "category": "Maritime & Shipping",
        "description": "Navigate or run the engines of huge cargo ships across the world's oceans. Among the highest-paying careers you can start after Class 12, with tax-free income, world travel, and long leave periods.",
        "salary_range": {"min": 80000, "max": 800000, "currency": "INR/month", "note": "Cadet to Captain / Chief Engineer (often tax-free)"},
        "growth_outlook": "Strong — global shipping demand",
        "work_style": ["Sea voyages", "Technical", "Long contracts"],
        "required_skills": [s("Navigation", "critical"), s("Technical Aptitude", "critical"), s("Mathematics", "important"),
                            s("Physical Fitness", "important"), s("Discipline", "critical"), s("Teamwork", "important"),
                            s("Mechanical Aptitude", "important")],
        "entry_paths": ["Class 12 (PCM) + IMU CET exam", "B.Tech Marine Engineering / B.Sc Nautical Science",
                        "DG Shipping-approved maritime academy", "Onboard cadet training + competency exams"],
        "tags": ["maritime", "merchant-navy", "high-pay", "travel"],
    },
    {
        "id": "port_operations",
        "title": "Port Operations Executive",
        "category": "Maritime & Shipping",
        "description": "Manage the loading, unloading, and movement of cargo at seaports. A growing logistics career as India expands its ports and shipping trade, with paths into terminal and operations management.",
        "salary_range": {"min": 25000, "max": 90000, "currency": "INR/month", "note": "Executive to Operations Manager"},
        "growth_outlook": "Strong — port infrastructure growth",
        "work_style": ["On-site", "Coordination", "Shift work"],
        "required_skills": [s("Operations Management", "critical"), s("Coordination", "critical"),
                            s("Logistics", "important"), s("Communication", "important"), s("Computer Basics", "important"),
                            s("Safety Procedures", "helpful")],
        "entry_paths": ["Graduation / Diploma in logistics or shipping", "Port & terminal management courses",
                        "Major Port Trust / private port recruitment", "Start in cargo / terminal operations"],
        "tags": ["maritime", "port", "logistics", "operations"],
    },
    # ---------------- Railways (beyond RRB officer) ----------------
    {
        "id": "loco_pilot",
        "title": "Railway Loco Pilot (Train Driver)",
        "category": "Transport & Logistics",
        "description": "Drive passenger and freight trains across India's vast rail network. A secure government job with good pay, allowances, and clear promotion from assistant to senior loco pilot.",
        "salary_range": {"min": 35000, "max": 90000, "currency": "INR/month", "note": "Assistant to Senior Loco Pilot + allowances"},
        "growth_outlook": "Stable — secure government job",
        "work_style": ["Shift work", "High-responsibility", "Technical"],
        "required_skills": [s("Concentration & Focus", "critical"), s("Technical Aptitude", "important"),
                            s("Quick Decision Making", "important"), s("Discipline", "critical"),
                            s("Safety Procedures", "critical"), s("Mechanical Aptitude", "helpful")],
        "entry_paths": ["Class 10 + ITI / diploma (relevant trade)", "RRB ALP (Assistant Loco Pilot) exam",
                        "Aptitude test + medical", "Promotion to Loco Pilot with experience"],
        "tags": ["railways", "government", "driving", "stable"],
    },
    {
        "id": "station_master",
        "title": "Railway Station Master",
        "category": "Transport & Logistics",
        "description": "Run the safe operation of a railway station — train movements, signals, and passenger coordination. A respected, secure government job with authority and steady promotion.",
        "salary_range": {"min": 35000, "max": 95000, "currency": "INR/month", "note": "Station Master to Area Manager"},
        "growth_outlook": "Stable — secure government job",
        "work_style": ["Shift work", "Coordination", "High-responsibility"],
        "required_skills": [s("Coordination", "critical"), s("Communication", "critical"), s("Quick Decision Making", "important"),
                            s("Computer Basics", "important"), s("Discipline", "critical"), s("General Knowledge", "important")],
        "entry_paths": ["Graduation (any discipline)", "RRB NTPC exam (Station Master)",
                        "Computer-based test + aptitude", "Departmental training"],
        "tags": ["railways", "government", "operations", "stable"],
    },
    # ---------------- Science & Research ----------------
    {
        "id": "research_scientist",
        "title": "Research Scientist",
        "category": "Science & Research",
        "description": "Push the boundaries of knowledge through experiments and discovery in physics, biology, chemistry, or other fields. Work in universities, national labs (CSIR), or R&D, publishing papers and solving hard problems.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "INR/month", "note": "JRF/SRF to Senior Scientist"},
        "growth_outlook": "Stable — research & academia",
        "work_style": ["Lab-based", "Analytical", "Deep work"],
        "required_skills": [s("Research", "critical"), s("Analytical Thinking", "critical"), s("Mathematics", "important"),
                            s("Scientific Writing", "important"), s("Data Analysis", "important"), s("Patience", "important"),
                            s("Subject Expertise", "critical")],
        "entry_paths": ["B.Sc / M.Sc in a science discipline", "CSIR-UGC NET / GATE for fellowships",
                        "PhD in specialization", "Postdoc / lab positions (CSIR, IISc, IITs)"],
        "tags": ["science", "research", "academia", "R&D"],
    },
    {
        "id": "space_scientist",
        "title": "Space Scientist / Aerospace Engineer (ISRO)",
        "category": "Science & Research",
        "description": "Design rockets, satellites, and space missions — be the 'rocket scientist' building India's space program. Work at ISRO or aerospace firms on launch vehicles, propulsion, and spacecraft. Prestigious and deeply impactful.",
        "salary_range": {"min": 60000, "max": 250000, "currency": "INR/month", "note": "Scientist/Engineer 'SC' to senior grades"},
        "growth_outlook": "Strong — booming space sector",
        "work_style": ["Technical", "Project-based", "Cutting-edge"],
        "required_skills": [s("Physics", "critical"), s("Mathematics", "critical"), s("Aerospace Engineering", "critical"),
                            s("Problem Solving", "critical"), s("Research", "important"), s("CAD Software", "helpful"),
                            s("Programming", "important")],
        "entry_paths": ["B.Tech (Aerospace/Mechanical/Electronics) or M.Sc Physics", "ISRO Centralised Recruitment (ICRB) exam",
                        "GATE + higher studies (IIST, IITs)", "Aerospace R&D / private space startups"],
        "tags": ["science", "space", "ISRO", "aerospace", "rocket"],
    },
    {
        "id": "defence_scientist_drdo",
        "title": "Defence Scientist (DRDO)",
        "category": "Science & Research",
        "description": "Develop missiles, radars, and advanced defence technology for the nation at DRDO. A prestigious R&D career combining science and national security, with strong job stability and impact.",
        "salary_range": {"min": 60000, "max": 230000, "currency": "INR/month", "note": "Scientist 'B' to senior grades"},
        "growth_outlook": "Stable — strategic R&D",
        "work_style": ["Lab-based", "Technical", "Confidential projects"],
        "required_skills": [s("Research", "critical"), s("Analytical Thinking", "critical"), s("Engineering", "critical"),
                            s("Mathematics", "important"), s("Problem Solving", "critical"), s("Programming", "helpful"),
                            s("Subject Expertise", "important")],
        "entry_paths": ["B.Tech / M.Sc / M.Tech (relevant field)", "GATE score / DRDO RAC recruitment",
                        "Interview + technical assessment", "Higher studies for senior research"],
        "tags": ["science", "defence", "DRDO", "R&D", "government"],
    },
]


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))
    existing = {c["id"] for c in careers}
    added = []
    for c in NEW:
        if c["id"] in existing:
            print(f"  skip (exists): {c['id']}")
            continue
        c["region"] = "IN"
        careers.append(c)
        added.append(c["title"])
    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nAdded {len(added)} careers. Total: {len(careers)}")
    for t in added:
        print(f"  + {t}")
    cats = sorted(set(c["category"] for c in careers))
    print(f"\nCategories ({len(cats)}): {cats}")


if __name__ == "__main__":
    main()
