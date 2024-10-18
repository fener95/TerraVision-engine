# create_dataset.py

import json
import random

# Load Agriverts data
with open('agriverts_products.json', 'r', encoding='utf-8') as f:
    agriverts_products = json.load(f)

# List to hold all records
all_records = agriverts_products.copy()

# Function to generate fictitious entries
def generate_fictitious_entries(start_id, count):
    titles = [
        "EcoFlow Irrigation System", "GreenEnergy Biomass Converter", "SolarHarvest Energy Solutions",
        "BioBoost Soil Enhancer", "AquaPure Water Filtration", "CropShield Pest Control",
        "TerraTech Drone Monitoring", "SeedSentry Smart Planter", "AgriSense Soil Sensors", "WindWave Turbine Systems"
    ]
    descriptions = [
        "An advanced irrigation system optimizing water use for orchards.",
        "Machinery converting agricultural waste into renewable energy.",
        "Solar-powered equipment for sustainable farming operations.",
        "Organic soil enhancer for improved crop yields.",
        "State-of-the-art water filtration system for agriculture.",
        "Eco-friendly pest control solutions.",
        "Drone-based crop monitoring for precision agriculture.",
        "Smart planter with automatic seed distribution.",
        "Soil sensors providing real-time nutrient data.",
        "Wind turbine systems tailored for farm energy needs."
    ]
    locations = ["Sicily, Italy", "Andalusia, Spain", "California, USA", "Queensland, Australia", "Ontario, Canada"]
    production_types = [["apricots", "citrus"], ["olives", "grapes"], ["all"], ["wheat", "barley"], ["corn", "soybeans"]]
    solution_types = [["irrigation management"], ["energy recovery machinery"], ["renewable energy"], ["soil management"], ["pest control"]]
    websites = [
        "https://example-agri1.com/product", "https://example-agri2.com/product", "https://example-agri3.com/product",
        "https://example-agri4.com/product", "https://example-agri5.com/product", "https://example-agri6.com/product",
        "https://example-agri7.com/product", "https://example-agri8.com/product", "https://example-agri9.com/product",
        "https://example-agri10.com/product"
    ]

    entries = []
    for i in range(count):
        entry = {
            'id': start_id + i,
            'title': random.choice(titles),
            'description': random.choice(descriptions),
            'location': random.choice(locations),
            'production_type': random.choice(production_types),
            'solution_type': random.choice(solution_types),
            'website': random.choice(websites)
        }
        entries.append(entry)
    return entries

# Determine how many fictitious entries are needed
desired_total_records = 50
current_record_count = len(all_records)
entries_needed = desired_total_records - current_record_count

# Generate fictitious entries
if entries_needed > 0:
    fictitious_entries = generate_fictitious_entries(start_id=current_record_count+1, count=entries_needed)
    all_records.extend(fictitious_entries)

# Save to dataset.json
with open('dataset.json', 'w', encoding='utf-8') as f:
    json.dump(all_records, f, ensure_ascii=False, indent=4)

print(f"Total records in dataset: {len(all_records)}")
