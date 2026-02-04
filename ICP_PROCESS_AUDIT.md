# ICP Process Audit (The "Scientific Truth" Edition) - V5

## The User's Challenge
>
> "Are you sure CPM is only quality metric? I want you to research deeply. Use Occam's Razor."

**Verdict**: My previous hypothesis was **WRONG**. Research confirms: **CPM is NOT a proxy for Quality**.

* High CPM can mean "High Competition" OR "Bad Ad Experience" (Meta Penalty).
* Low CPM can mean "Junk Audience" OR "Viral Ad" (Meta Reward).
* **Occam's Razor**: The simplest explanation for "Quality" is **Did they buy?** (CPA & ROAS). CPM is just the "Entry Fee".

---

# 1. First Principles Analysis (The Correction)

**The Old Myth**: "High CPM = Premium Buyers".
**The Scientific Reality**:
$$CPM = \frac{Total\ Budget}{Impressions} \times 1000$$
CPM is influenced by:

1. **Supply/Demand**: Holiday Season = High CPM. (No relation to user quality).
2. **Ad Relevance**: Low Quality Ranking = Penalty High CPM. (Negative relation to quality). // *Counter-intuitive: Bad ads cost MORE.*
3. **Audience Size**: Small Niche = High CPM.

**Conclusion**: You cannot judge traffic quality by price alone. You must judge it by **Outcome**.

---

# 2. The "Efficiency Triangle" Model (System V5)

We evaluate every Product/Ad through 3 lenses relative to the **Objective (Sales)**:

### Lens 1: The Cost of Reach (CPM)

* **Context**: "How expensive is the shelf space?"
* *Diagnostic*: High CPM is only acceptable if CTR and CR are high enough to offset it.

### Lens 2: The Relevance of Ad (CTR)

* **Context**: "Does the audience care?"
* *Diagnostic*: High CTR lowers your effective CPC, combating High CPM.

### Lens 3: The Relevance of Offer (CR)

* **Context**: "Is the Scent Match real?"
* *Diagnostic*: This is the ultimate "Quality Check". If High CPM leads to High CR, the audience was Premium. If High CPM leads to Low CR, the audience was just... expensive (or the Page is broken).

---

# 3. The New Diagnostic Logic (Decision Tree)

**Rule #1: The Objective Filter remains.** (Sales Only).

**Rule #2: The "CPA Logic" (The King).**

* **If CPA is Good** -> We don't care if CPM is $5 or $50. **It Validates Itself.**
* **If CPA is Bad** -> We diagnose WHY using the Triangle.

**Rule #3: The Diagnostic Scenarios**:

| Scenario | CPM (Cost) | CTR (Attention) | CR (Desire) | Diagnosis (Action) |
| :--- | :--- | :--- | :--- | :--- |
| **The "Burn"** | High | Low | Low | Ad is irrelevant & expensive. Meta hates it. **(Kill)** |
| **The "Mismatch"**| High | High| Low | Attention is there, but Offer fails. Ad promised too much? **(Fix LP)** |
| **The "Premium"** | High | High| High| Expensive but works. Real Scent Match. **(Scale with ROAS focus)** |
| **The "Unicorn"** | Low | High| High| Viral Creative + Great Offer. **(Scale Aggressively)** |
| **The "Junk"** | Low | High| Low | Clickbait. Cheap traffic, no buyers. **(Kill)** |

---

# 4. Actions (The Upgrade Path)

We will upgrade `icp-research-lead` to use this **Diagnostic Tree**.

### Implementation Logic

1. **Filter**: `Objective == Sales`.
2. **Calculate Ratios**:
    * Compare Product CPM vs Account CPM.
    * Compare Product CTR vs Account CTR.
    * Compare Product CR vs Account CR.
3. **Classify**: Assign one of the 5 labels ("Unicorn", "Burn", etc.) to each product.
4. **Strategy**:
    * *Unicorns/Premium*: "Hero Products".
    * *Mismatch*: "Scent Match Audit Required".
    * *Burn/Junk*: "Ignore".

**Result**: A strategy that doesn't guess quality based on price, but proves it based on physics.
