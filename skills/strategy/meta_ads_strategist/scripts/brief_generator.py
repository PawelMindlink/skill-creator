
import pandas as pd
import json
import os
import sys
import random

# Chaos Spectrum Styles
CHAOS_SPECTRUM = [
    {
        "name": "Raw Native",
        "desc": "iPhone 13, dim lighting, messy desk setup, flash photography. Authentic UGC.",
        "neg": "professional lighting, studio, bokeh, 4k, cinematic, perfect"
    },
    {
        "name": "The Studio Void",
        "desc": "Absolute minimalism. Product on Vantablack or sterile white infinite background. Zero distractions. High-end luxury.",
        "neg": "messy, grain, noise, people, hands, dust"
    },
    {
        "name": "The Human Element",
        "desc": "Focus on emotion. Close-up of a gamer's face in RGB reflection, or a stressed office worker. Hand on mouse.",
        "neg": "product only, empty room, render"
    },
    {
        "name": "The Ugly (Meme/Glitch)",
        "desc": "Low quality, red circle drawn in Paint, comic sans text overlay, weird angle, 'looks like a mistake'. Pattern Interrupt.",
        "neg": "high quality, professional, hdr, smooth"
    },
    {
        "name": "The Context",
        "desc": "Product in unexpected place. Monitor on a kitchen counter next to cereal, or on a floor in an empty apartment.",
        "neg": "standard desk, office, gaming room"
    }
]

def load_voc(client_dir):
    voc_path = os.path.join(client_dir, "voc_input.json")
    if os.path.exists(voc_path):
        with open(voc_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_random_voc(voc_data, persona):
    # Mapping: Strategy Map Persona -> VoC Keys
    key_map = {
        "Enthusiast": "Enthusiast",
        "Enthusiast (Gaming)": "Enthusiast",
        "Specialist": "Specialist",
        "Specialist (Office)": "Specialist",
        "Klient Ogólny": random.choice(["Enthusiast", "Specialist"]) # Fallback for legacy items
    }
    
    target_key = key_map.get(persona, persona) # Default to self if not found
    
    if target_key in voc_data:
        pains = voc_data[target_key].get("PAIN", [])
        dreams = voc_data[target_key].get("DREAM", [])
        all_quotes = pains + dreams
        if all_quotes:
            return random.choice(all_quotes)
            
    return "Click here to see why experts recommend this model." # Fallback

def generate_briefs(client_name):
    # Paths
    client_dir = os.path.join("C:\\Users\\Paweł\\Documents\\GitHub\\ICP Research\\Clients", client_name)
    strategy_map_path = os.path.join(client_dir, f"{client_name}_Mapa_Strategii.csv")
    output_brief_path = os.path.join(client_dir, f"{client_name}_Briefy_Produkcyjne.md")

    if not os.path.exists(strategy_map_path):
        print(f"Error: Strategy Map not found at {strategy_map_path}")
        return

    # Load Strategy Map
    df = pd.read_csv(strategy_map_path)
    voc_data = load_voc(client_dir)

    # Filter for Stars (GWIAZDA)
    stars = df[df['Zestaw Reklam (AdSet)'].str.contains('GWIAZDA', na=False)]

    if stars.empty:
        print("No 'GWIAZDA' products found to brief.")
        return

    brief_content = f"# 📝 Production Briefs: {client_name.upper()}\n"
    brief_content += f"**Role**: Meta Ads Strategist (The Alchemist)\n"
    brief_content += f"**Objective**: 'Hidden Gems' Scale-up using Chaos Spectrum Diversity.\n\n"

    for _, row in stars.iterrows():
        sku = row['Nazwa Reklamy'].split('_')[-1]
        persona = row['Persona']
        # Override CSV quote with Real VoC
        real_quote = get_random_voc(voc_data, persona) 
        
        promise = row['Obietnica (Dream)']
        bid_cap = row['Bid Cap (PLN)']
        url = row['Link URL']
        
        # Pick Random Style
        style = random.choice(CHAOS_SPECTRUM)

        brief_content += f"## [BRIEF] SKU: {sku} | Persona: {persona}\n"
        brief_content += f"**Status**: GWIAZDA (Scale Aggressively)\n\n"
        
        brief_content += "### 🧠 The Alchemy (Core Angle)\n"
        brief_content += f"*   **The Hook (Real VoC)**: \"{real_quote}\"\n"
        brief_content += f"*   **The Desire**: {promise}\n"
        brief_content += f"*   **The Target**: {persona}\n\n"

        brief_content += "### ✍️ Copywriter Brief (@[creative/meta_ads_copywriter])\n"
        brief_content += f"1.  **Framework**: Hyperdopamine (Tabloid Psychology).\n"
        brief_content += f"2.  **Headline Options (Director's Cut - Pick One)**:\n"
        brief_content += f"    *   *Option A (Fear)*: \"Is your monitor destroying your K/D ratio?\"\n"
        brief_content += f"    *   *Option B (VoC)*: \"'{real_quote[:50]}...' - read the full story.\"\n"
        brief_content += f"    *   *Option C (Greed)*: \"The unfair advantage for under {bid_cap} PLN.\"\n"
        brief_content += f"3.  **Mandatory**: Use short sentences. Greased Chute style.\n\n"

        brief_content += "### 🎨 Designer Brief (@[creative/nano-banana-creative])\n"
        brief_content += f"1.  **Selected Aesthetic**: **{style['name']}**.\n"
        brief_content += f"2.  **Visual Description**: {style['desc']}\n"
        brief_content += f"3.  **Negative Prompt**: {style['neg']}\n"
        brief_content += f"4.  **Vibe**: Stop the scroll. {style['name']} must look different from generic ads.\n\n"
        
        brief_content += f"**Technical Note**: Bid Cap set to **{bid_cap} PLN**.\n"
        brief_content += "---\n\n"

    with open(output_brief_path, 'w', encoding='utf-8') as f:
        f.write(brief_content)

    print(f"✅ Briefy Produkcyjne wygenerowane: {output_brief_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brief_generator.py [client_name]")
    else:
        generate_briefs(sys.argv[1])
