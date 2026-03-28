# Tab 1

---

## name: offer-architect description: \> Interview-based offer design and evaluation skill. Activates when user says "design an offer", "create an offer", "price my service", "value ladder", "Grand Slam Offer", "what should I charge", "how do I package", "offer architecture", "money model", or "Godfather offer". Conducts structured interview, scores offers on 6 dimensions \+ Value Equation, and produces an Offer Blueprint document. Handles full offer ecosystems (lead magnets, core, upsells, downsells, continuity). Also activates as INTERCEPTOR when user jumps to marketing/ads/copy without a defined offer. version: 1.0.0 changelog: | v1.0.0: Initial version. Synthesizes Hormozi (Value Equation, Grand Slam, Money Models), Brunson (Value Ladder, Big Domino, Stack Slide), Suby (Godfather Offer, Premiums), and Thiel (Monopoly Positioning) into a 6-phase interview with dual scoring.

# Offer Architect

## 1\. Purpose

Transform vague service or product ideas into scored, priced, and positioned offer architectures. This skill interviews the user, evaluates offers across multiple dimensions, and produces a structured Offer Blueprint document.

**Input**: A service, product, or business idea at any stage of development. **Output**: `{Service}_Offer_Blueprint.md` — a scored, priced offer with value ladder positioning.

This skill is a **conversational partner** — it asks questions, challenges assumptions, suggests improvements, and evaluates trade-offs. It does not just collect answers; it pushes back when something scores poorly and proposes alternatives.

---

## 2\. Trigger & Interceptor

### Direct Trigger

Activate when user mentions: offer design, offer architecture, pricing strategy, value ladder, Grand Slam Offer, Godfather offer, money model, "what should I charge", "how do I package", offer stacking, offer chain.

### Interceptor (CRITICAL)

**IF** user jumps to marketing, ads, funnels, or copy **AND** no defined offer exists:

1. **STOP.** Do not proceed with marketing tasks.  
2. **BLOCK** with: "You need an offer before you need a funnel. Let's design one first."  
3. **INITIATE** the Interview Flow.

   **Rationale**: Offer before funnel, funnel before traffic. Without a compelling offer, no amount of marketing will work.

   ---

   ## 3\. Core Philosophy

- **Value Equation**: `Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice)` — This skill OPERATIONALIZES it with scoring. See `references/value_equation_scoring.md`.  
- **"Make people an offer so good they would feel stupid saying no."** — Hormozi  
- **Starving crowd \> offer strength.** Market selection beats offer quality. Always validate the market first.  
- **Big Domino**: Find the ONE belief that if knocked down, all other objections become irrelevant. Every additional belief required drops conversion 50% (Perry Belcher). See Expert Secrets.  
- **"The business that can spend the most to acquire a customer wins."** — Dan Kennedy via Brunson. Your offer economics determine your competitive ceiling.  
- **Monopoly positioning**: "All happy companies are different" — Thiel. Your offer should be a category of one, impossible to compare to commodity alternatives.  
- **Simple scales, fancy fails**: 100 ways to offer your product, not 100 products. Perfect one offer at a time before adding the next.  
- **Sales-to-Fulfillment Continuum**: "Create flow. Monetize flow. Then add friction." Over-deliver first, then systematize.

  ---

  ## 4\. The Interview Flow

  Six phases. 2-5 questions per phase. Each phase ends with a synthesis confirmation before proceeding. Do NOT overwhelm — ask one phase at a time. If the user provides information proactively, merge phases.

  ### Phase 1: Market & Niche (2-3 questions)

  **Goal**: Validate the starving crowd before designing the offer.

  **Questions**:

1. What do you sell, or plan to sell? (product/service, physical/digital/hybrid)  
2. Who is your buyer? (B2B/B2C, demographics, psychographics, purchasing power)  
3. What is their BURNING pain — the thing that keeps them up at night?

   **Optional**: Where do they congregate online? (communities, platforms, influencers they follow)

   **Synthesis**: Perform the **Starving Crowd Check** (3-point validation):

| Check | Pass | Fail |
| :---- | :---- | :---- |
| Urgent pain? | They're actively seeking solutions, spending money on alternatives | "Nice to have", no urgency |
| Purchasing power? | They have money and willingness to spend | Can't afford solutions |
| Reachable? | You know where to find them, can target them affordably | Scattered, expensive to reach |

   If any check fails, **flag it** and discuss before continuing. A weak market cannot be fixed by a strong offer.

   ### Phase 2: Dream Outcome (3-4 questions)

   **Goal**: Define the destination, not the vehicle.

   **Questions**:

1. What is your buyer's DREAM outcome? Not your product — the result. The "Heaven" state. What does their life look like AFTER?  
2. What is their CURRENT reality? The "Hell" state. What does life look like without you?  
3. What have they tried before, and why did it fail? (Failed solutions \= positioning gold)  
4. What is the ONE thing they must believe for everything else to fall into place? (The Big Domino)

   **Synthesis**: Draft the **Dream Outcome Statement**:

"I help \[AVATAR\] achieve \[DREAM OUTCOME\] without \[EFFORT/SACRIFICE\] in \[TIME FRAME\]."

Also draft the **Big Domino**:

"If I can make people believe that \[X is the key to Y\] and is only attainable through \[MY SOLUTION\], then all other objections become irrelevant."

Confirm both with user before proceeding.

### Phase 3: Problems & Solutions (3-5 questions)

**Goal**: Map every obstacle between the buyer and their dream outcome.

**Process**:

1. "List every obstacle your buyer faces on their way to the dream outcome. Think about what happens BEFORE, DURING, and AFTER using your solution. The more problems, the better — each is an opportunity for value."  
2. For each obstacle: "What is your solution?"  
3. For each solution: "How would you deliver it?" Use the Delivery Vehicle Matrix:  
   - **Attention level**: 1-on-1 / Small group / 1-to-many  
   - **Effort level**: DFY (done for you) / DWY (done with you) / DIY (do it yourself)  
   - **Medium**: In-person / Phone / Video / Email / Chat / Recorded / Software  
4. "Which solutions already exist (you've built them) vs. need to be created?"  
5. Apply the **10x-to-1/10th test**: "If they paid you 10x your price, what would you provide? If they paid 1/10th, how would you STILL deliver value?"

   **Synthesis**: Build the **Solution Stack Table**:

| \# | Obstacle | Solution | Vehicle | DFY/DWY/DIY | Exists? |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | {obstacle} | {solution} | {vehicle} | {type} | Yes/No |

   ### Phase 4: Trim, Stack & Price (3-4 questions)

   **Goal**: Bundle the solutions into a high-value, high-margin offer.

   **Process**:

1. **Trim**: Remove items that are high cost \+ low value. Then remove low cost \+ low value. What remains should be low cost \+ high value AND high cost \+ high value.  
2. For each remaining item: "What is this worth individually?" (anchor price for the stack)  
3. "Which items are CORE (essential to the promise) vs BONUSES (valuable extras)?"  
4. "What guarantee would make this a no-brainer?" See `references/offer_enhancers.md` for guarantee types.  
5. "What is your target price point?" Or: "What does the competition charge?"

   **Synthesis**: Build the **Stack Slide**:

```
Core: [Name] .......................... Value: $X,XXX
Bonus 1: [Name] ...................... Value: $X,XXX
Bonus 2: [Name] ...................... Value: $XXX
Premium: [Name] ...................... Value: $XXX
                      Total Value:   $XX,XXX
                     Your Price:     $X,XXX
                     Value Ratio:    XX:1
```

   **Minimum target**: 10:1 value-to-price ratio. If below 3:1, add more bonuses or restructure.

   ### Phase 5: Offer Position & Chain (2-3 questions)

   **Goal**: Place this offer in the value ladder and money model context.

   **Questions**:

1. "Where does this offer sit on the value ladder?" (Lead Magnet / Frontend / Middle / Backend / High-Ticket / Continuity) See `references/value_ladder_and_money_models.md`.  
2. "What comes BEFORE this offer? How does the buyer discover you and get warmed up?"  
3. "What comes AFTER this offer? What is the natural next purchase? What problem does THIS offer CREATE that the next offer SOLVES?"

   **For "no" scenarios**: "If someone says no to this offer, what would you offer instead? Same thing with different payment terms, or a different/smaller thing?" See Downsell rules in `references/value_ladder_and_money_models.md`.

   **Synthesis**: Render the **Ecosystem View**:

```
[Lead Magnet] --> [Frontend $XX] --> [THIS OFFER $XXX] --> [Upsell $X,XXX] --> [Continuity]
  Type: HVCO      Type: Decoy       Type: Grand Slam      Type: Classic        Type: Bonus
  Stage: I         Stage: I           Stage: I               Stage: II            Stage: III
  Score: --        Score: --          Score: 55 <--CURRENT   (not designed)       (not designed)
```

   ### Phase 6: Enhance & Name (2-3 questions)

   **Goal**: Polish the offer with enhancers and create compelling names.

   **Questions**:

1. "Is there any REAL scarcity? Limited capacity, limited spots, limited inventory? What is the genuine reason you can't serve unlimited people?"  
2. "Any urgency triggers? Seasonal, event-based, deadline, price increase?"  
3. "What premiums could you include? What is a high-perceived-value, low-cost gift that complements the offer?"  
4. For naming — gather MAGIC components: "Who is the avatar? What is the goal/outcome? What is the timeframe? What container word fits?"

   **Synthesis**:

- Generate **3-5 MAGIC name options** using `references/naming_formulas.md`  
- Identify the **3 False Beliefs** (Vehicle, Internal, External) and suggest counter-stories  
- Outline the **Epiphany Bridge** story arc

  ---

  ## 5\. Scoring Framework

  After all 6 phases, score the offer using two systems.

  ### 5A: 6-Dimension Offer Score (max 60\)

| Dimension | What It Measures | Scoring Guide |
| :---- | :---- | :---- |
| Attractiveness | "I need that" reaction, Godfather quality | 10 \= people beg to buy; 1 \= "meh" |
| Pattern Interrupt | Breaks expectations vs. market norms | 10 \= category of one; 1 \= commodity |
| Ease of Understanding | Big Domino clarity — one belief, one sentence | 10 \= instantly clear; 1 \= needs 30-min explanation |
| Ease of Delivery | Sales-Fulfillment Continuum position | 10 \= automated/trivial; 1 \= fly-out-and-live-with-them |
| Time to Value | Speed of client's first meaningful result | 10 \= instant; 1 \= 12+ months |
| Time to Money | Speed of seller's CAC recovery | 10 \= same day; 1 \= 12+ months |

  **Thresholds**:

- **50-60**: GREEN LIGHT — proceed to blueprint  
- **35-49**: YELLOW — refine weak dimensions before finalizing  
- **Below 35**: RED — fundamental redesign needed

  ### 5B: Value Equation Score (max 80 combined)

  Scored from BOTH buyer and seller perspectives (1-10 per factor). See `references/value_equation_scoring.md` for detailed anchors.

| Factor | Buyer /10 | Seller /10 |
| :---- | :---- | :---- |
| Dream Outcome | How desirable? | How meaningful to deliver? |
| Perceived Likelihood | Believes it works? | Confident in delivery? |
| Time Delay (inverse) | Fast results? 10=instant | Fast to fulfill? 10=instant |
| Effort & Sacrifice (inverse) | Easy for buyer? 10=effortless | Easy to operate? 10=automated |

  **Thresholds**: 65-80 GREEN, 45-64 YELLOW, Below 45 RED

  **Divergence Alert**: Flag any factor where buyer and seller scores differ by 5+ points.

  ### 5C: Profitability Assessment

| Metric | How to Calculate |
| :---- | :---- |
| Gross Margin | (Price \- Fulfillment Cost) / Price |
| Scalability | Can you 10x clients without 10x-ing effort? Low/Med/High |
| CAC Recovery | Days to recover customer acquisition cost. Target: under 30 days |
| LTV:CAC | Estimated lifetime value vs acquisition cost. Target: 3:1+ |

  ---

  ## 6\. Offer Chaining

  When designing multiple offers in an ecosystem:

- Discuss ONE offer at a time through all 6 phases  
- After scoring and blueprinting, render the Ecosystem View  
- When adding another offer: Phase 1 (Market/Niche) is pre-filled from the first offer  
- **Transition question**: "What problem does this offer CREATE that the next offer SOLVES?"  
- For each new offer, specify its **Money Model type**: Attraction, Upsell, Downsell, or Continuity  
- Follow the 3-Stage development: perfect Stage I before adding Stage II, then Stage III

  See `references/value_ladder_and_money_models.md` for complete chaining mechanics.

  ---

  ## 7\. Output

  After scoring passes GREEN or YELLOW (with noted improvements), generate the Offer Blueprint:

  **File**: `{Service}_Offer_Blueprint.md` **Template**: `references/blueprint_template.md`

  The blueprint contains 14 sections covering identity, beliefs, solution stack, stack slide, pricing, guarantee, enhancers, both score cards, profitability, ecosystem view, naming options, Epiphany Bridge story, and next steps.

  ---

  ## 8\. Integration Points

| Direction | Skill | Handoff |
| :---- | :---- | :---- |
| Upstream (optional) | `client-researcher` | Audience data, customer language, competitor analysis |
| Downstream | `creative-angle-writer` | Big Domino \+ 3 False Beliefs → GAM angle files |
| Downstream | `meta_ads_strategist` | Offer architecture → ad strategy and briefs |

  ---

  ## 9\. Troubleshooting

| Symptom | Diagnosis | Fix |
| :---- | :---- | :---- |
| Value ratio below 3:1 | Stack too thin or price too high | Add bonuses/premiums. Suby: premiums can 2x-3x sales |
| Can't explain in one sentence | Multiple beliefs required | Find the Big Domino. Each extra belief \= 50% conversion drop (Belcher) |
| RED on Ease of Delivery | Too much custom/manual work | Apply 10x-to-1/10th test. Convert DFY to DWY with templates |
| RED on Time to Value | Results take too long | Add "quick win" — first 48-72 hour deliverable |
| Buyer \+ Seller scores diverge by 5+ | Misalignment — seller hates delivering or buyer doesn't believe | Redesign delivery vehicle or add proof elements |
| No natural "before" offer | Cold traffic problem | Design a lead magnet first: 3 types x 4 delivery methods \= 12 options |
| Offer fatigue after months | Market saturated on wrapper | Change creative → copy → name → duration → giveaway. Machine \= last resort |
| "Competitor X is $29/mo" | Commodity comparison | You're selling the plane flight, not the vacation. Reframe around dream outcome |
| Starving Crowd Check fails | Wrong market, not wrong offer | Pivot market before refining offer. "Starving crowd \> offer strength" |
| Guarantee feels too risky | Fear of refunds | Do the math: 130% more sales with 2x refund rate \= 23% net increase. See `references/offer_enhancers.md` |


# Tab 2

# Offer Blueprint Template

Use this template to generate the final output document after completing all 6 interview phases.

Replace all `{PLACEHOLDER}` values with actual content from the interview.

---

