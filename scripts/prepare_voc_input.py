
import json
import os
from pathlib import Path

# Paths
CLIENT_DIR = Path(r"C:\Users\Paweł\Documents\GitHub\Meta Ads Analysis Production Upload\research\Clients\iiyama")
GAMING_FILE = CLIENT_DIR / "RAW_HARVEST_DATA_gaming.json"
OFFICE_FILE = CLIENT_DIR / "RAW_HARVEST_DATA_office.json"
OUTPUT_FILE = CLIENT_DIR / "voc_input.json"

def extract_quotes(file_path):
    quotes = {"PAIN": [], "DREAM": [], "BoW": []} # BoW = Best of World (Trust/Positive)
    
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return quotes

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Looking primarily in deep_harvest_insights.phase_1_ceneo and phase_2_reddit
    insights = data.get("deep_harvest_insights", {})
    
    all_items = []
    if "phase_1_ceneo" in insights:
        all_items.extend(insights["phase_1_ceneo"])
    if "phase_2_reddit" in insights:
        all_items.extend(insights["phase_2_reddit"])

    for item in all_items:
        basket = item.get("basket", "")
        raw_quote = item.get("raw_quote", "").strip()
        
        if not raw_quote:
            continue
            
        if basket == "PAIN":
            quotes["PAIN"].append(raw_quote)
        elif basket == "DREAM":
            quotes["DREAM"].append(raw_quote)
        elif basket == "TRUST" or basket == "SLANG":
            quotes["BoW"].append(raw_quote)

    return quotes

def main():
    print("Extracting VoC Data...")
    
    voc_data = {}
    
    # Map Gaming -> Enthusiast
    print(f"Processing Gaming (Enthusiast)...")
    voc_data["Enthusiast"] = extract_quotes(GAMING_FILE)
    
    # Map Office -> Specialist
    print(f"Processing Office (Specialist)...")
    voc_data["Specialist"] = extract_quotes(OFFICE_FILE)
    
    # Save
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(voc_data, f, ensure_ascii=False, indent=4)
        
    print(f"✅ VoC Input saved to: {OUTPUT_FILE}")
    
    # Statistics
    for persona, baskets in voc_data.items():
        print(f"  {persona}: {len(baskets['PAIN'])} Pains, {len(baskets['DREAM'])} Dreams")

if __name__ == "__main__":
    main()
