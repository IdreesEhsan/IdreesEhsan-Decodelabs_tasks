# Project 3 — AI Recommendation Logic 🎯
**DecodeLabs | Industrial Training Kit | Batch 2026**

---

## Overview
A content-based filtering recommendation engine that maps a user's skills to the most relevant tech career paths. Using **TF-IDF vectorization** and **Cosine Similarity**, the system mathematically measures how closely a user's profile aligns with 14 job role profiles — then returns the Top 3 matches.

---

## Objective
Build a personalization engine that takes raw user skill inputs and produces ranked, intelligent career recommendations — no historical user data required.

---

## Key Concepts

| Concept | Description |
|---|---|
| **Content-Based Filtering** | Matches user profile to item attributes directly |
| **TF-IDF Vectorization** | Weights specific skills higher than common generic ones |
| **Cosine Similarity** | Measures angular alignment between two vectors (scale-invariant) |
| **Cold Start Bypass** | Onboarding survey (3+ skills) bootstraps the user vector |
| **Top-N Filtering** | Returns only Top 3 results to prevent choice overload |

---

## Why Cosine Similarity over Euclidean Distance?

| Method | Problem |
|---|---|
| Euclidean Distance | Sensitive to vector magnitude — longer skill lists score higher unfairly |
| **Cosine Similarity** ✅ | Measures orientation only — focus is on the *direction* of interests |

---

## IPO Pipeline

```
INPUT                    PROCESS                    OUTPUT
──────────────           ──────────────────         ──────────────
User Skills (3+)   →     TF-IDF Vectorize     →     Top 3 Job Roles
                         Cosine Similarity           Match Score %
                         Sort (descending)           Skill Tags
                         Filter (Top-N)
```

---

## 4-Step Ranking Pipeline

```
Step 1: Ingestion   →  Capture 3+ user skills
Step 2: Scoring     →  Cosine similarity for all 14 job roles
Step 3: Sorting     →  Rank by score (descending)
Step 4: Filtering   →  Return Top 3 only
```

---

## Project Structure

```
project3/
└── recommender.py
```

---

## Requirements

```bash
pip install scikit-learn
```

---

## How to Run

```bash
python recommender.py
```

---

## Sample Output

```
====================================================
   DecodeLabs — Project 3: Tech Stack Recommender
   Engine: TF-IDF  ×  Cosine Similarity
====================================================

  Enter your skills (minimum 3, comma-separated)
  Example: Python, SQL, Machine Learning
====================================================

Your skills: Python, Machine Learning, SQL, TensorFlow, Data Analysis

[✓] Skills captured: ['python', 'machine learning', 'sql', 'tensorflow', 'data analysis']

====================================================
  TOP 3 RECOMMENDED CAREER PATHS FOR YOU
====================================================

  🥇  Data Scientist
     Match Score : 53.1%  ███████████████
     Key Skills  : Python Sql Machine Learning Data Analysis Statistics...

  🥈  ML Engineer
     Match Score : 44.4%  █████████████
     Key Skills  : Python Machine Learning Deep Learning Tensorflow...

  🥉  AI Research Engineer
     Match Score : 24.1%  ███████
     Key Skills  : Python Deep Learning Neural Networks Nlp Computer Vision...

====================================================
```

---

## Supported Job Roles (14 total)

| Role | Core Skills |
|---|---|
| Data Scientist | Python, SQL, ML, Statistics |
| ML Engineer | Python, Deep Learning, MLOps |
| Backend Developer | Python, Java, APIs, Databases |
| Frontend Developer | JavaScript, React, CSS |
| DevOps Engineer | Docker, Kubernetes, AWS, CI/CD |
| Cloud Architect | AWS, Azure, Terraform |
| Data Analyst | SQL, Excel, Power BI, Tableau |
| Cybersecurity Analyst | Networking, Security, Linux |
| Mobile Developer | Kotlin, Swift, Flutter |
| AI Research Engineer | NLP, Computer Vision, PyTorch |
| Database Administrator | SQL, MongoDB, Optimization |
| Full Stack Developer | React, Node, Python, Docker |
| Systems Administrator | Linux, Bash, Networking |
| Blockchain Developer | Solidity, Web3, Smart Contracts |

---

## Checklist ✅

- [x] Accepts minimum 3 user skill inputs
- [x] TF-IDF vectorization applied to job role corpus
- [x] Cosine similarity computed for all roles
- [x] Results sorted in descending order
- [x] Top 3 results displayed with match score and progress bar
- [x] Cold start handled via mandatory onboarding input
- [x] Repeat mode — user can run multiple queries

---

## Skills Demonstrated
`Content-Based Filtering` · `TF-IDF` · `Cosine Similarity` · `Vector Space Models` · `Recommendation Systems` · `Scikit-Learn`