```
# Offer Blueprint: {OFFER_NAME}

**Version:** {VERSION} | **Date:** {DATE} | **Status:** {DRAFT/FINAL}
**Architect:** offer-architect v1.0.0

---

## 1. Offer Identity

- **Name:** {MAGIC_NAME}
- **One-Sentence Pitch:** {ELEVATOR_PITCH}
- **Avatar:** {WHO — specific description}
- **Niche/Market:** {MARKET}
- **Value Ladder Tier:** {TIER: Lead Magnet / Frontend / Middle / Backend / High-Ticket / Continuity}
- **Money Model Type:** {TYPE: Attraction / Upsell / Downsell / Continuity}
- **Money Model Stage:** {STAGE: I / II / III}

---

## 2. Dream Outcome & Belief Architecture

**Dream Outcome Statement:**
> "I help {AVATAR} achieve {DREAM_OUTCOME} without {EFFORT/SACRIFICE} in {TIME_FRAME}."

**Current Reality (Hell):** {CURRENT_STATE — what life looks like without the solution}

**Desired Reality (Heaven):** {DESIRED_STATE — what life looks like after the transformation}

**Big Domino Belief:**
> "If I can make people believe that {X is the key to Y} and is only attainable through {MY_SOLUTION}, then all other objections become irrelevant."

**3 False Beliefs:**

| Belief Type | False Belief | Counter-Story / Evidence |
| --- | --- | --- |
| Vehicle | "{THIS_WON'T_WORK}" | {COUNTER} |
| Internal | "{I_CAN'T_DO_THIS}" | {COUNTER} |
| External | "{OUTSIDE_MY_CONTROL}" | {COUNTER} |

---

## 3. Solution Stack

| # | Obstacle | Solution | Delivery Vehicle | DFY/DWY/DIY | Perceived Value |
| --- | --- | --- | --- | --- | --- |
| 1 | {OBSTACLE_1} | {SOLUTION_1} | {VEHICLE_1} | {TYPE} | ${VALUE} |
| 2 | {OBSTACLE_2} | {SOLUTION_2} | {VEHICLE_2} | {TYPE} | ${VALUE} |
| 3 | {OBSTACLE_3} | {SOLUTION_3} | {VEHICLE_3} | {TYPE} | ${VALUE} |
| ... | ... | ... | ... | ... | ... |

---

## 4. The Stack Slide

{CORE_OFFER_NAME}:
  {COMPONENT_1} .......................... Value: ${VALUE_1}
  {COMPONENT_2} .......................... Value: ${VALUE_2}
  {COMPONENT_3} .......................... Value: ${VALUE_3}

Bonuses:
  {BONUS_1} .............................. Value: ${BONUS_VALUE_1}
  {BONUS_2} .............................. Value: ${BONUS_VALUE_2}

Premium:
  {PREMIUM} .............................. Value: ${PREMIUM_VALUE}

                          Total Value:   ${TOTAL_VALUE}
                         Your Investment: ${PRICE}
                         Value Ratio:     {RATIO}:1

---

## 5. Pricing & Economics

| Metric | Value |
| --- | --- |
| **Price** | ${PRICE} |
| **Total Perceived Value** | ${TOTAL_VALUE} |
| **Value-to-Price Ratio** | {RATIO}:1 |
| **Cost of Fulfillment** | ${FULFILLMENT_COST} |
| **Gross Margin** | {MARGIN}% |
| **Estimated CAC** | ${CAC} |
| **CAC Recovery Timeline** | {DAYS} days |
| **Estimated LTV** | ${LTV} |
| **LTV:CAC Ratio** | {LTV_CAC_RATIO}:1 |

---

## 6. Guarantee

- **Type:** {GUARANTEE_TYPE}
- **Statement:** "{GUARANTEE_TEXT}"
- **Conditions (if any):** {CONDITIONS}
- **Rationale:** {WHY_THIS_GUARANTEE}
- **Refund risk estimate:** {ESTIMATED_REFUND_RATE}%

---

## 7. Enhancers

| Enhancer | Details |
| --- | --- |
| **Scarcity** | {SCARCITY_DESCRIPTION — or "None (not applicable)"} |
| **Urgency** | {URGENCY_DESCRIPTION — or "None (not applicable)"} |
| **Bonuses** | {BONUS_LIST_WITH_VALUES} |
| **Premiums** | {PREMIUM_DESCRIPTION — or "None"} |

---

## 8. 6-Dimension Score Card

| Dimension | Score (/10) | Rationale |
| --- | --- | --- |
| Attractiveness | {SCORE} | {WHY} |
| Pattern Interrupt | {SCORE} | {WHY} |
| Ease of Understanding | {SCORE} | {WHY} |
| Ease of Delivery | {SCORE} | {WHY} |
| Time to Value | {SCORE} | {WHY} |
| Time to Money | {SCORE} | {WHY} |
| **TOTAL** | **{TOTAL}/60** | **{GREEN/YELLOW/RED}** |

---

## 9. Value Equation Score Card

| Factor | Buyer (/10) | Seller (/10) | Notes |
| --- | --- | --- | --- |
| Dream Outcome | {B_SCORE} | {S_SCORE} | {NOTES} |
| Perceived Likelihood | {B_SCORE} | {S_SCORE} | {NOTES} |
| Time Delay | {B_SCORE} | {S_SCORE} | {NOTES} |
| Effort & Sacrifice | {B_SCORE} | {S_SCORE} | {NOTES} |
| **TOTAL** | **{B_TOTAL}/40** | **{S_TOTAL}/40** | **Combined: {COMBINED}/80 — {VERDICT}** |

**Divergence Alerts:** {ANY_FACTORS_WHERE_BUYER_SELLER_DIFFER_BY_5+}

---

## 10. Profitability Assessment

| Metric | Value | Assessment |
| --- | --- | --- |
| Gross Margin | {MARGIN}% | {HIGH/MED/LOW} |
| Scalability | {LOW/MED/HIGH} | {RATIONALE} |
| LTV:CAC | {RATIO}:1 | {HEALTHY/AT_RISK/UNSUSTAINABLE} |
| 30-Day CAC Recovery | {YES/NO} | {DETAILS} |

---

## 11. Value Ladder / Ecosystem View

{ECOSYSTEM_DIAGRAM — see references/value_ladder_and_money_models.md for format}

---

## 12. Naming Options

| # | Name | MAGIC Components | Rationale |
| --- | --- | --- | --- |
| 1 | {NAME_1} | {M+A+G+I+C used} | {WHY_IT_WORKS} |
| 2 | {NAME_2} | {M+A+G+I+C used} | {WHY_IT_WORKS} |
| 3 | {NAME_3} | {M+A+G+I+C used} | {WHY_IT_WORKS} |

**Recommended:** #{RECOMMENDED_NUMBER} — {REASONING}

---

## 13. Epiphany Bridge Story Arc

| Element | Content |
| --- | --- |
| **Backstory** | {HOW_YOU_DISCOVERED_THIS — your origin in this space} |
| **The Wall** | {WHAT_WASN'T_WORKING — the failure/frustration} |
| **Epiphany** | {THE_AHA_MOMENT — what changed everything} |
| **The Plan** | {WHAT_YOU_DID_DIFFERENTLY} |
| **The Result** | {THE_TRANSFORMATION_YOU_ACHIEVED} |
| **The Offer** | {NATURAL_TRANSITION — "and now I packaged this into..."} |

**"Kinda Like" Bridge:** {SIMPLIFIED_ANALOGY — "It's kinda like [familiar concept]"}

---

## 14. Next Steps

1. {NEXT_STEP_1 — e.g., "Build the core delivery system for Component 1"}
2. {NEXT_STEP_2 — e.g., "Create the lead magnet that feeds this offer"}
3. {NEXT_STEP_3 — e.g., "Write 3 Epiphany Bridge stories for the 3 False Beliefs"}
4. {NEXT_STEP_4 — e.g., "Test 3 offer names with dark post A/B test ($50 budget)"}
5. {NEXT_STEP_5 — e.g., "Design the upsell offer that solves the problem this offer creates"}

---

*Generated by offer-architect v1.0.0 — Frameworks: Hormozi (Value Equation, Grand Slam, Money Models), Brunson (Value Ladder, Big Domino, Stack Slide), Suby (Godfather Offer), Thiel (Monopoly Positioning)*
```

# Tab 3

# Offer Naming — MAGIC Formula & Container Words

## The MAGIC Formula (Hormozi)

Not all components are mandatory. Use 3-5 in combination. Shorter and punchier wins. The only way to know what works is to write names out and test them.

| Component | Purpose | Maps To |
| :---- | :---- | :---- |
| **M** — Magnetic Reason Why | Tells people WHY you're making this offer | Attention |
| **A** — Announce Your Avatar | Calls out exactly WHO this is for | Discrimination |
| **G** — Give Them a Goal | Articulates the DREAM OUTCOME | Purpose |
| **I** — Indicate a Time Period | Shows HOW LONG it takes | Timeline |
| **C** — Complete with Container Word | Signals this is a SYSTEM/BUNDLE, not commodity | Method |

---

### M — Magnetic Reason Why

Answers: "Why are they making this great offer?" or "What's in it for me?"

Think like a fraternity party planner — the reason can be anything as long as you believe it.

**Examples**: Free, 88% off, Giveaway, Grand Opening, New Management, Anniversary, Back to School, New Year, Spring, Summer, Holiday, Black Friday, Launch, Limited Release

### A — Announce Your Avatar

Call out your ideal buyer. Be as specific as possible. In local markets: go hyperlocal.

**Examples**: Busy Dads, SaaS Founders, E-commerce Store Owners, Lakeway Moms, First-Time Homebuyers, Agency Owners Under $50k/mo, Coaches With No Clients

**Rule**: Not "Baltimore" but "Towson, MD." Not "entrepreneurs" but "solo consultants making $5-15k/mo."

### G — Give Them a Goal

Articulate the dream outcome. Can be an event, feeling, experience, or measurable result. The more specific and tangible, the better.

**Examples**: Pain Free, Celebrity Smile, 1st Place, Double Your Profit, First 5 Clients, Grand Slam Offer, Little Black Dress, $10k Month, Perfect Product, 7-Figure, Never Out Of Breath

### I — Indicate a Time Period

Duration to expect results. Adds urgency and believability.

**Warning**: If making quantifiable income/outcome claims with a duration, many ad platforms will reject it (implies guarantee). Use non-claim goals with duration, or save duration for non-regulated channels.

**Examples**: 4 Hour, 14 Day, 21 Day, 6 Week, 3 Month, 90 Day, 12 Month

### C — Complete with Container Word

Signals this is a bundled system, not a single product. Makes it impossible to compare to commodity alternatives.

---

## Container Word Taxonomy

| Container Word | Connotation | Best For |
| :---- | :---- | :---- |
| Challenge | Low commitment, gamified, community | Frontend, lead magnets |
| Blueprint | Step-by-step, visual, actionable | Courses, frameworks |
| Bootcamp | Intense, short-term, transformative | Short programs (1-4 weeks) |
| Intensive | Deep, focused, high-effort short period | Weekend/week-long programs |
| Incubator | Nurturing, developmental, emerging | Early-stage businesses |
| Masterclass | Premium, expert-level, polished | Mid-high ticket courses |
| Program | Structured, professional, multi-phase | Multi-week/month offerings |
| System | Proven, mechanical, repeatable | Methodologies, processes |
| Accelerator | Speed, momentum, fast results | Time-compressed transformations |
| Fast Track | Shortcut, skip-the-line | Premium tiers of existing offers |
| Sprint | Short, intense, specific goal | 1-2 week focused pushes |
| Experience | Immersive, memorable, premium | Events, retreats |
| Summit | Community, expert access, event-like | Virtual events, conferences |
| Academy | Depth, transformation, long-term | Comprehensive learning programs |
| Mastermind | Peer group, accountability, high-level | High-ticket group offerings |
| Workshop | Hands-on, practical, do-it-now | Half/full-day sessions |
| Deep Dive | Thorough, investigative | Audit/analysis services |
| Transformation | Complete change, before/after | Identity-level change offers |
| Launch | Beginning, new start, momentum | New product/service introductions |
| Toolkit | Practical, ready-to-use, assets | Template/resource packages |

---

## Worked Examples

| Niche | MAGIC Name | Components Used |
| :---- | :---- | :---- |
| Dentist | $2,000-Off Celebrity Smile Transformation | M \+ G \+ C |
| Dentist | Lakeway Moms — 12 Months to a Perfect Smile ($1000 off for 15 families) | A \+ I \+ G \+ M |
| Fitness | Grand Opening Free X-Ray & Treatment — Instant Relief | M \+ G |
| Coaching | 5 Clients in 5 Days Blueprint | G \+ I \+ C |
| Agency | 7F Agency 12 Week Intensive | A \+ G \+ I \+ C |
| E-commerce | 14 Day Find Your Perfect Product Launch | I \+ G \+ C |
| Gym | Fill Your Gym in 30 Days (Free\!) | G \+ I \+ M |
| Weight Loss | Back Sore No More\! 90 Day Rapid Healing Intensive (81% off\!) | G \+ I \+ C \+ M |
| Massage | Free Six-Week Stress Release Challenge | M \+ I \+ G \+ C |
| SaaS | $0 Setup — Double Your Pipeline 90-Day Accelerator for B2B Founders | M \+ G \+ I \+ C \+ A |

---

## Name Sub-Items and Bonuses

Apply MAGIC to EVERY component in your stack, not just the main offer.

**Problem → Solution Wording → Sexier Bundle Name**

Examples from Hormozi's weight loss offer:

- Buying food → "How anyone can buy food fast, easy, cheaply" → **Foolproof Bargain Grocery System** ($1,000 value)  
- Eating healthy → "Personalized plan so good you won't miss junk food" → **Lick Your Fingers Good Meal Plan** ($500 value)  
- Exercise → "Workouts proven to burn more fat than going alone" → **Fat Burning Workouts** ($699 value)  
- Traveling → "Get amazing workouts with no equipment" → **Tone Up While You Travel Blueprint** ($199 value)  
- Accountability → "System that works without your permission" → **Never Fall Off Accountability System** ($1,000 value)  
- Social eating → "Freedom to eat out without being the odd one out" → **Live It Up While Slimming Down Eating Out System** ($349 value)

  **Total perceived value: $4,351. Price: $599. That's 7.3:1 value ratio.**

  ---

  ## Anti-Patterns (Names That Fail)

- Too generic: "Business Coaching Package" (commodity)  
- No avatar: "Marketing Course" (for whom?)  
- No outcome: "Module 1-12 Video Series" (so what?)  
- Too long: 15+ words become unmemorable  
- Jargon: uses insider language the buyer doesn't know yet  
- No container word: "Lose Weight Program" → just a description, not a branded system

  ---

  ## Offer Fatigue & Name Rotation

  Offers fatigue over time, especially in local markets. When they do, change the WRAPPER, not the offer.

  **Rotation Priority** (change top first, bottom last):

1. Creative (images, videos) — cheapest to change  
2. Ad copy (hooks, headlines) — easy to change  
3. Offer NAME/wrapper — moderate change  
4. Duration (6 weeks → 28 days → 8 weeks) — small operational change  
5. What you give away free/discounted — moderate operational change  
6. The actual offer structure — LAST RESORT, heavy operational change

   **Example**: "Six-Week Stress Release Challenge" → "42-Day Relaxing Holidays Challenge" — same core offer, different wrapper.

   ---

   ## Name Testing (from $100M Leads)

"When you have written your headline, you have spent 80 cents of your advertising dollar." — David Ogilvy

**What to test (in order)**: Headline \> Image \> Subheadline

**Methods**:

- Run polls on social if you have a following  
- Post on every platform asking for responses (Option 1 vs Option 2\)  
- Dark post A/B tests on Facebook with small budget ($50-500)  
- Message people directly and ask


# Tab 4

# Offer Enhancers — Guarantees, Scarcity, Urgency, Bonuses, Premiums

## Guarantees

"The single greatest objection for any product or service being sold is RISK." — Hormozi

A guarantee can 2-4x conversion just by changing its quality (Jason Fladlien).

**Structure**: "If you do not get X result in Y time period, we will Z."

Without the "or what" portion, the guarantee sounds weak. Always include it.

### Guarantee Types

| Type | Description | Risk to Seller | Best For |
| :---- | :---- | :---- | :---- |
| **Unconditional** | Full refund, no questions asked | High | Low-ticket B2C, digital products |
| **Conditional: Outsized Refund** | 2x-3x money back if conditions met | Medium-High | High-margin products with consumption conditions |
| **Conditional: Modified Service** | Extra Y period free if no result | Medium | Service businesses with clear timelines |
| **Conditional: Credit-Based** | Money back as credit toward other services | Low | Upsell sequences, maintaining goodwill |
| **Conditional: Personal Service** | Work 1-on-1 free until result achieved | Medium | Premium services with strong confidence |
| **Conditional: Release of Service** | Let them out of contract free | Low | Businesses with contracts/commitments |
| **Conditional: Delayed 2nd Payment** | Don't bill again until first result | Medium | Activation-driven businesses |
| **Conditional: First Outcome** | Pay ancillary costs until first result | Medium | Agency/ad-spend models |
| **Anti-Guarantee** | All sales final — exclusive access | None | Ultra-premium, "once seen can't be unseen" |
| **Performance/Revshare** | Pay only for results | Variable | Agencies, consulting, quantifiable outcomes |
| **Profit-Share** | X% of profit generated | Variable | Long-term partnerships |
| **Ratchet** | 10% if over X, 20% if over Y, 30% if over Z | Variable | Scaling partnerships |

### Guarantee Math

Even if refund rate doubles, stronger guarantees almost always net positive:

```
Without guarantee:  100 sales, 5 refunds (5%)  = 95 net sales
With guarantee:     130 sales, 13 refunds (10%) = 117 net sales
Net improvement: 117/95 = 1.23x (23% increase)
```

For a guarantee to NOT be worth it, the absolute increase in refunds would have to fully offset the absolute increase in sales. This almost never happens.

### Guarantee Decision Tree

```
Q: Is your cost of fulfillment high per client?
├─ YES → Use Conditional or Anti-Guarantee (you can't eat fulfillment cost + refund)
└─ NO
   Q: Is your price point low (<$500)?
   ├─ YES → Unconditional works well (most won't bother refunding)
   └─ NO
      Q: Are your results measurable and predictable?
      ├─ YES → Performance/Revshare or Conditional (outsized/personal service)
      └─ NO → Modified Service guarantee or Credit-Based
```

### Pro Tip: Unconditional vs Conditional by Business Type

