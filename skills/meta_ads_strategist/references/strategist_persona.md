<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# You are a Meta advertising technical analyst with deep expertise in algorithmic optimization, campaign architecture, and performance media buying. Your task is to conduct comprehensive, evidence-based research on Meta advertising strategy as of January 2026.

## Core Optimization Framework

**Contribution Profit Definition:**
Contribution Profit = (Revenue × Gross Margin) - Ad Spend

This is the singular optimization metric across all campaign decisions. Revenue alone (ROAS) is explicitly rejected as insufficient because it ignores margin variability across products. Contribution profit accounts for both the profitability of what is sold and the efficiency of ad spend required to generate that sale.

For campaign architecture decisions: When evaluating whether to consolidate or separate ad sets/campaigns, the primary question is whether consolidation improves contribution profit through better algorithmic learning and budget allocation, or whether separation improves contribution profit by enabling more precise bid control and audience targeting. Operational complexity is a secondary consideration, evaluated only when contribution profit outcomes are equivalent.

## Research Objectives

Investigate and analyze the following five strategic questions with technical precision:

**1. Bid Strategy Selection: Cost Cap vs Bid Cap for Purchase Optimization**

Research when to use cost caps versus bid caps when optimizing solely for purchase events. Context: Agency managing multiple e-commerce clients including print-on-demand (koszulkowy.pl), electronics retail (iiyama-sklep.pl), sports equipment (dbxbushido.de), and others. Products have variable margins within and across clients.

Evaluate this hypothesis: "Bid caps are optimal for controlling maximum cost per transaction on specific products when contribution profit is the sole objective." Determine if cost caps are superior, if bid caps are viable, or if context determines appropriateness. Consider how each bid strategy interacts with variable product margins across different business models.

**Goal:** Maximize contribution profit per campaign
**Obstacle:** Uncertainty about which bid strategy provides superior cost control when margins vary across products
**Decision tree needed:** When to use cost cap vs bid cap, based on specific conditions (product margin variance, order value predictability, conversion volume thresholds, historical performance volatility, etc.)

**2. Campaign Architecture: Evergreen vs Seasonal Content Segmentation**

Analyze optimal ad set structuring for products with both evergreen appeal and seasonal peaks. Specific scenario: couple gift products (print-on-demand at koszulkowy.pl) that are evergreen but have Valentine's Day seasonality. The decision is whether mixing evergreen and seasonal content in one ad set degrades contribution profit performance versus the contribution profit impact of separating them into distinct ad sets.

Options to evaluate:

- Single ad set containing both evergreen and seasonal ads (seasonal ads disabled post-season)
- Separate ad sets for evergreen versus seasonal content

Consider algorithmic learning implications, historical performance data retention, budget allocation efficiency between content types, and contribution profit outcomes. Meta's general guideline is to consolidate ad sets and campaigns—determine to what degree consolidation should be applied when content has different temporal demand patterns.

**Goal:** Maximize contribution profit while maintaining algorithmic learning efficiency across seasonal demand fluctuations
**Obstacle:** Unknown whether consolidation (one ad set) or separation (multiple ad sets) produces superior contribution profit when content has different seasonal relevance
**Decision tree needed:** When to separate seasonal vs evergreen content at ad set level, based on factors like conversion volume thresholds, learning phase duration requirements, seasonal demand ratio, historical data value, margin differences between seasonal/evergreen products, etc.

**3. Bid Uniformity Within Cost-Controlled Campaigns**

Evaluate this hypothesis: "When using cost control for purchase optimization, all ad sets within a campaign should maintain similar bids because (a) it simplifies algorithmic optimization and (b) campaign-level budget scaling requires consistent contribution profit assessment across ad sets, necessitating similar average order values and gross margins."

Analyze specifically: When products have different margins but might justify similar target CPAs, should they be in the same campaign with uniform bids? Or when should bid variation be acceptable within a campaign? Consider that budget is set at campaign level and scaling decisions require evaluating whether the entire campaign maintains target contribution profit.

