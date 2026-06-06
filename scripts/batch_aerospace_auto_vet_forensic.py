"""Batch: Aerospace & Space, Automotive & EV, Veterinary & Animal Care, Forensic & Investigation"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


CAREERS = [

    # ══════════════════════════════════════════════════════
    # AEROSPACE & SPACE — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "isro_scientist_in",
        "title": "ISRO Scientist / Engineer",
        "category": "Aerospace & Space",
        "region": "IN",
        "description": "Work at the Indian Space Research Organisation (ISRO) on missions including Chandrayaan, Gaganyaan (India's crewed spaceflight), Aditya-L1, and communication satellite launches. ISRO employs scientists and engineers across propulsion, guidance, control, avionics, software, structures, and ground systems. The Space sector is now partially opened to private players — startups like Skyroot, Agnikul, and Pixxel are emerging employers.",
        "salary_range": {"min": 60000, "max": 250000, "currency": "INR/month", "note": "Scientist/Engineer SC (entry) to Distinguished Scientist; government pay scale with assured growth"},
        "growth_outlook": "Excellent — India's Space sector privatised; new space startups + ISRO expansion = growing talent demand",
        "work_style": ["Technical", "Research-intensive", "Government / Mission-driven"],
        "required_skills": [
            s("Aerospace / Mechanical / Electronics Engineering", "critical"),
            s("Mathematics & Physics", "critical"), s("Embedded Systems or Control Systems", "important"),
            s("MATLAB / Simulation Tools", "important"), s("Analytical Problem Solving", "critical"),
            s("Technical Report Writing", "important"),
        ],
        "entry_paths": [
            "Score very high in JEE Advanced → pursue B.Tech/BE in Aerospace, Mechanical, Electronics, or CS at IIT/NIT",
            "Write ICRB (ISRO Centralised Recruitment Board) ISRO exam — held for specific posts periodically",
            "Complete M.Tech or PhD from IIT/IISc for research scientist roles",
            "Join private space startups (Skyroot, Agnikul Cosmos, Dhruva Space) — now a viable alternative pathway",
        ],
        "qualifications": [
            "B.Tech/BE in Aerospace, Mechanical, Electronics, CS or Physics from reputed institute",
            "M.Tech / ME / MS / PhD for senior scientist roles (IIT, IISc preferred)",
            "ISRO ICRB exam score (written + interview)",
        ],
        "tags": ["isro", "space", "aerospace", "satellite", "scientist"],
    },
    {
        "id": "aerospace_engineer_in",
        "title": "Aerospace Engineer (Private Sector)",
        "category": "Aerospace & Space",
        "region": "IN",
        "description": "Design, develop, and test aircraft, spacecraft, and related systems for defence PSUs (HAL, DRDO, BEL), private aviation (IndiGo, Air India engineering), MRO companies, or the growing Indian new-space startup ecosystem. HAL (Hindustan Aeronautics Limited) builds the Tejas fighter jet and helicopters. DRDO works on missiles and UAVs. India's aerospace MRO market is expanding with aviation growth.",
        "salary_range": {"min": 50000, "max": 300000, "currency": "INR/month", "note": "Graduate engineer trainee at HAL / DRDO to senior engineer at a private aerospace firm"},
        "growth_outlook": "Strong — India's defence manufacturing push (Make in India), growing aviation, and space privatisation",
        "work_style": ["Technical", "Analytical", "Design-intensive"],
        "required_skills": [
            s("Aerospace Engineering Fundamentals (aerodynamics, propulsion, structures)", "critical"),
            s("CAD / CAE (CATIA, ANSYS, SolidWorks)", "critical"), s("FEM / CFD Analysis", "important"),
            s("MATLAB & Simulink", "important"), s("Systems Engineering", "important"),
        ],
        "entry_paths": [
            "B.Tech/BE in Aerospace Engineering from IIT, IISc, MIT-Manipal, SRM, or Amity",
            "Apply to HAL Graduate Engineer Trainee or DRDO through CEPTAM entrance exam",
            "Join private MRO companies (Air India Engineering Services, Lufthansa Technik India)",
            "Join new-space startups (Skyroot, Agnikul, Pixxel, Dhruva Space) as early-stage engineer",
        ],
        "qualifications": [
            "B.Tech/BE in Aerospace, Mechanical, or Electronics Engineering",
            "GATE score for HAL / DRDO / ISRO (assists in selection)",
            "M.Tech in Aerospace or Avionics for senior roles",
        ],
        "tags": ["aerospace", "hal", "drdo", "aircraft", "engineering"],
    },
    {
        "id": "drone_operator_in",
        "title": "Drone Pilot / UAV Operator",
        "category": "Aerospace & Space",
        "region": "IN",
        "description": "Operate unmanned aerial vehicles (UAVs / drones) for aerial photography, survey & mapping, agriculture spraying, infrastructure inspection, disaster management, and delivery. DGCA's 2021 Drone Rules liberalised the sector — India's drone industry is now one of the fastest growing, with government PLI incentives for drone manufacturing. DGCA remote pilot licence is mandatory for commercial operations.",
        "salary_range": {"min": 25000, "max": 200000, "currency": "INR/month", "note": "Junior drone operator at a survey company to senior pilot or drone service entrepreneur"},
        "growth_outlook": "Very strong — India's drone policy among the world's most progressive; demand across agriculture, infrastructure, defence, and delivery",
        "work_style": ["Field-based", "Technical", "Outdoor"],
        "required_skills": [
            s("UAV / Drone Piloting (multi-rotor & fixed-wing)", "critical"),
            s("DGCA Regulations & Airspace Knowledge", "critical"),
            s("Aerial Photography / Photogrammetry", "important"),
            s("Mission Planning Software (DJI Terra, Pix4D)", "important"),
            s("Data Processing & GIS", "helpful"),
        ],
        "entry_paths": [
            "Obtain a DGCA Remote Pilot Certificate (RPC) from an authorised DGCA remote pilot training organisation (RPTO)",
            "Choose a specialisation: agriculture spraying (Garuda Aerospace, TechEagle), aerial survey (Genesys), inspection, or media",
            "Start with a drone service company; build 200+ flight hours for senior roles",
            "Set up your own drone service business for survey, agri-spraying, or aerial photography",
        ],
        "qualifications": [
            "DGCA Remote Pilot Certificate (RPC) — mandatory for commercial drone operation",
            "Minimum Class X pass (12th preferred); no engineering degree required",
            "GIS / Photogrammetry certification (helpful for survey & mapping roles)",
        ],
        "tags": ["drone", "uav", "dgca", "aerial-survey", "agri-drone"],
    },

    # ─── AEROSPACE — USA ──────────────────────────────────
    {
        "id": "us_aerospace_engineer",
        "title": "Aerospace Engineer",
        "category": "Aerospace & Space",
        "region": "US",
        "description": "Design, develop, and test aircraft, spacecraft, satellites, and defence systems. The US aerospace industry employs over 500,000 engineers at companies like Boeing, Lockheed Martin, Raytheon, SpaceX, Blue Origin, NASA, and hundreds of defence contractors. The sector spans commercial aviation, defence, NASA missions, and a booming private space industry.",
        "salary_range": {"min": 90000, "max": 200000, "currency": "USD/year", "note": "Entry aerospace engineer to senior systems engineer at Boeing, SpaceX, or Lockheed Martin"},
        "growth_outlook": "Stable — BLS projects 6% growth; commercial space boom driving private sector demand",
        "work_style": ["Technical", "Analytical", "Design & Test intensive"],
        "required_skills": [
            s("Aerodynamics & Propulsion", "critical"), s("Structural Analysis & FEM", "critical"),
            s("CAD (CATIA, SolidWorks, NX)", "critical"), s("MATLAB / Simulink", "important"),
            s("Systems Engineering (Model-Based SE)", "important"), s("DoD / FAA Compliance", "helpful"),
        ],
        "entry_paths": [
            "Bachelor's or Master's in Aerospace Engineering from AIAA-recognised universities (MIT, Stanford, Georgia Tech, Purdue, UCLA)",
            "Intern at NASA, SpaceX, Boeing, Lockheed during undergraduate years",
            "Obtain DoD secret clearance for defence contractor roles (significant advantage)",
            "Join new-space companies (SpaceX, Blue Origin, Rocket Lab, Relativity Space) for fastest growth",
        ],
        "qualifications": [
            "ABET-accredited Bachelor's in Aerospace Engineering (or Mechanical / Electrical for crossover roles)",
            "PE (Professional Engineer) licence (for systems requiring sign-off)",
            "DoD Security Clearance (required for defence aerospace roles)",
            "MS or PhD in Aero/Astro for R&D and senior engineering positions",
        ],
        "tags": ["aerospace", "nasa", "spacex", "aircraft", "defence-engineering"],
    },

    # ══════════════════════════════════════════════════════
    # AUTOMOTIVE & EV — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "automobile_engineer_in",
        "title": "Automobile Engineer (Design & Development)",
        "category": "Automotive & EV",
        "region": "IN",
        "description": "Design, develop, and test vehicles — cars, two-wheelers, commercial vehicles, and electric vehicles — for Indian OEMs (Tata Motors, Mahindra, Hero, Bajaj, Maruti Suzuki, Hyundai India) and their Tier-1 suppliers. India is the 3rd-largest automobile market globally. EV transition has created massive demand for powertrain, battery management, and NVH engineers.",
        "salary_range": {"min": 40000, "max": 400000, "currency": "INR/month", "note": "Graduate engineer trainee at Tier-2 supplier to senior design / development engineer at an OEM"},
        "growth_outlook": "Strong — India's EV push and rising vehicle production creating sustained engineering demand",
        "work_style": ["Technical", "Design & Test", "Team-based"],
        "required_skills": [
            s("Vehicle Dynamics & Powertrain", "critical"), s("CAD (CATIA V5/V6, SolidWorks, NX)", "critical"),
            s("CAE / FEA (ANSYS, Nastran)", "important"), s("MATLAB / Simulink for control systems", "important"),
            s("Automotive Standards (AIS, CMVR)", "important"), s("Testing & Validation", "critical"),
        ],
        "entry_paths": [
            "B.Tech/BE in Automobile, Mechanical, or Electronics Engineering from NIT / VIT / SRM / BITS",
            "Internship at Tata Motors, Mahindra, Hero, or a Tier-1 auto supplier (BOSCH, Valeo, ZF India)",
            "Join the GET (Graduate Engineer Trainee) programme at an OEM",
            "Specialise in EV — battery management, e-axle, or ADAS — for higher demand and salary",
        ],
        "qualifications": [
            "B.Tech/BE in Automobile, Mechanical, or Electrical/Electronics Engineering",
            "GATE score helpful for PSU automotive roles (BHEL, BEML)",
            "M.Tech in Automotive Engineering (NIT Hamirpur, VIT, BITS) for senior development roles",
            "Professional certification from SAE India (Society of Automotive Engineers)",
        ],
        "tags": ["automobile", "automotive", "ev", "tata-motors", "engineering"],
    },
    {
        "id": "ev_technician_in",
        "title": "EV Battery Technician / Electric Vehicle Technician",
        "category": "Automotive & EV",
        "region": "IN",
        "description": "Service, diagnose, and repair electric vehicles — covering battery packs, BMS (Battery Management System), electric motors, charging systems, and power electronics. India's EV revolution — Ola Electric, Ather, TVS iQube, Tata Nexon EV — has created urgent demand for skilled EV technicians. This is a blue-collar role with rapidly rising wages as EVs displace ICE vehicles.",
        "salary_range": {"min": 20000, "max": 80000, "currency": "INR/month", "note": "Junior EV service technician at dealership to senior EV specialist; wages rising rapidly"},
        "growth_outlook": "Excellent — EV adoption in India accelerating; massive shortage of certified EV technicians",
        "work_style": ["Hands-on", "Workshop-based", "Technical"],
        "required_skills": [
            s("EV Powertrain Fundamentals", "critical"), s("Battery Pack Diagnosis & Replacement", "critical"),
            s("EV Diagnostic Software (OEM-specific)", "critical"), s("High Voltage Safety", "critical"),
            s("Charging Systems & EVSE", "important"), s("Basic Electronics", "critical"),
        ],
        "entry_paths": [
            "Complete ITI (Industrial Training Institute) in Electrician, Electronics, or Auto Mechanic",
            "Pursue dedicated EV technician courses from ASDC (Automotive Skills Development Council), C-STEP, or OEM training centres",
            "Get certified by OEMs: Ola Electric, Ather, Tata Motors, TVS — all run technician training programmes",
            "Work at an EV dealership service centre; gain certification through OEM training",
        ],
        "qualifications": [
            "ITI in Electrician / Electronics / Auto Mechanic (2-year trade certificate)",
            "ASDC-certified EV Technician (National Skills Qualification Framework Level 4/5)",
            "OEM-specific EV certification from Ola Electric, Ather Energy, Tata Motors, or TVS",
            "High-Voltage Safety training certificate (mandatory for working on EV battery systems)",
        ],
        "tags": ["ev", "electric-vehicle", "technician", "battery", "automotive"],
    },
    {
        "id": "auto_mechanic_in",
        "title": "Automobile Mechanic / Service Technician",
        "category": "Automotive & EV",
        "region": "IN",
        "description": "Service, repair, and maintain motor vehicles — cars, two-wheelers, and commercial vehicles — at authorised dealerships, multi-brand garages, or self-owned repair shops. India has 450+ million vehicles on the road. Automotive service is one of the most employment-intensive sectors in the country. Skilled mechanics who specialise in premium brands or EVs command higher wages.",
        "salary_range": {"min": 15000, "max": 60000, "currency": "INR/month", "note": "Junior mechanic at a service centre to senior diagnostic technician at an authorised dealership"},
        "growth_outlook": "Stable — growing vehicle fleet sustains demand; EV adds new specialisation layer",
        "work_style": ["Hands-on", "Workshop-based", "Physical"],
        "required_skills": [
            s("Vehicle Diagnostics (OBD scan tools)", "critical"), s("Engine & Transmission Repair", "critical"),
            s("Electrical & AC Systems", "important"), s("Brake & Suspension Service", "critical"),
            s("Manufacturer-Specific Service Manuals", "important"), s("Tool Proficiency", "critical"),
        ],
        "entry_paths": [
            "Complete ITI in Mechanic (Motor Vehicle) — the most direct 2-year trade path",
            "Apprenticeship under the Apprentices Act at an authorised dealership (Maruti, Hero, Hyundai)",
            "Join a multi-brand garage and work up through specialisations (AC, engine, electrical)",
            "Start your own workshop after 5+ years of experience",
        ],
        "qualifications": [
            "ITI Mechanic Motor Vehicle (MMV) — 2-year trade certificate from government ITI",
            "Diploma in Automobile Engineering (polytechnic — 3 years)",
            "OEM-specific dealership technician certification (Maruti, Hyundai, Hero, Bajaj)",
        ],
        "tags": ["mechanic", "automobile", "service-technician", "iti", "repair"],
    },

    # ─── AUTOMOTIVE — USA ─────────────────────────────────
    {
        "id": "us_automotive_engineer",
        "title": "Automotive Engineer",
        "category": "Automotive & EV",
        "region": "US",
        "description": "Design and develop vehicles at Ford, GM, Stellantis, Tesla, Rivian, Lucid, and hundreds of Tier-1 automotive suppliers. The US auto industry is in its biggest transformation since the Model T — EV platforms, autonomous driving systems (ADAS), and software-defined vehicles are driving demand for mechatronic, electrical, and software engineers.",
        "salary_range": {"min": 80000, "max": 180000, "currency": "USD/year", "note": "Entry engineer at a Tier-1 supplier to principal engineer at Tesla, Ford EV, or GM BrightDrop"},
        "growth_outlook": "Strong — EV transformation driving up demand for battery, powertrain, and software engineers",
        "work_style": ["Technical", "Design & Test", "Team-based"],
        "required_skills": [
            s("Vehicle Dynamics & Powertrain", "critical"), s("CAD (CATIA, SolidWorks)", "critical"),
            s("Control Systems & MATLAB", "important"), s("CAN Bus & Automotive Protocols (LIN, FlexRay)", "important"),
            s("FMEA & Quality Engineering", "important"), s("Battery Systems (for EV roles)", "helpful"),
        ],
        "entry_paths": [
            "ABET-accredited bachelor's in Mechanical, Electrical, or Automotive Engineering",
            "Intern at Ford, GM, Toyota, Tesla, or Tier-1 suppliers (BOSCH, Continental, Aptiv)",
            "Join SAE International student chapters for competitions and networking",
            "Focus on ADAS / software or EV battery specialisation for highest demand roles",
        ],
        "qualifications": [
            "ABET-accredited Bachelor's in Mechanical, Electrical, Automotive, or Computer Engineering",
            "PE licence (for certain system sign-off roles)",
            "SAE International certifications in specific automotive disciplines",
        ],
        "tags": ["automotive", "ev", "tesla", "ford", "engineering"],
    },

    # ══════════════════════════════════════════════════════
    # VETERINARY & ANIMAL CARE — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "veterinarian_in",
        "title": "Veterinarian (Veterinary Doctor)",
        "category": "Veterinary & Animal Care",
        "region": "IN",
        "description": "Diagnose, treat, and prevent diseases in animals — companion animals (dogs, cats), livestock (cattle, poultry, sheep), and wild animals. India has over 75,000 registered veterinarians and a severe shortage in rural areas. Government veterinarians serve through state animal husbandry departments; private vets serve urban pet clinics; and specialisations include surgery, pathology, radiology, and zoo medicine.",
        "salary_range": {"min": 40000, "max": 300000, "currency": "INR/month", "note": "Government AHD veterinarian to specialist private vet or clinic owner in a metro city"},
        "growth_outlook": "Good — pet industry booming; government programmes for livestock disease control and dairy sector expanding",
        "work_style": ["Clinical", "Hands-on", "Varied (indoor + outdoor)"],
        "required_skills": [
            s("Animal Anatomy & Physiology", "critical"), s("Clinical Diagnosis", "critical"),
            s("Surgical Skills", "important"), s("Pharmacology & Drug Administration", "critical"),
            s("Animal Handling", "critical"), s("Communication with Pet Owners", "important"),
        ],
        "entry_paths": [
            "Score well in PCB (Physics, Chemistry, Biology) at 12th and appear for state veterinary entrance exams (PCVET, AP EAPCET-Vet)",
            "Complete BVSc & AH (Bachelor of Veterinary Science and Animal Husbandry) — 5.5-year degree",
            "Register with Veterinary Council of India (mandatory to practise)",
            "Join government Animal Husbandry Department (AHD) through state UPSC/PSC exam",
        ],
        "qualifications": [
            "BVSc & AH from a VCI-recognised veterinary college (5.5 years including internship)",
            "MVSc for specialisation (surgery, pathology, internal medicine, zoo medicine)",
            "Veterinary Council of India (VCI) registration (mandatory)",
            "PhD in veterinary science for academic and research careers",
        ],
        "tags": ["veterinarian", "vet", "animal-care", "livestock", "pet-clinic"],
    },
    {
        "id": "pet_groomer_in",
        "title": "Pet Groomer / Animal Care Specialist",
        "category": "Veterinary & Animal Care",
        "region": "IN",
        "description": "Provide grooming, bathing, nail trimming, and coat care services for pet animals — primarily dogs and cats. India's pet industry is growing at 20%+ annually, driven by urban pet ownership. Pet grooming salons, mobile grooming vans, and grooming services attached to vet clinics are all expanding. Top groomers also compete in international grooming championships.",
        "salary_range": {"min": 15000, "max": 80000, "currency": "INR/month", "note": "Junior groomer at a salon to senior groomer / self-employed mobile grooming business owner"},
        "growth_outlook": "Very strong — India's pet care market crossing ₹20,000 crore; grooming is a key service segment",
        "work_style": ["Hands-on", "Physical", "Client / Animal-facing"],
        "required_skills": [
            s("Dog & Cat Coat Grooming Techniques", "critical"), s("Breed-Specific Styling", "important"),
            s("Animal Handling & Temperament", "critical"), s("Bathing & Drying Equipment", "critical"),
            s("Nail & Ear Care", "important"), s("Customer Communication", "important"),
        ],
        "entry_paths": [
            "Take a professional pet grooming course from institutes like Heads Up For Tails, Supertails, or private grooming academies",
            "Apprentice at an established pet grooming salon",
            "Start as an assistant groomer and work up to certified groomer",
            "Launch a mobile grooming service for higher margins and flexibility",
        ],
        "qualifications": [
            "Professional Pet Grooming Certificate from a recognised grooming school or brand",
            "No mandatory formal qualification — practical skill and portfolio is primary",
            "City Pet Shop / Grooming salon licence (municipal requirement)",
        ],
        "tags": ["pet-grooming", "pet-care", "dog-grooming", "animal", "salon"],
    },
    {
        "id": "wildlife_biologist_in",
        "title": "Wildlife Biologist / Conservation Officer",
        "category": "Veterinary & Animal Care",
        "region": "IN",
        "description": "Study wild animal populations, habitats, and ecosystems; support conservation programmes for endangered species like tigers, elephants, and leopards. India has 54 Tiger Reserves and 99 National Parks employing field biologists, Wildlife Institute of India researchers, NGO conservationists, and state forest department rangers. Research data informs conservation policy.",
        "salary_range": {"min": 30000, "max": 150000, "currency": "INR/month", "note": "Field research assistant at NGO to senior scientist at WII (Wildlife Institute of India) or government Forest Service"},
        "growth_outlook": "Stable — conservation funding growing with eco-tourism and international climate finance",
        "work_style": ["Outdoor / Field", "Research-intensive", "Remote posting"],
        "required_skills": [
            s("Wildlife Survey & Monitoring Methods", "critical"), s("Species Identification", "critical"),
            s("Ecological Data Collection & Analysis", "critical"), s("GIS & Spatial Analysis", "important"),
            s("Camera Trapping & Radio Telemetry", "important"), s("Scientific Report Writing", "critical"),
        ],
        "entry_paths": [
            "Bachelor's in Zoology, Forestry, Life Sciences, or Environmental Science",
            "Master's in Wildlife Science (WII Dehradun, SACON, NCF), Ecology, or Zoology",
            "Join an NGO (WCS India, WWF-India, NCF, Aaranyak) as a field researcher",
            "Qualify IFS (Indian Forest Service) exam for a government forest officer career",
        ],
        "qualifications": [
            "BSc / MSc in Zoology, Wildlife Science, Forestry, or Environmental Science",
            "WII M.Sc Wildlife Science (Wildlife Institute of India, Dehradun) — most prestigious",
            "IFS (Indian Forest Service) exam (UPSC) for government forest officer career",
            "PhD in Ecology / Wildlife Biology for research and academic careers",
        ],
        "tags": ["wildlife", "conservation", "ecology", "forest", "research"],
    },

    # ─── VETERINARY — USA ─────────────────────────────────
    {
        "id": "us_veterinarian",
        "title": "Veterinarian (DVM)",
        "category": "Veterinary & Animal Care",
        "region": "US",
        "description": "Diagnose, treat, and prevent diseases in companion animals, livestock, exotic animals, and wildlife. The US veterinary profession is among the most respected and consistently highest-paying in healthcare. Specialisations (internal medicine, oncology, cardiology, surgery, emergency & critical care) require additional residency training. The AVMA predicts growing shortages of vets in rural and food-animal practice.",
        "salary_range": {"min": 90000, "max": 250000, "currency": "USD/year", "note": "General practitioner at a small animal clinic to veterinary specialist at a referral centre"},
        "growth_outlook": "Excellent — AVMA reports veterinarian shortage; pet industry boom and food safety demand sustaining growth",
        "work_style": ["Clinical", "Hands-on", "Variable hours (emergency care is 24/7)"],
        "required_skills": [
            s("Animal Anatomy & Physiology", "critical"), s("Clinical Diagnosis", "critical"),
            s("Surgical Techniques", "important"), s("Pharmacology", "critical"),
            s("Radiology & Diagnostic Imaging", "important"), s("Client Communication", "critical"),
        ],
        "entry_paths": [
            "Complete prerequisite undergraduate coursework (biology, chemistry, biochemistry) → apply to AVMA-accredited veterinary college (DVM — 4 years)",
            "Gain hands-on experience volunteering at clinics, shelters, and farms before applying",
            "Pass the NAVLE (North American Veterinary Licensing Examination) for state licensure",
            "Complete a residency (3+ years) and board certification for specialisation",
        ],
        "qualifications": [
            "DVM (Doctor of Veterinary Medicine) or VMD from AVMA-accredited college",
            "NAVLE (state veterinary licence examination)",
            "Board certification from ABVP (speciality) after residency and examination",
        ],
        "tags": ["veterinarian", "dvm", "animal-medicine", "pet-care", "livestock"],
    },

    # ══════════════════════════════════════════════════════
    # FORENSIC & INVESTIGATION — INDIA
    # ══════════════════════════════════════════════════════
    {
        "id": "forensic_scientist_in",
        "title": "Forensic Scientist",
        "category": "Forensic & Investigation",
        "region": "IN",
        "description": "Examine physical evidence from crime scenes — fingerprints, DNA, ballistics, questioned documents, toxicology samples, and digital evidence — to support criminal investigations and judicial proceedings. Central and State Forensic Science Laboratories (FSLs) and the CFSL under MHA are the primary employers. Private forensic labs and cybercrime investigation firms are also growing employers.",
        "salary_range": {"min": 40000, "max": 150000, "currency": "INR/month", "note": "Junior forensic examiner at state FSL to senior scientist / director at CFSL"},
        "growth_outlook": "Growing — India expanding forensic infrastructure; digital forensics seeing rapid growth",
        "work_style": ["Laboratory-based", "Analytical", "Precise"],
        "required_skills": [
            s("Evidence Collection & Chain of Custody", "critical"), s("Laboratory Techniques (chromatography, spectroscopy)", "critical"),
            s("DNA Analysis & Serology", "important"), s("Digital Forensics Tools (Cellebrite, Autopsy)", "important"),
            s("Report Writing for Court Admissibility", "critical"), s("Forensic Photography", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Forensic Science, Chemistry, Biology, or Physics",
            "Master's in Forensic Science from NFSU (National Forensic Sciences University, Gandhinagar), Panjab University, or state forensic universities",
            "Qualify for FSL (Forensic Science Laboratory) recruitment through state PSC exams",
            "Join private cybercrime labs, CERT-In empanelled firms, or multinational forensic firms",
        ],
        "qualifications": [
            "BSc / MSc in Forensic Science or a core science (Chemistry, Biology, Physics)",
            "MSc Forensic Science from NFSU (National Forensic Sciences University) — India's premier forensic institution",
            "State FSL / CFSL recruitment exam for government forensic scientist posts",
            "Certified Digital Forensics Examiner (CDFE) or Cellebrite Certified Examiner (CCE) for digital specialisation",
        ],
        "tags": ["forensic", "crime-lab", "fsl", "investigation", "evidence"],
    },
    {
        "id": "private_investigator_in",
        "title": "Private Investigator / Detective",
        "category": "Forensic & Investigation",
        "region": "IN",
        "description": "Conduct investigations for private clients — individuals, law firms, corporations, and insurance companies — covering matrimonial cases, corporate fraud, background verification, surveillance, and asset tracing. India's private detective industry is large but unregulated — no national licensing exists yet. Reputed agencies build credibility through quality and client relationships. Former police and intelligence officers often enter this field.",
        "salary_range": {"min": 30000, "max": 200000, "currency": "INR/month", "note": "Junior field investigator at a detective agency to senior partner / owner of an established firm; fee-based at senior levels"},
        "growth_outlook": "Growing — corporate due diligence, insurance fraud investigation, and background verification driving demand",
        "work_style": ["Field-based", "Independent", "Confidential / Discreet"],
        "required_skills": [
            s("Surveillance Techniques", "critical"), s("Legal Evidence Gathering", "critical"),
            s("Open Source Intelligence (OSINT)", "critical"), s("Interview & Interrogation Skills", "important"),
            s("Report Writing", "critical"), s("Discretion & Confidentiality", "critical"),
        ],
        "entry_paths": [
            "Background in law enforcement (police / intelligence agencies) provides the most direct entry",
            "Bachelor's in Criminology, Law, or Psychology",
            "Join an established detective agency as a junior investigator",
            "Specialise in corporate investigations or digital OSINT for higher-paying clients",
        ],
        "qualifications": [
            "No mandatory national licence in India (proposed legislation under review)",
            "Bachelor's in Criminology, Law, or Social Science",
            "OSINT framework training (online courses), digital investigation certifications",
            "Former police / IB / intelligence background is a strong credential",
        ],
        "tags": ["private-investigator", "detective", "surveillance", "osint", "corporate-fraud"],
    },
    {
        "id": "cyber_forensics_in",
        "title": "Cyber Forensic Analyst / Digital Investigator",
        "category": "Forensic & Investigation",
        "region": "IN",
        "description": "Investigate cybercrimes — hacking, ransomware, online fraud, child exploitation content, corporate data theft, and financial cybercrime. Cyber forensic analysts work for state cybercrime cells, CERT-In, banks, fintech companies, law firms, and private forensic labs. This is one of the fastest-growing areas of Indian law enforcement and private security, driven by rapid digitisation and rising cybercrime rates.",
        "salary_range": {"min": 40000, "max": 300000, "currency": "INR/month", "note": "Cyber crime cell analyst (government) to senior digital forensics examiner in a private firm"},
        "growth_outlook": "Excellent — India among the top 5 most cyber-targeted nations; cybercrime growing 15% annually",
        "work_style": ["Lab-based", "Analytical", "Detail-intensive"],
        "required_skills": [
            s("Digital Evidence Acquisition & Analysis", "critical"), s("Cellebrite / UFED / Axiom", "critical"),
            s("Network Forensics (Wireshark, NetworkMiner)", "important"), s("Malware Analysis", "helpful"),
            s("Chain of Custody Documentation", "critical"), s("OSINT & Social Media Forensics", "important"),
        ],
        "entry_paths": [
            "Bachelor's in Computer Science, Cybersecurity, or Forensic Science",
            "Master's in Cyber Forensics from NFSU (National Forensic Sciences University)",
            "Get certified: CEH (Certified Ethical Hacker), CHFI (Computer Hacking Forensic Investigator), CCE",
            "Join cybercrime cells (state police), CERT-In, or private forensic firms",
        ],
        "qualifications": [
            "BSc/MSc in Computer Science, Cybersecurity, or Forensic Science",
            "CHFI (Computer Hacking Forensic Investigator) — EC-Council certification",
            "Cellebrite Certified Examiner (CCE) for mobile forensics",
            "Certified Digital Forensics Examiner (CDFE) from IACRB",
        ],
        "tags": ["cyber-forensics", "digital-investigation", "cybercrime", "chfi", "cert-in"],
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
