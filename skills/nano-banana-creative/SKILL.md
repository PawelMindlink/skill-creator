---
name: nano-banana-creative
description: Expert skill for generating high-converting e-commerce Meta Ad images using Nano Banana (Gemini 3 Pro Image). Handles consistent character/product creation and complex text rendering.
---

# Goal

Teach the agent how to construct professional "production briefs" for Nano Banana to create high-quality Meta Ad assets for e-commerce clients.

# Instructions

When the user asks to create an ad image or product visual, follow these steps:

1. **Identify the Use Case**: Determine if it is a "Clean Product Shot," "Lifestyle Mockup," or "Multi-Image Fusion" (using reference images).
2. **Apply the Nano Banana Anatomy**: Every prompt must include:
    * **Subject**: Precise description of the product or person (including brand traits).
    * **Composition**: Shot type (e.g., "Macro," "Low-angle"), POV, and Aspect Ratio (4:5 for Meta Feed, 9:16 for Stories).
    * **Action/Location**: Where the product is used and the specific mood.
    * **Style**: Lighting (e.g., "Hard rim light," "Soft box") and Film Stock/Aesthetic.
    * **Text Rendering**: Specify exact text to be rendered using Nano Banana's advanced OCR capabilities.
3. **Ensure Character/Product Consistency**:
    * If using references, explicitly tell the model: "Maintain exact facial features from Image A" or "Preserve the product label and bottle shape from Image B."
4. **Meta Ad Optimization**:
    * Suggest "Rule of Thirds" for text placement to avoid overlapping UI elements on Instagram/Facebook.
    * Use "Search Grounding" for location-accurate backgrounds if the brand requires real-world locales.

# Examples

## Example 1: High-End Skincare Ad

**Input**: "Create a Meta Ad for a luxury face serum called 'Glow-Up'."
**Output**:
Prompt: "Close-up macro shot, 4:5 aspect ratio. A sleek frosted glass bottle of 'Glow-Up' serum sitting on a wet marble surface. Soft morning sunlight through a window creating caustic reflections. In the background, a blurred modern bathroom. Render the text 'GLOW UP' in a minimalist serif font on the bottle label. Cinematic, 8k, photorealistic."

## Example 2: Lifestyle Fashion (Consistent Subject)

**Input**: "Put this model from Image A in a 1980s Tokyo street at night for a jacket brand."
**Output**:
Prompt: "[Reference Image A] Wide shot, 9:16 aspect ratio. The female subject from Image A wearing a vintage oversized leather jacket, walking through a neon-lit Shinjuku street at night. Rain-slicked pavement with reflections of pink and blue neon signs. Moody, cyber-noir style. Maintain exact hairstyle and facial structure from Image A."

# Constraints

* Do not use vague terms like "high quality"—use technical terms like "shallow depth of field" or "volumetric lighting."
* Always specify Aspect Ratio for Meta (4:5 or 9:16).
* Always use "Thinking" model (Nano Banana Pro) for text-heavy images.
