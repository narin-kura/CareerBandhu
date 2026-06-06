"""Add financial-sector careers for both India (IN) and USA (US)."""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"


def s(skill, level):
    return {"skill": skill, "level": level}


IN = [
    {
        "id": "chartered_accountant",
        "title": "Chartered Accountant (CA)",
        "category": "Finance",
        "description": "Handle audit, taxation, and financial advisory as a licensed CA — one of India's most respected and lucrative professional qualifications. CAs work in firms, corporates, or independent practice with strong earning potential.",
        "salary_range": {"min": 60000, "max": 400000, "currency": "INR/month", "note": "Fresher to senior/partner or own practice"},
        "growth_outlook": "Strong — evergreen demand",
        "work_style": ["Office", "Detail-oriented", "Seasonal peaks"],
        "required_skills": [s("Accounting", "critical"), s("Taxation", "critical"), s("Auditing", "critical"),
                            s("Financial Analysis", "important"), s("MS Excel", "important"),
                            s("Attention to Detail", "critical"), s("Integrity", "important")],
        "entry_paths": ["Register with ICAI after Class 12 (Foundation route)", "Clear CA Foundation, Intermediate, Final",
                        "3-year articleship training", "Membership with ICAI"],
        "tags": ["finance", "accounting", "CA", "professional", "high-pay"],
    },
    {
        "id": "investment_banker_in",
        "title": "Investment Banker",
        "category": "Finance",
        "description": "Advise companies on raising capital, mergers, and acquisitions. A high-pressure, high-reward career at the top of the financial sector, with excellent pay and exits into private equity and corporate finance.",
        "salary_range": {"min": 80000, "max": 700000, "currency": "INR/month", "note": "Analyst to VP/MD"},
        "growth_outlook": "Strong — premium finance career",
        "work_style": ["High-pressure", "Long hours", "Deal-driven"],
        "required_skills": [s("Financial Analysis", "critical"), s("Financial Modeling", "critical"),
                            s("MS Excel", "critical"), s("Valuation", "important"), s("Communication", "critical"),
                            s("Mathematics", "important"), s("Negotiation", "important")],
        "entry_paths": ["Bachelor's in Finance/Commerce/Economics", "MBA (Finance) from top B-school or CFA",
                        "Internships at banks/boutiques", "Analyst roles at investment banks"],
        "tags": ["finance", "investment-banking", "high-pay", "corporate"],
    },
    {
        "id": "company_secretary",
        "title": "Company Secretary (CS)",
        "category": "Finance",
        "description": "Ensure a company follows corporate laws and governance rules — the bridge between the board, shareholders, and regulators. A respected professional qualification with strong demand in corporates.",
        "salary_range": {"min": 40000, "max": 200000, "currency": "INR/month", "note": "Fresher to senior CS / Compliance Head"},
        "growth_outlook": "Stable — governance demand",
        "work_style": ["Office", "Compliance-focused", "Detail-oriented"],
        "required_skills": [s("Corporate Law", "critical"), s("Compliance", "critical"), s("Communication", "important"),
                            s("Attention to Detail", "critical"), s("Documentation", "important"), s("Integrity", "important")],
        "entry_paths": ["Register with ICSI (CSEET after Class 12)", "Clear CS Executive & Professional",
                        "Practical training", "Membership with ICSI"],
        "tags": ["finance", "compliance", "CS", "corporate-law", "professional"],
    },
    {
        "id": "stock_broker_in",
        "title": "Stock Broker / Equity Dealer",
        "category": "Finance",
        "description": "Buy and sell stocks and securities for clients and advise on investments. With India's surge in retail investing and demat accounts, dealers and advisors are in strong demand at brokerages and trading firms.",
        "salary_range": {"min": 25000, "max": 150000, "currency": "INR/month", "note": "Dealer to Senior Relationship Manager"},
        "growth_outlook": "Strong — retail investing boom",
        "work_style": ["Fast-paced", "Market hours", "Client-facing"],
        "required_skills": [s("Stock Market Knowledge", "critical"), s("Financial Analysis", "important"),
                            s("Communication", "critical"), s("Sales", "important"), s("Mathematics", "important"),
                            s("Decision Making", "important")],
        "entry_paths": ["Graduation (commerce preferred)", "NISM certifications (Equity/Derivatives)",
                        "Join a brokerage / trading firm", "Build client base & advisory skills"],
        "tags": ["finance", "stock-market", "trading", "sales"],
    },
    {
        "id": "bank_clerk_in",
        "title": "Bank Clerk (IBPS / SBI)",
        "category": "Finance",
        "description": "Handle customer transactions, accounts, and day-to-day branch operations at public-sector banks. A secure government-sector job with good benefits and a clear path to promotion into officer roles.",
        "salary_range": {"min": 25000, "max": 45000, "currency": "INR/month", "note": "Clerk + allowances, promotions to officer"},
        "growth_outlook": "Stable — secure banking job",
        "work_style": ["Office", "Customer-facing", "Structured"],
        "required_skills": [s("Computer Basics", "critical"), s("Customer Service", "critical"),
                            s("Mathematics", "important"), s("General Knowledge", "important"),
                            s("Communication", "important"), s("Attention to Detail", "important")],
        "entry_paths": ["Graduation (any discipline)", "IBPS Clerk / SBI Clerk exam (Prelims + Mains)",
                        "Language proficiency test", "Branch training"],
        "tags": ["finance", "banking", "government", "stable"],
    },
    {
        "id": "insurance_advisor_in",
        "title": "Insurance Advisor / Agent",
        "category": "Finance",
        "description": "Help individuals and families protect their future with life, health, and general insurance. A flexible, commission-driven career (LIC and private insurers) with no degree barrier and unlimited earning potential for good networkers.",
        "salary_range": {"min": 15000, "max": 150000, "currency": "INR/month", "note": "Commission-based; varies widely"},
        "growth_outlook": "Stable — large under-insured market",
        "work_style": ["Flexible", "Self-driven", "Client-facing"],
        "required_skills": [s("Sales", "critical"), s("Communication", "critical"), s("Customer Service", "important"),
                            s("Networking", "important"), s("Negotiation", "important"), s("Financial Literacy", "helpful")],
        "entry_paths": ["Class 10/12 pass", "IRDAI agent training + exam", "Tie up with LIC / private insurer",
                        "Build referral network"],
        "tags": ["finance", "insurance", "sales", "no-degree", "flexible"],
    },
    {
        "id": "actuary_in",
        "title": "Actuary",
        "category": "Finance",
        "description": "Use mathematics and statistics to measure and price risk for insurance and pensions. One of the most highly-paid niche careers in India for those strong in maths — small in number, high in demand.",
        "salary_range": {"min": 50000, "max": 500000, "currency": "INR/month", "note": "Trainee to Fellow Actuary"},
        "growth_outlook": "Strong — scarce specialists",
        "work_style": ["Analytical", "Office/remote", "Exam-driven"],
        "required_skills": [s("Mathematics", "critical"), s("Statistics", "critical"), s("Financial Analysis", "important"),
                            s("Data Analysis", "important"), s("Problem Solving", "critical"), s("MS Excel", "important")],
        "entry_paths": ["Strong maths/stats background (Class 12+)", "Institute of Actuaries of India (IAI) membership",
                        "Clear actuarial exams (ACET then series)", "Roles at insurers / consultancies"],
        "tags": ["finance", "actuary", "mathematics", "high-pay", "niche"],
    },
    {
        "id": "financial_advisor_in",
        "title": "Financial Advisor / Wealth Manager",
        "category": "Finance",
        "description": "Help clients plan investments, taxes, retirement, and wealth. A growing advisory career as India's middle class builds wealth and seeks guidance on mutual funds, insurance, and financial planning.",
        "salary_range": {"min": 30000, "max": 250000, "currency": "INR/month", "note": "Advisor to Senior Wealth Manager"},
        "growth_outlook": "Strong — rising investor base",
        "work_style": ["Client-facing", "Advisory", "Relationship-driven"],
        "required_skills": [s("Financial Planning", "critical"), s("Communication", "critical"),
                            s("Financial Analysis", "important"), s("Sales", "important"), s("Customer Service", "important"),
                            s("Stock Market Knowledge", "helpful")],
        "entry_paths": ["Graduation (finance/commerce preferred)", "NISM / CFP certification",
                        "Join a bank/wealth firm or go independent (RIA)", "Build a client portfolio"],
        "tags": ["finance", "wealth-management", "advisory", "advisor"],
    },
]

