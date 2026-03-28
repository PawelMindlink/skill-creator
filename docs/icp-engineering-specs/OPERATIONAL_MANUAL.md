# Operational Manual: ICP Framework (v3.2)

## 1. Setup Phase (Initialization)

Before any analysis, the client environment must be initialized. This ensures the agent is proactive and has all necessary margins and keywords.

1. Navigate to `skills/strategy/icp-research-lead/scripts/`.
2. Run the setup script:

    ```powershell
    python setup_client.py [ClientName]
    ```

3. **Action**: Answer the interactive prompts regarding Margin, Keywords, and Personas.
4. **Result**: `client_config.json` is generated in the client folder.

---

## 2. Analysis Phase (The Architect)

Once data (GA4 CSV / Feed) is uploaded to the client folder:

1. Run the TCP Analyzer:

    ```powershell
    python tcp_analyzer.py [ClientName]
    ```

2. **Logic**: The script will automatically filter out non-conversion objectives and cluster products by Price Buckets.
3. **Result**: `[Client]_Mapa_Strategii.csv` is generated.

---

## 3. Briefing Phase (The Alchemist)

Translate the data into creative instructions for the production team.

1. Navigate to `skills/strategy/meta_ads_strategist/scripts/`.
2. Run the Brief Generator:

    ```powershell
    python brief_generator.py [ClientName]
    ```

3. **Result**: `[Client]_Briefy_Produkcyjne.md` is generated.
4. **Action**: Hand this file to the Copywriter and Designer agents.

---

## 4. Maintenance (Syncing Skills)

If the framework instructions (SKILL.md) are updated in the repository, they must be deployed to the Agent's global environment:

1. Run the deployment script:

    ```powershell
    ./deploy_global_skills.ps1
    ```

2. **Result**: Global skill definitions are synchronized.
