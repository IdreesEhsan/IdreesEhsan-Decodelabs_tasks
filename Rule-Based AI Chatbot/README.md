# Project 1 — Rule-Based AI Chatbot 🤖
**DecodeLabs | Industrial Training Kit | Batch 2026**

---

## Overview
A rule-based AI chatbot that responds to predefined user inputs using a dictionary-driven logic engine. This project focuses on **Control Flow**, **Input Sanitization**, and **Decision-Making Logic** — the foundational skeleton of every intelligent system.

---

## Objective
Build a continuous chatbot loop that simulates basic human interaction through pure programmatic decision-making — no machine learning, no external APIs.

---

## Key Concepts

| Concept | Description |
|---|---|
| **Input Sanitization** | `.lower().strip()` normalizes raw user input |
| **Dictionary Lookup** | O(1) key-value mapping replaces slow if-elif chains |
| **Fallback Response** | `.get(key, default)` handles unknown inputs gracefully |
| **Infinite Loop** | `while True` keeps the chatbot alive until exit |
| **Exit Strategy** | `break` on `exit`, `quit`, or `q` ends the session cleanly |

---

## Project Structure

```
project1/
└── chatbot.py
```

---

## How to Run

```bash
python chatbot.py
```

No external libraries required. Pure Python only.

---

## Sample Output

```
==========================================
         DecoBot — AI Assistant
   Type 'exit' anytime to end the session.
==========================================

You: hello
Bot: Hey there! How can I help you today?

You: what is ai
Bot: AI is the simulation of human intelligence by machines.

You: exit
Bot: Session ended. See you next time!
==========================================
```

---

## Supported Intents

| User Input | Bot Response |
|---|---|
| `hello` / `hi` | Greeting response |
| `how are you` | Status response |
| `what is ai` | AI definition |
| `what is ml` | ML definition |
| `your name` | Bot identity |
| `who made you` | Origin story |
| `help` | Lists available commands |
| `thank you` / `thanks` | Acknowledgement |
| `bye` | Farewell |
| *(anything else)* | Fallback: "I don't understand" |

---

## Checklist ✅

- [x] Continuous `while` input loop
- [x] Input sanitization (case + whitespace)
- [x] Dictionary knowledge base with 10+ intents
- [x] Fallback response for unknown inputs
- [x] Clean exit command (`exit`, `quit`, `q`)
- [x] Modular functions (`get_response`, `run_chatbot`)

---

## Skills Demonstrated
`Control Flow` · `String Manipulation` · `Dictionary Operations` · `Function Design` · `Basic AI Concepts`