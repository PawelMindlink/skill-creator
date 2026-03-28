# Claude API — Prompt Engineering Guide

Source: [Claude Docs](https://docs.anthropic.com) | [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)

---

## The Core Rule: XML Tags Are Primary Structure

Claude is trained extensively with XML tags. Use them to separate every major prompt component.

```xml
<context>
  You are building a SaaS for e-commerce analytics. The product is called AnalyticsEdge.
</context>

<brand-voice>
  Direct. No adjectives that don't carry information. Short sentences.
</brand-voice>

<instructions>
  Write a 100-word product description for the landing page hero section.
</instructions>

<constraints>
  - No more than 2 sentences per paragraph
  - No use of words: "powerful", "seamless", "robust", "leverage"
  - End with a single-sentence CTA
</constraints>
```

---

## System vs. User Turn — What Goes Where

| Content Type | Where to Put It |
|---|---|
| Role / persona ("You are a...") | `system` |
| Standing behavioral rules | `system` |
| Output format requirements | `system` |
| Document or data to process | User turn |
| Specific task instruction | User turn |
| Examples of desired output | User turn (inside `<examples>` tags) |

**Anti-pattern:** Putting the role definition in the user turn. It works but doesn't persist reliably across multi-turn conversations.

---

## Extended Thinking — Chain of Thought

For complex tasks, instruct Claude to reason before outputting:

```
Prompt: "First, think step-by-step inside <thinking> tags.
Then write the final result inside <answer> tags."
```

This is especially effective for:

- Tasks with multiple competing constraints
- Copywriting that requires reasoning about audience psychology
- Complex data analysis requiring intermediate steps

---

## Few-Shot Prompting

Provide 2–3 input/output examples inside `<examples>` tags:

```xml
<examples>
  <example>
    <input>Product: Noise-cancelling headphones</input>
    <output>Block the world out. Hear every detail. 30-hour battery.</output>
  </example>
  <example>
    <input>Product: Ergonomic keyboard</input>
    <output>Type for hours. No compromise on speed or comfort.</output>
  </example>
</examples>

<task>Product: Standing desk converter</task>
```

---

## Prompt Chaining for Long Tasks

For multi-step workflows, break into sequential prompts rather than one mega-prompt:

1. **Step 1**: "Extract the 5 main customer pain points from this review data."
2. **Step 2**: "Given these pain points: [Step 1 output], write a messaging hierarchy for our landing page."
3. **Step 3**: "Given this messaging hierarchy: [Step 2 output], write the hero headline and 3 supporting bullets."

Each step maintains quality because the context window isn't overwhelmed.

---

## Tool Use / Function Calling

```python
tools = [
    {
        "name": "get_product_inventory",
        "description": "Retrieve current stock levels for a product SKU.",
        "input_schema": {
            "type": "object",
            "properties": {
                "sku": {"type": "string", "description": "The product SKU code"}
            },
            "required": ["sku"]
        }
    }
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "How many units of SKU-4821 do we have?"}]
)
```

For standardized tool integration across models, see: [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)

---

## Common Prompt Engineering Mistakes

1. **Role in user turn.** Always put "You are a..." in the `system` parameter.
2. **Wall of text.** Unstructured prompts lead to unfocused outputs. Use XML tags.
3. **Missing negative constraints.** Claude treats "don't use X" as a hard rule — use it.
4. **No output format specification.** Without format guidance, Claude invents its own structure. Specify markdown, JSON, or plain text explicitly.
5. **Asking for everything in one prompt.** Long outputs from a single prompt degrade linearly. Chain instead.
