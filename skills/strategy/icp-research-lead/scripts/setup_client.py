import json
import os
import sys

def prompt_user(question, default=None):
    """Safe prompt helper."""
    msg = f"{question} [{default}]: " if default else f"{question}: "
    response = input(msg).strip()
    return response if response else default

def setup_client(client_name):
    print(f"\n--- Konfiguracja Klienta: {client_name} ---")
    print("Agent: Potrzebuję kilku informacji, aby zbudować Strategię.")
    
    # 1. Base Config
    url_prefix = prompt_user("1. Jaki jest prefiks URL sklepu? (np. https://sklep.pl)", default="")
    margin_default = float(prompt_user("2. Jaka jest domyślna marża? (0.0 - 1.0)", default="0.30"))
    vat_rate = float(prompt_user("3. Jaka jest stawka VAT? (np. 1.23)", default="1.23"))
    
    # 2. Segments
    segments = []
    print("\n--- Definiowanie Segmentów (Person) ---")
    print("Agent: Podzielmy produkty na grupy. Np. 'Gaming', 'Biuro'.")
    
    while True:
        seg_id = prompt_user("\nPodaj ID Segmentu (lub ENTER by zakończyć)", default="")
        if not seg_id: break
        
        persona = prompt_user(f"  > Jak nazwiemy Personę dla '{seg_id}'?", default="Klient")
        keywords_str = prompt_user(f"  > Podaj słowa kluczowe (po przecinku)", default="")
        keywords = [k.strip() for k in keywords_str.split(',') if k.strip()]
        
        # Fallbacks (Optional but good)
        pain_1 = prompt_user(f"  > (Opcjonalne) Podaj przykładowy Ból (Pain) dla '{persona}'", default="Brak danych")
        dream_1 = prompt_user(f"  > (Opcjonalne) Podaj przykładowe Marzenie (Dream)", default="Brak danych")

        segments.append({
            "id": seg_id,
            "persona": persona,
            "keywords": keywords,
            "fallbacks": {
                "PAIN": [pain_1],
                "DREAM": [dream_1]
            }
        })
        
    # 3. Save
    config = {
        "url_prefix": url_prefix,
        "margins": {"default": margin_default},
        "vat_rate": vat_rate,
        "frequency_multiplier": 1.0,
        "segments": segments,
        "default_segment": {
            "id": "general",
            "persona": "Klient Ogólny",
            "fallbacks": {
                "PAIN": ["Standardowy ból"],
                "DREAM": ["Standardowa korzyść"]
            }
        }
    }
    
    # Path logic
    # Try to find the client folder or create it
    if os.path.isdir(client_name):
        base_dir = client_name
    elif os.path.exists(os.path.join("Clients", client_name)):
        base_dir = os.path.join("Clients", client_name)
    else:
        # Create new
        path_repo = os.path.join(os.path.dirname(os.getcwd()), "ICP Research", "Clients", client_name)
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
             # Hardcoded fallback for environment weirdness
             path_repo = f"C:/Users/Paweł/Documents/GitHub/Meta Ads Analysis Production Upload/research/Clients/{client_name}"
        
        print(f"Agent: Nie znalazłem folderu. Tworzę nowy: {path_repo}")
        os.makedirs(path_repo, exist_ok=True)
        base_dir = path_repo

    out_path = os.path.join(base_dir, "client_config.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
        
    print(f"\n[SUKCES] Konfiguracja zapisana w: {out_path}")
    print("Agent: Teraz możesz uruchomić 'tcp_analyzer.py', aby wygenerować strategię.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python setup_client.py [NazwaKlienta]")
    else:
        setup_client(sys.argv[1])
