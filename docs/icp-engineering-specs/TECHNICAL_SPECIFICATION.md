# Technical Specification: ICP Research & Strategy Framework (v3.2)

## 1. Abstract

This document defines the engineering standards for the **TCP (Targeting-Category-Persona) Protocol**. The system is designed to automate the transition from raw transactional data (GA4/Feeds) to psychologically triggered creative briefs for Meta Ads, optimizing for **Contribution Margin** and **Attention Retention**.

---

## 2. System Architecture

The framework operates as a **One Piece Flow** assembly line, moving a single client environment through three specialized logic layers.

### 2.1 Layer 1: Data Architecture (The Architect)

* **Module**: `icp-research-lead`
* **Logic**: **Efficiency Triangle** (CPA vs CPM vs ROAS).
* **Clustering**: Products are grouped into **Price Buckets** (Ad Sets) based on 50% variance thresholds. This ensures "Apples-to-Apples" bidding environments.
* **Output**: `[Client]_Mapa_Strategii.csv`.

### 2.2 Layer 2: Psychological Alchemy (The Strategist)

* **Module**: `meta_ads_strategist`
* **Logic**: **Hyperdopamine Framework** (Sabri Suby).
* **Transformation**: Transactional nodes (SKUs) are enriched with **Voice of Customer (VoC)** quotes harvested from reviews.
* **Briefing**: Translates static data into **Pattern Interrupt** triggers for the creative team.
* **Output**: `[Client]_Briefy_Produkcyjne.md`.

### 2.3 Layer 3: Creative Execution (The Manufacture)

* **Modules**: `nano-banana-creative` & `meta_ads_copywriter`.
* **Output**: High-resolution visuals (Raw/Native style) and **Greased Chute** copy.

---

## 3. Data Flow Standards

| Stage | Input | Transformation Logic | Output format |
| :--- | :--- | :--- | :--- |
| **Ingestion** | `GA4_Segments.csv` + `Feed.xml/csv` | SKU-level stitching. | Dataframe |
| **Analysis** | Transactional Data | Price-based clustering (Binning). | `Strategy Map (CSV)` |
| **Briefing** | Customer Quotes | Pattern Interrupt + Curiosity Gap. | `Production Brief (MD)` |

---

## 4. Key Performance Indicators (First Principles)

1. **Creative IS Targeting**: The system optimizes for **User Value** to drop CPMs (The Zuckerberg Discount).
2. **One Piece Flow**: We eliminate Batch Waste by producing specific, high-intent campaign structures.
3. **Efficiency Triangle**: ROAS is a secondary metric; **Contribution Margin** is the North Star.

---

## 5. Directory Structure Standards

All client-specific data must reside in:
`Clients/[ClientName]/`

* `/Input/`: Raw CSVs and JSONs.
* `/Output/`: Generated Maps and Briefs.