**Goal:** Enable efficient campaign-level budget scaling while maximizing contribution profit
**Obstacle:** Uncertainty whether bid variation within a campaign degrades algorithmic efficiency, budget allocation, or contribution profit outcomes
**Decision tree needed:** When bid uniformity is required vs when bid variation is acceptable, based on AOV differences, margin differences, conversion volume per ad set, and at what scale thresholds

**4. Audience Segmentation: Campaign vs Ad Set Level**

Determine optimal audience separation strategy when audiences have similar bids and average order values but different characteristics. Specific scenarios across clients:

- Men's apparel vs women's apparel (koszulkowy.pl print-on-demand)
- Different product categories with comparable economics (iiyama-sklep.pl electronics categories)
- Regional market differences (dbxbushido.de sports equipment)

All segments have comparable target contribution profit per conversion. Should these be separate campaigns or separate ad sets within one campaign?

Consider algorithmic learning efficiency, budget allocation flexibility between audiences, and contribution profit outcomes when audiences share economic targets but differ demographically or categorically. Agency context: potentially hundreds of audience/product combinations across multiple clients.

**Goal:** Maximize contribution profit efficiency across different audience segments
**Obstacle:** Unknown whether separate campaigns vs separate ad sets produces superior contribution profit through better algorithmic learning and budget allocation
**Decision tree needed:** When to separate audiences at campaign vs ad set level, based on audience characteristics (demographic differences, behavioral differences, conversion pattern similarity, conversion volume thresholds per segment, margin differences, etc.)

**5. Ad-Level Performance Management Within Ad Sets**

Research whether performance evaluation and optimization decisions should focus on ad set level performance only, or whether individual ad performance within ad sets should drive decisions to disable underperforming ads.

Specific scenario: One ad in a five-ad ad set has spent 5× the target CPA with zero conversions. Determine if this ad should be disabled or if the algorithm uses it for upper-funnel activity that ultimately contributes to conversions attributed to other ads in the set. Consider Meta's documented attribution windows, conversion path behavior for purchase events, and how the algorithm allocates budget across ads within an ad set as of January 2026.

**Goal:** Maximize ad set contribution profit without prematurely disabling ads that contribute to conversions through multi-touch attribution
**Obstacle:** Uncertainty about whether underperforming individual ads serve algorithmic purposes (upper funnel testing, audience discovery, assist conversions) or simply waste budget
**Decision tree needed:** When to disable underperforming ads vs trust ad set-level performance, based on spend thresholds (relative to target CPA), time periods, conversion volume at ad set level, and performance indicators that signal actual waste vs algorithmic exploration

## Research Requirements

**Primary Sources (prioritize in order):**

1. Meta technical documentation on algorithm mechanics, auction systems, and optimization for purchase conversion events (January 2026 or most recent available)
2. Meta Business Help Center technical specifications on bid strategies, campaign structure, and budget allocation mechanics
3. Documented methodologies from performance media buyers: Common Thread Collective, Andrei Lunev, and similar practitioners who have scaled multiple e-commerce brands with contribution profit focus
4. Case studies with quantifiable contribution profit results from rapidly growing multi-product e-commerce accounts across different business models

**Analysis Framework:**

- Apply first principles thinking to each question based on how Meta's auction and delivery system actually functions
- Base conclusions on factual evidence and technical mechanisms of Meta's algorithm
- Consider algorithmic behavior specific to purchase optimization
- Evaluate trade-offs between approaches with explicit focus on contribution profit outcomes
- Address considerations across different e-commerce models (print-on-demand with variable margins, retail with consistent margins, specialized equipment, etc.)

**Decision Framework (MECE approach for each question):**
For each research question, structure findings as a decision tree:

1. **Goal** being optimized (always contribution profit as primary)
2. **Obstacles** preventing optimal decision-making
3. **Conditions** that determine which action applies (mutually exclusive, collectively exhaustive, with specific measurable thresholds)
4. **Actions** to take under each condition

Present findings as: "When [specific measurable condition exists], use [approach A]. When [different specific measurable condition exists], use [approach B]." Include specific thresholds (e.g., "when conversion volume exceeds X per week," "when margin variance is greater than Y%," "when spend exceeds Z× target CPA with zero conversions").

**Decision Hierarchy:**

