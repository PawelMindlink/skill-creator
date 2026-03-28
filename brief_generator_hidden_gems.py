import json
import os

def generate_briefs():
    input_json = r"c:\Users\Paweł\Documents\GitHub\ICP Research\Clients\iiyama\hidden_gems_enriched.json"
    output_md = r"c:\Users\Paweł\Documents\GitHub\ICP Research\Clients\iiyama\iiyama_Briefy_Produkcyjne.md"
    
    if not os.path.exists(input_json):
        print(f"Error: {input_json} not found.")
        return

    encodings = ['utf-8', 'utf-16', 'cp1250', 'iso-8859-2']
    products = None
    
    for enc in encodings:
        try:
            with open(input_json, 'r', encoding=enc) as f:
                products = json.load(f)
            print(f"Successfully loaded using {enc} encoding.")
            break
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
            
    if products is None:
        print("Failed to load JSON with any common encoding.")
        return

    brief_content = "# 📝 Production Briefs: IIYAMA (Hidden Gems)\n"
    brief_content += "**Status**: Generated from Top Revenue Products (Organic/Total) due to low direct Ad attribution.\n"
    brief_content += "**Objective**: Test highly profitable products with fresh creative angles.\n\n"

    for product in products:
        title = product.get('feed_title', 'Unknown Product')
        landing_page = product.get('landing_page', '')
        revenue = product.get('TotalRevenue', 0)
        persona = product.get('makro_persona', 'General Audience')
        features = product.get('wykryte_cechy') or "High-performance monitor"
        
        # Clean SKU from title
        sku = title.split('iiyama')[-1].strip() if 'iiyama' in title else title
        
        brief_content += f"## [BRIEF] Product: {sku} | Persona: {persona}\n"
        brief_content += f"**Performance**: {revenue:,.2f} PLN Total Revenue (Organic Winner)\n"
        brief_content += f"**URL**: {landing_page}\n\n"
        
        brief_content += "### 🧠 The Alchemy (Core Angle)\n"
        brief_content += f"*   **The Hook**: Stop scrolling. This isn't just a monitor. It's your unfair advantage.\n"
        brief_content += f"*   **The Desire**: Experience {features[:100]}... without the lag/blur.\n"
        brief_content += f"*   **The Target**: {persona} who demands precision.\n\n"

        brief_content += "### ✍️ Copywriter Brief (@[creative/meta_ads_copywriter])\n"
        brief_content += "1.  **Framework**: Hyperdopamine (Pattern Interrupt -> Intrigue -> Benefit).\n"
        brief_content += f"2.  **Angle**: 'The Hidden Champion'. Why is this specific model ({sku}) the secret weapon of {persona}s?\n"
        brief_content += "3.  **CTA**: 'Sprawdź dostępność' / 'Upgrade Your Setup'.\n\n"

        brief_content += "### 🎨 Designer Brief (@[creative/nano-banana-creative])\n"
        brief_content += "1.  **Style**: 'Raw Native' (iPhone/Desk Setup style). No white background product shots.\n"
        brief_content += "2.  **Visual Hook**: Zoom in on the bezel/stand or a screen displaying high-contrast content.\n"
        brief_content += "3.  **Vibe**: 'Setup Wars' winner. Clean, aspirational, yet attainable.\n\n"
        
        brief_content += "---\n\n"

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(brief_content)
    
    print(f"✅ Briefs generated at: {output_md}")

if __name__ == "__main__":
    generate_briefs()
