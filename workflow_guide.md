# How to Run ICP Research (V5 Protocol)

**Logic**: "Efficiency Triangle" (CPA is King).

## 1. Setup

1. **Create Client Config**: Copy `skills/strategy/icp-research-lead/templates/client_config.json` to your workspace and fill in Margins/Personas.
2. **Inventory Data**: Get `GA4.csv` and `Meta.csv`. Ensure they have Product IDs/SKUs.

## 2. Phase 1: The Truth (Data Foundation)

Run the standardized script to classify products:

```bash
python skills/strategy/icp-research-lead/scripts/generate_data_foundation.py \
  --config client_config.json \
  --ga4 GA4_Data.csv \
  --meta Meta_Data.csv \
  --output [Client]_Plik_1_Mapowanie.csv
```

*Result*: A CSV with "Unicorn", "Burn", "Mismatch" labels.

## 3. Phase 2: The Agent (Psych & Scent)

Prompt the Agent:
> "Run ICP Research Phase 2 for [Client]. Here is the Plik_1_Mapowanie.csv and the Website URL."

*Action*:

1. Agent reads CSV.
2. Agent visits Landing Pages for "Mismatch" products (Scent Check).
3. Agent maps reviews to Personas.

## 4. Phase 3: The Plan (Execution)

Prompt the Agent:
> "Run ICP Research Phase 3."

*Action*:

1. Agent writes the Bid Strategy based on the Diagnostic Labels.
    * **Unicorns** = Scale.
    * **Mismatch** = Fix Page first.
    * **Burn** = Kill.
