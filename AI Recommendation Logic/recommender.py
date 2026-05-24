# ============================================================
#  DecodeLabs — Artificial Intelligence | Project 3
#  AI Recommendation Logic — Tech Stack Recommender
#  Engine: Content-Based Filtering (TF-IDF + Cosine Similarity)
#  Batch: 2026
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SEPARATOR = "=" * 52
TOP_N     = 3

# ── KNOWLEDGE BASE: Job Roles & Their Skill Tags ────────────
JOB_ROLES = {
    "Data Scientist" : "python sql machine learning data analysis statistics numpy pandas scikit-learn jupyter",
    "ML Engineer" : "python machine learning deep learning tensorflow pytorch model deployment mlops docker",
    "Backend Developer" : "python java sql apis rest databases node django flask microservices",
    "Frontend Developer" : "javascript react html css typescript ui ux web design responsive",
    "DevOps Engineer" : "docker kubernetes aws cloud ci cd linux automation git pipeline infrastructure",
    "Cloud Architect" : "aws azure cloud automation infrastructure devops terraform serverless security",
    "Data Analyst" : "sql excel python data visualization power bi tableau statistics reporting",
    "Cybersecurity Analyst" : "networking security linux ethical hacking penetration testing firewalls encryption",
    "Mobile Developer" : "java kotlin swift ios android react native flutter mobile ui",
    "AI Research Engineer" : "python deep learning neural networks nlp computer vision research pytorch tensorflow",
    "Database Administrator" : "sql databases mysql postgresql mongodb oracle data modeling backup optimization",
    "Full Stack Developer" : "javascript python react node sql html css rest apis git docker",
    "Systems Administrator" : "linux windows networking servers automation bash scripting cloud monitoring",
    "Blockchain Developer" : "solidity ethereum smart contracts web3 cryptography python javascript decentralized",
}

# ── 1. INGEST: Collect user skills ──────────────────────────
def get_user_skills() -> str:
    print(f"\n{SEPARATOR}")
    print("  Enter your skills (minimum 3, comma-separated)")
    print(f"  Example: Python, SQL, Machine Learning")
    print(SEPARATOR)
 
    raw   = input("\nYour skills: ")
    skills = [s.strip().lower() for s in raw.split(",") if s.strip()]
 
    if len(skills) < 3:
        print("\n[!] Please enter at least 3 skills for accurate matching.")
        return get_user_skills()
 
    print(f"\n[✓] Skills captured: {skills}")
    return " ".join(skills)
 
 # ── 2. SCORE: TF-IDF vectorize + Cosine Similarity ──────────
def score_roles(user_profile: str) -> list[tuple[str, float]]:
    role_names = list(JOB_ROLES.keys())
    role_docs  = list(JOB_ROLES.values())
 
    # Build corpus: user profile is the last document
    corpus    = role_docs + [user_profile]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
 
    # Compare user vector (last row) against all job role vectors
    user_vec   = tfidf_matrix[-1]
    role_matrix = tfidf_matrix[:-1]
    scores     = cosine_similarity(user_vec, role_matrix).flatten()
 
    return list(zip(role_names, scores))
 
 
# ── 3 & 4. SORT + FILTER: Get Top-N ─────────────────────────
def get_top_recommendations(scored: list[tuple[str, float]], n: int = TOP_N):
    return sorted(scored, key=lambda x: x[1], reverse=True)[:n]
 
 
# ── DISPLAY: Print results cleanly ──────────────────────────
def display_results(recommendations: list[tuple[str, float]]):
    print(f"\n{SEPARATOR}")
    print(f"  TOP {TOP_N} RECOMMENDED CAREER PATHS FOR YOU")
    print(SEPARATOR)
 
    medals = ["🥇", "🥈", "🥉"]
    for i, (role, score) in enumerate(recommendations):
        bar      = "█" * int(score * 30)
        pct      = score * 100
        tools    = JOB_ROLES[role].title()
        print(f"\n  {medals[i]}  {role}")
        print(f"     Match Score : {pct:.1f}%  {bar}")
        print(f"     Key Skills  : {tools[:60]}...")
 
    print(f"\n{SEPARATOR}\n")
 
 
# ── MAIN PIPELINE ────────────────────────────────────────────
def main():
    print(SEPARATOR)
    print("   Engine: TF-IDF  ×  Cosine Similarity")
    print(SEPARATOR)
 
    while True:
        # Step 1 — Ingest
        user_profile = get_user_skills()
 
        # Step 2 — Score
        scored = score_roles(user_profile)
 
        # Steps 3 & 4 — Sort + Filter
        top = get_top_recommendations(scored)
 
        # Output
        display_results(top)
 
        again = input("Run again? (yes / no): ").strip().lower()
        if again in ("No", "n"):
            print("\nGoodbye! Keep building. 🚀\n")
            break
        elif again not in ('yes', 'y', 'no', 'n'):
            print("Please enter yes/no")
            again = input("Run again? (yes / no): ").strip().lower()
 
 
if __name__ == "__main__":
    main()