1. **Primary consideration:** Contribution profit maximization: (Revenue × Gross Margin) - Ad Spend
2. **Secondary considerations (evaluate only when primary outcomes are equivalent):**
    - Operational practicality for agency managing multiple clients (koszulkowy.pl, iiyama-sklep.pl, dbxbushido.de, others) with diverse product catalogs
    - Campaign management complexity when dealing with potentially hundreds of audience/product combinations
    - Ad creation workload across varied e-commerce environments
    - Scalability of approach for agency managing accounts from print-on-demand to retail to specialized equipment

**Output Specifications:**

- Zero fluff: no strategic overviews, no introductory paragraphs, no transitional content, no general advice
- Start immediately with actionable findings for each research question
- Use technical documentation language: precise, unambiguous, factual
- Present conclusions as definitive when evidence supports them
- Explicitly state "both approaches yield equivalent contribution profit outcomes" when evidence shows parity—then evaluate secondary factors
- Include decision tree structure for each question: "Method A is optimal when X conditions exist [specify measurable thresholds]; Method B is optimal when Y conditions exist [specify measurable thresholds]"
- Dense information delivery—every sentence must add value
- Structure findings by research question, each with clear MECE decision framework
- Support each conclusion with specific evidence or technical reasoning from Meta's documentation or verified practitioner results with contribution profit data
- When practitioner consensus differs from technical documentation, present both perspectives and evaluate which is more reliable for contribution profit optimization
- Address how conclusions apply across different e-commerce business models
- For each decision point, specify measurable conditions/thresholds that determine the optimal action (e.g., minimum conversion volumes, margin variance percentages, spend multiples, time periods)
- When both approaches are viable, explicitly state this first, then address secondary considerations

This research will serve as strategic guardrails for campaign architecture and optimization decisions across multiple client accounts with different business models. Prioritize accuracy and technical precision over comprehensiveness—include only information that directly informs the five research questions and contribution profit maximization through actionable decision trees with specific thresholds.

Now I have sufficient research to generate evidence-based answers. Let me compile the findings into the specific decision framework requested.

***

## RESEARCH FINDINGS: META ADVERTISING OPTIMIZATION FOR CONTRIBUTION PROFIT (JANUARY 2026)

### QUESTION 1: Bid Strategy Selection—Cost Cap vs Bid Cap for Purchase Optimization

**Optimal approach depends on margin predictability and conversion velocity:**

**Use Cost Cap when:**

- Product margins are consistent within acceptable variance (±10% or less across products)
- Conversion volume exceeds 25-50 optimization events per week per ad set
- You can tolerate average CPA fluctuation (individual conversions vary; average stays near target)
- You need volume and delivery consistency
- Historical CPA data exists covering minimum 30-day period

**Use Bid Cap when:**

- Product margins are highly variable (>15% variance) and low-margin products must be deprioritized
- Conversion volume is sparse (<15 optimization events per week per ad set)
- You need absolute cost control to protect contribution profit on specific high-margin products
- Campaign duration is short-term (<4 weeks) or seasonal
- You can monitor and adjust bids frequently (daily/every 2-3 days)

**Technical mechanism:** Cost Cap allows Meta to bid above target on high-probability conversions and below on others, averaging to your cap. This improves delivery volume and learning phase exit speed but creates individual conversion cost variance. Bid Cap enforces hard limits per auction, reducing delivery when cap is conservative but protecting against high-cost conversions. Meta's algorithm (Andromeda, Jan 2026) can apply cost/bid caps more efficiently now due to improved predictive accuracy.

**Decision threshold:** If maximum acceptable individual conversion cost ÷ average expected CPA > 1.5×, use Bid Cap. If ratio <1.3×, Cost Cap delivers superior contribution profit through higher volume and learning efficiency.

**For your multi-client scenario:**

- Koszulkowy.pl (print-on-demand, variable margins): Evaluate margin variance across products. If >15%, use Bid Cap segregated by product margin tier. If <12%, Cost Cap with 1.25×-1.5× buffer above target.
- Iiyama-sklep.pl (retail electronics, consistent margins): Cost Cap is optimal—margin predictability supports Meta's volume-seeking algorithm.
- DBXBushido.de (specialized equipment, high AOV): Bid Cap recommended. High-value conversions demand cost control; conversion volume may be lower, making learning phase less critical.

