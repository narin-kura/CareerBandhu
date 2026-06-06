"""Add aviation, airport, and customs careers to careers.json (UTF-8 safe)."""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"

NEW = [
    {
        "id": "air_traffic_controller",
        "title": "Air Traffic Controller",
        "category": "Aviation & Airport",
        "description": "Guide aircraft safely through takeoff, landing, and airspace from the control tower. One of the most respected and high-responsibility government jobs in India, recruited through AAI. Excellent pay, prestige, and job security for those who can stay calm under pressure.",
        "salary_range": {"min": 60000, "max": 250000, "currency": "INR/month", "note": "Junior Executive to Senior ATC (AAI)"},
        "growth_outlook": "Strong — airport expansion across India",
        "work_style": ["High-pressure", "Shift work", "Control tower"],
        "required_skills": [
            {"skill": "Situational Awareness", "level": "critical"},
            {"skill": "Quick Decision Making", "level": "critical"},
            {"skill": "Communication", "level": "critical"},
            {"skill": "Concentration & Focus", "level": "critical"},
            {"skill": "Aviation Knowledge", "level": "important"},
            {"skill": "English Proficiency", "level": "critical"},
            {"skill": "Mathematics", "level": "important"},
            {"skill": "Stress Management", "level": "important"},
        ],
        "entry_paths": [
            "B.E/B.Tech (Electronics/Telecom/Electrical) + AAI Junior Executive exam",
            "Airports Authority of India (AAI) recruitment",
            "Pass medical and voice tests",
            "On-the-job ATC training & rating",
        ],
        "tags": ["aviation", "airport", "government", "high-responsibility"],
    },
    {
        "id": "commercial_pilot",
        "title": "Commercial Pilot",
        "category": "Aviation & Airport",
        "description": "Fly passenger or cargo aircraft for airlines across domestic and international routes. A dream career with high pay and global travel. India's aviation sector is booming with new airlines and aircraft orders, creating strong demand for trained pilots.",
        "salary_range": {"min": 150000, "max": 700000, "currency": "INR/month", "note": "First Officer to Captain (wide-body)"},
        "growth_outlook": "Very Strong — record aircraft orders",
        "work_style": ["Travel-heavy", "Shift/roster", "High-responsibility"],
        "required_skills": [
            {"skill": "Aircraft Handling", "level": "critical"},
            {"skill": "Aviation Knowledge", "level": "critical"},
            {"skill": "Quick Decision Making", "level": "critical"},
            {"skill": "Situational Awareness", "level": "critical"},
            {"skill": "Communication", "level": "important"},
            {"skill": "Mathematics", "level": "important"},
            {"skill": "Physics", "level": "important"},
            {"skill": "Stress Management", "level": "important"},
        ],
        "entry_paths": [
            "Class 12 with Physics & Maths",
            "Commercial Pilot License (CPL) from DGCA-approved flying school",
            "Type rating on specific aircraft",
            "Cadet pilot programs (IndiGo, Air India, Akasa)",
        ],
        "tags": ["aviation", "pilot", "travel", "high-pay"],
    },
    {
        "id": "cabin_crew",
        "title": "Cabin Crew / Flight Attendant",
        "category": "Aviation & Airport",
        "description": "Ensure passenger safety, comfort, and service onboard flights. A glamorous, people-facing career with travel perks and quick entry without a degree. Strong demand from India's fast-growing airlines for well-groomed, service-minded candidates.",
        "salary_range": {"min": 40000, "max": 130000, "currency": "INR/month", "note": "Trainee to Senior/Lead crew"},
        "growth_outlook": "Strong — fleet expansion",
        "work_style": ["Travel-heavy", "Customer-facing", "Roster"],
        "required_skills": [
            {"skill": "Customer Service", "level": "critical"},
            {"skill": "Communication", "level": "critical"},
            {"skill": "Grooming & Presentation", "level": "critical"},
            {"skill": "Safety Procedures", "level": "critical"},
            {"skill": "English Proficiency", "level": "important"},
            {"skill": "Teamwork", "level": "important"},
            {"skill": "First Aid", "level": "helpful"},
            {"skill": "Calm Under Pressure", "level": "important"},
        ],
        "entry_paths": [
            "Class 12 pass (any stream)",
            "Air hostess / cabin crew training course",
            "Airline cabin crew recruitment & interview",
            "Meet height, medical & grooming standards",
        ],
        "tags": ["aviation", "airport", "hospitality", "travel"],
    },
    {
        "id": "aircraft_maintenance_engineer",
        "title": "Aircraft Maintenance Engineer (AME)",
        "category": "Aviation & Airport",
        "description": "Inspect, repair, and certify aircraft for safe flight. A licensed, technical career that combines hands-on mechanical work with high responsibility. AMEs are in steady demand as India's airline fleets and MRO industry grow.",
        "salary_range": {"min": 35000, "max": 200000, "currency": "INR/month", "note": "Trainee to Licensed AME"},
        "growth_outlook": "Strong — growing MRO sector",
        "work_style": ["Hands-on", "Technical", "Shift work"],
        "required_skills": [
            {"skill": "Aircraft Maintenance", "level": "critical"},
            {"skill": "Mechanical Aptitude", "level": "critical"},
            {"skill": "Attention to Detail", "level": "critical"},
            {"skill": "Aviation Knowledge", "level": "important"},
            {"skill": "Electrical Wiring", "level": "important"},
            {"skill": "Problem Solving", "level": "important"},
            {"skill": "Safety Procedures", "level": "critical"},
        ],
        "entry_paths": [
            "Class 12 with Physics & Maths",
            "AME course from DGCA-approved institute",
            "DGCA AME License exams",
            "Apprenticeship with airline / MRO",
        ],
        "tags": ["aviation", "engineering", "technical", "licensed"],
    },
    {
        "id": "airport_ground_staff",
        "title": "Airport Ground Staff / Customer Service Agent",
        "category": "Aviation & Airport",
        "description": "Handle check-in, boarding, baggage, and passenger assistance at the airport. A great entry point into aviation without a degree, with chances to grow into supervisory and operations roles. High demand at India's expanding airports.",
        "salary_range": {"min": 18000, "max": 60000, "currency": "INR/month", "note": "Agent to Duty Supervisor"},
        "growth_outlook": "Strong — new airports opening",
        "work_style": ["Customer-facing", "Shift work", "Fast-paced"],
        "required_skills": [
            {"skill": "Customer Service", "level": "critical"},
            {"skill": "Communication", "level": "critical"},
            {"skill": "Computer Basics", "level": "important"},
            {"skill": "English Proficiency", "level": "important"},
            {"skill": "Grooming & Presentation", "level": "important"},
            {"skill": "Problem Solving", "level": "helpful"},
            {"skill": "Teamwork", "level": "important"},
        ],
        "entry_paths": [
            "Class 12 pass",
            "Diploma in airport management / aviation (optional)",
            "Ground handling agency recruitment (AISATS, Celebi, Bird)",
            "Airline customer service openings",
        ],
        "tags": ["airport", "aviation", "customer-service", "entry-level"],
    },
    {
        "id": "airport_manager",
        "title": "Airport Operations Manager",
        "category": "Aviation & Airport",
        "description": "Oversee day-to-day airport operations — terminals, safety, security coordination, and passenger flow. A leadership role connecting airlines, ground staff, and authorities. Growing opportunities as private players run more Indian airports.",
        "salary_range": {"min": 70000, "max": 300000, "currency": "INR/month", "note": "Operations Exec to Airport Manager"},
        "growth_outlook": "Strong — privatised airports",
        "work_style": ["Leadership", "Coordination", "On-site"],
        "required_skills": [
            {"skill": "Operations Management", "level": "critical"},
            {"skill": "Leadership", "level": "critical"},
            {"skill": "Communication", "level": "critical"},
            {"skill": "Aviation Knowledge", "level": "important"},
            {"skill": "Safety Procedures", "level": "important"},
            {"skill": "Crisis Management", "level": "important"},
            {"skill": "Coordination", "level": "important"},
        ],
        "entry_paths": [
            "Bachelor's degree + Airport/Aviation Management diploma (MBA helpful)",
            "Start in ground operations / customer service",
            "Airport operator recruitment (GMR, Adani, AAI)",
            "Internal promotion from operations roles",
        ],
        "tags": ["airport", "aviation", "management", "operations"],
    },
    {
        "id": "customs_officer",
        "title": "Customs Officer (Indian Customs)",
        "category": "Government & Public Service",
        "description": "Inspect goods and passengers at airports, seaports, and borders to enforce import/export laws and prevent smuggling. A respected gazetted government job under CBIC with authority, stability, and growth. Recruited via SSC and UPSC.",
        "salary_range": {"min": 45000, "max": 180000, "currency": "INR/month", "note": "Inspector to Assistant/Deputy Commissioner"},
        "growth_outlook": "Stable — secure government career",
        "work_style": ["Government", "Field + office", "Authority"],
        "required_skills": [
            {"skill": "General Knowledge", "level": "critical"},
            {"skill": "Attention to Detail", "level": "critical"},
            {"skill": "Integrity", "level": "critical"},
            {"skill": "Communication", "level": "important"},
            {"skill": "Reasoning & Aptitude", "level": "critical"},
            {"skill": "Law & Regulations", "level": "important"},
            {"skill": "Computer Basics", "level": "helpful"},
        ],
        "entry_paths": [
            "Graduation in any discipline",
            "SSC CGL exam (Inspector of Customs)",
            "UPSC Civil Services (IRS - Customs & Indirect Taxes)",
            "Department training academy",
        ],
        "tags": ["government", "gazetted", "customs", "airport", "security"],
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
