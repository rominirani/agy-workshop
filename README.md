![Workshop Cover](assets/workshop_cover.png)

# Agentic Developer Workshop

Welcome to the Antigravity workshop! This repository contains 10 activities, all built using **Python and Flask**, designed to showcase the power of agentic development.

> [!NOTE]
> For a deep dive into the philosophy, benefits, and target audience of this curriculum, read our **[Workshop Overview](file:///Users/romin/agy-projects/agy-workshop/WORKSHOP_OVERVIEW.md)**.

You will explore 10 real-world software engineering tasks across two powerful platforms (Antigravity and Gemini CLI).

---

## 🛠️ Unified Environment Setup

Before starting any activity, ensure you have Python 3.8+ installed. Follow these steps for **EACH** project folder:

1. **Enter the activity directory**:

   ```bash
   cd 0X-[activity-name]
   ```

2. **Set up your virtual environment**:

   ```bash
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## 🤖 Choose Your Agent Path

You can complete this workshop using either the **Antigravity** or the **Gemini CLI**.

### Path A: The Visual Experience (Antigravity IDE)

**Best for:** Visualizing implementation plans, side-by-side diffing, and multi-file orchestrations.

1. **Open Workspace**: Go to `File` > `Open Folder...` and select the `agy-workshop` directory.
2. **Launch Agent Manager**: Open the **Agent Manager** tab (usually at the side or bottom).
3. **Prompt**: Type your instructions directly into the chat box. Antigravity will create implementation plans and artifacts for you to approve.

### Path B: The Terminal Warrior (Gemini CLI)

**Best for:** Fast, keyboard-centric iterations and staying in your development shell.

1. **Launch Gemini**: From your terminal (inside a project folder), simply type `gemini`.
2. **Interactive Mode**: You are now in an interactive session with the AI agent.
3. **Context is Key**: Use the `@` symbol to load the files you want to work on.
   * *Example:* `@app.py fix the security vulnerabilities in the search route.`
4. **Shell Integration**: Use the `!` prefix to run terminal commands (like `pytest` or `flask run`) without leaving the Gemini session.

---

## 📝 The Curriculum: 10 Projects

| # | Activity | Goal | Unified Prompt / Instruction |
| :--- | :--- | :--- | :--- |
| **01** | **Vibe-Coding** | **Prototyping** | "Create a stunning, glassmorphic Zen Travel Planner using Flask. The UI should have smooth animations and a premium color palette." |

### 01: Vibe-Coding (Rapid UI)

1. **Reproduce**: Run `python3 app.py` and visit `http://127.0.0.1:5000`. You'll see a completely empty, unstyled page.
2. **Prompt**: Paste the "Unified Prompt" above into Antigravity or Gemini CLI.
3. **Verify**: Refresh the browser to see a fully reactive, high-end travel dashboard generated from scratch.

### 02: Documentation (Knowledge)

| **02** | **Documentation** | **Knowledge** | "@scheduler.py analyze this async logic and generate Google-style docstrings and a comprehensive README.md." |

1. **Reproduce**: Open `scheduler.py`. The logic is complex and lacks any comments or documentation.
2. **Prompt**: Use the prompt above to generate clear, structured documentation.
3. **Verify**: Check the file for newly added docstrings and look for the new `README.md` in the `02-documentation` folder.

### 03: Feature-Building (Expansion)

| **03** | **Feature-Building** | **Expansion** | "@app.py implement a 'Low Stock Alert' system (< 5 units) with a new dashboard page and visual warnings." |

1. **Reproduce**: Run `python3 app.py`. Notice there's no way to see which items are low on stock.
2. **Prompt**: Ask the agent to add the alert system and a new dashboard route.
3. **Verify**: Visit `/dashboard` to see the new low-stock warnings in action.

### 04: Refactoring (Cleanup)

| **04** | **Refactoring** | **Cleanup** | "@processor.py refactor this messy calculation logic into clean, modular functions. Remove the global state variables." |

1. **Reproduce**: Read `processor.py`. It's a "spaghetti" monolithic script with global variables that are hard to test.
2. **Prompt**: Ask the agent to modularize the logic.
3. **Verify**: Run the refactored code and ensure calculations remain identical, but the code is now testable and clean.

### 05: Testing (Quality)

| **05** | **Testing** | **Quality** | "Write a complete pytest suite for this Finance API, covering edge cases like divisions by zero and negative currency values." |

1. **Reproduce**: Run `pytest`. It will fail because there are no tests or they are incomplete.
2. **Prompt**: Use the agent to generate a robust test suite for the `app.py` logic.
3. **Verify**: Run `pytest` again and see all tests pass, including the complex edge cases.

### 06: Migration (Modernization)

| **06** | **Migration** | **Modernization** | "Migrate this legacy Flask app to Python 3.12 standards. Replace old formatting with f-strings and add comprehensive type hints." |

1. **Reproduce**: Run `python3 legacy_script.py`. Observe the old `%` string formatting and lack of type safety.
2. **Prompt**: Ask the agent to migrate the logic into a modern, type-hinted Flask API.
3. **Verify**: Run the new Flask app and confirm the output matches the legacy script but with a modern architecture.

### 07: Bug-Fixing (Diagnostics)

| **07** | **Bug-Fixing** | **Diagnostics** | "Find and fix the 3 bugs in the Inventory API: the ZeroDivision error, the shared order state, and the discount math error." |

1. **Reproduce**: Run `python3 app.py`. Submit an empty order (ZeroDivision). Submit two orders in a row (Order Bleeding). Add a loyalty discount and notice the incorrect total ($0.10 instead of 10%).
2. **Prompt**: Ask the agent to "Find and fix all logic bugs in the 07-bug-fixing/app.py file."
3. **Verify**: Use curl or Postman to submit orders and ensure the calculations are accurate and orders don't persist across requests.

### 08: Security (Hardening)

| **08** | **Security** | **Hardening** | "@app.py identify and patch the SQL Injection and XSS vulnerabilities. Use parameterized queries and proper output escaping." |

1. **Reproduce**: In the search box, type `' OR '1'='1` (SQLi) or `<script>alert('XSS')</script>`.
2. **Prompt**: Use the agent to audit `app.py` for vulnerabilities and apply security best practices.
3. **Verify**: Attempt the same attacks; they should now be safely handled/escaped.

### 09: Performance (Optimization)

| **09** | **Performance** | **Optimization** | "@data_proc.py optimize the sales reporting logic. Replace the O(n^2) nested sorting loop with an efficient algorithm." |

1. **Reproduce**: Run the analytics report and notice the significant lag (3+ seconds) caused by the inefficient sorting loop in `data_proc.py`.
2. **Prompt**: Ask the agent to optimize the data processing logic for better time complexity.
3. **Verify**: Run the report again; it should be near-instantaneous.

### 10: Deployment (Ops)

| **10** | **Deployment** | **Ops** | "Generate a multi-stage Dockerfile and a GitHub Actions workflow that runs tests and builds the image on every push." |

1. **Reproduce**: Inspect the existing `Dockerfile`. It's massive and unoptimized.
2. **Prompt**: Ask the agent to create a slim, multi-stage Docker build and a CI/CD pipeline.
3. **Verify**: Build the image locally (`docker build . -t workshop-app`) and check the image size reduction.

---

## 💡 Efficiency Pro-Tips

* **Context Loading**: In Gemini CLI, always start by loading your file context with `@`.
* **Iteration**: Agentic coding is a conversation. If the first result isn't perfect, just follow up: *"That looks great, but could you move the button to the header?"*
* **Shell Tasks**: Don't exit the agent to run tests. In the CLI, use `!pytest`. In Antigravity, the agent can run commands for you!

**Happy Coding!** 🚀
