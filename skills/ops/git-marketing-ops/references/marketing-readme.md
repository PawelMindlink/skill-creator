# [Project Name]

> **Business Goal**: [One sentence summary of WHY this project exists, e.g., "Increase Q4 ROAS by 15% via dynamic creative testing"]

## Definition (Business Logic)

**Objective**:

- [Primary KPI, e.g., TAS (Total Ad Spend) optimized for ROAS > 4.0]
- [Secondary KPI, e.g., Decrease CPA by 10%]

**Target Audience**:

- [Who are we talking to? e.g., "Young Professionals (25-34) looking for premium gifts"]

**Hypotheses**:

1. [Hypothesis 1, e.g., "Video hooks showing 'unboxing' will outperform static product shots"]
2. [Hypothesis 2, e.g., "Social Proof in headlines increases CTR"]

## Structure (Assets & Code)

This project is organized as follows:

- **`campaigns/`**: Specific marketing pushes (e.g., `2024-Q4-BlackFriday`).
- **`assets/`**: Raw deliverables.
  - `images/`: Static banners (PSD/JPG).
  - `videos/`: raw footage and exports (MP4).
  - `copy/`: Ad texts, headlines, scripts (MD/DOCX).
- **`reports/`**: Analysis output and performance reviews.
- **`scripts/`**: Automation tools (e.g., for resizing images or pulling data).

## Operation (How to use)

### 1. New Campaign

To start a new campaign variant:

1. Duplicate `campaigns/_template`.
2. Update `assets/copy/main.md`.

### 2. QC Process

Before launching:

- Check mobile aspect ratio (4:5 or 9:16).
- Verify UTM parameters.
- Check spelling in `copy/`.

### 3. Reporting

Run `python scripts/generate_report.py` (if available) or check Looker Studio dashboard [LINK].

---
*Maintained by: Marketing Engineering Team*
