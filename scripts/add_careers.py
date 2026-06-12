import json

with open('c:/Narin_Workspace/loka-bandhuv/backend/data/careers.json') as f:
    careers = json.load(f)

new_careers = [
  # ── TRADES & CONSTRUCTION ──
  {
    "id": "electrician",
    "title": "Electrician",
    "category": "Trades & Construction",
    "description": "Install, maintain, and repair electrical systems in homes, buildings, and factories. Read blueprints, work with circuit breakers and wiring, and ensure electrical safety. One of the most in-demand trades across India.",
    "salary_range": {"min": 8000, "max": 50000, "currency": "INR/month", "note": "Apprentice to Master Electrician"},
    "growth_outlook": "Very High",
    "work_style": ["Hands-on", "On-site", "Problem-solving"],
    "required_skills": [
      {"skill": "Electrical Wiring", "level": "critical"},
      {"skill": "Circuit Diagrams", "level": "critical"},
      {"skill": "Safety Practices", "level": "critical"},
      {"skill": "Hand Tools", "level": "important"},
      {"skill": "Troubleshooting", "level": "important"},
      {"skill": "Mathematics", "level": "important"},
      {"skill": "Blueprint Reading", "level": "helpful"}
    ],
    "entry_paths": ["ITI Electrician trade", "Apprenticeship under master electrician", "Polytechnic diploma in Electrical"],
    "tags": ["trade", "blue-collar", "in-demand", "hands-on"]
  },
  {
    "id": "plumber",
    "title": "Plumber",
    "category": "Trades & Construction",
    "description": "Install and repair water supply systems, drainage pipes, and sanitation equipment. Plumbers work independently or with construction teams and can eventually run their own business.",
    "salary_range": {"min": 7000, "max": 40000, "currency": "INR/month", "note": "Apprentice to Senior"},
    "growth_outlook": "High",
    "work_style": ["Hands-on", "On-site", "Independent"],
    "required_skills": [
      {"skill": "Pipe Fitting", "level": "critical"},
      {"skill": "Hand Tools", "level": "critical"},
      {"skill": "Safety Practices", "level": "critical"},
      {"skill": "Problem Solving", "level": "important"},
      {"skill": "Mathematics", "level": "important"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["ITI Plumber trade", "Apprenticeship", "On-the-job training"],
    "tags": ["trade", "blue-collar", "in-demand", "self-employment"]
  },
  {
    "id": "carpenter",
    "title": "Carpenter / Furniture Maker",
    "category": "Trades & Construction",
    "description": "Craft, install, and repair wooden structures, furniture, doors, and cabinets. Skilled carpenters are in demand for home interiors, construction sites, and custom furniture workshops.",
    "salary_range": {"min": 8000, "max": 45000, "currency": "INR/month", "note": "Helper to Master Carpenter"},
    "growth_outlook": "High",
    "work_style": ["Hands-on", "Creative", "On-site"],
    "required_skills": [
      {"skill": "Wood Working", "level": "critical"},
      {"skill": "Hand Tools", "level": "critical"},
      {"skill": "Measuring & Marking", "level": "critical"},
      {"skill": "Blueprint Reading", "level": "important"},
      {"skill": "Finishing & Polishing", "level": "important"},
      {"skill": "Mathematics", "level": "important"},
      {"skill": "Design Sense", "level": "helpful"}
    ],
    "entry_paths": ["ITI Carpentry trade", "Apprenticeship with furniture maker", "Vocational training centre"],
    "tags": ["trade", "craft", "hands-on", "self-employment"]
  },
  {
    "id": "auto_mechanic",
    "title": "Auto Mechanic / Car Technician",
    "category": "Trades & Construction",
    "description": "Diagnose, repair, and service cars, two-wheelers, and trucks. Work in garages, service centres, and dealerships. With EV adoption growing in India, EV-trained mechanics are in very high demand.",
    "salary_range": {"min": 8000, "max": 50000, "currency": "INR/month", "note": "Helper to Senior Technician"},
    "growth_outlook": "Very High",
    "work_style": ["Hands-on", "Technical", "Team-based"],
    "required_skills": [
      {"skill": "Engine Repair", "level": "critical"},
      {"skill": "Diagnostics", "level": "critical"},
      {"skill": "Hand Tools", "level": "critical"},
      {"skill": "Electrical Systems", "level": "important"},
      {"skill": "Troubleshooting", "level": "important"},
      {"skill": "Mathematics", "level": "helpful"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["ITI Motor Mechanic Vehicle", "Diploma in Automobile Engineering", "Apprenticeship at dealership"],
    "tags": ["trade", "automotive", "hands-on", "ev-opportunity"]
  },
  {
    "id": "welder",
    "title": "Welder / Fabricator",
    "category": "Trades & Construction",
    "description": "Join and cut metals to build structures, machinery, pipelines, and vehicles. Essential in construction, shipbuilding, manufacturing, and infrastructure. Skilled welders are always in demand globally.",
    "salary_range": {"min": 9000, "max": 45000, "currency": "INR/month", "note": "Helper to Certified Welder"},
    "growth_outlook": "High",
    "work_style": ["Hands-on", "Physical", "Precise"],
    "required_skills": [
      {"skill": "Welding Techniques", "level": "critical"},
      {"skill": "Safety Practices", "level": "critical"},
      {"skill": "Metal Fabrication", "level": "critical"},
      {"skill": "Blueprint Reading", "level": "important"},
      {"skill": "Hand Tools", "level": "important"},
      {"skill": "Mathematics", "level": "helpful"}
    ],
    "entry_paths": ["ITI Welder trade", "NSDC Welding certification", "Apprenticeship in factory"],
    "tags": ["trade", "manufacturing", "hands-on", "global-demand"]
  },
  {
    "id": "civil_engineer",
    "title": "Civil Engineer / Site Engineer",
    "category": "Trades & Construction",
    "description": "Design and oversee construction of roads, bridges, buildings, dams, and infrastructure. India's massive infrastructure push under PM GatiShakti creates enormous demand for civil engineers at all levels.",
    "salary_range": {"min": 20000, "max": 150000, "currency": "INR/month", "note": "Junior Engineer to Project Director"},
    "growth_outlook": "Very High",
    "work_style": ["Field + office", "Technical", "Project-based"],
    "required_skills": [
      {"skill": "Structural Design", "level": "critical"},
      {"skill": "AutoCAD", "level": "critical"},
      {"skill": "Mathematics", "level": "critical"},
      {"skill": "Site Management", "level": "important"},
      {"skill": "Blueprint Reading", "level": "important"},
      {"skill": "Project Management", "level": "important"},
      {"skill": "Soil Testing", "level": "helpful"}
    ],
    "entry_paths": ["B.E./B.Tech in Civil Engineering", "Diploma in Civil Engineering", "Government PWD / CPWD recruitment"],
    "tags": ["engineering", "infrastructure", "government", "growing"]
  },
  # ── HEALTHCARE ──
  {
    "id": "nurse",
    "title": "Nurse / Nursing Professional",
    "category": "Healthcare",
    "description": "Provide patient care, administer medicines, assist doctors, and support recovery. Work in hospitals, clinics, homes, and schools. Nursing offers strong job security with global opportunities in the UK, Canada, Middle East, and Australia.",
    "salary_range": {"min": 15000, "max": 80000, "currency": "INR/month", "note": "Staff Nurse to Senior Nurse"},
    "growth_outlook": "Very High",
    "work_style": ["Patient-facing", "Team-based", "Shift-based"],
    "required_skills": [
      {"skill": "Patient Care", "level": "critical"},
      {"skill": "Medical Knowledge", "level": "critical"},
      {"skill": "First Aid & CPR", "level": "critical"},
      {"skill": "Medication Administration", "level": "critical"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Empathy", "level": "important"},
      {"skill": "Record Keeping", "level": "important"}
    ],
    "entry_paths": ["GNM (General Nursing & Midwifery)", "B.Sc Nursing", "ANM (Auxiliary Nurse Midwife)"],
    "tags": ["healthcare", "stable", "global-opportunity", "essential"]
  },
  {
    "id": "anaesthesiologist",
    "title": "Anaesthesiologist",
    "category": "Healthcare",
    "description": "Administer anaesthesia before surgery, monitor patients during operations, and manage pain and critical care. One of the highest paid medical specialisations in India. Anaesthesiologists are always in short supply.",
    "salary_range": {"min": 100000, "max": 500000, "currency": "INR/month", "note": "Senior Resident to Consultant"},
    "growth_outlook": "Very High",
    "work_style": ["High-pressure", "Precise", "Hospital-based"],
    "required_skills": [
      {"skill": "Medical Knowledge", "level": "critical"},
      {"skill": "Pharmacology", "level": "critical"},
      {"skill": "Patient Monitoring", "level": "critical"},
      {"skill": "Emergency Response", "level": "critical"},
      {"skill": "Attention to Detail", "level": "critical"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Critical Care", "level": "important"}
    ],
    "entry_paths": ["MBBS + MD in Anaesthesiology", "DNB Anaesthesiology", "Senior residency in teaching hospital"],
    "tags": ["healthcare", "specialist", "highest-paid", "critical-care"]
  },
  {
    "id": "pharmacist",
    "title": "Pharmacist",
    "category": "Healthcare",
    "description": "Dispense medicines, counsel patients on drug use, and ensure safe medication. Work in hospitals, retail pharmacies, and the pharmaceutical industry. Growing demand with expanding healthcare access across India.",
    "salary_range": {"min": 18000, "max": 70000, "currency": "INR/month", "note": "Entry to Senior Pharmacist"},
    "growth_outlook": "High",
    "work_style": ["Detail-oriented", "Patient-facing", "Regulatory"],
    "required_skills": [
      {"skill": "Pharmacology", "level": "critical"},
      {"skill": "Medical Knowledge", "level": "critical"},
      {"skill": "Attention to Detail", "level": "critical"},
      {"skill": "Inventory Management", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["D.Pharm (Diploma in Pharmacy)", "B.Pharm degree", "M.Pharm for specialisation"],
    "tags": ["healthcare", "stable", "pharmacy", "science"]
  },
  {
    "id": "physiotherapist",
    "title": "Physiotherapist",
    "category": "Healthcare",
    "description": "Help patients recover from injuries, surgeries, and chronic conditions through physical therapy. Work in hospitals, sports clubs, and run independent clinics. Great scope in sports physiotherapy as India grows in athletics.",
    "salary_range": {"min": 18000, "max": 80000, "currency": "INR/month", "note": "Junior to Senior PT"},
    "growth_outlook": "High",
    "work_style": ["Hands-on", "Patient-facing", "Empathetic"],
    "required_skills": [
      {"skill": "Human Anatomy", "level": "critical"},
      {"skill": "Exercise Therapy", "level": "critical"},
      {"skill": "Patient Care", "level": "critical"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Empathy", "level": "important"},
      {"skill": "Assessment Skills", "level": "important"}
    ],
    "entry_paths": ["BPT (Bachelor of Physiotherapy)", "MPT for specialisation", "Internship in hospital"],
    "tags": ["healthcare", "wellness", "hands-on", "growing"]
  },
  {
    "id": "ayurvedic_doctor",
    "title": "Ayurvedic Doctor (BAMS)",
    "category": "Healthcare",
    "description": "Practice traditional Indian medicine to treat diseases holistically through herbs, diet, yoga, and panchakarma. Government hospitals, private clinics, wellness resorts, and the global wellness industry all need BAMS graduates.",
    "salary_range": {"min": 20000, "max": 120000, "currency": "INR/month", "note": "Junior Doctor to Specialist"},
    "growth_outlook": "Very High",
    "work_style": ["Patient-facing", "Holistic", "Consultative"],
    "required_skills": [
      {"skill": "Medical Knowledge", "level": "critical"},
      {"skill": "Ayurvedic Principles", "level": "critical"},
      {"skill": "Patient Care", "level": "critical"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Herbal Medicine", "level": "important"},
      {"skill": "Yoga & Wellness", "level": "helpful"}
    ],
    "entry_paths": ["BAMS (Bachelor of Ayurvedic Medicine & Surgery)", "MD Ayurveda for specialisation", "Government AYUSH hospital posting"],
    "tags": ["healthcare", "ayurveda", "india-heritage", "growing"]
  },
  # ── FOOD & HOSPITALITY ──
  {
    "id": "chef",
    "title": "Chef / Cook",
    "category": "Food & Hospitality",
    "description": "Prepare, cook, and present food in restaurants, hotels, canteens, and cloud kitchens. From street food stalls to five-star hotels — chefs are needed everywhere. India's food delivery boom with Zomato and Swiggy created thousands of new kitchen jobs.",
    "salary_range": {"min": 8000, "max": 80000, "currency": "INR/month", "note": "Cook Helper to Executive Chef"},
    "growth_outlook": "Very High",
    "work_style": ["Creative", "Fast-paced", "Team-based"],
    "required_skills": [
      {"skill": "Cooking Techniques", "level": "critical"},
      {"skill": "Food Safety & Hygiene", "level": "critical"},
      {"skill": "Knife Skills", "level": "important"},
      {"skill": "Recipe Development", "level": "important"},
      {"skill": "Time Management", "level": "important"},
      {"skill": "Teamwork", "level": "important"},
      {"skill": "Baking", "level": "helpful"},
      {"skill": "Menu Planning", "level": "helpful"}
    ],
    "entry_paths": ["Hotel Management course", "IHM (Institute of Hotel Management)", "On-the-job training", "YouTube & self-practice"],
    "tags": ["food", "hospitality", "creative", "growing"]
  },
  {
    "id": "hotel_manager",
    "title": "Hotel & Hospitality Manager",
    "category": "Food & Hospitality",
    "description": "Oversee operations of hotels, resorts, guest houses, or restaurants. Manage staff, bookings, guest experience, and revenue. India's tourism boom makes hospitality management one of the fastest growing careers.",
    "salary_range": {"min": 20000, "max": 120000, "currency": "INR/month", "note": "Trainee to General Manager"},
    "growth_outlook": "High",
    "work_style": ["People-facing", "Leadership", "Fast-paced"],
    "required_skills": [
      {"skill": "Customer Service", "level": "critical"},
      {"skill": "Team Management", "level": "critical"},
      {"skill": "Communication", "level": "critical"},
      {"skill": "Problem Solving", "level": "important"},
      {"skill": "Financial Management", "level": "important"},
      {"skill": "MS Office", "level": "important"},
      {"skill": "Languages", "level": "helpful"}
    ],
    "entry_paths": ["BHM (Bachelor of Hotel Management)", "Diploma in Hotel Management", "Start in front desk and grow up"],
    "tags": ["hospitality", "tourism", "management", "people-facing"]
  },
  {
    "id": "baker",
    "title": "Baker / Pastry Chef",
    "category": "Food & Hospitality",
    "description": "Create breads, cakes, pastries, and confections for bakeries, restaurants, and home-based businesses. Home baking businesses have exploded in India — many bakers earn well running their own kitchen startup.",
    "salary_range": {"min": 8000, "max": 60000, "currency": "INR/month", "note": "Baker to Head Pastry Chef"},
    "growth_outlook": "High",
    "work_style": ["Creative", "Early hours", "Self-employment possible"],
    "required_skills": [
      {"skill": "Baking", "level": "critical"},
      {"skill": "Food Safety & Hygiene", "level": "critical"},
      {"skill": "Recipe Development", "level": "important"},
      {"skill": "Decoration & Presentation", "level": "important"},
      {"skill": "Time Management", "level": "important"},
      {"skill": "Inventory Management", "level": "helpful"}
    ],
    "entry_paths": ["Bakery & Confectionery certificate", "IHM pastry module", "Online courses + home practice", "Apprenticeship in bakery"],
    "tags": ["food", "creative", "self-employment", "growing"]
  },
  # ── BEAUTY & WELLNESS ──
  {
    "id": "hair_stylist",
    "title": "Hair Stylist / Beautician",
    "category": "Beauty & Wellness",
    "description": "Provide hair cutting, styling, colouring, makeup, and beauty treatments. Salons are everywhere in India — this career offers fast self-employment and good income. Celebrity stylists and bridal makeup artists earn very well.",
    "salary_range": {"min": 8000, "max": 80000, "currency": "INR/month", "note": "Trainee to Salon Owner / Celebrity Stylist"},
    "growth_outlook": "High",
    "work_style": ["Creative", "People-facing", "Self-employment possible"],
    "required_skills": [
      {"skill": "Hair Styling", "level": "critical"},
      {"skill": "Hair Cutting", "level": "critical"},
      {"skill": "Customer Service", "level": "critical"},
      {"skill": "Makeup", "level": "important"},
      {"skill": "Skin Care", "level": "important"},
      {"skill": "Colour Theory", "level": "important"},
      {"skill": "Communication", "level": "helpful"}
    ],
    "entry_paths": ["VLCC / Lakme Academy diploma", "NSDC Beauty & Wellness certificate", "Apprenticeship at salon", "NIOS Beauty & Wellness course"],
    "tags": ["beauty", "self-employment", "people-facing", "creative"]
  },
  {
    "id": "fitness_trainer",
    "title": "Fitness Trainer / Personal Trainer",
    "category": "Beauty & Wellness",
    "description": "Help clients achieve fitness goals through workout plans, nutrition guidance, and motivation. Work in gyms, corporate wellness programmes, or independently. Growing market in urban India with fitness culture booming.",
    "salary_range": {"min": 12000, "max": 80000, "currency": "INR/month", "note": "Gym Trainer to Celebrity Coach"},
    "growth_outlook": "Very High",
    "work_style": ["Active", "People-facing", "Flexible hours"],
    "required_skills": [
      {"skill": "Exercise Science", "level": "critical"},
      {"skill": "Nutrition Basics", "level": "critical"},
      {"skill": "Coaching", "level": "critical"},
      {"skill": "First Aid & CPR", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Motivation & Psychology", "level": "important"},
      {"skill": "Social Media", "level": "helpful"}
    ],
    "entry_paths": ["CPT certification (ACE/ISSA/Reebok)", "Diploma in Sports Science", "B.P.Ed degree", "Start at local gym"],
    "tags": ["fitness", "wellness", "active", "growing"]
  },
  {
    "id": "yoga_instructor",
    "title": "Yoga Instructor",
    "category": "Beauty & Wellness",
    "description": "Teach yoga postures, breathing, and meditation to students of all levels. Work in studios, gyms, schools, corporates, and online. India is the birthplace of yoga — strong global demand with excellent export opportunities.",
    "salary_range": {"min": 10000, "max": 70000, "currency": "INR/month", "note": "Local Instructor to International Teacher"},
    "growth_outlook": "High",
    "work_style": ["Flexible", "Mindful", "Global-friendly"],
    "required_skills": [
      {"skill": "Yoga Practice", "level": "critical"},
      {"skill": "Teaching & Instruction", "level": "critical"},
      {"skill": "Anatomy Basics", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Meditation", "level": "important"},
      {"skill": "Online Teaching", "level": "helpful"},
      {"skill": "Sanskrit Basics", "level": "helpful"}
    ],
    "entry_paths": ["200-Hour Yoga Teacher Training (YTT)", "Morarji Desai National Institute of Yoga", "Kaivalyadhama / Bihar School of Yoga"],
    "tags": ["wellness", "yoga", "global-demand", "india-strength"]
  },
  # ── FASHION & APPAREL ──
  {
    "id": "fashion_designer",
    "title": "Fashion Designer",
    "category": "Fashion & Apparel",
    "description": "Design clothes, accessories, and textiles for brands, boutiques, or private clients. India is one of the world's largest textile and fashion markets. From bridal wear to streetwear — opportunities are everywhere.",
    "salary_range": {"min": 12000, "max": 100000, "currency": "INR/month", "note": "Trainee to Senior Designer"},
    "growth_outlook": "High",
    "work_style": ["Creative", "Portfolio-based", "Trend-aware"],
    "required_skills": [
      {"skill": "Fashion Illustration", "level": "critical"},
      {"skill": "Sewing & Stitching", "level": "critical"},
      {"skill": "Fabric Knowledge", "level": "critical"},
      {"skill": "Pattern Making", "level": "important"},
      {"skill": "Colour Theory", "level": "important"},
      {"skill": "Trend Research", "level": "important"},
      {"skill": "Adobe Illustrator", "level": "helpful"}
    ],
    "entry_paths": ["NIFT (National Institute of Fashion Technology)", "Pearl Academy", "Diploma in Fashion Design"],
    "tags": ["fashion", "creative", "design", "india-strength"]
  },
  {
    "id": "tailor",
    "title": "Tailor / Garment Stitcher",
    "category": "Fashion & Apparel",
    "description": "Stitch, alter, and repair clothing for customers or garment factories. India's wedding and festive wear market keeps skilled tailors constantly busy. Master tailors with design skills run thriving boutiques.",
    "salary_range": {"min": 7000, "max": 50000, "currency": "INR/month", "note": "Apprentice to Master Tailor"},
    "growth_outlook": "Stable",
    "work_style": ["Hands-on", "Detail-oriented", "Self-employment possible"],
    "required_skills": [
      {"skill": "Sewing & Stitching", "level": "critical"},
      {"skill": "Measuring & Marking", "level": "critical"},
      {"skill": "Fabric Knowledge", "level": "critical"},
      {"skill": "Pattern Making", "level": "important"},
      {"skill": "Alteration Techniques", "level": "important"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["ITI Dress Making trade", "NSDC Tailoring course", "Apprenticeship at tailoring shop"],
    "tags": ["apparel", "craft", "self-employment", "india-market"]
  },
  # ── TRANSPORT & LOGISTICS ──
  {
    "id": "commercial_driver",
    "title": "Commercial Driver / Transport Operator",
    "category": "Transport & Logistics",
    "description": "Drive trucks, buses, taxis, or auto-rickshaws. With Ola, Uber, and Rapido, self-employed driving careers have boomed. Long-haul truck drivers are in very high demand with India's expanding highway network.",
    "salary_range": {"min": 12000, "max": 50000, "currency": "INR/month", "note": "Auto/Taxi Driver to Long-Haul Trucker"},
    "growth_outlook": "High",
    "work_style": ["Independent", "Flexible", "Physical"],
    "required_skills": [
      {"skill": "Driving", "level": "critical"},
      {"skill": "Traffic Rules & Safety", "level": "critical"},
      {"skill": "Route Navigation", "level": "critical"},
      {"skill": "Vehicle Maintenance Basics", "level": "important"},
      {"skill": "Time Management", "level": "important"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["Heavy Motor Vehicle (HMV) license", "Light Motor Vehicle (LMV) license", "Register on Ola/Uber/Rapido"],
    "tags": ["transport", "self-employment", "gig-economy", "flexible"]
  },
  {
    "id": "logistics_manager",
    "title": "Logistics & Warehouse Manager",
    "category": "Transport & Logistics",
    "description": "Manage movement, storage, and delivery of goods. India's e-commerce boom — Amazon, Flipkart, Meesho, Blinkit — has created massive demand for logistics professionals at all levels from warehouse to fleet manager.",
    "salary_range": {"min": 15000, "max": 80000, "currency": "INR/month", "note": "Coordinator to Operations Manager"},
    "growth_outlook": "Very High",
    "work_style": ["Systematic", "Team-based", "Fast-paced"],
    "required_skills": [
      {"skill": "Inventory Management", "level": "critical"},
      {"skill": "Logistics Planning", "level": "critical"},
      {"skill": "MS Excel", "level": "important"},
      {"skill": "ERP Software", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Team Management", "level": "helpful"},
      {"skill": "Problem Solving", "level": "important"}
    ],
    "entry_paths": ["Diploma in Logistics & Supply Chain", "B.Com + logistics experience", "Start in warehouse and grow up"],
    "tags": ["logistics", "ecommerce", "growing", "stable"]
  },
  # ── AGRICULTURE & FARMING ──
  {
    "id": "progressive_farmer",
    "title": "Progressive Farmer / Agripreneur",
    "category": "Agriculture & Farming",
    "description": "Grow crops and run agri-businesses using modern techniques like organic farming, hydroponics, and direct-to-consumer models. Young farmers using technology and government schemes earn very well and are transforming Indian agriculture.",
    "salary_range": {"min": 10000, "max": 100000, "currency": "INR/month", "note": "Subsistence to Agripreneur"},
    "growth_outlook": "Growing",
    "work_style": ["Outdoor", "Seasonal", "Self-employed"],
    "required_skills": [
      {"skill": "Crop Knowledge", "level": "critical"},
      {"skill": "Soil Management", "level": "critical"},
      {"skill": "Irrigation Techniques", "level": "important"},
      {"skill": "Pest Control", "level": "important"},
      {"skill": "Financial Planning", "level": "important"},
      {"skill": "Marketing", "level": "helpful"},
      {"skill": "Technology Adoption", "level": "helpful"}
    ],
    "entry_paths": ["B.Sc Agriculture", "Krishi Vigyan Kendra (KVK) training", "ATMA scheme training", "Government PM-KISAN scheme"],
    "tags": ["agriculture", "outdoor", "self-employment", "india-core"]
  },
  {
    "id": "agricultural_officer",
    "title": "Agriculture Extension Officer (Govt)",
    "category": "Agriculture & Farming",
    "description": "Bridge between agricultural research and farmers. Advise on modern techniques, government schemes, and market access. Stable government jobs available at block, district, state, and central level with IBPS Agri Officer exam.",
    "salary_range": {"min": 25000, "max": 80000, "currency": "INR/month", "note": "Officer to Senior Officer (Grade Scale I-III)"},
    "growth_outlook": "Stable",
    "work_style": ["Field-based", "Advisory", "Government"],
    "required_skills": [
      {"skill": "Crop Knowledge", "level": "critical"},
      {"skill": "Communication", "level": "critical"},
      {"skill": "Regional Language", "level": "critical"},
      {"skill": "Soil Management", "level": "important"},
      {"skill": "Government Schemes Knowledge", "level": "important"},
      {"skill": "Data Collection", "level": "important"},
      {"skill": "Report Writing", "level": "helpful"}
    ],
    "entry_paths": ["B.Sc Agriculture", "IBPS Agri Officer exam", "State agricultural department exam", "NABARD development assistant"],
    "tags": ["agriculture", "government", "advisory", "stable"]
  },
  # ── ARTS & PERFORMANCE ──
  {
    "id": "photographer",
    "title": "Photographer / Videographer",
    "category": "Arts & Performance",
    "description": "Capture photos and videos for weddings, events, fashion, journalism, and brands. India's massive wedding market and growing content economy make photography very profitable. Top wedding photographers charge lakhs per event.",
    "salary_range": {"min": 15000, "max": 200000, "currency": "INR/month", "note": "Assistant to Premium Photographer"},
    "growth_outlook": "High",
    "work_style": ["Creative", "Freelance-friendly", "Portfolio-based"],
    "required_skills": [
      {"skill": "Photography", "level": "critical"},
      {"skill": "Photo Editing", "level": "critical"},
      {"skill": "Lighting Techniques", "level": "critical"},
      {"skill": "Composition", "level": "important"},
      {"skill": "Video Editing", "level": "important"},
      {"skill": "Client Management", "level": "important"},
      {"skill": "Social Media", "level": "helpful"}
    ],
    "entry_paths": ["Photography courses (online + offline)", "Assistant to experienced photographer", "Start with events and build portfolio"],
    "tags": ["arts", "creative", "freelance", "events"]
  },
  {
    "id": "musician",
    "title": "Musician / Performer",
    "category": "Arts & Performance",
    "description": "Perform, compose, or teach music across classical, film, fusion, or contemporary genres. India's music industry — Bollywood, classical, indie — offers careers in live performance, background scoring, YouTube, and teaching.",
    "salary_range": {"min": 10000, "max": 200000, "currency": "INR/month", "note": "Music Teacher to Film Composer"},
    "growth_outlook": "Moderate",
    "work_style": ["Creative", "Freelance", "Passion-driven"],
    "required_skills": [
      {"skill": "Musical Instrument", "level": "critical"},
      {"skill": "Music Theory", "level": "critical"},
      {"skill": "Ear Training", "level": "important"},
      {"skill": "Stage Performance", "level": "important"},
      {"skill": "Music Production", "level": "helpful"},
      {"skill": "Teaching", "level": "helpful"}
    ],
    "entry_paths": ["Music school / Gurukul", "B.A. in Music", "Self-learning + YouTube", "Bollywood assistant gigs"],
    "tags": ["arts", "music", "creative", "passion"]
  },
  {
    "id": "actor",
    "title": "Actor / Theatre Artist",
    "category": "Arts & Performance",
    "description": "Perform in films, TV serials, OTT platforms, theatre, and advertisements. India has one of the world's largest entertainment industries — Bollywood, regional cinema, and OTT are all creating more roles than ever before.",
    "salary_range": {"min": 5000, "max": 500000, "currency": "INR/month", "note": "Background Actor to Lead"},
    "growth_outlook": "High",
    "work_style": ["Performance", "Audition-based", "Unpredictable hours"],
    "required_skills": [
      {"skill": "Acting Techniques", "level": "critical"},
      {"skill": "Stage Performance", "level": "critical"},
      {"skill": "Voice & Diction", "level": "critical"},
      {"skill": "Improvisation", "level": "important"},
      {"skill": "Script Reading", "level": "important"},
      {"skill": "Dancing", "level": "helpful"},
      {"skill": "Physical Fitness", "level": "helpful"}
    ],
    "entry_paths": ["FTII (Film & Television Institute of India)", "NSD (National School of Drama)", "Theatre groups + auditions", "Acting workshops"],
    "tags": ["entertainment", "film", "performance", "bollywood"]
  },
  # ── GOVERNMENT & PUBLIC SERVICE ──
  {
    "id": "civil_servant_ias",
    "title": "Civil Servant — IAS / IPS / IFS",
    "category": "Government & Public Service",
    "description": "Serve the nation through administrative, police, or foreign service. IAS officers run districts and departments, IPS officers lead police forces, IFS officers represent India abroad. The most prestigious career in India with full state benefits.",
    "salary_range": {"min": 56100, "max": 250000, "currency": "INR/month", "note": "Probationer to Cabinet Secretary level"},
    "growth_outlook": "Stable",
    "work_style": ["Administrative", "Leadership", "Field + office"],
    "required_skills": [
      {"skill": "General Knowledge", "level": "critical"},
      {"skill": "Essay Writing", "level": "critical"},
      {"skill": "Analytical Thinking", "level": "critical"},
      {"skill": "Ethics & Integrity", "level": "critical"},
      {"skill": "Decision Making", "level": "important"},
      {"skill": "Leadership", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Report Writing", "level": "helpful"}
    ],
    "entry_paths": ["UPSC Civil Services Exam (CSE)", "State PCS exam", "2–3 years dedicated preparation + coaching"],
    "tags": ["government", "upsc", "prestigious", "india-specific"]
  },
  {
    "id": "bank_officer",
    "title": "Bank Officer / Probationary Officer",
    "category": "Government & Public Service",
    "description": "Manage banking operations, customer accounts, loans, and financial products at public sector banks (SBI, PNB, Bank of Baroda). IBPS PO and SBI PO are among India's most sought-after government job exams with lakhs of applicants each year.",
    "salary_range": {"min": 23700, "max": 85000, "currency": "INR/month", "note": "PO to General Manager"},
    "growth_outlook": "Stable",
    "work_style": ["Customer-facing", "Regulated", "Office-based"],
    "required_skills": [
      {"skill": "Banking & Finance", "level": "critical"},
      {"skill": "Mathematics", "level": "critical"},
      {"skill": "General Knowledge", "level": "important"},
      {"skill": "English Communication", "level": "important"},
      {"skill": "Reasoning & Aptitude", "level": "critical"},
      {"skill": "Computer Basics", "level": "important"},
      {"skill": "Customer Service", "level": "helpful"}
    ],
    "entry_paths": ["IBPS PO exam", "SBI PO exam", "RBI Grade B exam", "B.Com / B.A. graduation required"],
    "tags": ["government", "banking", "stable", "pension"]
  },
  {
    "id": "police_officer",
    "title": "Police Officer / Sub-Inspector",
    "category": "Government & Public Service",
    "description": "Maintain law and order, investigate crimes, and protect citizens. Entry as constable through state police recruitment, or Sub-Inspector/DSP through state PSC exams. Stable government career with pension and social respect.",
    "salary_range": {"min": 21000, "max": 100000, "currency": "INR/month", "note": "Constable to Superintendent"},
    "growth_outlook": "Stable",
    "work_style": ["Field-based", "Disciplined", "Shift-based"],
    "required_skills": [
      {"skill": "Physical Fitness", "level": "critical"},
      {"skill": "General Knowledge", "level": "critical"},
      {"skill": "Regional Language", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "Decision Making", "level": "important"},
      {"skill": "Teamwork", "level": "important"},
      {"skill": "Legal Knowledge", "level": "helpful"}
    ],
    "entry_paths": ["State Police Constable Recruitment", "Sub-Inspector exam", "UPSC CAPF for central forces", "Physical + written + medical tests"],
    "tags": ["government", "law-enforcement", "stable", "public-service"]
  },
  {
    "id": "railway_officer",
    "title": "Railway Officer / RRB Employee",
    "category": "Government & Public Service",
    "description": "Work with Indian Railways — one of the world's largest employers. From station master and loco pilot to Group A gazetted officers through UPSC IRPS. Indian Railways offers enormous variety in roles, good salaries, and housing.",
    "salary_range": {"min": 19900, "max": 180000, "currency": "INR/month", "note": "Group D to IRPS Officer"},
    "growth_outlook": "Stable",
    "work_style": ["Shift-based", "Operational", "Government"],
    "required_skills": [
      {"skill": "General Knowledge", "level": "critical"},
      {"skill": "Mathematics", "level": "critical"},
      {"skill": "Reasoning & Aptitude", "level": "critical"},
      {"skill": "Computer Basics", "level": "important"},
      {"skill": "Technical Knowledge", "level": "important"},
      {"skill": "Physical Fitness", "level": "helpful"}
    ],
    "entry_paths": ["RRB NTPC exam", "RRB Group D exam", "RRB JE (Junior Engineer) exam", "UPSC for gazetted railway officers"],
    "tags": ["government", "railway", "stable", "pension"]
  },
  # ── RETAIL & COMMERCE ──
  {
    "id": "retail_manager",
    "title": "Retail Store Manager",
    "category": "Retail & Commerce",
    "description": "Manage staff, inventory, store presentation, and customer experience. Retail is India's second largest employer. With organised retail and quick commerce booming, store managers at good chains earn very well.",
    "salary_range": {"min": 18000, "max": 80000, "currency": "INR/month", "note": "Sales Executive to Store Manager"},
    "growth_outlook": "High",
    "work_style": ["People-facing", "Fast-paced", "Target-driven"],
    "required_skills": [
      {"skill": "Customer Service", "level": "critical"},
      {"skill": "Team Management", "level": "critical"},
      {"skill": "Sales", "level": "critical"},
      {"skill": "Inventory Management", "level": "important"},
      {"skill": "Communication", "level": "important"},
      {"skill": "MS Excel", "level": "important"},
      {"skill": "Problem Solving", "level": "helpful"}
    ],
    "entry_paths": ["Start as sales associate", "Retail management diploma", "Grow within D-Mart/Reliance/Big Bazaar chain"],
    "tags": ["retail", "management", "people-facing", "growing"]
  },
  # ── SOCIAL WORK ──
  {
    "id": "social_worker",
    "title": "Social Worker / NGO Professional",
    "category": "Social Work & Community",
    "description": "Work with communities, NGOs, and government bodies to address education, poverty, health, and women's empowerment. The sector is professionalising rapidly with international funding and growing FCRA-registered NGOs in India.",
    "salary_range": {"min": 12000, "max": 70000, "currency": "INR/month", "note": "Field Worker to Programme Manager"},
    "growth_outlook": "Growing",
    "work_style": ["Field-based", "Community-focused", "Purpose-driven"],
    "required_skills": [
      {"skill": "Communication", "level": "critical"},
      {"skill": "Empathy", "level": "critical"},
      {"skill": "Community Outreach", "level": "critical"},
      {"skill": "Regional Language", "level": "important"},
      {"skill": "Project Management", "level": "important"},
      {"skill": "Report Writing", "level": "important"},
      {"skill": "Data Collection", "level": "helpful"}
    ],
    "entry_paths": ["BSW/MSW (Bachelor/Master of Social Work)", "TISS (Tata Institute of Social Sciences)", "Join local NGO as volunteer first"],
    "tags": ["ngo", "social-impact", "community", "purpose-driven"]
  },
  # ── MEDIA & JOURNALISM ──
  {
    "id": "journalist",
    "title": "Journalist / Reporter",
    "category": "Media & Journalism",
    "description": "Research, investigate, and report news for print, digital, TV, or radio. India's massive media market — national TV channels, regional digital outlets, fact-checking sites — creates diverse opportunities. Investigative journalists drive real change.",
    "salary_range": {"min": 15000, "max": 100000, "currency": "INR/month", "note": "Junior Reporter to Senior Correspondent"},
    "growth_outlook": "Changing",
    "work_style": ["Fast-paced", "Deadline-driven", "Field + desk"],
    "required_skills": [
      {"skill": "Writing & Reporting", "level": "critical"},
      {"skill": "Research", "level": "critical"},
      {"skill": "News Sense", "level": "critical"},
      {"skill": "Interview Skills", "level": "important"},
      {"skill": "Communication", "level": "critical"},
      {"skill": "Social Media", "level": "important"},
      {"skill": "Video Shooting", "level": "helpful"}
    ],
    "entry_paths": ["BA/MA in Journalism (IIMC, AJK MCRC)", "Internship at news outlet", "Start a blog or YouTube channel", "Regional news agencies"],
    "tags": ["media", "writing", "journalism", "storytelling"]
  }
]

# Add only careers not already present
existing_ids = {c['id'] for c in careers}
added = 0
for c in new_careers:
    if c['id'] not in existing_ids:
        careers.append(c)
        added += 1

with open('c:/Narin_Workspace/loka-bandhuv/backend/data/careers.json', 'w') as f:
    json.dump(careers, f, indent=2, ensure_ascii=False)

print(f'Added {added} new careers. Total: {len(careers)}')
cats = {}
for c in careers:
    cats[c['category']] = cats.get(c['category'], 0) + 1
for cat, n in sorted(cats.items()):
    print(f'  {cat}: {n}')