- **Low-ticket B2C**: Bigger, broader unconditional guarantees work best (many people won't bother)  
- **High-ticket B2B**: Specific conditional guarantees with conditions tied to actions \+ results  
- **Agency/Services**: Performance-based or revshare — perfect alignment between client and provider

  ---

  ## Premiums (Strategic Free Gifts)

"Premiums can double or triple sales." — Suby

**What**: A free gift included with purchase that has high perceived value but low cost to deliver.

**Sports Illustrated Case Study**: 1986, subscriptions were tanking. Added a Football Phone as premium. Result: 1.6 million subscriptions. The premium sold the product.

### Criteria for Great Premiums

| Criterion | Why |
| :---- | :---- |
| Aligned with your business | Reinforces your brand and value proposition |
| Relevant to the buyer | Solves a related problem they have |
| High perceived value | Buyer thinks it's worth a lot |
| Low cost to deliver | Doesn't kill your margins |

### Premium Examples by Industry

| Industry | Premium |
| :---- | :---- |
| Identity theft insurance | Free document shredder |
| Homebuilder | $5,000 furniture and appliances voucher |
| Car detailing | New floor mats |
| Moving company | Free bond recovery kit or lease-end cleaning |
| Divorce lawyer | Free $500 travel voucher |
| SaaS | Free 1-on-1 onboarding call |
| Online course | Physical workbook shipped to door |
| Agency | Free audit or strategy document |

---

## Scarcity

"If I don't act now, when will I act? Never." — The question scarcity answers

**CRITICAL**: Must be GENUINE. Fake scarcity (countdown timers that reset) erodes trust permanently. Once trust is destroyed, it cannot be rebuilt.

### Types of Real Scarcity

| Type | How It Works | Example |
| :---- | :---- | :---- |
| Capacity-Based | Limited by your ability to serve | "We can only take 10 clients per quarter because each gets 4 hours of 1-on-1 time" |
| Cohort-Based | Limited by enrollment window | "Next cohort starts March 1, only 20 spots" |
| Resource-Based | Limited physical inventory or materials | "Only 500 copies of the physical edition" |
| Time-Based | Offer disappears after date | "Enrollment closes Friday at midnight" |

### Scarcity Best Practices

- State the REASON for the scarcity (makes it believable)  
- "Because" increases compliance — any reason works better than no reason (Harvard study)  
- If you can't find real scarcity, don't fake it — use urgency instead

  ---

  ## Urgency

  **Distinct from scarcity**: Scarcity \= limited quantity. Urgency \= limited time.

| Type | How It Works | Example |
| :---- | :---- | :---- |
| Deadline-Based | Offer expires on a specific date | "Enrollment closes Friday at midnight" |
| Event-Based | Tied to external event or season | "Pre-conference pricing ends when doors open" |
| Price-Based | Price increases after threshold | "Price goes up by $500 after the first 50 sign up" |
| Seasonal | Natural calendar urgency | "Back-to-school special", "New Year transformation" |

  ---

  ## Bonuses

"But wait, there's more\!" — the infomercial principle, but done strategically

### Rules for Effective Bonuses

1. Each bonus should solve a DISTINCT related problem (not the same problem as the core offer)  
2. Each bonus should be individually priced in the stack (anchors perceived value)  
3. Bonuses should have HIGH perceived value, LOW fulfillment cost  
4. Name each bonus using the MAGIC formula (see `references/naming_formulas.md`)  
5. Bonuses should make the offer feel "unfair" in favor of the buyer

   ### The Stack Effect

   When presenting the offer, list each component with its individual value:

```
Core: [Name] ........................ Value: $X,XXX
Bonus 1: [Name] .................... Value: $X,XXX
Bonus 2: [Name] .................... Value: $XXX
Bonus 3: [Name] .................... Value: $XXX
Premium: [Name] .................... Value: $XXX
                     Total Value:   $XX,XXX
                    Your Price:     $X,XXX
                    Savings:        XX%
```

   This visual stacking creates the "I get all this for only THAT?" reaction — the hallmark of a Grand Slam Offer.

   

   

# Tab 5

# Value Equation — Scoring Rubric

## The Equation

```
Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice)
```

**Goal**: Maximize the numerator (top), minimize the denominator (bottom) toward zero. Anything divided by zero \= infinite value.

**Perception IS Reality**: The London Underground's biggest increase in rider satisfaction wasn't faster trains — it was a dotted map showing when the next train was coming. The perceived decrease in wait time drove more satisfaction than actual speed improvements. Your offer's value is what the buyer PERCEIVES, not what you know to be true.

---

## Dual-Perspective Scoring

Every offer is scored from TWO perspectives:

| Perspective | Why It Matters |
| :---- | :---- |
| **Buyer** | Does the buyer perceive this as high value? Will they buy? |
| **Seller** | Is this sustainable, profitable, and energizing to deliver? |

An offer scoring 10/10 for buyers but 2/10 for sellers will kill the business. An offer scoring 10/10 for sellers but 2/10 for buyers won't sell. Both must score well.

---

## Factor 1: Dream Outcome (MAXIMIZE)

**What it measures**: How desirable is the end result? Not the product — the DESTINATION.

"No one wants a membership; they want to lose weight." — Hormozi

| Score | Buyer Perspective | Seller Perspective |
| :---- | :---- | :---- |
| 1-2 | Vague aspiration, can't visualize the outcome | Feels meaningless to deliver |
| 3-4 | Clear but not emotionally charged | Competent but not passionate |
| 5-6 | Specific and desirable, can picture it | Proud to deliver, sees impact |
| 7-8 | Emotionally charged, tells friends about it | Energized, mission-aligned |
| 9-10 | Life-changing, "I would do anything for this" | "This is my life's work" |

**Improvement Levers**:

- Reframe product as destination: "6-week coaching" → "First 5 clients in 30 days"  
- Use customer language (verbatim quotes about their dream)  
- Make the outcome specific and measurable: not "grow your business" but "add $10k/month"  
- Apply Inversion: "Get \[Dream\] WITHOUT \[Sacrifice\]"

  ---

  ## Factor 2: Perceived Likelihood of Achievement (MAXIMIZE)

  **What it measures**: Does the buyer believe THEY can achieve this result with YOUR solution?

| Score | Buyer Perspective | Seller Perspective |
| :---- | :---- | :---- |
| 1-2 | "Sounds too good to be true" / No proof | Not confident in delivery; untested |
| 3-4 | Believes it works for some people, not them | Can deliver but inconsistent results |
| 5-6 | Sees relevant social proof, cautiously optimistic | Reliable process, most clients succeed |
| 7-8 | Strong guarantee \+ case studies of people like them | Proven system, high success rate |
| 9-10 | "If THEY did it, I definitely can" — overwhelming evidence | 95%+ success rate with clear metrics |

  **Improvement Levers**:

- Social proof: testimonials from people LIKE the buyer (same situation, same doubts)  
- Guarantees: shift risk from buyer to seller (see `references/offer_enhancers.md`)  
- Specificity: "283 students have completed this" \> "hundreds of students"  
- Authority: endorsements, credentials, media features  
- Case studies with before/after and timeline  
- "Legal" language (Hormozi): "swears under oath" type conviction

  ---

  ## Factor 3: Time Delay (MINIMIZE — score INVERSELY)

  **What it measures**: How long until the buyer sees the first meaningful result?

"The best companies make things immediate, seamless, and effortless. Amazon made purchasing one click. Apple made the iPhone effortless." — Hormozi

| Score | Buyer Perspective | Seller Perspective |
| :---- | :---- | :---- |
| 1-2 | 12+ months to see any result | 12+ months to fulfill per client |
| 3-4 | 3-6 months to first meaningful result | Months of setup before delivery |
| 5-6 | 4-8 weeks to first result | Can start delivering within a week |
| 7-8 | 1-2 weeks to first result | Systems in place, onboarding is fast |
| 9-10 | Same-day or instant result | Automated or near-instant delivery |

**Note**: Score 10 \= FAST (low delay). Score 1 \= SLOW (high delay). We score inversely because we want to DECREASE time delay.

**Improvement Levers**:

- Add a "Quick Win" component: what can you deliver in the first 48-72 hours?  
- Front-load the most visible result  
- "Instant access" to digital materials upon purchase  
- First milestone within first week  
- Show progress indicators (the "dotted map" principle)

  ---

  ## Factor 4: Effort & Sacrifice (MINIMIZE — score INVERSELY)

  **What it measures**: How much work, discomfort, or sacrifice does the buyer have to endure?

"This is the strongest lever. 'Without cardio', 'Done-for-you', 'Cheatsheet'." — Hormozi

| Score | Buyer Perspective | Seller Perspective |
| :---- | :---- | :---- |
| 1-2 | Massive lifestyle change required, painful process | Requires constant hand-holding |
| 3-4 | Significant effort, must learn new skills | Labor-intensive fulfillment |
| 5-6 | Moderate effort, guided process | Manageable with systems |
| 7-8 | Minimal effort, mostly plug-and-play | Mostly automated, light touch |
| 9-10 | Effortless — "done for you" or "works without your permission" | Fully systematized, runs itself |

**Note**: Score 10 \= EASY (low effort). Score 1 \= HARD (high effort).

**Improvement Levers**:

- Move from DIY → DWY → DFY on the delivery spectrum  
- Provide templates, checklists, swipe files (reduce cognitive load)  
- Automate what can be automated  
- "Works without your permission" — build accountability systems  
- Remove steps from the process  
- Apply 10x-to-1/10th test: "If they paid 1/10th, how would I STILL make them successful?"

  ---

  ## Calculating the Value Score

  **Per perspective** (Buyer or Seller):

```
Value Score = Dream Outcome + Perceived Likelihood + Time Delay + Effort & Sacrifice
Max = 40 per perspective, 80 combined
```

  (Time Delay and Effort & Sacrifice are scored inversely — 10 \= fast/easy — so higher score \= better.)

  **Thresholds**:

| Combined Score (Buyer \+ Seller) | Verdict |
| :---- | :---- |
| 65-80 | GREEN — Exceptional value, proceed to blueprint |
| 45-64 | YELLOW — Good but has weak spots, address before finalizing |
| Below 45 | RED — Fundamental redesign needed on weak factors |

  **Divergence Alert**: If buyer and seller scores differ by more than 10 points on any single factor, flag it. This indicates misalignment — the seller hates delivering what the buyer loves, or the seller is confident but the buyer doesn't believe it.

  ---

  ## Connection to Pricing

  The Value Score directly informs pricing tier:

| Value Score (Buyer only) | Justifiable Price Range | Reasoning |
| :---- | :---- | :---- |
| 35-40 | Premium ($5k+) | Overwhelming value perception supports premium pricing |
| 28-34 | Mid-High ($997-4,997) | Strong value, can command above-market pricing |
| 20-27 | Mid ($97-997) | Solid value, competitive pricing |
| Below 20 | Low ($7-97) or Free | Weak value perception — use as lead magnet or frontend |

  **Rule**: Always maintain minimum 10x value-to-price ratio. If total stack value \= $5,000, price should be at most $500. This makes the offer feel like "stealing."


# Tab 6

# Value Ladder & Money Models

## The Value Ladder (Brunson)

Every business needs a ladder of offers at increasing price points and value levels. Without a complete Value Ladder, funnels cannot work profitably.

"The business that can spend the most to acquire a customer wins." — Dan Kennedy

### The 6 Tiers

| Tier | Price Range | Purpose | Margin | Scalability | Funnel Type |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Lead Magnet | Free | Build trust, solve narrow problem, get contact | N/A (cost center) | High | Squeeze page |
| Frontend | $7-97 | Convert lead to customer, cover ad spend | Low-Medium | High | Free+shipping, Tripwire, SLO |
| Middle | $97-997 | Deliver core transformation | Medium-High | Medium-High | Webinar, VSL, Product Launch |
| Backend | $997-4,997 | Done-with-you, deeper access | High | Medium | Application, Sales call |
| High-Ticket | $5,000-25,000+ | Done-for-you, custom solutions | Very High | Low | Consultation, Proposal |
| Continuity | $29-299/mo | Recurring revenue, ongoing support | Medium | High | Membership, SaaS, Retainer |

### Transition Mechanics

Each tier's job is to:

1. Deliver massive value at its price point  
2. CREATE a new problem that the next tier SOLVES  
3. Filter and qualify buyers for the next level

   **Key Question Between Tiers**: "What problem does Tier N create that Tier N+1 solves?"

   Examples:

- Lead Magnet (free checklist) creates: "I know what to do but don't know HOW" → Frontend (mini-course)  
- Frontend (mini-course) creates: "I learned the theory but need hands-on help" → Middle (group program)  
- Middle (group program) creates: "I got results but want faster/custom scaling" → Backend (1-on-1 coaching)  
- Backend (coaching) creates: "I don't have time to do this myself anymore" → High-Ticket (done-for-you agency)  
- Any tier creates: "I want ongoing support/updates" → Continuity (membership)

  ---

  ## The Four Offer Types — Money Models (Hormozi)

  A Money Model is a deliberate sequence of offers. It's what you offer, when, and how — to make as much money as fast as possible.

  ### Type 1: Attraction Offers

  **Purpose**: Turn strangers into customers. Cover acquisition costs.

| Model | How It Works | Best For |
| :---- | :---- | :---- |
| Win Your Money Back | Pay X, meet goals, get money back (cash or credit) | Services with measurable outcomes |
| Giveaways | Free high-value item to drive traffic and engagement | Building audience, launching |
| Decoy Offer | Free DIY option vs Premium done-with-you option | Consultants, agencies |
| Buy X Get Y Free | Purchase triggers free bonus items | Physical products, bundles |
| Pay Less Now / Pay More Later | Discounted launch price that increases later | Subscriptions, courses |
| Free Goodwill | Genuinely free value with no strings attached | Building authority, entering new markets |

  ### Type 2: Upsell Offers

  **Purpose**: Get existing customers to spend more. This is where profit lives.

"Do you want fries with that?" turned a $0.25 profit burger into a $3.00 profit meal — an 11.6x increase.

| Model | How It Works | When to Use |
| :---- | :---- | :---- |
| Classic Upsell | "You can't have X without Y" — solve the next problem | Right after purchase |
| Menu Upsell | Multiple options at different price points | During purchase (add-ons) |
| Anchor Upsell | Show expensive option first, then reasonable one | High-ticket sales |
| Rollover Upsell | Credits/value from current purchase apply to next | Retaining customers between purchases |

**Upsells fail when**: You offer something they don't want, at the wrong time, or the wrong way.

**Upsells tend to offer**: More of what they got (quantity), better versions (quality), or complementary items (different).

### Type 3: Downsell Offers

**Purpose**: Turn "no" into "yes" with a different configuration.

**Critical Rules**:

- They said no to THIS offer, not all offers  
- Never drop price for the same thing (that's discounting, and it kills trust)  
- Offer something DIFFERENT for less, or the SAME THING with different payment terms  
- Downsells are trades — if you give something, get something

| Model | How It Works | When to Use |
| :---- | :---- | :---- |
| Payment Plan | Same product, spread cost over time | When price is the objection |
| Trial With Penalty | Try for low/no cost, auto-charge if they stay | When commitment is the objection |
| Feature Downsell | Remove features for lower price | When they want less scope |

  **Seesaw Downsell Flow**: Full price → $X down \+ payments → Lower down \+ more payments → Minimum viable payment

  ### Type 4: Continuity Offers

  **Purpose**: Recurring revenue. Sell once, get paid repeatedly.

"You can shear a sheep for a lifetime, but you can only skin it once."

| Model | How It Works | When to Use |
| :---- | :---- | :---- |
| Continuity Bonus | Join membership, get high-value bonus on signup | Converting one-time buyers to recurring |
| Continuity Discount | Prepay longer term, get lower rate | Locking in committed members |
| Waived Fee Offer | Waive setup/enrollment fee if they start today | Reducing friction for recurring commitment |

**Important**: No successful continuity business has ONLY a standalone membership offer. They all have attraction offers, upsells, and downsells alongside.

---

## The 3-Stage Money Model Development

**Don't build the whole model at once. Perfect one stage before moving to the next.**

| Stage | Goal | Focus | When |
| :---- | :---- | :---- | :---- |
| I: Get Cash | Turn strangers into customers reliably | Attraction Offer | Day 1 — may take up to a year |
| II: Get More Cash | Make 30-day profit well above acquisition cost | Upsell \+ Downsell Offers | Once Stage I is reliable |
| III: Get The Most Cash | Stack recurring revenue \+ maximize LTV | Continuity Offers | Once Stage II is reliable |

**The 30-Day Rule**: Cover your customer acquisition cost within 30 days. Any business can get interest-free money for 30 days via credit card. If you clear balance before month-end, it's free capital. Rinse and repeat.

**"Simple Scales, Fancy Fails"**: Think 100 ways to offer your product, not 100 products to offer.

---

## Lead Magnet Design (from $100M Leads)

A lead magnet is a complete solution to a NARROW problem that reveals a broader problem your core offer solves.

**The Pretzel/Drink Analogy**: Free pretzels (narrow: hunger) → create thirst (broader) → drink \= core offer (paid).

### 3 Types of Lead Magnets

| Type | How It Works | Example |
| :---- | :---- | :---- |
| Reveal Their Problem | Diagnosis that shows problems getting worse | Free website speed test, posture analysis |
| Samples & Trials | Full but limited access to core offer | Free first month, free first session |
| One Step of Multi-Step | Give one valuable step free, rest when they buy | Free first module of a course |

### 4 Delivery Methods

| Method | Examples |
| :---- | :---- |
| Software | Calculators, dashboards, spreadsheets, tools |
| Information | Courses, lessons, interviews, tips, presentations |
| Services | Do work for free (limited scope) |
| Physical Products | Books, assessment charts, sample products |

**3 types x 4 methods \= 12 possible lead magnets** for a single problem. Rotate to keep fresh.

---

## The 3% / 97% Split (Suby)

| Segment | Size | Behavior | Offer Strategy |
| :---- | :---- | :---- | :---- |
| 3% | Small | Ready to buy NOW | Fast path: opt-in → offer → qualify → close |
| 97% | Large | Need nurturing | Slow path: opt-in → email/video nurture → educate → eventual close |

**Design offers for BOTH paths.** The 97% is where the real money is — but only if you have a nurture sequence.

---

## Ecosystem View Format

When displaying offers in context, use this visualization:

```
[Lead Magnet] → [Frontend $XX] → [Core Offer $XXX] → [Upsell $X,XXX] → [Continuity $XX/mo]
  Type: HVCO     Type: Decoy      Type: Grand Slam     Type: Classic       Type: Bonus
  Stage: I        Stage: I          Stage: I              Stage: II           Stage: III
  Score: --       Score: --         Score: 55 <--CURRENT  (not designed)      (not designed)
```

**Rules**:

- Always mark `<--CURRENT` on the offer being designed  
- Show offer type (from Money Models) under each  
- Show Money Model stage under each  
- Leave `(not designed)` for future offers — don't force all at once  
- When 4+ offers, switch to vertical format


# Tab 7

{  
 "name": "offer-architect",  
 "version": "1.0.0",  
 "description": "Interview-based offer design and evaluation skill. Conducts a 6-phase structured interview, scores offers on 6 dimensions \+ Value Equation, and produces an Offer Blueprint document. Synthesizes Hormozi, Brunson, Suby, and Thiel frameworks.",  
 "author": {  
   "name": "Paweł — Mindlink"  
 },  
 "keywords": \[  
   "offer design",  
   "pricing",  
   "value ladder",  
   "grand slam offer",  
   "money models"  
 \]  
}

# Tab 8

# **Offer Architect**

Interview-based offer design and evaluation skill for Claude Cowork.

## **What it does**

Transforms vague service or product ideas into scored, priced, and positioned offer architectures through a structured 6-phase interview. Acts as a conversational partner — asks questions, challenges assumptions, scores the offer across two systems, and produces a completed Offer Blueprint document.

## **When it activates**

**Direct triggers**: "design an offer", "create an offer", "price my service", "value ladder", "Grand Slam Offer", "what should I charge", "how do I package", "offer architecture", "money model", "Godfather offer"

**Interceptor**: If you jump to marketing, ads, funnels, or copy without a defined offer, the skill will stop you and initiate the interview first. Offer before funnel. Funnel before traffic.

## **The 6-Phase Interview**

1. **Market & Niche** — Starving crowd validation (urgent pain, purchasing power, reachability)  
2. **Dream Outcome** — Heaven/Hell states, Big Domino belief  
3. **Problems & Solutions** — Obstacle mapping, delivery vehicle matrix, 10x-to-1/10th test  
4. **Trim, Stack & Price** — Solution trimming, stack slide construction, guarantee selection  
5. **Offer Position & Chain** — Value ladder placement, ecosystem view, upsell/downsell logic  
6. **Enhance & Name** — Scarcity/urgency, premiums, MAGIC naming formula

   ## **Scoring**

After the interview, every offer is scored on two systems:

* **6-Dimension Score** (max 60): Attractiveness, Pattern Interrupt, Ease of Understanding, Ease of Delivery, Time to Value, Time to Money  
* **Value Equation Score** (max 80): Scored from both buyer and seller perspective across Dream Outcome, Perceived Likelihood, Time Delay, and Effort & Sacrifice

GREEN (proceed) / YELLOW (refine) / RED (redesign) thresholds on both systems.

## **Output**

`{Service}_Offer_Blueprint.md` — 14-section document covering offer identity, belief architecture, solution stack, stack slide, pricing & economics, guarantee, enhancers, both scorecards, profitability assessment, ecosystem view, naming options, Epiphany Bridge story arc, and next steps.

## **Reference Files**

| File | Contents |
| ----- | ----- |
| `blueprint_template.md` | 14-section blueprint output template |
| `naming_formulas.md` | MAGIC formula, container word taxonomy, worked examples |
| `offer_enhancers.md` | Guarantees (12 types \+ math), premiums, scarcity, urgency, bonuses |
| `value_equation_scoring.md` | Dual-perspective scoring rubrics with improvement levers |
| `value_ladder_and_money_models.md` | 6-tier value ladder, 4 money model types, 3-stage development |

## **Frameworks**

Synthesizes: Hormozi (Value Equation, Grand Slam Offer, Money Models), Brunson (Value Ladder, Big Domino, Stack Slide, Epiphany Bridge), Suby (Godfather Offer, Premiums), Thiel (Monopoly Positioning), Belcher (Belief conversion math).

## **Version**

v1.0.0 — Author: Paweł, Mindlink

# Tab 9

# META-ANALYSIS: Offer Design Frameworks Across 10 Authors

**Purpose**: Synthesize all notes from 10 books into a unified framework for offer design, especially for paid media (Meta Ads) scalability.

**Scope**: What every author agrees on, where they differ, dimensions that matter when designing offers, and what's missing from the current offer-architect skill.

**Date**: March 2026

---

## 1\. Universal Laws (What Every Author Agrees On)

### 1.1 Market Selection \> Offer Strength

- **Hormozi**: "Starving crowd beats a perfect offer."  
- **Suby**: "The 3% vs 97% market split—focus on nurturing."  
- **Brunson**: "Dream 100 identifies where your customers already congregate."  
- **Thiel**: "Start small, dominate completely, then expand."

  **Consensus**: You cannot overcome a weak market with a strong offer. Market validation is prerequisite, not add-on.

  ### 1.2 The Value Equation Rules

- **Hormozi**: Value \= (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort & Sacrifice)  
- **Brunson**: "People buy BELIEFS, not products."  
- **Suby**: "The Godfather offer is irresistible—nobody can say no."

  **Consensus**: All paths lead to the Value Equation. Every dimension matters. Perception is reality.

  ### 1.3 One Big Domino Belief, Everything Else Follows

- **Brunson** (Expert Secrets): "Identify the ONE belief that, if knocked down, makes all other objections irrelevant."  
- **Suby**: "The 3 False Beliefs—Vehicle, Internal, External—but one is the fulcrum."  
- **Hormozi**: "Clear value proposition eliminates the need for complex sales."

  **Consensus**: Simplicity scales. The more beliefs required to make a sale, the lower conversion. Multiple beliefs compound objections exponentially (Perry Belcher: each additional belief \= 50% conversion drop).

  ### 1.4 Offer Stacking Creates Perceived Value

- **Brunson**: The Stack Slide—list each component with individual price, then announce the special price.  
- **Hormozi**: "Bonuses can 2-4x sales without changing the core offer."  
- **Suby**: "Premiums double or triple conversions."

  **Consensus**: Value ratio matters more than absolute value. 10:1 value-to-price minimum. Stacking makes the offer feel like "stealing."

  ### 1.5 You Must Own Your Distribution or Pay Dearly

- **Brunson**: "Dream 100—identify the 100 people/platforms that control traffic to your market."  
- **Thiel**: "Distribution is a core competency, not a side effect."  
- **Hormozi**: "The business that can spend the most to acquire a customer wins."  
- **BAMF**: "Custom audiences are your most valuable asset."

  **Consensus**: Traffic is expensive unless you build relationships first. Owned channels (email, community, referral networks) have 10x ROI of cold paid ads.

  ### 1.6 Cash Flow Matters More Than Profit Margin

- **Hormozi**: "Payback Period in Days (PPD) is the third metric after CAC and LTGP."  
- **Suby**: "The 30-Day Rule: Cover your customer acquisition cost within 30 days."  
- **Brunson**: "Price your offer so the first sale recovers enough to fund the next sale."

  **Consensus**: A business can die from profitability if cash is slow. Immediate payback unlocks exponential scaling.

  ### 1.7 Stories Sell, Logic Doesn't

- **Brunson**: "The Epiphany Bridge Story—people don't believe logical arguments, they believe stories."  
- **Expert Secrets**: "The Hero's Two Journeys—internal identity shift must precede external action."  
- **BAMF**: "Relatability \+ vulnerability \+ specificity \= engagement."

  **Consensus**: Stories create belief transfer. Testimonials are stories. Case studies are stories. The best copy is a story hiding inside a sales message.

  ### 1.8 Free/Discount Offers Reveal Truth Faster

- **Hormozi**: "If a free offer doesn't work, your offer is broken or your targeting is wrong."  
- **Expert Secrets/Brunson**: "Free offers scale traffic 9x—the Penny Gap (Dan Ariely)."

  **Consensus**: Start with free/massively discounted to build testimonials. Monetize only after proof exists.

  ### 1.9 Premium Positioning Filters Out Low-Quality Customers

- **Hormozi**: "Premium customers help fund your growth; cheap customers demand support."  
- **Zero to One / Thiel**: "Monopolies have different incentives—they can afford ethics because they're profitable."

  **Consensus**: Higher prices attract better customers, reduce churn, improve LTV, and paradoxically reduce operational drag.

  ### 1.10 Guarantees Increase Sales More Than Refund Rate Increases

- **Hormozi**: "Guarantee math: 30% more sales, 2x refund rate \= 23% net positive."  
- **Suby**: "Guarantees can 2-4x conversions."

  **Consensus**: The fear of refunds is larger than actual refunds. Unconditional guarantees work for low-ticket; conditional for high-ticket.

  ---

  ## 2\. Author-Unique Contributions

  ### 2.1 Alex Hormozi ($100M Offers / Leads / Money Models)

  **Unique Frameworks**:

- **The Grand Slam Offer**: Four-part formula (Market/Avatar, Problem, Value Stack, Price) designed to feel irresistible.  
- **The Value Grid**: Upsells mapped by effort (Y-axis) × value (X-axis). Start with low-effort, high-value quadrant first.  
- **Customer-Financed Acquisition (CFA)**: When CAC \< LTGP, customers help finance their own acquisition \+ the next one.  
- **The Penny Gap**: Moving from $0.01 to free \= 9x conversion lift.  
- **Premium Promotions**: Positioning offers at premium prices attracts different customer caliber entirely.  
- **Vista Method**: Identify top 20% customers by spend \+ longevity, find 3-5 commonalities, speak ONLY to those attributes.

  **What He Doesn't Cover**:

- Tactical paid media specifics (he focuses on organic growth, referrals, partnerships).  
- Cold traffic psychology (he builds warm/owned channels).  
- Offer testing methodology (A/B testing is assumed to happen elsewhere).

  ### 2.2 Russell Brunson (DotCom Secrets / Expert Secrets / Traffic Secrets)

  **Unique Frameworks**:

- **The Perfect Webinar Script**: 45-60 minute presentation structure using Origin Story → 3 Secrets (Vehicle/Internal/External) → Stack → Close.  
- **The Opportunity Switch**: The specific reframe that makes people move from "that won't work for me" to "oh I get it now."  
- **The Value Ladder**: 6-tier hierarchy (Lead Magnet → Frontend → Middle → Backend → High-Ticket → Continuity) with explicit purpose at each tier.  
- **The Dream 100**: Instead of buying random ads, identify 100 people/platforms that control your market traffic. Build relationships. 30% will say yes to a promotion.  
- **Three Journeys**: Internal (identity), External (skills), and Sales journey (belief \+ action).  
- **Funnelology**: The science of moving leads through sequential offers with increasing friction.

  **What He Doesn't Cover**:

- Unit economics (he assumes offers work, focuses on positioning/narrative).  
- Guarantee strategy (mentions risk but not systematically).  
- Premium offer economics (his offers tend toward volume-based).

  ### 2.3 Sabri Suby (Sell Like Crazy)

  **Unique Frameworks**:

- **The Godfather Offer**: An irresistible offer that feels like you'd be "stupid to say no."  
- **Three Phases of Offer Design**: Phase 1 (Dream Buyer), Phase 2 (Perfect Bait/Lead Magnet), Phase 3+ (Godfather).  
- **The Premium Lever**: Premiums can 2-3x sales with near-zero cost increase.  
- **The 3% vs 97% Split**: 3% are ready to buy NOW (price-sensitive). 97% need nurturing (will pay premium for right sequence).  
- **Premium Positioning in Paid Ads**: Different ad copy/targeting for ready-now vs nurture audiences.  
- **The Magic Lantern Technique**: Using metaphor/story to make a boring offer feel magical.

  **What He Doesn't Cover**:

- Email sequence details (assumes email exists, focuses on offer).  
- Community/organic growth (he's heavily paid-ads focused).  
- Long-form content strategy (his focus is ads → landing page → offer).

  ### 2.4 Peter Thiel (Zero to One)

  **Unique Frameworks**:

- **Monopoly vs Competition**: "Capitalism requires monopoly power. Competition drives all profit away."  
- **The Contrarian Question**: "What important truth do very few people agree with you on?" reveals future positioning.  
- **Secrets**: "An important truth that few people know"—the foundation of defensible competitive advantage.  
- **Last Mover Advantage**: Value \= sum of all future cash flows. The last company to dominate a market captures the most value because it has the longest horizon.  
- **Category of One Positioning**: "All happy companies are different." Your offer must be impossible to compare to commodity alternatives.  
- **10x vs 10%**: "Your offer should be dramatically better in key dimensions, not marginally better at everything."  
- **The Niche-to-Adjacent Expansion**: Dominate small niche → establish moat → expand to adjacent markets from position of strength.

  **What He Doesn't Cover**:

- Offer mechanics (he's about market positioning, not product stacking).  
- Sales process (he assumes business model is the sales process).  
- Guarantee/urgency/scarcity (he focuses on structural defensibility, not behavioral psychology).

  ### 2.5 BAMF Bible (25+ Growth Hacks)

  **Unique Frameworks**:

- **Content Hierarchy**: Curate → Learn what works → Mix in original → Dominate.  
- **Custom Audience Sequencing**: Map warm audiences (email, LinkedIn connections, fans) → cool audiences (website visitors) → cold audiences (interest-based).  
- **Dark Post A/B Testing**: Use $25-100 tests to validate offer positioning, copy, and targeting before scaling.  
- **Reverse Targeting for PR**: Target the "wrong" audience to create controversy → get PR → pivot to right audience (earned media).  
- **Group Extraction for Cold Email**: Extract emails from 50 relevant Facebook Groups → run cold email sequence → segment by warmth.  
- **Chatbot Conversion Mechanics**: Engagement ad (low friction) → automated messenger (personalization) → click-through → conversion tracking.

  **What He Doesn't Cover**:

- Offer design philosophy (assumes offer exists, focuses on channel mechanics).  
- Pricing strategy (mentions offer positioning but not price testing).  
- Funnel architecture (tactical execution, not strategic sequencing).

  ---

  ## 3\. The Master Dimension Map

  For each of the user's 9 evaluation dimensions, synthesize what the books say, which frameworks apply, what the current skill covers, and what it misses.

  ### Dimension 1: How Easy Is It to Sell?

  **Sub-dimensions**: Ease of understanding, does market know they have the problem, Big Domino clarity

  **What the Books Say**:

- **Brunson**: The Big Domino is the ONE belief that, if knocked down, makes all other objections irrelevant. If you need multiple beliefs to sell, you've already lost 50%+ on each additional belief (Perry Belcher).  
- **Hormozi**: "If you can explain it in one sentence, it's clear enough to sell." Use the Dream Outcome Statement.  
- **Thiel**: The offer should be so specific to its niche that comparison becomes irrelevant. "British food in Palo Alto" vs "Palo Alto restaurants"—the latter is the real market.  
- **Suby**: "The 97% don't know they have the problem yet. Your job is to educate them first, then offer." Lead magnets diagnose. Offers solve.

  **Frameworks**:

- **Value Equation Factor**: Perceived Likelihood (buyer believes they can achieve it)  
- **Big Domino Identification** (Expert Secrets)  
- **The Opportunity Switch** (Brunson)  
- **3 False Beliefs** (Vehicle, Internal, External)  
- **Pattern Interrupt** scoring (Is it obviously different from status quo?)

  **What Current Skill Covers**:

- Big Domino identification (Phase 2\)  
- Dream Outcome Statement clarity (Phase 2\)  
- "Ease of Understanding" dimension in 6-point scorecard  
- 3 False Beliefs mapping (Phase 6\)

  **What Current Skill MISSES**:

- **No quantitative test for Big Domino clarity**: How do you KNOW one belief is enough? The skill assumes you can find it but doesn't have validation mechanics.  
- **No "market awareness" assessment**: Does the market already know they have the problem? (Suby's 3% vs 97% split). The skill treats all markets as aware.  
- **No "pattern interrupt" testing**: Is this offer categorically different or incremental? BAMF shows how to test this with dark posts pre-interview.  
- **No cold traffic consideration**: If the market doesn't know they have the problem, the offer name and positioning must DO that work. Current skill doesn't optimize for this.  
- **Positioning clarity score vs. sales clarity score**: An offer can be clear to insiders but confusing to cold traffic. No distinction.

  **Missing Mechanics**:

- Framework: "Cold Traffic Clarity Test" — Can someone unfamiliar with the market understand this offer in \<5 seconds from headline alone?  
- Framework: "Pattern Interrupt Audit" — Is this offer a new vehicle/method (0→1) or just a better version of existing (1→n)?  
- Metric: "Assumption clarity ranking" — How many beliefs/assumptions must the buyer accept? (Target: 1\. Good: 2\. Bad: 3+)

  ---

  ### Dimension 2: How Attractive Is It?

  **Sub-dimensions**: Desire, perceived value, Godfather quality

  **What the Books Say**:

- **Hormozi**: Attractiveness \= (Dream Outcome DESIRABILITY) × (Believe it works) / (Easy to do). The first factor is purely aspirational.  
- **Suby**: "The Godfather Offer makes people feel stupid saying no. It's so stacked you literally can't refuse."  
- **Brunson**: "People don't buy products. They buy BELIEFS about what the product will do for their identity."  
- **BAMF**: "Reverse-engineer what your audience engages with, then test value propositions with $25 dark posts."

  **Frameworks**:

- **Value Equation Factor**: Dream Outcome (desirability)  
- **The Stack Slide** (Brunson)  
- **Value Ratio Minimum** (10:1)  
- **Premium Element Addition** (Suby)  
- **Epiphany Bridge Story** (Brunson)  
- **Attractiveness Dimension** in 6-point scorecard  
- **Value Stacking** (Expert Secrets)

  **What Current Skill Covers**:

- Dream Outcome desirability (Phase 2\)  
- Stack Slide construction (Phase 4\)  
- Bonus naming and valuation (Phase 4\)  
- Attractiveness dimension score (5A)  
- Value-to-price ratio (5C)  
- Epiphany Bridge story arc (Phase 6 \+ Output 13\)

  **What Current Skill MISSES**:

- **No specific "appeal to desire" copywriting**: The skill talks about identifying desirable outcomes but doesn't give patterns for making those outcomes emotionally compelling.  
- **No contrarian/premium positioning framework**: Suby's "premium offer" is different from regular stacking. Thiel's "category of one" is different again. No unified framework for positioning desirability.  
- **No "aspiration gap" mapping**: What is the emotional distance between current identity and dream identity? (Brunson's internal journey)  
- **Bonus naming uses MAGIC but limited to bonuses**: Every element (core offer, bonuses, premiums, guarantees) should use MAGIC naming. Current skill only names the offer overall \+ some bonuses.  
- **No reverse-engineering of audience preference**: BAMF's approach is to test what sticks BEFORE finalizing. Skill assumes you know.

  **Missing Mechanics**:

- Framework: "Identity Shift Mapping" — What must the buyer believe about THEMSELVES for the offer to be attractive? (Brunson's internal journey)  
- Framework: "Emotional Benefit Anchor" — For each component, what emotion does it trigger? (Aspiration, relief, status, belonging, etc.)  
- Metric: "Desire Divergence Check" — Does the seller believe this is desirable, or just the market? If divergence \> 3 points, the seller won't sell it with conviction.  
- Process: "Offer Positioning Test" — Run 3 different value propositions through a $25 dark post test BEFORE finalizing stack.

  ---

  ### Dimension 3: How Profitable Is It?

  **Sub-dimensions**: Margins, unit economics, LTV:CAC

  **What the Books Say**:

- **Hormozi**: "The business that can spend the most to acquire a customer wins." LTV:CAC ratio determines your competitive ceiling. CAC Recovery in 30 days determines if you can scale.  
- **Thiel**: "Company value \= sum of all future cash flows." Profitability is about long-term capture, not short-term extraction.  
- **Suby**: "Do the premium math: same offer, 3x price for top 3% \= 10x profit."  
- **BAMF**: "Warm audiences have 10x lower CAC than cold audiences."

  **Frameworks**:

- **CAC (Cost to Acquire Customer)**  
- **LTGP (Lifetime Gross Profit)**  
- **PPD (Payback Period in Days)**  
- **LTV:CAC Ratio** (Target: 3:1+)  
- **30-Day Rule** (Hormozi)  
- **Gross Margin** calculation  
- **Scalability Assessment** (Can you 10x volume without 10x-ing fulfillment cost?)

  **What Current Skill Covers**:

- Fulfillment cost estimation (Phase 3 \+ Phase 4\)  
- Gross margin calculation (5C)  
- CAC recovery timeline (5C)  
- LTV:CAC ratio (5C)  
- Profitability Assessment section (10)

  **What Current Skill MISSES**:

- **No offer repositioning for profitability**: If margin is low, the skill doesn't systematically suggest: (a) 10x-to-1/10th test to reduce fulfillment cost, (b) premium tier addition, (c) moving to higher LTV market, (d) changing money model stage.  
- **No traffic source profitability mapping**: BAMF shows that warm audiences cost 10x less than cold. Skill doesn't map offer design to traffic source economics.  
- **No "customer financed acquisition" optimization**: Hormozi's CFA framework is barely mentioned. If CAC \< first-month profit, you can reinvest immediately. Skill doesn't optimize for this.  
- **No scalability constraint identification**: What breaks if you 10x volume? (Fulfillment bottleneck, founder dependency, payment processing, etc.) Skill assumes scalability linearly.  
- **No premium tier profit modeling**: Adding a premium 2x-3x price can 5-10x profit without changing core offer. Skill doesn't explore this systematically during pricing (Phase 4).

  **Missing Mechanics**:

- Framework: "Profitability Lever Analysis" — For each margin gap, which of these levers could improve it? (1) Reduce fulfillment cost (10x-to-1/10th test), (2) Add premium tier, (3) Change money model, (4) Change market/segment.  
- Framework: "Traffic Source Profitability Mapping" — Same offer, different traffic sources \= different CAC \= different profitability. Design offers with cheapest traffic source in mind (owned/warm first).  
- Metric: "Customer Financed Acquisition Indicator" — If PPD \< 30 days, you can reinvest immediately (capital efficient). Design goal: achieve this before scaling cold traffic.  
- Process: "Scalability Constraint Audit" — Before finalizing, ask: "If we 10x clients, what breaks first? How do we solve it?"

  ---

  ### Dimension 4: How Scalable Is It?

  **Sub-dimensions**: Can volume increase without linear cost increase

  **What the Books Say**:

- **Hormozi**: "Automation is the highest level of fulfillment. DFY \> DWY \> DIY. Move left as volume increases."  
- **Thiel**: "Economies of scale are a moat. 10x better, not 10% better."  
- **Brunson**: "Simple scales, fancy fails. Perfect one offer at a time before adding the next."  
- **BAMF**: "Warm audiences \+ custom segmentation \= leverage. You don't need to make things simpler if you're targeting the right people."

  **Frameworks**:

- **Delivery Vehicle Matrix** (Attention level, Effort level, Medium)  
- **DFY / DWY / DIY Spectrum**  
- **10x-to-1/10th Test** (What would you deliver if price 10x? If price 1/10th?)  
- **Ease of Delivery** dimension in 6-point scorecard  
- **Scalability Assessment** (Low/Med/High)

  **What Current Skill Covers**:

- Delivery vehicle identification (Phase 3\)  
- DFY/DWY/DIY classification (Phase 3\)  
- 10x-to-1/10th test framing (Phase 3\)  
- "Ease of Delivery" dimension score (5A)  
- Scalability assessment in profitability section (5C)

  **What Current Skill MISSES**:

- **No systematic path from DFY-required to DFY-possible**: The skill identifies "this requires DFY but can't be automated," then troubleshoots weakly. No structured approach to either (a) re-engineer the offer to be more DWY, (b) hire to deliver DFY, or (c) move to higher market segment.  
- **No "founder dependency" audit**: Is the seller essential to delivery? If yes, it doesn't scale. Skill doesn't force this confrontation until Ease of Delivery scores low (too late).  
- **No technology/automation recommendations**: Skill says "automate" but doesn't suggest WHAT to automate or which tools/systems.  
- **No "warm audience scaling" strategy**: BAMF shows that with warm (segmented) audiences, you can hand-deliver and still scale because CAC is so low. Skill doesn't map warm audience strategy to delivery requirements.  
- **No cohort-based vs. open enrollment trade-off**: Some models (cohort \= fixed group) scale differently than others (open \= rolling admissions). Skill doesn't explore.

  **Missing Mechanics**:

- Framework: "Founder Dependency Audit" — Which parts of delivery REQUIRE the founder? Design to eliminate or delegate each. If any remain, it's not scalable beyond founder capacity.  
- Framework: "Technology Leverage Points" — For each solution component, what technology could automate it? (e.g., assessment software, templates, automation tools, booking systems, etc.)  
- Framework: "Warm Audience Leverage" — If targeting warm audiences, hand-delivery can actually improve LTV because of personal touch. Map this explicitly.  
- Process: "Scalability Path Planning" — If scalability is LOW, present three paths: (1) re-engineer offer (change delivery vehicle), (2) hire team to deliver, (3) move to higher-paying market that justifies higher delivery cost.

  ---

  ### Dimension 5: How Quickly Do I Get Paid?

  **Sub-dimensions**: CAC recovery speed, cash flow

  **What the Books Say**:

- **Hormozi**: "PPD (Payback Period in Days) is critical. Target: \< 30 days. 30 days \= interest-free capital from credit cards."  
- **Suby**: "The 30-Day Rule: if you can't cover CAC in 30 days, the model doesn't scale."  
- **Brunson**: "Price your offer so the first customer's profit funds the next customer's acquisition."

  **Frameworks**:

- **PPD Calculation** \= (CAC / Monthly Gross Profit) × 30  
- **Customer-Financed Acquisition** (when CAC \< first-month GP)  
- **Time to Money** dimension in 6-point scorecard  
- **30-Day Rule** assessment

  **What Current Skill Covers**:

- CAC estimation (5C)  
- Monthly gross profit (implicit in PPD calculation, 5C)  
- "Time to Money" dimension score (5A)  
- CAC Recovery Timeline (5C)

  **What Current Skill MISSES**:

- **No pricing tier strategy for cash flow**: A lower-priced offer recovers CAC faster. Skill doesn't show the trade-off or help optimize for it.  
- **No payment plan impact**: If offer is $997 one-time but you offer 3×$399 payments, PPD changes dramatically. Skill doesn't model this.  
- **No subscription optimization**: Continuity offers have instant revenue recognition. Better PPD than one-time. Skill covers in money model but not in cash flow assessment.  
- **No "quick win" integration**: Hormozi's approach: front-load first result within 72 hours so customer perceives value immediately. Skill doesn't require this.  
- **No cash flow variance by traffic source**: Warm traffic converts faster \= shorter sales cycle \= faster cash. Cold traffic slower. Skill assumes same timing across all traffic.

  **Missing Mechanics**:

- Framework: "Cash Flow Optimization" — If PPD \> 30 days, which of these levers improves it? (1) Lower price (faster recovery), (2) Add payment plan (spread cost), (3) Add subscription (immediate recognition), (4) Move to warm traffic (faster conversion).  
- Metric: "Capital Efficiency Score" — Combine PPD \+ LTV:CAC to assess if the business model can self-fund growth. (Good: PPD \< 30 days AND LTV:CAC \> 3:1)  
- Process: "Quick Win Sequencing" — Identify what first deliverable customer gets within 48-72 hours. This shows value, reduces refund risk, and improves repeat purchase likelihood.

  ---

  ### Dimension 6: Time to Value for the Buyer

  **Sub-dimensions**: Speed of first result

  **What the Books Say**:

- **Hormozi**: "Time Delay is the strongest lever. 'Instant,' 'within 48 hours,' 'first week' \= massive value perception lift."  
- **Suby**: "The quick win is non-negotiable. Deliver a win in the first 48-72 hours to prove the system works."  
- **Brunson**: "People want results, not lessons. Lead with transformation, then teach mechanics."

  **Frameworks**:

- **Time Delay Inverse Scoring** (10 \= instant, 1 \= 12+ months)  
- **Quick Win Component** (first deliverable)  
- **Time to Value** dimension in 6-point scorecard

  **What Current Skill Covers**:

- Time Delay factor in Value Equation (5B)  
- "Time to Value" dimension score (5A)  
- Quick Win mention in troubleshooting section

  **What Current Skill MISSES**:

- **No systematic "first 48-72 hour" plan**: The skill asks about time to value but doesn't require a detailed plan for what the customer gets in the first 3 days.  
- **No speed positioning leverage**: Suby uses "14 Day Find Your Perfect Product," "90 Day Rapid Healing"—speed is part of the offer NAME. Skill doesn't optimize naming for speed.  
- **No result visualization**: For long-cycle offers (6+ months), Hormozi's principle is "show progress indicators"—the Dotted Map. Skill doesn't address this.  
- **No "activation vs. result" distinction**: First 48 hours \= activation (customer is set up). First result \= measurable outcome. Skill conflates them.  
- **No deferral risk assessment**: If time to value \> 30 days, refund risk increases. Skill doesn't map this.

  **Missing Mechanics**:

- Framework: "Time to Value Breakdown" — What happens Day 1? Day 7? Day 30? Day 90? Design each milestone.  
- Framework: "Speed as Positioning\*\* — If time to value is fast, make it part of the offer name/narrative (e.g., "14-Day," "Instant," "First-Week Results").  
- Metric: "Activation vs. Outcome Timeline" — How long until customer is SET UP (activated)? How long until RESULT (outcome)? Both matter.  
- Process: "Quick Win Design\*\* — For every offer with time-to-value \> 2 weeks, design a specific first deliverable (within 72 hours) that demonstrates the system works.

  ---

  ### Dimension 7: What Is the Downside?

  **Sub-dimensions**: Delivery risk, refund exposure, operational fragility

  **What the Books Say**:

- **Hormozi**: "Guarantees actually INCREASE sales net-positive even if refunds double, because conversions increase 30%+."  
- **Brunson**: "Operational fragility \= founder dependency. If the founder leaves, does the offer still deliver?"  
- **Thiel**: "Distribution is a moat. Without distribution, you're vulnerable."  
- **Suby**: "Guarantee types matter. Use conditional guarantees for high-ticket."

  **Frameworks**:

- **Guarantee Types & Decision Tree** (offer\_enhancers.md)  
- **Guarantee Math** (increased sales \> increased refunds)  
- **Fulfillment Risk Assessment** (Can we deliver consistently?)  
- **Operational Fragility Audit** (Founder dependency, system brittleness)

  **What Current Skill Covers**:

- Guarantee type selection (Phase 4\)  
- Guarantee decision tree (Phase 4\)  
- Guarantee math (5C)  
- Refund risk estimate (Output 6\)

  **What Current Skill MISSES**:

- **No systematic failure mode analysis**: What goes wrong if you deliver 100 of these offers? What if you deliver 1,000? Skill doesn't force this.  
- **No "scalability death points"**: E.g., if the offer requires 1-on-1 calls, what happens at 50 clients? 100 clients? Skill mentions "Ease of Delivery" but doesn't map to actual breaking points.  
- **No refund reason analysis**: Hormozi distinguishes between refunds due to (a) buyer's own failure, (b) offer's failure, (c) misalignment. Skill doesn't help diagnose which risk applies.  
- **No "dependency cascade" mapping**: If founder delivers, what happens if they're sick? On vacation? What if key person A leaves? Skill doesn't audit this.  
- **No "guarantee risk by market type"**: Conditional guarantees work for B2B (measurable). Unconditional for B2C (lower-ticket). Skill treats all markets the same.  
- **No supplier/vendor risk**: If offer depends on third-party (ad spend, affiliates, partners), what if they change pricing/availability? Not addressed.

  **Missing Mechanics**:

- Framework: "Failure Mode Analysis" — For each component, what could go wrong? (1) Delivery failure, (2) Customer failure to execute, (3) Market change, (4) Dependency loss. Rank by likelihood \+ impact.  
- Framework: "Scalability Death Point Audit" — At what volume does fulfillment break? Is there a solution before that point? (Hire, automate, restructure offer)  
- Framework: "Guarantee Risk Assessment" — Map guarantee type to market type. Conditional for B2B (clear metrics). Unconditional for B2C low-ticket (friction-free). Credit-based for high-ticket (maintain relationship).  
- Metric: "Operational Resilience Score" — Can the offer be delivered without the founder? Rate: 1 (founder-essential), 2 (founder-optional), 3 (fully systematized). Target: 2+

  ---

  ### Dimension 8: What Is the Upside?

  **Sub-dimensions**: Ceiling, what happens if it works perfectly

  **What the Books Say**:

- **Thiel**: "Company value \= sum of all future cash flows. The last company to dominate a market is worth the most because it has the longest horizon."  
- **Hormozi**: "A business model's upside \= LTV × market size × share you can capture. Optimize each."  
- **Brunson**: "The value ladder extends infinitely. One offer creates the problem that the next offer solves."

  **Frameworks**:

- **LTV Maximization** (through upsells, continuity, higher-tier market)  
- **Market Size Assessment** (SAM, TAM, addressable market)  
- **Expansion Path** (Thiel's: dominate small niche → expand to adjacent markets)  
- **Money Model Progression** (Stage I → Stage II → Stage III \= 3-10x revenue growth)

  **What Current Skill Covers**:

- LTV estimation (5C, implicit)  
- Value ladder ecosystem view (Phase 5, Output 11\)  
- Money model stage identification (Phase 5\)

  **What Current Skill MISSES**:

- **No "market ceiling" calculation**: How big can this offer grow if it becomes perfect? What's the addressable market? Skill doesn't estimate.  
- **No "expansion path" planning**: The natural expansion from this offer to the next (what problem does it CREATE?). Skill asks this but doesn't optimize for it.  
- **No "premium tier" upside scenario**: "What if we added a high-ticket tier?" Could change revenue trajectory dramatically. Skill covers but doesn't scenario-test.  
- **No "continuity embedding"**: How could continuity (recurring revenue) be added? If a $997 one-time offer becomes $99/month, upside is 12x. Skill doesn't explore systematically.  
- **No "network effect" assessment**: Could this offer grow through referral, community, or network effects? Skill doesn't prompt this.  
- **No "monopoly positioning" upside**: Thiel's framework: how defensible is this offer? If defensible (moat), upside is unlimited (long time horizon). If not, upside has ceiling. Skill doesn't assess defensibility.

  **Missing Mechanics**:

- Framework: "Upside Scenario Modeling" — If everything works perfectly: (1) How many customers could you serve? (2) What's the revenue at that scale? (3) What's the profit? (4) What's the LTV? This shows the ceiling.  
- Framework: "Expansion Path Planning" — For each component, what problem does it solve? What problem does solving that create? (This becomes the next offer). Map 3-5 tiers forward.  
- Framework: "Monopoly Positioning Assessment" (Thiel) — Does this offer have a moat (brand, network effects, switching costs, economies of scale)? If yes, upside is very high. If no, it's vulnerable to competition.  
- Metric: "Addressable Market Size" — Not just market, but "attainable market" given your distribution. (BAMF's warm audiences have 10x higher conversion than cold, changing market size.)

  ---

  ### Dimension 9: Elements Impacting Probability of NOT Delivering

  **Sub-dimensions**: Fulfillment bottlenecks, dependency risks

  **What the Books Say**:

- **Hormozi**: "Your offer is only as good as your ability to fulfill it. Prove you can deliver before selling."  
- **Brunson**: "Operational excellence is the foundation of scaling. Perfect one offer before adding the next."  
- **Thiel**: "The first team determines everything. Founder dependency is the biggest risk."

  **Frameworks**:

- **Delivery Vehicle Assessment** (DFY/DWY/DIY, Attention level, Medium)  
- **Fulfillment Cost Mapping** (Phase 3\)  
- **Ease of Delivery Scoring** (5A)  
- **Operational Fragility Audit** (implicit in Ease of Delivery)

  **What Current Skill Covers**:

- Fulfillment cost identification (Phase 3\)  
- Delivery vehicle classification (Phase 3\)  
- Ease of Delivery dimension score (5A)

  **What Current Skill MISSES**:

- **No "build/buy/partner" decision**: For each component, decide: build (develop), buy (use existing tool), or partner (outsource). Skill doesn't force this decision.  
- **No "critical path" mapping**: Which components must work perfectly for the offer to deliver? Which have margin for error? Skill doesn't distinguish.  
- **No "vendor/supplier risk" assessment**: If offer depends on partnerships, what if they fail? Skill doesn't address.  
- **No "quality degradation" scenario**: As volume increases, does quality degrade? At what point? Skill doesn't forecast.  
- **No "testing/proof" requirement before finalizing**: Hormozi's principle: "Prove you can deliver before selling." Skill doesn't require this gate.  
- **No "milestone-based delivery" framework**: Some offers should be delivered in phases (Week 1, Week 2, etc.). Skill doesn't plan this.

  **Missing Mechanics**:

- Framework: "Fulfillment Build/Buy/Partner Decision" — For each component, which approach minimizes risk and cost? Build (owned), Buy (vendor), or Partner (outsourced)?  
- Framework: "Critical Path Analysis" — Which components are "critical path" (must work)? Which have slack (can fail)? Prioritize testing for critical path first.  
- Framework: "Quality Degradation Forecast" — As volume increases, what quality metrics degrade first? At what volume? How do we fix it?  
- Framework: "Proof-Before-Selling Gate" — Don't finalize offer until you've delivered to at least 5-10 customers (for DFY) or 50+ (for DWY/DIY). Skill should make this non-negotiable for RED or YELLOW offers.

  ---

  ## 4\. Chain Economics — What the Books Say

  ### The Core Principle: Profitable at Each Tier, Cascading Problem-Solution

  **Hormozi ($100M Money Models)**:

- Every money model has 3-4 offer types: Attraction, Upsell, Downsell, Continuity  
- Each tier's job: deliver value \+ create the problem that the next tier solves  
- Example: Free challenge → $600 program → gym membership. Each creates demand for the next.  
- Economics: First offer covers acquisition cost. Second offer (upsell) covers operating cost. Third (continuity) \= profit

  **Brunson (DotCom Secrets / Value Ladder)**:

- The value ladder has 6 tiers, each with explicit purpose  
- Transition mechanics: Lead Magnet creates awareness → Frontend converts to customer → Middle delivers core transformation → Backend provides done-with-you → High-Ticket is done-for-you  
- Key question: "What problem does THIS tier create that the NEXT tier solves?"  
- Each tier filters customers: only those who see success move to next tier (quality improves as you go up)

  **Suby (3% vs 97% Split)**:

- 3% are ready to buy immediately. 97% need nurturing.  
- Money model must have both paths: Fast path (3% → offer → qualify → close) and Slow path (97% → lead magnet → nurture sequence → gradual offer)  
- Premiums bridge this: same offer, different price/positioning to serve both segments

  **Thiel (Zero to One) / Expansion**:

- Start with dominant position in small niche  
- Then expand concentrically to adjacent markets from position of strength  
- Each expansion is a "market expansion," not "offer expansion"  
- E.g., Google: dominate search (niche) → expand to ads (adjacent) → expand to video (YouTube) → expand to maps → etc.

  ### Chaining Rules

  **Stage I: Get Cash**

- Goal: Turn strangers into customers reliably  
- Offer: Attraction offer (low-price, high-volume)  
- May take: 6-18 months to perfect  
- Must achieve: Positive unit economics (revenue \> fulfillment cost)

  **Stage II: Get More Cash**

- Goal: Make 30-day profit well above acquisition cost  
- Offer: Upsell \+ Downsell (different configurations for different customer preferences)  
- Trigger: After Stage I works reliably  
- Must achieve: LTV:CAC \> 3:1, PPD \< 30 days

  **Stage III: Get The Most Cash**

- Goal: Recurring revenue \+ maximize lifetime value  
- Offer: Continuity (membership, subscription, retainer)  
- Trigger: After Stage II is reliable  
- Must achieve: Customer lifetime value 5-10x higher than Stage I

  **Downsell Rules (Suby)**:

- If customer says NO to offer, present alternative  
- Never drop price for same thing (kills trust)  
- Offer something DIFFERENT for less OR same thing with different payment terms  
- Example: "Too expensive?" → "Try the 3-payment plan" OR "Try the lighter version"

  **Ecosystem Economics**

- Each offer must be profitable on its own merit  
- BUT: Total funnel profitability matters more than individual tier  
- Scenario: Tier 1 (frontend) loses money, Tier 2 (core) breaks even, Tier 3 (backend) is 10x profit  
- This is fine if Tier 3 revenue \> Tier 1 loss \+ Tier 2 cost

  ### What Current Skill Covers

- Value ladder tier identification (Phase 5\)  
- Ecosystem view rendering (Output 11\)  
- Money model type classification (Phase 5\)  
- Money model stage identification (Phase 5\)  
- Concept: "What problem does this offer create that the next offer solves?" (Phase 5\)

  ### What Current Skill MISSES

- **No "tiering profitability" model**: Skill identifies tiers but doesn't calculate if each tier should be profitable standalone vs. loss leader  
- **No "downsell cascade" design**: If customer rejects primary offer, what's the downsell? Skill asks but doesn't plan the seesaw (full price → payment plan → feature downsell)  
- **No "stage progression gates"**: When can you move from Stage I → Stage II → Stage III? Skill suggests timing but doesn't define gates (e.g., "Must have 100 Stage I customers before building Stage II")  
- **No "customer migration" tracking**: As customers upgrade, what percentage convert from Tier 1 → Tier 2? Skill assumes sequential purchase but doesn't track or optimize conversion rates  
- **No "margin requirement" by stage**: Stage I can have low margins (volume game). Stage III must have high margins (fewer customers). Skill doesn't enforce this constraint  
- **No "continuity integration" strategy**: When should continuity be introduced? Before, alongside, or after Stage II? Skill doesn't plan the timing or positioning

  ### What's Missing

- Framework: "Tiering Profitability Audit" — For each tier, specify: Should it be profitable standalone, or is it a loss leader? If loss leader, what's the acceptable loss? What's the payback timeline?  
- Framework: "Downsell Cascade Planning" — If customer says NO to primary offer, design 3-5 downsell options in descending price/scope. Test each.  
- Framework: "Stage Progression Gates" — Define the metrics that trigger moving from Stage I → II → III. E.g., "Must have 100 Stage I customers with \>70% retention before building Stage II."  
- Framework: "Customer Migration Modeling" — What percentage of Stage I customers are expected to upgrade? If \<10%, the funnel won't work. Design offers to improve migration.  
- Framework: "Continuity Embedding Strategy" — Should continuity be a 6th tier (after High-Ticket), or should it be a parallel option at every tier? Map the architecture.

  ---

  ## 5\. Meta Ads Scalability — What the Books Say

  ### Cold Traffic Characteristics

  **BAMF (Paid Ads Focus)**:

- **Custom Audiences \= warm**. LinkedIn connections, email subscribers, website visitors, fans. CPM 10x lower than cold.  
- **Dark post A/B testing**: Validate offer with $25-100 tests before scaling  
- **Chatbot conversion mechanics**: Engagement ad (low friction) → auto-messenger → link click → conversion. High-intent conversion path.  
- **Content hierarchy**: Curate → learn what works → mix original → dominate. Don't create new content until you know what sticks.

  **Brunson (Traffic Secrets)**:

- **The Hook-Story-Offer Framework**: Hook (pattern interrupt) → Story (belief shift) → Offer (call to action)  
- **Traffic Temperature Spectrum**: Warm (owned) → Cool (lookalike/pixel) → Cold (interest-based)  
- **The Dream 100 as primary strategy**: Instead of buying ads at scale, partner with 100 traffic sources. Higher conversion, better fit.  
- **Conversion rate improvement \> traffic increase**: Doubling traffic costs 2x. Improving conversion from 1% to 2% is free and doubles revenue.

  **Hormozi (Mostly Organic Focus)**:

- **Organic/referral \> paid ads**: Free offers → testimonials → partnerships → exponential growth  
- **Paid ads as capital**: Only use when you have proof your offer works and can sustain CAC \> LTV ratio  
- **Premium positioning for cold traffic**: If offer is premium ($5k+), cold traffic doesn't work well. Warm/referral only.

  **Suby (Godfather Offer for Cold Traffic)**:

- **The offer MUST be irresistible for cold traffic**: If prospects don't know you, the offer has to do ALL the work  
- **Premiums are leverage**: Adding premium items can 2-3x cold traffic conversion  
- **Positioning matters more for cold**: The offer name, value stack, guarantee must jump off the page when prospects see it cold

  **Thiel (Defensibility)**:

- **Monopoly offers don't need paid ads**: If offer is incomparable, demand is organic  
- **Competitive offers require paid ads**: If offer is commodity, you have to pay to acquire

  ### Offer Design for Paid Ads

  **Core Principles**:

1. **Cold traffic demands ultra-clarity** (Value Equation: Perceived Likelihood must be very high for strangers)  
2. **Offer name is primary copy** — No space for nuance (MAGIC formula is critical)  
3. **Stack slide is the second hook** — Visual proof of value stacking  
4. **Guarantee removes primary objection** — Risk-reversal is essential for cold  
5. **Premiums drive conversions** — High perceived value, low cost to deliver  
6. **Scarcity/urgency adds friction** — Must be REAL. Fake scarcity kills trust permanently  
7. **Testimonials/social proof bridge stranger gap** — Use customer language verbatim

   **Paid Ads Offer Optimization**:

| Dimension | Warm Traffic | Cold Traffic |
| :---- | :---- | :---- |
| **Clarity required** | Medium (you know them) | Ultra-high (total stranger) |
| **Proof required** | Light (they trust you) | Heavy (credibility gap) |
| **Guarantee** | Optional | Critical |
| **Premium value** | Nice-to-have | Deal-maker |
| **Scarcity/urgency** | Low pressure | High pressure |
| **Name complexity** | Can be subtle | Must be obvious |

   ### What Current Skill Covers

- Big Domino clarity (critical for paid ads)  
- Value Equation scoring (applies to cold traffic too)  
- Offer naming (MAGIC applies to all traffic)  
- Guarantee strategy (essential for cold)  
- Premium addition (important for cold)  
- Scarcity/urgency assessment

  ### What Current Skill MISSES

- **No "warm vs cold" offer differentiation**: Same offer, different positioning for warm vs cold traffic. Skill doesn't plan this.  
- **No "proof requirement scaling"**: Cold traffic needs 3-5x more social proof than warm. Skill doesn't require this gate for cold traffic offers.  
- **No "paid ads unit economics"**: With $5 CPM and 2% conversion, what's your CAC? Does the offer support it? Skill doesn't work backward from traffic cost.  
- **No "creative hook library"**: What hooks work for cold traffic in this niche? Brunson's Hook-Story-Offer framework isn't operationalized in current skill.  
- **No "audience temperature assessment"**: Should this offer go to warm or cold traffic first? What's the progression? Skill doesn't suggest.  
- **No "dark post testing gate"**: Before scaling cold traffic, do a $50 dark post test. If CPL \> acceptable, don't scale. Skill doesn't require this.  
- **No "lookalike/pixel audience strategy"**: Between warm (owned) and cold (interests), there's cool (pixels, lookalikes). Skill doesn't address.

  ### What's Missing

- Framework: "Paid Ads Readiness Assessment" — Before launching cold traffic, is the offer positioned for strangers? (Name, guarantee, proof, premium all present?)  
- Framework: "Traffic Temperature Roadmap" — Start with warm (owned audiences). When can you move to cool (pixel-based)? When to cold (interest-based)? At what CPL ceiling?  
- Framework: "Dark Post Test Protocol" — For cold traffic offers, run $50-250 test with 3-5 offer variations. Acceptance threshold: CPL \< 20% of offer price.  
- Framework: "Hook-Story-Offer Operationalization" (Brunson) — For each offer, define the hook (what breaks expectations?), story (belief shift), offer (call to action).  
- Metric: "Cold Traffic Unit Economics" — With estimated CPM/CPL, can you hit profitability? Work backward from acceptable CAC to required conversion rate.

  ---

  ## 6\. Critical Gaps in the Current Skill

  Specific, numbered list of what the current skill is missing or handles poorly:

  ### 1\. **No Market Validation Gate Before Interview**

  The skill assumes the market is "starving." Hormozi's first principle is validating the market BEFORE designing the offer. Current skill should gate the interview with: "Is there urgent demand for solutions like this? Do people have budget and are actively seeking?"

  **Impact**: RED offers built for weak markets waste time.

  ### 2\. **No "Cold Traffic Clarity" Testing**

  The skill produces offers that are clear to insiders but confusing to strangers. Missing: A framework to test offer clarity with cold prospects BEFORE finalizing. BAMF's dark post testing ($25) should be a required gate.

  **Impact**: Offers fail on paid ads despite scoring GREEN.

  ### 3\. **No Warm-to-Cold Offer Differentiation**

  Same offer can succeed with warm audiences but fail with cold. Skill treats all traffic the same. Missing: Explicit positioning/naming changes for cold traffic (more proof, stronger guarantee, premium addition).

  **Impact**: Offers that work organically fail when scaled to paid ads.

  ### 4\. **No Profitability Lever Analysis**

  When margin is low or LTV:CAC is poor, skill doesn't systematically suggest levers: (1) Reduce fulfillment cost (10x test), (2) Add premium tier, (3) Change money model, (4) Change market segment. Skill identifies the problem but doesn't fix it.

  **Impact**: RED offers stay RED instead of being re-architected.

  ### 5\. **No "Founder Dependency" Confrontation**

  The skill identifies "Ease of Delivery \= 3" but doesn't force a decision: Either delegate/automate or accept limited scalability. Missing: A hard audit forcing "Can this be delivered without you?" If not, what's the plan?

  **Impact**: Founders build unscalable offers and blame the market.

  ### 6\. **No "Customer Financed Acquisition" Optimization**

  Hormozi's CFA framework (when first-month profit \> CAC, next customer is free) is barely mentioned. Missing: A goal to structure offers to hit PPD \< 30 days, enabling self-funded scaling.

  **Impact**: Businesses fail due to cash flow despite healthy profitability.

  ### 7\. **No Downsell Cascade Planning**

  Suby's seesaw framework (full price → payment plan → feature downsell) isn't operationalized. Current skill asks "What's the downsell?" but doesn't require designing 3-5 options or testing them.

  **Impact**: Missed revenue when customers can't afford primary offer.

  ### 8\. **No "Quick Win" Integration**

  Suby's principle: deliver meaningful result in first 48-72 hours. Current skill mentions this in troubleshooting but doesn't require it in design. Missing: Phase where user specifies exactly what customer gets on Day 1, Day 7, Day 30\.

  **Impact**: Offers with long time-to-value have high refund rates.

  ### 9\. **No Guarantee Risk Assessment by Market Type**

  Unconditional guarantees work for B2C low-ticket. Conditional for B2B/high-ticket. Skill doesn't distinguish. Missing: A decision tree that maps guarantee TYPE to market characteristics.

  **Impact**: Inappropriate guarantees either leave money on the table or create refund liability.

  ### 10\. **No Stage I → Stage II → Stage III Progression Gates**

  Skill identifies stages but doesn't define when to move between them. Missing: Explicit gates like "Don't build Stage II until you have 100+ Stage I customers with \>70% retention."

  **Impact**: Premature scaling of upsells before proof of primary offer.

  ### 11\. **No "Market Ceiling" Calculation**

  Skill estimates LTV but not addressable market size. Missing: Assessment of "If this offer becomes perfect, how many customers could we serve?" This reveals upside.

  **Impact**: Offers optimized for small markets when larger adjacent markets are available (Thiel's expansion).

  ### 12\. **No Premium Tier as Standalone Option**

  Skill treats premiums as add-ons (bonuses). Missing: Exploration of premium as a separate tier (2-3x price for 20% of buyers \= 5-10x profit). Should be tested early.

  **Impact**: Revenue left on the table by not surfacing premium options.

  ### 13\. **No Pattern Interrupt Assessment**

  Is this offer category-of-one or just a better version of existing? Missing: A test to determine if offer is 0→1 (new) or 1→n (improvement). Thiel's 10x rule and BAMF's dark post testing address this.

  **Impact**: Offers positioned as unique when they're commodity (or vice versa).

  ### 14\. **No Offer Fatigue Rotation Strategy**

  When offers fade over time, Suby's rotation framework (creative → copy → name → duration → structure) isn't mentioned. Missing: A workflow to refresh tired offers before replacing them.

  **Impact**: Offers abandoned when a simple wrapper change would revive them.

  ### 15\. **No Technology/Automation Tool Recommendation**

  Skill says "automate" but doesn't suggest WHAT to automate or which tools/systems. Missing: For each delivery component, suggest 2-3 tools/approaches (software, template, hire) to reduce fulfillment friction.

  **Impact**: Automation stays theoretical instead of tactical.

  ### 16\. **No "Proof-Before-Selling" Gate**

  Hormozi's principle: don't sell before delivering to 5-10 test customers. Skill doesn't require this for RED/YELLOW offers. Missing: A mandatory gate where user confirms they've tested with real customers.

  **Impact**: Offers finalized without proof of deliverability.

  ### 17\. **No "Time to Money" vs "Time to Value" Distinction**

  These are different: Time to value \= when customer sees result. Time to money \= when you recover CAC. Skill conflates them. Missing: Separate metrics for each \+ separate optimization.

  **Impact**: Offers optimized for one but not the other.

  ### 18\. **No Continuity Embedding Strategy**

  When should continuity be introduced? As 6th tier? Parallel option at every tier? Missing: Strategic framework for integrating recurring revenue into the funnel.

  **Impact**: One-time offers miss recurring revenue upside.

  ### 19\. **No Competitive Positioning (Thiel Framework)**

  Offers should be incomparable to alternatives, not just better. Missing: Explicit assessment: Is this offer monopoly-like (no substitutes) or competitive (compared to many alternatives)?

  **Impact**: Offers positioned as commodities when they could be differentiated.

  ### 20\. **No Asset Reuse Plan**

  After designing the offer, what assets can be reused across multiple tiers/funnels? Missing: A framework to plan how one solution component serves multiple offers.

  **Impact**: High creation cost per offer instead of asset leverage.

  ---

  ## 7\. Recommended New Structure

  ### Reorganization Proposal for offer-architect Skill

  The current skill is strong on interviews and scoring but weak on:

1. Market validation gatekeeping  
2. Cold traffic optimization  
3. Profitability troubleshooting/redesign  
4. Chain economics planning  
5. Paid ads scalability

   **Proposed New Phase Structure** (8 phases instead of 6):

   #### Phase 0: Market Validation (NEW GATE)

   **Purpose**: Validate "starving crowd" before spending time on offer design

   **Questions**:

1. What is the market size and growth rate?  
2. Are people actively seeking solutions (searching, spending money)?  
3. Can you reach them affordably?  
4. Do they have budget?

   **Output**: Pass/Fail gate. If FAIL, recommend: Pivot market before redesigning offer.

   #### Phase 1: Market & Niche (UNCHANGED)

   #### Phase 2: Dream Outcome (UNCHANGED)

   #### Phase 3: Problems & Solutions (UNCHANGED)

   #### Phase 4: Trim, Stack & Price (ENHANCED)

   **Add**:

- Profitability lever analysis (if margin is low, suggest: reduce cost, add premium, change market, change model)  
- Premium tier as standalone option (not just bonus)  
- Payment plan impact on PPD

  #### Phase 5: Offer Position & Chain (ENHANCED)

  **Add**:

- Downsell cascade planning (3-5 options, not just "what if they say no?")  
- Stage progression gates (when to move I→II→III)  
- Customer migration rate assumption (% that upgrade)  
- Continuity embedding strategy

  #### Phase 6: Warm vs Cold Traffic Positioning (NEW)

  **Purpose**: Adapt offer for traffic source

  **Questions**:

1. Where will this offer be sold? (Warm, cool, cold)  
2. For cold traffic, what changes are needed? (Proof, guarantee, premium, name clarity)  
3. What's the dark post test threshold? (Required for cold before scaling)

   **Output**: Warm offer spec \+ Cold offer spec (same core, different positioning)

   #### Phase 7: Enhance, Name, & Proof (MODIFIED from current Phase 6\)

   **Add**:

- Proof-before-selling gate (have you tested with real customers?)  
- Quick win specification (what customer gets Day 1, Week 1\)  
- Guarantee risk assessment by market type  
- Offer fatigue rotation plan

  #### Phase 8: Paid Ads Readiness Check (NEW GATE)

  **Purpose**: Before finalizing, confirm offer is ready for paid media

  **Checklist**:

- [ ] Offer name passes cold traffic clarity test  
- [ ] Guarantee present and compelling  
- [ ] 2+ premium options designed  
- [ ] Proof (testimonials, case studies) documented  
- [ ] Stack slide can stand alone (no need to explain)  
- [ ] Dark post test planned or completed  
- [ ] CAC assumption viable (PPD \< acceptable)

      **Output**: GREEN (ready for ads) or YELLOW (needs tweaks) or RED (redesign needed)

      ### Revised Scoring Framework

      **Current**: 6-Dimension Score \+ Value Equation Score

      **Proposed Addition**: Paid Ads Readiness Score

| Dimension | Score (/10) | Rationale |
| :---- | :---- | :---- |
| Offer Clarity (cold traffic) | ? | Can strangers understand in \<5 sec? |
| Proof Presence | ? | Testimonials, case studies present? |
| Guarantee Strength | ? | Compelling enough for cold? |
| Premium Appeal | ? | Does 20% prefer premium? |
| Stack Visual Impact | ? | Does stack slide stand alone? |
| CAC Viability | ? | Can you hit profitability at realistic CPL? |
| **Paid Ads Readiness Score** | **?/60** | **GREEN/YELLOW/RED** |

      ### Revised Output Format

      **Current**: 14-section Offer Blueprint

      **Proposed Addition**:

- Section 15: "Warm vs Cold Offer Spec" (positioning for different traffic)  
- Section 16: "Paid Ads Readiness Assessment" (gate before launch)  
- Section 17: "Downsell Cascade Plan" (3-5 options if primary rejected)  
- Section 18: "Stage Progression Roadmap" (I→II→III with gates)  
- Section 19: "Proof & Testing Plan" (what's been validated, what remains)

  ### Integration with Downstream Skills

  **Upstream** (from client-researcher):

- Market validation data  
- Customer language (verbatim)  
- Competitor positioning

  **Downstream** (to creative-angle-writer):

- Big Domino \+ 3 False Beliefs  
- Hook (pattern interrupt)  
- Story arc (for paid ads copy)  
- Warm vs Cold positioning specs

  **Downstream** (to meta\_ads\_strategist):

- Offer architecture \+ pricing  
- Paid Ads Readiness Score  
- Audience temperature roadmap  
- Dark post test thresholds  
- Quick win specification

  ---

  ## Summary

  The offer-architect skill has strong foundations (Value Equation, Big Domino, Money Models, Value Ladder) but is optimized for **organic growth and warm audiences**. To be truly useful for **paid media scaling**, it needs:

1. **Market validation gatekeeping** — Don't design offers for weak markets  
2. **Cold traffic optimization** — Adapt offers for strangers, not just fans  
3. **Profitability redesign framework** — When metrics are poor, fix the offer, not just note it  
4. **Chain economics** — Plan downsells, Stage progression, continuity systematically  
5. **Paid ads readiness gates** — Validation checkpoints before scaling spend

   Adding these dimensions would transform offer-architect from a "design tool" to a "scalability tool" — ensuring offers work not just in theory but in the real world of paid media acquisition.

   ---

   ## 11\. 10X Rule (Grant Cardone) — Additive Insights

   ### What 10X Rule Adds vs. Current Framework

   The 10X Rule enters from a **different angle than the previous 10 authors**: while most focus on offer *positioning* and *profitability*, Cardone focuses on **activity levels, market domination, and the magnitude of thinking required to execute offers at scale**.

   #### Key New Dimensions Added

   **1\. Activity Multiplier as Core Lever (New)**

   Current framework: "You need massive action" (implicit in Value Equation, proof, cold traffic clarity).

   **10X Rule adds**: A specific, quantified mechanic—multiply your initial activity estimate by 10X.

   Application to offer design:

- If your baseline is "10 calls/day to close sales," 10X \= 100 calls/day  
- If your baseline is "1 email campaign/month," 10X \= 10+/month  
- If your baseline is "post 2x/day on social," 10X \= 20+ posts/day  
- This applies to **acquisition velocity**, not just offer quality

  Why it matters for paid ads:

- CPL scaling depends not just on offer quality but on volume of outreach  
- Cold traffic requires higher frequency; warm can succeed with less  
- "Posting twice daily on social is little think" — you must dominate attention space  
- Competitors retreat during downturns → expand (take market share)

  **Actionable addition to skill**:

- After finalizing offer, define baseline activity level (sales calls, emails, content, personal visits)  
- Multiply by 10X to get required execution velocity  
- Assess whether team/founder can sustain that level  
- If not, add to constraints (scalability blockers)

  ---

  **2\. Domination Posture vs. Competitive Posture (Complements Thiel)**

  Current framework: Thiel's "monopoly vs. competitive" positioning

  **10X Rule adds**: Regardless of market position, your execution must be domination-oriented, not competitive.

- **Competitive posture**: "How do we beat Company X?" → Watch competitors, copy best practices, react to their moves  
- **Domination posture**: "How do we own this entire sector?" → Ignore competition, do what they refuse, set the pace

  Example: Cardone's "Information-Assisted Selling" (1980s, pre-internet). Instead of competing on traditional sales methods, he created a new method no competitor could match.

  **Why this matters for offer design**:

- Offer shouldn't be positioned as "better version of existing"  
- Offer should be positioned as "new category/solution"  
- Cardone: "Do what others refuse to do" \= create unfair advantage

  **Thiel \+ Cardone synthesis**:

- Thiel says: "Find a monopoly niche where you're 10x better"  
- Cardone says: "Position as the only solution in a category, THEN dominate through 10X activity"  
- Current skill assesses positioning; **needs to add: are we positioned as category creator or category competitor?**

  **Actionable addition**:

- For each offer, define: Are we competing ON a dimension (better price, faster delivery) or CREATING a new dimension (new problem solved)?  
- If competing ON existing dimension → offer likely commodity → requires higher volume to break through  
- If creating NEW dimension → offer has category monopoly → lower volume can work but attention-seeking activity still required

  ---

  **3\. Scaling Threshold: When Activity/Visibility Trumps Offer Quality (Nuance)**

  Current framework: Value Equation covers clarity. Cold traffic requires proof.

  **10X Rule adds**: There's a **visibility ceiling** below which even perfect offers fail. You must reach a minimum attention threshold first.

  Cardone's example:

- Launched company with "decent idea" but "absolutely zero know-how, zero connections, zero money"  
- Succeeded solely through 10X activity levels  
- Proves: Activity \+ persistence can overcome offer mediocrity; lack of activity kills even good offers

  Corollary: In cold traffic environments (social media, paid ads), the activity multiplier matters MORE than offer perfection.

  **Why this matters for paid ads**:

- "Posting twice daily is little think" — you will not be noticed  
- To break through noise, you must be relentless \+ consistent  
- Competitors scale spend; you scale activity (both, but activity is force multiplier)  
- Market response comes from repeated exposure (10 touchpoints, 100 touchpoints) not single perfect message

  **Current skill gap**: Doesn't assess visibility gap. A perfect offer with zero visibility \= zero sales.

  **Actionable addition**:

- Define visibility target: "How many eyeballs must see this offer weekly to hit conversion volume goal?"  
- Work backward from visibility target to activity requirement  
- Then assess: Can team execute that activity level? If no, it's a scalability blocker

  ---

  **4\. Expansion During Contraction as Unfair Advantage (Thiel \+ Cardone)**

  Current framework: Thiel discusses "defensibility." Suby discusses "market saturation."

  **10X Rule adds**: Specific mechanics of expansion as competitive advantage.

  Cardone's 2008 playbook:

- While 95% contracted (cut staff, reduce spend), he expanded 10X (tripled marketing spend over 18 months)  
- Result: Gained market share from competitors retreating  
- Principle: "I would rather die in expansion than die in contraction"

  **Why this matters for offer design**:

- Offers designed during growth assume growing market  
- Offers designed during contraction must be acquisition-focused (lower price, higher proof, stronger guarantee)  
- But execution (activity level) should INCREASE when market contracts, not decrease

  **How Cardone's framework adds**: Market downturns \= opportunity if you keep expanding while others retreat. Offer shouldn't change (fundamentally), but positioning \+ activity must.

  **Actionable addition**:

- When economic conditions worsen, don't reduce offer scope or add skepticism  
- Increase acquisition focus (Cardone's principle: "Customer acquisition is the only right target")  
- Increase activity 10X to capture retreating competitors' market share

  ---

  **5\. Customer Acquisition as Primary Goal, Satisfaction as Secondary (Reframes Suby/Brunson)**

  Current framework: Strong on satisfaction, product quality, customer success.

  **10X Rule adds**: Explicit hierarchy—acquisition must come first, satisfaction second.

  Cardone's principle: "Customer satisfaction is impossible without a customer first."

- WRONG target: "Maximize customer satisfaction"  
- RIGHT target: "Maximize customer acquisition"  
- Then overdeliver to created customers

  Current skill conflates these. Cardone separates them.

  **Application to offer**:

- Don't over-engineer offer for satisfaction if it sacrifices acquisition  
- Don't reduce visibility (proof, promise, clarity) out of fear of customer dissatisfaction  
- Acquire 10X more customers, accept 10% more complaints, still net better off (9x happy customers vs. 0\)

  **Example**: Starbucks doesn't have the best coffee; they dominate on convenience (acquisition). Apple doesn't worry about satisfaction so much they kill innovation velocity.

  **Current skill gap**: Asks "Will this satisfy customers?" Missing: "Will this ACQUIRE customers? And once acquired, can we overdeliver?"

  **Actionable addition**:

- For each offer, separate: Acquisition-optimized positioning vs. Satisfaction-optimized delivery  
- Don't sacrifice acquisition positioning for satisfaction guarantees  
- Plan to overdeliver post-acquisition to maintain retention

  ---

  **6\. Goal Sizing as Fuel for Action (New Dimension)**

  Current framework: Hormozi discusses dream outcome. Suby discusses target market size.

  **10X Rule adds**: Goal size directly fuels execution velocity. Small goals create small motivation.

  Cardone's principle: "Average goal setting cannot and will not fuel massive 10X actions."

- Small goals \= insufficient energy to persist through resistance  
- When obstacles appear (guaranteed), goal must be big enough to outweigh obstacle magnitude

  **Why this matters for paid ads offers**:

- $10K monthly revenue goal \= low motivation to scale spend to $5K/day  
- $1M/month goal \= sufficient motivation to justify that spend  
- Offer design should tie to founder's goal (not just market opportunity)

  **Example from Cardone**:

- First job at McDonald's, made $7/hour for "spending money" \= no passion, fired  
- Coworker made $7/hour for "learn business, open 100 franchises" \= passionate, succeeded

  **Current skill gap**: Doesn't assess alignment between offer potential and founder's stated goal.

  **Actionable addition**:

- During interview, ask: "If this offer succeeds, what's the 10X revenue goal in 12-24 months?"  
- Assess: Is offer architecture capable of supporting that goal?  
- If gap between goal and offer potential: Either resize goal or redesign offer

  ---

  **7\. Obsession as Competitive Advantage (Reframes Execution Mindset)**

  Current framework: Suby discusses "founder energy." Brunson discusses "belief."

  **10X Rule adds**: Obsession (intense focus \+ relentless persistence) is a gift, not a liability.

- Society labels obsessive people as "crazy" until they succeed, then calls them "genius"  
- Offers require obsessive execution (not casual part-time effort)  
- Founders must be obsessed to push through resistance

  **Why this matters for offer design**:

- Offers requiring split attention (founder doing 10 other things) \= fail  
- Offers requiring obsessive focus \= succeed  
- Skill should assess: "Is founder obsessed with this problem/market?" If not, red flag.

  **Actionable addition**:

- During interview, gauge founder obsession level  
- Low obsession \+ high effort required \= scalability blocker  
- Flag in output: "Founder must increase obsession level or hire obsessed person to execute"

  ---

  ### What 10X Rule Reinforces from Current Framework

  **1\. Big Domino Clarity**: Cardone's "10X thinking" is aligned with Brunson's "one belief that knocks everything down." Both say: Get the core promise right, everything else follows.

  **2\. Value Equation**: Cardone's emphasis on "10X goals" \= dream outcome magnitude. His "10X action" \= removing time delay and effort barriers. Reinforces the equation.

  **3\. Domination Mindset (Thiel)**: Cardone's "ignore competitors, dominate sector" \= Thiel's "monopoly positioning." Different language, same principle.

  **4\. Activity Scaling (Suby)**: Suby's CFA framework (first-month profit \> CAC) requires sustained high-activity acquisition. Cardone's 10X activity is the execution method.

  **5\. Proof & Social Proof**: Cardone emphasizes "omnipresence"—being everywhere so you can't be ignored. This requires proof/visibility infrastructure, aligning with current framework's emphasis on testimonials, case studies.

  ---

  ### What 10X Rule Doesn't Add (Gaps Remain)

  **1\. No Offer Mechanics**

- Cardone discusses activity/thinking; doesn't address value stacking, payment plans, downsells, premium tiers  
- Current framework covers these better

  **2\. No Market Validation Process**

- 10X Rule assumes starving market exists; doesn't provide framework to validate it  
- Current framework (Hormozi, Suby) does this better

  **3\. No Cold Traffic Clarity Framework**

- Cardone is organic-first (sales calls, personal visits, social media); assumes audience knows about you  
- Doesn't address the "stranger clarity" problem of paid ads  
- Current framework addresses this better (Hormozi's clarity, Suby's cold traffic offer design)

  **4\. No Profitability Constraints**

- Cardone focuses on scaling action; doesn't systematically address "Can we actually profit at this scale?"  
- Current framework's LTV/CAC analysis handles this

  ---

  ### Recommended Updates to Meta-Analysis

  Based on 10X Rule insights, recommend these additions to current framework:

  #### Update to Gap \#11: "No Visibility Ceiling Assessment"

  **Current Gap**: Skill doesn't determine whether offer is visible enough to break through noise.

  **10X Rule Addition**: Add framework: "How much activity is required to reach visibility threshold?"

- Baseline activity assumption (calls, emails, posts, personal visits per week)  
- Market noise level (how many competing messages)  
- 10X activity multiplier  
- Resulting visibility score (will this be noticed?)

  #### Update to Gap \#3: "No Warm-to-Cold Offer Differentiation"

  **Current Gap**: Same offer for warm and cold traffic.

  **10X Rule Addition**: But ALSO account for activity differential:

- Cold traffic \= high activity required \+ higher proof \+ stronger guarantee  
- Warm traffic \= lower activity required \+ lighter proof \+ softer guarantee  
- Offer mechanics stay same; activity execution changes 10X

  #### Update to Gap \#20: "No Asset Reuse Plan"

  **Current Gap**: How to scale offer efficiently.

  **10X Rule Addition**: Add planning for "Expansion vs. Contraction" strategy:

- In growth phase: Assets/messaging scale across channels (email, social, webinars, podcasts, personal)  
- In contraction: Same assets reused with higher frequency (10X posting, 10X emails)  
- Prevents need to constantly create new assets

  #### Update to Recommended Phase Structure (Section 7\)

  **Phase 9: Activity Scaling Plan (NEW)**

  **Purpose**: Define execution velocity required to hit revenue goal

  **Questions**:

1. What's baseline activity (calls, emails, content, visits)?  
2. What's 10X activity level?  
3. Can team execute that? If not, what's the constraint?  
4. If in contraction/competition, is activity high enough to dominate?

   **Output**: Activity velocity assessment \+ scalability blocker flagged

   ---

   ### Updated Critical Gaps (20 → 22\)

   **Gap \#21: No Activity-Scaling Assessment**

- **What's missing**: After finalizing offer, define required execution activity level and assess team capacity  
- **Why it matters**: Perfect offer with low activity fails; mediocre offer with high activity succeeds  
- **10X Rule teaches**: Activity multiplier is a lever (not just motivation factor)

  **Gap \#22: No Expansion-vs-Contraction Positioning**

- **What's missing**: Offers should have different activation strategies depending on market conditions  
- **Why it matters**: Same offer succeeds in growth phase but fails in contraction (or vice versa) if activity levels don't scale  
- **10X Rule teaches**: When market contracts, expand activity (don't reduce offer)

  ---

  ### Synthesis: What 10X Rule Contributes to Offer-Architect Skill

  **Overall Assessment**: 10X Rule is **orthogonal to current framework**, not reinforcing.

- **Current framework optimizes**: Offer clarity, market fit, profitability, scalability architecture  
- **10X Rule optimizes**: Execution velocity, domination mindset, activity multiplier, goal magnitude

  **Best integration point**: In the "Paid Ads Readiness" phase (Gap \#8), add assessment:

```
Can this offer be executed at 10X activity levels?
- Activity requirement defined? ☐
- Team capacity sufficient? ☐
- Founder obsession level adequate? ☐
- Expansion posture (not contraction) adopted? ☐
- Goal size sufficient to fuel required effort? ☐
 
If ANY ☐ is unchecked → YELLOW (needs refinement) or RED (blocker)
```

  This ensures offers aren't just well-designed but also well-executed at scale.


# Tab 10

# Conversation

All 5 phases done. Here's what the testing revealed — the numbers are damning in a useful way.

**Results: 7 PASS (28%) / 7 PARTIAL (28%) / 11 FAIL (44%)**

The skill passes almost nothing that involves real-world messiness. Here's where it breaks and why it matters:

**The 5 most critical failures (Tier 1 fixes):**

1. **Warm/cold traffic split** — When someone brings a working organic offer and wants to scale it to Meta, the skill gives zero guidance on what needs to change for cold traffic. This is your core use case as an agency. HIGH criticality.  
     
2. **Market validation gate** — Someone comes in excited about an offer for a market that has no urgent pain or no purchasing power. The skill runs them through all 6 phases, scores it, produces a blueprint, and never catches the fundamental problem. Complete waste.  
     
3. **Unit economics for paid media** — Skill doesn't work backward from CPM/CPL to required conversion rate to determine if the offer can support paid acquisition at all. It calculates margins but not whether those margins survive a $30 CPL on Meta.  
     
4. **Proof-before-selling gate** — New offer, zero customers, person wants to scale to paid ads immediately. Skill produces a blueprint without requiring any proof of deliverability or market response. Leads to burning ad spend on unproven offers.  
     
5. **Downsell cascade \+ funnel mandate** — Someone brings a single offer. Skill evaluates it in isolation. Never forces the question: "Is this offer designed as part of a sequence, or standalone?" Single offers evaluated without funnel context get wrong profitability readings.

   **The pattern underneath all failures:** The skill was built for a founder designing an offer in isolation for a warm audience. It breaks whenever the scenario involves paid media, chain economics, or an offer that needs to be re-engineered rather than just scored.

   **The implementation path suggested:**

- v1.1 (critical): Add market validation gate, warm/cold split, unit economics for paid ads, proof gate  
- v1.2 (important): Operational audit, downsell cascade, creative fatigue rotation, guarantee by market type  
- v1.3 (polish): Stage progression gates, premium tier testing, market ceiling, activity scaling

  This is enough to rewrite the skill with confidence. We know exactly what's broken and why. Want to move to the rebuild now?

I will tell you what I am considering regarding the offer, so maybe you will be able to test it against the real scenario. Below are my thoughts. Try to organize it and see how it would simulate real conversation with a skill

So far I have been trying to lead my offer with communication around fixing diagnostics, basically implementing conversion API, so the ads can be more profitable and the founders can see the real picture. Later I sort of got off the rails because it wasn't clear for people if I'm a technical company or if I provide my ads. I felt they cared more about the growth in revenue, not fixing some stuff regarding the e-commerce owners. I came up with the offer of profit share, where I charge a percentage of the contribution profit that I make for them in a particular channel. For example, in Meta Ads, they have revenue. We need to deduct VAT, cost of goods sold, and ad spend, and what's left we charge a percentage. There is also a €2,000 startup fee or initiation fee, and they have to cover the production costs, which were so far €25 per ad designer hour. Right now I was thinking about standardizing that, for example:

* image ad costs, let's say €2  
* video ad costs €10 or something like that so the client can have clarity, but I think that's not sufficient. Probably there should be some minimum on how much creative sense to be produced. I feel like it's getting more into the traditional model of retainer plus a percentage of the ad spend. I am not sure if that offer is that unique anymore, because I was leading with "agencies are screwing you over." If you're an e-commerce doing at least €200,000 in monthly revenue, you will earn money only when you earn money, but there are a couple of exceptions to this, as you can see. For example, I have a couple of clients that aren't making that much money, a profit, and close to nothing, and I charge them on my graphic designer hours, which is also quite low. I think there is a flaw in this offer. Maybe I didn't select the clients properly. I think the client selection should be also part of the skill. For example, with a client that has 10% gross profit, like Iiyama monitors, it will be harder to make profit than with somebody who has 70% gross profit. Correct me if I'm wrong. Maybe it's not linear; there are probably other elements in place here. I was thinking about an offer of an additional €100,000 in revenue, or you don't pay, and we would create a list of things that should be implemented in the business and may or may not implement them with the business owner, like:  
* Make sure the Meta pixel is tracking properly  
* Check the conversion rate  
* Create at least 40 ads with unique angles  
* Set up email marketing automation  
* Negotiate costs with suppliers  
* Stuff like that I don't know if it's a good idea for an offer. These are just my thoughts.

  

  Let me first organize what you've described into a clean scenario, then simulate the skill conversation against it — including where the current skill would fail and what an improved skill would catch.

  ---

  **Organizing your raw input:**

  What you have is not one offer — it's three offers in an identity crisis, layered on top of a positioning pivot that was never fully completed:

- **Offer 1 (original):** Tracking/CAPI fix → died because market didn't know they wanted it  
- **Offer 2 (current):** Profit share on contribution margin \+ startup fee \+ variable creative costs → live but economically broken on low-margin clients  
- **Offer 3 (idea):** "+€100K revenue or don't pay" with implementation checklist → undefined, untested

  The positioning statement "agencies are screwing you over" was your Big Domino. But the offer has accumulated exceptions and asterisks that contradict it. That's the core tension.

  ---

  Now let me simulate the skill conversation as it currently exists, then show what breaks.

  ---

  **SKILL SIMULATION — Current Version**

  ---

  **Phase 1: Market & Niche**

  Skill asks: *What do you sell, who is your buyer, what's their burning pain?*

  You'd answer: Meta Ads management for e-commerce owners doing €200K+/month revenue. Their pain: they're overpaying agencies that charge retainers regardless of results, and they can't trust their own data because tracking is broken.

  **Skill response:** Performs Starving Crowd Check.

- Urgent pain? ✅ — Ad costs rising, iOS changes broke attribution, owners can't tell what's working  
- Purchasing power? ✅ — €200K+/month means budget exists  
- Reachable? ✅ — E-commerce owners congregate in specific communities, targetable on Meta

  **Verdict: PASS.** Skill proceeds.

  *What's missing here:* No client selection criteria. The skill doesn't ask: "Are all €200K+ e-commerce businesses equally viable for this offer?" It should catch that a €200K/month business with 10% gross margin is structurally a bad client for a contribution-profit model. The Iiyama monitor example would kill you here — 10% gross margin means after VAT, COGS, and ad spend, contribution profit might be near zero. Your % of nearly-nothing is nearly nothing. **The skill doesn't screen for margin viability.** This is Gap \#1 (market validation gate) applied at the client level.

  ---

  **Phase 2: Dream Outcome**

  Skill asks: *What's the dream outcome? Current reality vs. desired reality? What have they tried before?*

  You'd answer: They want more revenue from Meta with confidence that their spend is working. Current reality: paying agency retainers, getting reports they don't trust, bleeding ad spend on campaigns that may or may not be working. Failed solutions: in-house media buyers who don't know what they're doing, previous agencies that charged €3-5K/month regardless of results.

  **Skill response:** Drafts Dream Outcome Statement and Big Domino.

*"I help e-commerce founders doing €200K+/month generate measurable contribution profit from Meta without paying for media buyers who aren't accountable for results."*

Big Domino: *"If I can make them believe that performance-based pricing is the only model that aligns agency and client incentives, and that Mindlink is the only agency that operates this way, all objections about fees and results become irrelevant."*

**Verdict: PASS.** Reasonable output.

*What's missing:* The skill doesn't flag that the Big Domino ("agencies are screwing you") is being undermined by the startup fee \+ creative costs. If your positioning is "you only pay when you win," then a €2,000 upfront fee is a contradiction that a cold prospect will immediately notice. **The skill should catch positioning contradictions between the Big Domino belief and the actual offer structure.** It doesn't.

---

**Phase 3: Problems & Solutions**

Skill asks: *List every obstacle between buyer and dream outcome.*

You'd generate a list: broken tracking → wrong data → wrong decisions / no creative production system → inconsistent ad creative / no email automation → lost revenue on traffic they're already paying for / wrong client-agency incentive structure → agency optimizes for spend, not profit / etc.

**Skill response:** Builds Solution Stack Table. For each obstacle, what's your solution and delivery vehicle?

This is where it starts to surface your actual problem: *you have listed 5-6 different solutions that span technical implementation, creative production, media buying, and email marketing.* The skill would ask you to classify each as DFY/DWY/DIY.

The checklist you described (+€100K or don't pay idea) — tracking fix, CRO check, 40 ads, email automation, supplier negotiation — that's not an offer. That's a scope document for a full-service growth agency. The skill would technically process it, but it would give you a dangerously high "Ease of Delivery" risk score without telling you *why* it's risky.

*What's missing:* The skill identifies "Ease of Delivery \= 3" but doesn't force the question: **Who delivers each of these things? You personally? A team? A contractor?** If the implementation checklist requires 6 different competencies (tech, creative, media buying, email, CRO, supplier negotiation) and you're a small agency, this offer fails at scale. The Founder Dependency audit is missing entirely. **This is Gap \#5 — and it's critical for you specifically.**

---

**Phase 4: Trim, Stack & Price**

Skill asks: *Trim low-value items, build the stack slide, define pricing, choose guarantee.*

This is where the economics break down hardest. Let me show you why.

Your current pricing:

- Startup fee: €2,000  
- Creative: variable (hourly) or standardized (€2/image, €10/video)  
- Performance: % of contribution margin

  Skill would ask: *What's the value-to-price ratio?*

  Problem: **You can't calculate a stack slide for a profit-share model.** The value is variable by definition. The skill is built around fixed-price stacking. It doesn't have a framework for: "What is the perceived value of an offer where price is unknown in advance?"

  For the client, the perceived risk is high precisely because they can't predict their cost. That's the opposite of what a stack slide achieves. A stack slide builds perceived value by making the price feel small relative to visible value. Your model makes the price feel unknowable, which some clients will read as risky.

  The standardization you're considering (€2/image, €10/video) is actually a move toward recoverability — it makes costs predictable. But it does push you toward the retainer model you're trying to avoid. **This is the fundamental tension in your offer and the skill doesn't have a framework for diagnosing it.**

  *What's missing:* The skill has no framework for evaluating **variable-price / performance-based models**. No profitability lever analysis for: "If contribution margin is low for some clients, what's the floor below which we don't take them?" No client qualification filter based on margin viability. **This is Gap \#4 combined with a completely missing dimension: performance-model economics.**

  ---

  **Phase 5: Offer Position & Chain**

  Skill asks: *Where does this sit on the value ladder? What comes before, what comes after?*

  Your current chain:

- Attraction: "Agencies are screwing you" positioning (cold traffic / organic)  
- Frontend: CAPI/tracking audit → this was your original lead, but it confused people  
- Core: Profit-share management model  
- Logical next: Upsell to retained services (email, full growth stack)

  **Skill response:** Renders Ecosystem View. Identifies your current offer as Stage I (Get Cash) — trying to turn strangers into clients. Points out the Stage II upsell isn't designed yet.

  *What's missing:* No downsell cascade. What happens when a good prospect says "I like the model but €2,000 upfront is too much right now"? Or "I want to test you before committing to profit share"? You have no designed answer. The skill asks "what's the downsell?" once, you'd probably say "nothing yet," and it would move on. **Gap \#7 — the seesaw from full commitment to trial to minimum viable entry isn't built.** For your offer specifically, a 30-day trial at cost-only could be a powerful downsell that converts hesitators.

  ---

  **Phase 6: Enhance & Name**

  Skill asks: *Scarcity, urgency, premiums, MAGIC naming.*

  This is where the "agencies are screwing you" positioning either becomes a brand weapon or a cliché. The skill would generate naming options. Something like:

- *"E-Commerce Profit Partnership — 90 Days to Measurable Meta ROI, or You Don't Pay"*  
- *"The Aligned Growth Model — Meta Ads on Pure Performance for €200K+ Stores"*

  These are fine. But **the positioning statement "agencies are screwing you" is the pattern interrupt**, and the skill doesn't tell you whether it's still differentiated or if it's become a commodity claim that every agency now uses. **Gap \#13 — no pattern interrupt assessment.** "Performance-based agency" was novel in 2020\. In 2026 it's a crowded category.

  ---

  **SCORING — What the current skill would output:**

| Dimension | Score | Reality |
| :---- | :---- | :---- |
| Attractiveness | 7 | The profit-share model is genuinely differentiated |
| Pattern Interrupt | 5 | Was stronger 3 years ago, now crowded |
| Ease of Understanding | 4 | "Contribution margin %" is not immediately clear to most founders |
| Ease of Delivery | 4 | Too many components, founder-dependent |
| Time to Value | 5 | First result in 30-60 days typically |
| Time to Money | 3 | Your CAC recovery is slow — startup fee helps but contribution profit takes months to accumulate |

  **Total: \~28/60 — YELLOW.** Skill says "refine before finalizing." But it doesn't tell you *what specifically is broken* or how to fix it. It just notes the scores.

  ---

  **What the improved skill would catch that the current one misses:**

  **1\. Client qualification filter — the Iiyama problem.** Before designing the offer, the improved skill asks: "What is the minimum gross margin a client must have for your profit-share model to be economically viable?" At 10% gross margin, after VAT (\~23%), COGS (10%), and ad spend (15%), contribution margin is near zero. You cannot charge a meaningful % of zero. The skill should output: **Minimum viable gross margin \= X%. Screen out clients below this threshold before onboarding.**

  **2\. Positioning contradiction audit.** The Big Domino is "you only pay when you win." The offer has a €2,000 startup fee. These are in direct conflict. The improved skill flags this immediately: *"Your positioning says no upfront risk, but your offer has upfront cost. Either rename the startup fee (reframe it as 'skin in the game' or 'onboarding investment') or remove it and absorb the cost into your performance %. You cannot have both without undermining the claim."*

  **3\. Performance model economics.** Your profit-share is variable income for you. The improved skill asks: "What is your estimated contribution margin per client per month? What % are you charging? What is your resulting revenue per client? How many clients do you need to hit your revenue target?" This reverse-engineers whether the model is even viable at your current client base size.

  **4\. The \+€100K guarantee idea.** The improved skill would flag this immediately with the Failure Mode Analysis: *"A €100K revenue guarantee has delivery risk tied to factors outside your control — client's product quality, website CRO, inventory levels, supplier costs. What conditions must be true for you to guarantee this? If those conditions aren't defined, you're taking unlimited liability."* The checklist (pixel fix, CRO, 40 ads, email setup) is actually your answer — it's the conditions. But they need to be framed as *client obligations*, not just your deliverables.

  **5\. Warm vs. cold traffic positioning.** Your current offer works when explained in person or through warm referrals. "Contribution margin %" requires a conversation to understand. For cold traffic on Meta, nobody reads the definition — they need to understand the benefit in 5 seconds. The improved skill forces you to separate: *Warm positioning* (detailed, nuanced, for prospects who already know you) vs. *Cold positioning* (simple, visceral — "We don't get paid until your Meta Ads make you money. Simple as that.").

  ---

  **The single biggest diagnosis the skill should make but doesn't:**

  Your offer is not one offer. It's a service model trying to solve a positioning problem. The original lead (CAPI/tracking) was the right entry point technically — broken tracking is the actual reason most e-commerce Meta campaigns underperform. But "fix your tracking" doesn't sell because **nobody wakes up wanting their pixel fixed. They wake up wanting more revenue.**

  The tracking fix is the mechanism. Revenue is the outcome. Your Big Domino should be: *"Your Meta ads are underperforming because your data is lying to you — and nobody in your current agency has any incentive to fix it because they get paid regardless."* That leads naturally into both the technical credibility (we fix the data) and the commercial proposition (and we only earn when the fixed data shows real results).

  The current skill would not surface this reframe. The improved skill should — because it separates "what the buyer wants" (revenue) from "what makes your solution credible" (tracking expertise) and asks: *Are you leading with mechanism or outcome? And does your lead match what cold traffic responds to?*

  ---

  Ready to rebuild the skill with all of this incorporated? That's the actual output of this whole process — a v2 of offer-architect that would have caught every one of these issues.

I really like your answer and the discussion. I want you to think about this type of conversation, because this skill will be used also to diagnose and audit existing offers. It should ask a follow-up question if something is unclear and also make suggestions on how to improve or what are potential elements to improve in particular elements. When you consider "do it for you", "do it with you", "do it yourself", the skills should also consider different approaches and propose some suggestions, providing pros and cons of each one. To sum up, the skill should be like an offer creation consultant or something like this. Do you know what I mean? Please think about it deeply and present me a plan on how it should be improved. Based on that, also ask me clarifying questions if you need any before improving the skill.

This is the right evolution. What you're describing is a shift in the skill's fundamental architecture — from **structured interview** to **thinking partner**. Let me lay out exactly what that means and what it requires, then ask you the questions I need answered before we rebuild.

---

## The Core Architecture Problem

The current skill is **linear and passive**. It moves through phases like a form — collects answers, scores them, outputs a blueprint. It processes inputs. It doesn't think about them.

A consultant does something structurally different:

1. **Listens for what wasn't said**, not just what was  
2. **Reflects tensions back** — "You said X but also Y, and those contradict each other"  
3. **Has a position** and shares it, even if uncomfortable  
4. **Works backward from the problem**, not forward from a template  
5. **Proposes alternatives with explicit trade-offs** instead of asking you to choose blindly  
6. **Knows when to push forward and when to stop and resolve something**

   The current skill can't do any of this because its architecture doesn't allow it. It's a questionnaire that happens to have smart questions. The rebuild needs to change the underlying model.

   ---

   ## Two Modes: Creation vs. Audit

   The skill currently only knows how to create. But your most valuable use case — and the one your conversation about Mindlink demonstrated — is **audit**: someone has an existing offer, it's underperforming, they need a diagnosis.

   These are different entry points with different logic:

   **Creation mode** starts from scratch. The consultant helps you build from the ground up, validating market fit before designing anything.

   **Audit mode** starts from a mess. The consultant receives whatever exists — a pricing page, a description, a confused brain dump like yours — and does three things before anything else: (1) organizes what it heard, (2) identifies the tensions and contradictions, (3) asks the 2-3 questions that would unlock the diagnosis. Only then does it move into prescription.

   The Mindlink conversation we just had is a perfect example of audit mode working correctly. You gave me a stream of consciousness. I organized it, identified the three core tensions (positioning contradiction, economics model mismatch, delivery scope creep), and diagnosed from there. The current skill couldn't have done that — it would have tried to run you through Phase 1 and waited for clean inputs.

   ---

   ## The Consultant Interaction Model

   Instead of phases, the rebuilt skill needs **states** — and it should know which state it's in and why.

   **State 1 — Intake.** Free-form. The person describes their situation. Creation mode or audit mode auto-detected from the description. Skill doesn't interrupt, doesn't ask clarifying questions yet, just listens.

   **State 2 — Reflection.** Before any questions, the skill reflects back what it heard. Three layers: (a) What you said — organized clearly, (b) What's implicit — tensions and assumptions embedded in what you said, (c) What's missing — the things not mentioned that matter. This reflection is the highest-value step a consultant performs. It proves they actually understood the problem, and it often surfaces the real issue before a single question is asked.

   **State 3 — Diagnosis questions.** Maximum 2-3 questions at a time. Each question should be targeted — not a checklist, not a phase, but specifically aimed at the highest-uncertainty element in the current picture. When the answer resolves that uncertainty, the next question addresses the next highest uncertainty. The skill should never ask a question whose answer it can reasonably infer.

   **State 4 — Options.** For every decision point, present alternatives. Not "what do you want to do?" but "here are three ways this could go, with trade-offs for each — here's which one I'd recommend and why." The recommendation matters. A consultant who presents options without a recommendation is just shifting the cognitive burden back to you.

   **State 5 — Synthesis.** Once enough is known, produce the blueprint. But the blueprint in audit mode looks different from the blueprint in creation mode. Audit mode produces a diagnosis first (what's broken and why), then a redesign recommendation (what to change and in what order), then the blueprint of the improved offer.

   ---

   ## The DFY/DWY/DIY Framework

   The current skill uses DFY/DWY/DIY as a classification — it labels each delivery component. That's not enough.

   For every component, the skill should:

   **1\. Identify current mode** — How is it being delivered today?

   **2\. Stress-test that mode** — Is this mode actually viable at scale? What breaks?

   **3\. Present all three modes with explicit trade-offs:**

| Mode | Pro | Con | Best for |
| :---- | :---- | :---- | :---- |
| DFY (you do it for them) | Highest value perception, client gets results without effort | Highest delivery cost, least scalable, founder-dependent | High-ticket, relationship-driven, proof-building phase |
| DWY (you do it with them) | Shared responsibility, teachable, more scalable | Quality variance, requires client execution, slower results | Mid-market, clients with some capability |
| DIY (you give them tools) | Fully scalable, lowest cost, infinite leverage | Lowest perceived value, high client failure rate, support burden | Low-ticket, high-volume, self-serve audiences |

   **4\. Give a recommendation** based on: stage of business (proof-building vs. scaling), client's capabilities, price point, and the founder's own bandwidth.

   For your specific situation — creative production for Mindlink clients — the right question isn't "which mode?" It's "which mode for which component, at which client revenue level?" A €2M/year e-commerce client gets different delivery than a €200K client, and the skill should force that differentiation explicitly.

   ---

   ## The Follow-Up Question Logic

   The skill needs triggers — conditions that automatically generate a follow-up. Here are the ones that matter most:

   **Contradiction trigger**: When two stated facts conflict (e.g., "we only get paid when they profit" AND "we charge a startup fee"). Surface the contradiction directly: *"These two elements are in tension. You said X but also Y. Which is the actual positioning, and which is the exception?"*

   **Vagueness trigger**: When a claim is unanchored (e.g., "they want more revenue"). Push to specific: *"More revenue" is not a buying trigger. What specific number, in what timeframe, from what current baseline?"*

   **Assumption trigger**: When something is stated as fact but sounds like a hope (e.g., "clients will see results in 30 days"). Ask for the evidence: *"On what basis — from what past client results — are you confident in that timeline?"*

   **Scope creep trigger**: When the solution stack grows to more than 3-4 distinct competencies. Flag it: *"You've just described 6 different capabilities. That's not an offer — it's a department. Which of these do you do better than anyone else? That's the offer. The rest are either bonuses or a separate service line."*

   **Economics trigger**: When pricing model is variable or performance-based. Always ask for the economics: *"What's your expected revenue per client per month under this model, based on real client data or realistic assumptions? And what's your cost to deliver?"*

   ---

   ## What Needs to Change in the Skill Files

   **SKILL.md** needs a fundamental rewrite. The phase structure becomes secondary to the interaction model. The skill needs a description of how to behave as a consultant — when to reflect, when to question, when to push back, when to recommend.

   **New reference file needed: `consultant_behaviors.md`** — The rules of engagement. How the skill detects mode (creation vs. audit), how it structures reflection, what the follow-up triggers are, how to present DFY/DWY/DIY options, how to make a recommendation with conviction.

   **New reference file needed: `offer_diagnostics.md`** — The audit-mode equivalent of the current interview. Common offer pathologies, their symptoms, and their causes. (E.g., "offer worked with warm audience but fails on cold" → symptom: low cold CTR, cause: clarity gap, treatment: cold positioning rewrite \+ proof addition.)

   **The blueprint template** needs an audit variant — different from the creation blueprint. It should have a "diagnosis" section at the top before the offer architecture.

   **The scoring framework** stays, but the trigger changes. Instead of scoring after Phase 6, the skill should score at State 2 (after reflection) as a preliminary read, flag the low-scoring dimensions, and then conduct targeted questioning specifically to address those dimensions.

   ---

   ## Clarifying Questions Before I Rebuild

   I have three questions, and one of them will significantly change the architecture:

   **1\. Who uses this skill — and in what context?**

   Is this purely for your own offers at Mindlink, or do you see yourself using it during client discovery calls — running a client's e-commerce offer through the skill in real-time? The reason this matters: if it's client-facing, the skill's language needs to shift (less jargon, more translation), and the output format changes (a document you hand to the client vs. a working document for yourself).

   **2\. How opinionated should the skill be?**

   There's a spectrum. On one end: the skill asks good questions and presents options, but defers to you on every decision. On the other end: the skill makes a recommendation, states its reasoning, and pushes back if you disagree. Your Mindlink scenario is a good test case — when you described the €100K revenue guarantee idea, should the skill have said "that's risky for these reasons, here's a safer version" and stopped? Or presented the idea neutrally with pros and cons and waited for you to decide? I'd argue the former is more valuable, but you need to want that kind of pushback.

   **3\. For the DFY/DWY/DIY analysis — are we analyzing Mindlink's delivery model, the client's delivery model, or both?**

   In your situation, there are two layers: (a) how Mindlink delivers its services to e-commerce clients (your offer), and (b) how those e-commerce clients deliver their products/services (their offer, which you're helping them optimize via ads). If someone uses this skill to audit their own offer, the DFY/DWY/DIY analysis is straightforward — it's about their delivery. But if Mindlink uses the skill to design its own offer, you're analyzing your own delivery. Are these the same skill, or do we need a mode distinction?

   