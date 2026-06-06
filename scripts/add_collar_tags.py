"""Tag every career with a collar type based on category + specific overrides.

Collar types used:
  white  — Office / knowledge / administrative
  blue   — Physical / manual skilled trades
  pink   — Service / care / people-oriented
  gray   — Technical blend (manual + knowledge)
  gold   — Elite / highly specialised / high demand
  new    — Skills-based tech (no traditional degree required)
  green  — Environment / sustainability / nature
  red    — Government / public sector
  brown  — Agriculture / military / natural resources
  no     — Passion / arts / creative freedom
  open   — Remote / freelance / digital nomad
"""
import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "careers.json"

CATEGORY_DEFAULT = {
    "Technology":                   "new",
    "Data & Analytics":             "white",
    "Business & Management":        "white",
    "Finance":                      "white",
    "Marketing & Sales":            "white",
    "Design & Creative":            "new",
    "Human Resources":              "white",
    "Education & Training":         "pink",
    "Healthcare":                   "pink",
    "Trades & Construction":        "blue",
    "Food & Hospitality":           "pink",
    "Beauty & Wellness":            "pink",
    "Fashion & Apparel":            "white",
    "Transport & Logistics":        "blue",
    "Agriculture & Farming":        "brown",
    "Arts & Performance":           "no",
    "Government & Public Service":  "red",
    "Retail & Commerce":            "pink",
    "Social Work & Community":      "pink",
    "Media & Journalism":           "white",
    "Aviation & Airport":           "gray",
    "Defence & Armed Forces":       "brown",
    "Maritime & Shipping":          "blue",
    "Science & Research":           "gold",
    "Mythology & Culture":          "no",
    "Film & Entertainment":         "no",
    "Animation Industry":           "new",
    "Mental Health & Therapy":      "pink",
    "Entrepreneurship & MSME":      "white",
    "Arts & Crafts":                "no",
    "Language & Diplomacy":         "white",
    "Trading & Commodities":        "white",
    "Medical Supplies & Distribution": "white",
    "Manufacturing & Production":   "gray",
    "Supply Chain & Logistics":     "gray",
    "Media & Broadcasting":         "no",
    "Everyday Work & Trades":       "blue",
}

# Career-specific overrides — take precedence over category default
OVERRIDES = {
    # ── GOLD (elite, top-of-field specialisation) ─────────
    "ifs_officer_in":               "gold",
    "us_foreign_service_officer":   "gold",
    "conference_interpreter_in":    "gold",
    "us_psychologist":              "gold",
    "us_bcba":                      "gold",

    # ── RED (government / public sector) ─────────────────
    "heritage_museum_professional": "red",
    "archaeologist_in":             "red",   # ASI government post
    "us_archaeologist":             "white",  # mostly CRM/private

    # ── WHITE (office/knowledge, re-routed from no/other) ─
    "news_anchor_in":               "white",
    "us_news_anchor":               "white",
    "film_producer_in":             "white",
    "us_film_producer":             "white",
    "animation_director_in":        "white",
    "franchise_owner_in":           "white",
    "us_franchise_owner":           "white",
    "us_small_business_owner":      "white",
    "import_export_consultant_in":  "white",
    "hospital_supply_manager_in":   "white",
    "us_healthcare_supply_chain":   "white",
    "loan_officer_in":              "white",
    "mythologist_in":               "white",  # academic/author

    # ── GRAY (technical blend) ────────────────────────────
    "ac_refrigeration_technician_in": "gray",
    "film_editor_in":               "gray",
    "cinematographer_in":           "gray",
    "manufacturing_engineer_in":    "gray",
    "production_manager_in":        "gray",
    "qc_engineer_in":               "gray",
    "industrial_engineer_in":       "gray",
    "automation_robotics_engineer_in": "gray",
    "us_manufacturing_engineer":    "gray",
    "us_industrial_engineer":       "gray",
    "msme_manufacturer":            "gray",
    "logistics_manager_in":         "gray",
    "freight_forwarder_in":         "gray",
    "us_supply_chain_manager":      "gray",

    # ── NEW (skills-based, no traditional degree required) ─
    "animator_2d_in":               "new",
    "animator_3d_in":               "new",
    "us_animator_3d":               "new",
    "storyboard_artist_in":         "new",
    "vfx_artist_in":                "new",
    "motion_graphics_designer_in":  "new",
    "us_motion_graphics":           "new",
    "mobile_repair_technician_in":  "new",
    "data_entry_operator_in":       "new",
    "ecommerce_entrepreneur":       "new",

    # ── OPEN (remote / freelance / digital nomad) ─────────
    "translator_interpreter_in":    "open",
    "us_interpreter_translator":    "open",
    "podcast_host_creator_in":      "open",

    # ── NO-COLLAR (passion / arts / creative freedom) ─────
    "model_in":                     "no",
    "us_model":                     "no",
    "radio_jockey_in":              "no",
    "video_jockey_in":              "no",
    "tv_host_in":                   "no",
    "fine_artist_in":               "no",
    "sculptor_ceramics_in":         "no",
    "textile_artist_in":            "no",
    "us_studio_craft_artist":       "no",
    "jewellery_designer_in":        "no",

    # ── PINK (service / care) ─────────────────────────────
    "medical_equipment_rep_in":     "pink",
    "pharma_sales_rep_in":          "pink",
    "domestic_cook_in":             "pink",
    "beautician_parlour_worker_in": "pink",   # alias check
    "beauty_parlour_worker_in":     "pink",
    "tailor_in":                    "pink",
    "gardener_mali_in":             "pink",   # service role
    "laundry_worker_in":            "pink",
    "front_desk_receptionist_in":   "pink",
    "office_administrator_in":      "white",  # admin = white
    "us_receptionist_admin":        "pink",
    "teaching_assistant_in":        "pink",
    "us_teaching_assistant":        "pink",

    # ── BLUE (physical / manual) ─────────────────────────
    "soap_cosmetics_manufacturer":  "blue",
    "garment_manufacturer_in":      "blue",
    "medical_distributor_in":       "blue",
    "electrician_helper_in":        "blue",
    "delivery_executive_in":        "blue",
    "cab_driver_in":                "blue",
    "auto_rickshaw_driver_in":      "blue",
    "truck_driver_in":              "blue",
    "security_guard_in":            "blue",
    "house_painter_in":             "blue",
    "carpenter_in":                 "blue",
    "plumber_in":                   "blue",
    "welder_in":                    "blue",
    "mason_in":                     "blue",
    "us_delivery_driver":           "blue",
    "us_warehouse_worker":          "blue",
    "us_security_guard":            "blue",
    "us_janitor_custodian":         "blue",
    "us_landscaper":                "blue",
    "us_house_painter":             "blue",

    # ── GREEN (environment / sustainability / nature) ─────
    "plant_nursery_owner":          "green",
    "us_nursery_horticulturist":    "green",
}


def main():
    careers = json.loads(PATH.read_text(encoding="utf-8"))

    tagged = 0
    collar_counts = {}
    for c in careers:
        collar = OVERRIDES.get(c["id"]) or CATEGORY_DEFAULT.get(c["category"], "white")
        c["collar"] = collar
        collar_counts[collar] = collar_counts.get(collar, 0) + 1
        tagged += 1

    PATH.write_text(json.dumps(careers, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Tagged {tagged} careers with collar type:\n")
    for collar, count in sorted(collar_counts.items(), key=lambda x: -x[1]):
        print(f"  {collar:8s}  {count:3d}")


if __name__ == "__main__":
    main()
