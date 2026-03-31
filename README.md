# Antigravity Workshop: Agentic Development 101

Welcome to the Antigravity workshop! This repository contains 10 activities, all built using **Python and Flask**, designed to showcase the power of agentic development.

> [!NOTE]
> For a deep dive into the philosophy, benefits, and target audience of this curriculum, read our **[Workshop Overview](file:///Users/romin/agy-projects/agy-workshop/WORKSHOP_OVERVIEW.md)**.

You will explore 10 real-world software engineering tasks across two powerful platforms.

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

You can complete this workshop using either the **Visual IDE** or the **Interactive Terminal**.

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
| **02** | **Documentation** | **Knowledge** | "@scheduler.py analyze this async logic and generate Google-style docstrings and a comprehensive README.md." |
| **03** | **Feature-Building** | **Expansion** | "@app.py implement a 'Low Stock Alert' system (< 5 units) with a new dashboard page and visual warnings." |
| **04** | **Refactoring** | **Cleanup** | "@processor.py refactor this messy calculation logic into clean, modular functions. Remove the global state variables." |
| **05** | **Testing** | **Quality** | "Write a complete pytest suite for this Finance API, covering edge cases like divisions by zero and negative currency values." |
| **06** | **Migration** | **Modernization** | "Migrate this legacy Flask app to Python 3.12 standards. Replace old formatting with f-strings and add comprehensive type hints." |
| **07** | **Bug-Fixing** | **Diagnostics** | "Find and fix the 3 bugs: the backend KeyError, the React state string conversion, and the unclickable UI overlay." |
| **08** | **Security** | **Hardening** | "@app.py identify and patch the SQL Injection and XSS vulnerabilities. Use parameterized queries and proper output escaping." |
| **09** | **Performance** | **Optimization** | "@data_proc.py optimize the sales reporting logic. Replace the O(n^2) nested sorting loop with an efficient algorithm." |
| **10** | **Deployment** | **Ops** | "Generate a multi-stage Dockerfile and a GitHub Actions workflow that runs tests and builds the image on every push." |

---

## 💡 Efficiency Pro-Tips

* **Context Loading**: In Gemini CLI, always start by loading your file context with `@`.
* **Iteration**: Agentic coding is a conversation. If the first result isn't perfect, just follow up: *"That looks great, but could you move the button to the header?"*
* **Shell Tasks**: Don't exit the agent to run tests. In the CLI, use `!pytest`. In Antigravity, the agent can run commands for you!

**Happy Coding!** 🚀