US = [
    {
        "id": "us_investment_banker",
        "title": "Investment Banker",
        "category": "Finance",
        "description": "Advise corporations on raising capital, mergers, and acquisitions on Wall Street and beyond. One of the highest-paying finance careers in the US, demanding long hours but offering elite exits into private equity and hedge funds.",
        "salary_range": {"min": 100000, "max": 400000, "currency": "USD/year", "note": "Analyst to VP (base + bonus)"},
        "growth_outlook": "Strong",
        "work_style": ["High-pressure", "Long hours", "Deal-driven"],
        "required_skills": [s("Financial Modeling", "critical"), s("Financial Analysis", "critical"),
                            s("MS Excel", "critical"), s("Valuation", "important"), s("Communication", "critical"),
                            s("Mathematics", "important")],
        "entry_paths": ["Bachelor's in Finance/Economics (target schools help)", "Finance internships (junior year)",
                        "MBA for career switchers", "Analyst programs at banks"],
        "tags": ["finance", "investment-banking", "high-pay", "wall-street"],
    },
    {
        "id": "us_actuary",
        "title": "Actuary",
        "category": "Finance",
        "description": "Assess financial risk using math, statistics, and modeling for insurers and pension funds. Consistently ranked among the best US careers for pay, work-life balance, and job security — with a clear exam-based path.",
        "salary_range": {"min": 75000, "max": 200000, "currency": "USD/year", "note": "Entry to Fellow (FSA/FCAS)"},
        "growth_outlook": "Strong",
        "work_style": ["Analytical", "Office/remote", "Exam-driven"],
        "required_skills": [s("Mathematics", "critical"), s("Statistics", "critical"), s("Problem Solving", "critical"),
                            s("MS Excel", "important"), s("Data Analysis", "important"), s("Programming", "helpful")],
        "entry_paths": ["Bachelor's in Actuarial Science, Math, or Stats", "Pass SOA/CAS actuarial exams",
                        "Internships at insurers", "Associate then Fellow designation"],
        "tags": ["finance", "actuary", "mathematics", "high-pay", "work-life-balance"],
    },
    {
        "id": "us_financial_advisor",
        "title": "Financial Advisor / Planner",
        "category": "Finance",
        "description": "Guide clients on investing, retirement, taxes, and building wealth. A relationship-driven US career with strong earning potential and growing demand as Americans plan for retirement; the CFP credential boosts credibility.",
        "salary_range": {"min": 60000, "max": 200000, "currency": "USD/year", "note": "Base + commission/AUM fees"},
        "growth_outlook": "Strong",
        "work_style": ["Client-facing", "Advisory", "Relationship-driven"],
        "required_skills": [s("Financial Planning", "critical"), s("Communication", "critical"),
                            s("Sales", "important"), s("Financial Analysis", "important"),
                            s("Customer Service", "important"), s("Integrity", "important")],
        "entry_paths": ["Bachelor's degree (finance helpful)", "Series 7 & 66 licenses",
                        "CFP certification", "Join a firm (Edward Jones, Fidelity) or RIA"],
        "tags": ["finance", "advisory", "wealth", "CFP"],
    },
    {
        "id": "us_loan_officer",
        "title": "Loan Officer / Mortgage Officer",
        "category": "Finance",
        "description": "Evaluate and approve loans for individuals and businesses, especially mortgages. A well-paid, commission-friendly US career you can enter without an advanced degree, with steady demand from the housing and lending markets.",
        "salary_range": {"min": 50000, "max": 130000, "currency": "USD/year", "note": "Base + commission"},
        "growth_outlook": "Stable",
        "work_style": ["Client-facing", "Sales-driven", "Office/remote"],
        "required_skills": [s("Financial Analysis", "critical"), s("Communication", "critical"),
                            s("Sales", "important"), s("Attention to Detail", "important"),
                            s("Customer Service", "important"), s("Negotiation", "helpful")],
        "entry_paths": ["High school diploma / bachelor's (varies)", "NMLS Mortgage Loan Originator license",
                        "On-the-job training at a bank/lender", "Build referral network"],
        "tags": ["finance", "lending", "mortgage", "sales"],
    },
    {
        "id": "us_underwriter",
        "title": "Insurance Underwriter",
        "category": "Finance",
        "description": "Decide whether to insure applicants and at what price by analyzing risk. A stable, analytical US finance career with good pay and clear advancement, blending data, judgment, and business rules.",
        "salary_range": {"min": 60000, "max": 120000, "currency": "USD/year", "note": "Trainee to Senior Underwriter"},
        "growth_outlook": "Stable",
        "work_style": ["Analytical", "Office/remote", "Detail-oriented"],
        "required_skills": [s("Risk Analysis", "critical"), s("Financial Analysis", "important"),
                            s("Attention to Detail", "critical"), s("Decision Making", "important"),
                            s("MS Excel", "important"), s("Communication", "helpful")],
        "entry_paths": ["Bachelor's (finance, business, or math)", "Entry underwriting trainee role",
                        "Industry designations (CPCU, AU)", "Advance to senior/complex lines"],
        "tags": ["finance", "insurance", "underwriting", "analytical"],
    },
    {
        "id": "us_auditor",
        "title": "Auditor",
        "category": "Finance",
        "description": "Examine financial records to ensure accuracy and compliance, internally or for public firms. A dependable US finance career with strong demand, clear paths to CPA, and exits into controller and CFO roles.",
        "salary_range": {"min": 55000, "max": 120000, "currency": "USD/year", "note": "Staff to Senior/Manager"},
        "growth_outlook": "Stable",
        "work_style": ["Office/remote", "Detail-oriented", "Seasonal peaks"],
        "required_skills": [s("Accounting", "critical"), s("Auditing", "critical"), s("Attention to Detail", "critical"),
                            s("MS Excel", "important"), s("Analytical Thinking", "important"), s("Integrity", "important")],
        "entry_paths": ["Bachelor's in Accounting", "CPA or CIA certification",
                        "Internships at accounting firms", "Staff auditor roles (Big 4 / internal audit)"],
        "tags": ["finance", "audit", "accounting", "compliance"],
    },
    {
        "id": "us_personal_banker",
        "title": "Personal Banker / Bank Teller",
        "category": "Finance",
        "description": "Help customers with accounts, deposits, loans, and financial products at retail bank branches. A great entry point into the financial sector — no degree required — with paths into lending, advising, and management.",
        "salary_range": {"min": 35000, "max": 65000, "currency": "USD/year", "note": "Teller to Personal Banker / Branch Mgr"},
        "growth_outlook": "Stable",
        "work_style": ["Customer-facing", "Branch-based", "Structured"],
        "required_skills": [s("Customer Service", "critical"), s("Communication", "critical"),
                            s("Sales", "important"), s("Attention to Detail", "important"),
                            s("Computer Basics", "important"), s("Math", "helpful")],
        "entry_paths": ["High school diploma / GED", "On-the-job bank training",
                        "Move into personal banker / lending roles", "Optional finance certifications"],
        "tags": ["finance", "banking", "entry-level", "customer-service"],
    },
]


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))
    existing = {c["id"] for c in careers}
    added = []
    for region, group in (("IN", IN), ("US", US)):
        for c in group:
            if c["id"] in existing:
                print(f"  skip (exists): {c['id']}")
                continue
            c["region"] = region
            careers.append(c)
            added.append(f"[{region}] {c['title']}")
    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")
    in_n = sum(1 for c in careers if c.get("region") == "IN")
    us_n = sum(1 for c in careers if c.get("region") == "US")
    print(f"\nAdded {len(added)} finance careers. Total: {len(careers)}  (IN: {in_n}, US: {us_n})")
    for t in added:
        print(f"  + {t}")


if __name__ == "__main__":
    main()
