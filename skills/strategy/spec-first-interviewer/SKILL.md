---
name: Spec-First Interviewer
description: Intercepts vague coding requests to enforce a structured requirements gathering interview before any code is written.
---

# Spec-First Interviewer

## 1. Trigger

This skill activates automatically when the user's request is **vague**, **broad**, or **lacks specific technical details**.

**Trigger Keywords & Phrases:**

- "Build an app..."
- "Start a new project..."
- "Scaffold..."
- "Create a feature for..."
- "I have an idea for..."
- "Make a website..."
- "Setup a..."

## 2. The Interceptor (CRITICAL)

**IF** the user's request matches the trigger criteria AND no `PRD.md` or detailed specification exists in the context:

1. **STOP.** Do not write any code. Do not create any files (except potentially a scratchpad).
2. **ACKNOWLEDGE** the request enthusiasm but **BLOCK** immediate execution.
3. **INITIATE** the Interview Loop.

*Example Interceptor Message:*
> "That sounds like a great project! Before I write a single line of code, I need to understand exactly what we're building to avoid rewriting it later. Let's spec this out first."

## 3. The Interview Loop

You must explicitly ask **3-5 clarifying questions**. Do not overwhelm the user; group them if necessary, but ensure these core areas are covered:

### A. Tech Stack & Nuance

* **Frontend:** (e.g., React, Vue, Vanilla? Tailwind vs CSS Modules?)
- **Backend/Data:** (e.g., Node, Python, Firebase, Supabase, Local JSON?)
- **Environment:** (e.g., Vite, Next.js, CRA?)

### B. User Flows & Functionality

* **Core Action:** What is the *one thing* the user must do?
- **Auth:** Is authentication required? (Email, Social, None?)
- **Admin:** Is an admin panel needed?

### C. Vibe & UX

* **Aesthetic:** (e.g., "Dashboard", "Landing Page", "Minimalist", "Cyberpunk")
- **Device:** Mobile-first or Desktop-centric?

## 4. The Output: PRD.md

**AFTER** the user answers your questions:

1. **SYNTHESIZE** their answers into a comprehensive Product Requirements Document.
2. **CREATE** a file named `PRD.md` in the root of the workspace (or appropriate doc folder).
3. **FORMAT** the `PRD.md` to include:
    - **Project Overview**: High-level summary.
    - **Tech Stack**: The agreed-upon technologies.
    - **Core Features**: Bulleted list of must-haves.
    - **User Flow**: Step-by-step user journey.
    - **File Structure**: A proposed directory tree.

**ONLY AFTER** the user confirms the `PRD.md` is correct, you may proceed to "Scaffold" or "Execute" the code generation.