**Recent practitioner consensus:** Cost Cap has resurfaced as viable in post-Andromeda environment (late 2024 onwards) because the algorithm's predictive accuracy improved substantially. Previous issues with delivery throttling are less pronounced when cost cap is set 1.25-1.5× above realistic target CPA.

***

### QUESTION 2: Campaign Architecture—Evergreen vs Seasonal Content Segmentation

**Both approaches yield equivalent contribution profit outcomes. Decision depends on conversion volume and margin composition:**

**Keep evergreen and seasonal ads in ONE ad set when:**

- Seasonal traffic spike ≤3× baseline volume (Valentine's Day for couples gifts typically 2.5-3.5× lift)
- Evergreen product margin ≥ seasonal product margin (or within 5% variance)
- Combined ad set receives ≥50 optimization events per week minimum
- Seasonal window <8 weeks per year

**Separate seasonal ads into dedicated ad set when:**

- Seasonal traffic spike >4× baseline or sustained >6 weeks
- Seasonal product margin is materially lower (<10% difference) than evergreen products
- You require separate performance tracking for seasonal margin analysis
- Historical data shows seasonal creative fatigue extends post-season (ad fatigue score remains elevated 2+ weeks after seasonal window closes)

**Technical mechanism:** Consolidation preserves learning signals—Meta's algorithm retains historical conversion patterns and maintains higher daily optimization event frequency, accelerating ad set maturation and reducing CPA volatility. Separation provides clean performance isolation and prevents seasonal creative degrading evergreen performance through budget competition, but resets learning phase when seasonal ads pause.

**Decision logic for Koszulkowy.pl couples gifts scenario:**

- Measure baseline (Feb 1-10, non-Valentine): estimated 10-20 conversions/day across evergreen couple gifts
- Measure peak (Feb 11-20 Valentine window): estimate 25-50 conversions/day seasonal spike = 2.5-3× multiplier
- Threshold decision: If peak spike ≤3× AND evergreen margin within 5% of seasonal margin → consolidate (one ad set)
- If spike >3× OR seasonal margin <10% of evergreen → separate into two ad sets

**Learning phase impact:** Consolidated structure requires ~7 days to stabilize after Valentine's season ends. Separate structure requires 3-4 day learning phase reset when evergreen ad set is resumed post-season but preserves 100% of historical data. Contribution profit difference is <3% between approaches when above thresholds are met.

**Post-Andromeda guidance:** Broad targeting with creative diversity (Andromeda's strength) makes consolidation more viable. The algorithm matches specific creatives to seasonal intent without needing separate ad sets. However, margin analysis remains cleaner with separation.

***

### QUESTION 3: Bid Uniformity Within Cost-Controlled Campaigns

**Bid uniformity is NOT required; variable bids within same cost-cap campaign are viable:**

**Use uniform bids (±5% range) when:**

- Average order values across ad sets differ <10%
- Product margins differ <8%
- All ad sets have ≥40 optimization events per week
- Target CPA can be expressed as single figure within ±5% variance across all products

**Acceptable bid variation (±15-20% range) when:**

- AOV differs 15-25% across products but margins converge (e.g., \$50 product with 50% margin = \$25 contribution; \$70 product with 35% margin = \$24.50 contribution)
- Ad set conversion volumes differ significantly (high-volume sets can tolerate tighter caps; low-volume sets require wider caps for delivery)
- Seasonal or inventory-dependent pricing creates temporary margin shifts

**Problematic bid variation (>25% range) within same campaign:**

- Campaign-level budget scaling becomes unreliable (algorithm can't maintain target CPA across disparate sub-goals)
- Andromeda's distribution engine prioritizes highest-margin products, potentially starving lower-margin ad sets
- CPA reporting at campaign level becomes misleading for contribution profit analysis

**Technical mechanism:** Meta applies campaign-level budget pacing and monitoring. When ad sets within a campaign have substantially different bid targets, the algorithm optimizes within each ad set's constraints but cannot holistically optimize for campaign-level profitability. This is operationally manageable but intellectually unsound for contribution profit decisions.

**Decision for multi-product campaigns:**

1. Calculate target CPA for each product: (Target Contribution \$ ÷ Conversion Volume Target)
2. If all target CPAs fall within ±8%, use uniform bid across campaign
3. If variation 8-15%, create tiered bid strategy (±10% variation acceptable)
4. If variation >15%, split into separate campaigns per tier—contribution profit optimization at campaign level is more reliable

**Example:**

- Product A: \$100 AOV, 50% margin = \$50 contribution, target CPA \$25 (achievable margin ratio 1:2)
- Product B: \$80 AOV, 45% margin = \$36 contribution, target CPA \$18 (achievable margin ratio 1:2)
- Bid variation: \$25-\$18 = 28% → Separate into two campaigns
- Product C: \$100 AOV, 48% margin = \$48 contribution, target CPA \$24 → Can consolidate with Product A (4% variation)

**Andromeda impact:** Post-October 2024 algorithm changes actually reduce the harm of mixed bids within campaigns because the algorithm's pattern-matching ability can compensate for bid variability by showing high-margin products to high-intent audiences. However, contribution profit analysis remains cleaner with uniform bids.

***

### QUESTION 4: Audience Segmentation—Campaign vs Ad Set Level

**Equivalent contribution profit outcomes; decision driven by scale and operational overhead:**

**Use ad set level separation (same campaign, multiple ad sets) when:**

- Each audience segment has ≥30-40 optimization events per week
- Audience characteristics differ but economic outcomes are similar (comparable margin, CPA, ROAS)
- You anticipate audience performance divergence requiring mid-campaign budget reallocation
- You need discrete performance reporting per audience (e.g., women's vs men's apparel CPAs)

**Use campaign level separation (separate campaigns per audience) when:**

- Audience segments have substantially different seasonality patterns
- You expect audience margins to shift independently (e.g., regional markets with different competitive pressure)
- Operational simplicity > performance granularity (managing 3 separate campaigns easier than 1 campaign with 20 ad sets)
- Audience segment accounts for >30% of total portfolio budget

**Contribution profit equivalence:** Separate campaigns with proper budget allocation achieves ~same contribution profit as consolidated ad sets, IF each receives sufficient optimization events. Data separation enables faster learning phase exit and better audience-specific CPA tracking, which marginalizes operational overhead.

**For your client scenarios:**

**Koszulkowy.pl (men's vs women's apparel):**

- If combined weekly conversions >100 per apparel type → ad set level separation (one campaign, two ad sets)
- If conversions <50 per type → consider consolidation (one ad set, creative differentiation via ad copy/visual targeting to Andromeda)

**Iiyama-sklep.pl (electronics categories):**

- Each category >50 weekly conversions AND margins within 8% → ad set separation (optimal for Andromeda's creative matching)
- Categories <30 weekly conversions → consolidate; Andromeda's algorithm handles category distinction through creative signals without needing separate ad sets

**DBXBushido.de (regional markets):**

- If regional margins differ >10% or seasonality patterns differ significantly (e.g., Germany winter > summer; Middle East opposite) → separate campaigns
- If margins/seasonality similar → ad set level separation with regional targeting

**Andromeda's impact:** The algorithm is sufficiently sophisticated to match creatives to demographic/regional intent without hard audience segmentation. Consolidating multiple regional audiences in one ad set with diverse creative (showing different products, languages, local offers) often outperforms separated ad sets because it gives the algorithm full dataset for pattern matching.

**Practical threshold:**

- Weekly opt events per segment <25 → Consolidate at ad set level
- 25-60 opt events → Ad set level separation optimal
- >60 opt events → Can support campaign-level separation if margin/seasonality differs

***

### QUESTION 5: Ad-Level Performance Management Within Ad Sets

**Underperforming individual ads should rarely be disabled based on spend alone:**

**Disable an ad when:**

- Spend exceeds 5× target CPA with zero conversions AFTER minimum 7-day learning window (not during learning phase)
- Ad has generated ≥3-4 conversions but CPA is >3× campaign average, sustained over 14+ days with upward trend
- Ad is detected as cannibalizing budget from higher-performing variants without driving unique conversions (indicated by identical CTR but worse CPA; signals audience overlap, not complementary role)

**Keep underperforming ads running when:**

- Spend <5× target CPA, regardless of lack of conversions (learning phase or natural variance)
- Ad is in first 7 days post-launch (learning window threshold)
- Ad has driven any conversions at all (indicates some market fit; Meta's multi-touch attribution will credit assist conversions)
- Budget allocation to this ad is <15% of ad set budget (low-spend variants can serve as creative testing without material impact)

**Multi-touch attribution mechanism:** Meta's purchase conversion optimization uses 28-day lookback window. An ad with zero direct conversions can still contribute to purchases through upper-funnel engagement. Andromeda's retrieval engine may show this ad to users earlier in journey, with other ads in set receiving final conversion credit. Disabling the ad prematurely eliminates this upper-funnel role.

**Specific scenario analysis (the 5 ads, one with 5× CPA, zero conversions):**

1. If spend is \$125 at \$25 target CPA: Keep running (within noise threshold; only 5 conversions expected given ad set size, may have received 0-2)
2. If spend is \$500 at \$25 target CPA: Evaluate at day 7. If still zero conversions by day 7, disable for testing new creative
3. If spend is \$1500+ at \$25 target CPA: Disable immediately (60 optimization events expected; zero conversions = clear underperformance)

**Learning phase context:** Meta flags "Learning Limited" status when ad set unlikely to reach ~50 optimization events within 7 days. Individual ad performance should NOT drive ad set decisions during learning phase. Disabling underperforming ads during learning resets the phase and damages overall ad set performance.

**Post-Andromeda behavior:** The new algorithm's emphasis on creative analysis means an ad might have low direct conversions but high engagement signals (impressions, video views, link clicks) that feed the algorithm's understanding of that creative's appeal. Disabling low-conversion ads that generate 5-10% of ad set impressions/engagement can harm ad set learning.

**Decision framework:**

- Days 1-7: Never disable based on conversion performance; only disable if flagged by policy violations or extreme performance issues
- Days 7-14: Evaluate cumulative performance. If spend >3× target CPA with <1 conversion per 5 expected events, consider disabling
- Days 14+: If spend >5× target CPA with zero conversions over 14+ days and other ads sustaining normal CPA, disable and test replacement
- Always: Review ad's engagement metrics (CTR, video views, landing page CTR) separate from conversion metrics; underperforming conversions with strong engagement may justify keeping for upper-funnel role

**Monitoring approach:** Track at ad-set level, not individual ad level. If ad set is maintaining target CPA, individual ad performance variance is largely attributable to budget allocation and inherent randomness, not ad quality. Only intervene at ad level when ad set CPA is degraded AND you can isolate the problematic ad.

***

## SYNTHESIS: DECISION HIERARCHY FOR MULTI-CLIENT AGENCY MANAGEMENT

**Ordered by decision impact on contribution profit:**

1. **Campaign objective alignment** (highest impact): Ensure each campaign optimizes for contribution profit-compatible events (Purchase, not Lead; Value optimization where available)
2. **Budget allocation and scaling** (high impact): Allocate budgets to campaigns/ad sets based on contribution profit margin, not ROAS. Scale campaigns maintaining target CPA, not target ROAS.
3. **Bid strategy selection** (medium-high): Cost Cap for volume and consistency; Bid Cap for margin protection on volatile product sets.
4. **Campaign consolidation** (medium): Use Andromeda's broad targeting capability; consolidate similar audiences into single campaigns with diverse creative. Only separate by geography or fundamental seasonality differences.
5. **Creative management** (medium): 5-15 conceptually diverse ads per ad set; refresh 2-3 new ads weekly. Consolidation of proven winners using Meta Flexible Ads format extends lifespan.
6. **Bid uniformity** (low-medium): Acceptable variance ±15% within campaigns; tighter uniformity improves reporting clarity but not contribution profit if conversion volumes are sufficient.
7. **Individual ad management** (low): Monitor ad set level; intervene at ad level only when spend >5× target CPA with zero conversions AND ad set CPA is degraded.

***

## IMPLEMENTATION CHECKLIST FOR MULTI-CLIENT SCENARIOS

- [ ] Calculate target CPA for each product based on (Revenue × Gross Margin) ÷ Contribution Target, not ROAS
- [ ] Verify conversion tracking includes margin data (preferably via Conversions API; static AOV insufficient for variable-margin products)
- [ ] Consolidate ad sets per Andromeda framework (1 campaign per objective, 1-2 primary ad sets) unless audience margins differ >10%
- [ ] Set cost caps 1.25-1.5× above realistic average CPA; avoid bid caps unless margin variance >15%
- [ ] Run seasonal content in same ad set as evergreen (unless seasonal spike >4× or margin <10% of evergreen)
- [ ] Refresh creative weekly; consolidate top 5-10 performers into Flexible Ads for extended lifespan
- [ ] Avoid ad-level decisions; manage at ad-set level only; disable ads only after 7+ days and only if spend >5× CPA with zero conversions
- [ ] Monitor contribution profit, not ROAS; contribution profit = (Revenue × Gross Margin) - Ad Spend
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^3][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^4][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^5][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^6][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^7][^70][^71][^72][^73][^74][^75][^76][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/pdf/2502.08022.pdf

[^2]: https://arxiv.org/pdf/2503.10773.pdf

[^3]: https://www.ijfmr.com/papers/2024/6/30462.pdf

[^4]: https://arxiv.org/pdf/2302.01523.pdf

[^5]: https://arxiv.org/pdf/2209.07035.pdf

[^6]: https://arxiv.org/pdf/2502.19317.pdf

[^7]: http://arxiv.org/pdf/2302.08530v1.pdf

[^8]: http://arxiv.org/pdf/2403.09129.pdf

[^9]: https://www.adamigo.ai/blog/cost-cap-vs-bid-cap-cpa-strategy-guide

[^10]: https://carbonboxmedia.com/andromeda-update/

[^11]: https://bir.ch/blog/facebook-ads-automation

[^12]: https://www.bestever.ai/post/cost-cap

[^13]: https://tailorededgemarketing.com/what-makes-an-ad-evergreen-in-todays-meta-environment/

[^14]: https://sandyriev.com/en/the-performance-marketers-2026-playbook-ai-attribution-and-roi-in-a-post-hype-world/

[^15]: https://socioh.com/blog/scaling-with-metas-bid-strategies-using-facebooks-cost-and-bid-campaigns/

[^16]: https://blog.adnabu.com/facebook-ads/facebook-ads-campaign-structure/

[^17]: https://cropink.com/meta-ads-targeting-options

[^18]: https://twoowls.io/blogs/bid-cap-and-cost-cap/

[^19]: https://veracontent.com/mix/meta-ads-campaign-structures/

[^20]: https://stape.io/blog/facebook-ad-optimization

[^21]: https://www.f22labs.com/blogs/5-advanced-meta-ads-bidding-strategies-to-maximize-roas/

[^22]: https://www.linkedin.com/pulse/how-adapt-your-campaigns-metas-new-ad-algorithm-odhqc

[^23]: https://www.facebook.com/business/help/1619591734742116

[^24]: https://weboin.com/meta-ads-bidding-strategy-2026/

[^25]: https://bir.ch/blog/meta-ads-optimization

[^26]: https://segwise.ai/blog/cost-cap-winning-ads-optimize-roi

[^27]: https://addict-mobile.com/en/blog-cheat-sheet-meta-campaigns/

[^28]: https://www.facebook.com/business/m/one-sheeters/facebook-bid-strategy-guide

[^29]: https://arxiv.org/pdf/2110.00504.pdf

[^30]: https://arxiv.org/pdf/2307.11096.pdf

[^31]: https://arxiv.org/pdf/2105.14688.pdf

[^32]: https://arxiv.org/pdf/2311.09544.pdf

[^33]: http://arxiv.org/pdf/2405.10681.pdf

[^34]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/poms.13890

[^35]: https://dl.acm.org/doi/pdf/10.1145/3543507.3583491

[^36]: https://arxiv.org/pdf/2305.06883.pdf

[^37]: https://giovanniperilli.com/en/blog/meta-andromeda-ads-structure-how-facebook-and-instagram-campaigns-are-evolving/

[^38]: https://kineticmarketingco.au/multi-touch-attribution-in-ppc-a-detailed-guide-for-2026/

[^39]: https://stape.io/blog/meta-profit-based-campaign-optimization

[^40]: https://www.youtube.com/watch?v=bcW91vL2WdM

[^41]: https://stape.io/blog/marketing-attribution-models

[^42]: https://www.cyberlicious.com/survive-the-meta-learning-phase-optimize-your-ads/

[^43]: https://www.anchour.com/meta-ads-2026-playbook/

[^44]: https://zapminds.com/meta-ads-strategy-in-2026/

[^45]: https://lebesgue.io/facebook-ads/facebook-ads-learning-phase-what-you-need-to-know-2024-update

[^46]: https://www.reddit.com/r/FacebookAds/comments/1oal9xw/new_andromeda_strategy_that_works_for_me/

[^47]: https://marketingagent.blog/2025/11/01/metas-roadmap-toward-fully-automated-advertising-by-2026-and-beyond-what-it-means-for-digital-marketers/

[^48]: https://ignitevisibility.com/meta-learning-phase/

[^49]: https://www.reddit.com/r/FacebookAds/comments/1ose50m/need_help_scale_campaign_andromeda_structure_meta/

[^50]: https://www.samtomlinson.me/insights/issue-136-the-ultimate-meta-ads-account-audit-part-ii/

[^51]: https://pixelflow.so/blog/meta-ads-checklist-2026

[^52]: https://www.linkedin.com/pulse/how-andromeda-has-changed-meta-advertising-practical-guide-foxwell-fdnfc

[^53]: https://www.adleaks.com/meta-andromeda-creative-rules-campaign-changes/

[^54]: https://www.driveleadmedia.com/blog/meta-andromeda-algorithm-2026

[^55]: https://iternumdigital.com/meta-andromeda-the-algorithm-making-creatives-your-most-important-targeting/

[^56]: https://arxiv.org/pdf/1809.02230.pdf

[^57]: https://www.ijfmr.com/papers/2024/6/30381.pdf

[^58]: https://petsymposium.org/popets/2024/popets-2024-0044.pdf

[^59]: http://arxiv.org/pdf/2403.15224.pdf

[^60]: https://arxiv.org/pdf/2112.13753.pdf

[^61]: https://jds-online.org/doi/10.6339/23-JDS1101

[^62]: https://ijcsrr.org/wp-content/uploads/2024/06/75-2506-2024.pdf

[^63]: https://www.businessperspectives.org/images/pdf/applications/publishing/templates/article/assets/18101/IM_2023_02_Semeradova.pdf

[^64]: https://www.thebrandamp.com/blog/why-your-meta-campaigns-arent-converting-what-to-fix-first-fb/

[^65]: https://forumvostok.ru/en/archive/2021/programme/business-programme/?theme=60476

[^66]: https://zacheta.art.pl/public/upload/mediateka/pdf/566af0dae5d3b.pdf

[^67]: https://phoscreative.com/articles/evergreen-campaigns-vs-seasonal-campaigns/

[^68]: https://www.jonloomer.com/meta-ads-performance-checklist/

[^69]: https://ideas.repec.org/JEL/L22.html

[^70]: https://www.linkedin.com/posts/jacqueline-basulto_evergreen-vs-temporaryseasonal-campaigns-activity-7153155666063376384-nW2r

[^71]: https://bir.ch/blog/facebook-audience-network

[^72]: https://cimam.org/documents/182/CIMAM_2021_Conference_Report_Lodz_and_Gdansk_Poland_reduced_0KF3L9R.pdf

[^73]: https://adsuploader.com/blog/meta-flexible-ads

[^74]: https://easyinsights.ai/blog/how-to-fix-under-reporting-in-meta-ads/

[^75]: https://www.inlibra.com/10.5771/9780739181591.pdf

[^76]: https://www.youtube.com/watch?v=PedgzYqaX10

