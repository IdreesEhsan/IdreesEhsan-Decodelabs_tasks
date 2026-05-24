# ============================================================
#  DecodeLabs — Artificial Intelligence | Project 2
#  Data Classification Using AI (KNN + Iris Dataset)
#  Batch: 2026
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

SEPARATOR = "=" * 50
K         = 5
TEST_SIZE = 0.20
SEED      = 42

# ── 1. LOAD DATASET ─────────────────────────────────────────
def load_data():
    iris = load_iris()
    X, y =  iris.data, iris.target
    names = iris.target_names
    return X, y, names

# ── 2. SPLIT ────────────────────────────────────────────────
def split_data(X, y):
    return train_test_split(
        X, y,
        test_size= TEST_SIZE,
        random_state= SEED,
        shuffle= True
    )

# ── 3. SCALE (Gatekeeper Rule) ───────────────────────────────
def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)     # fit only on train
    X_test = scaler.transform(X_test)           # apply same scale on test
    return X_train, X_test

# ── 4. TRAIN MODEL ──────────────────────────────────────────
def train_model(X_train, y_train):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(X_train, y_train)
    return model

# ── 5. EVALUATE ─────────────────────────────────────────────
def evaluate(model, X_test, y_test, class_names):
    predictions = model.predict(X_test)
 
    print(f"\n{SEPARATOR}")
    print("  CONFUSION MATRIX")
    print(SEPARATOR)
    cm = confusion_matrix(y_test, predictions)
    # Pretty-print with class labels
    header = f"{'':15}" + "  ".join(f"{n:10}" for n in class_names)
    print(header)
    for i, row in enumerate(cm):
        label = class_names[i]
        vals  = "  ".join(f"{v:10}" for v in row)
        print(f"{label:15}{vals}")
 
    print(f"\n{SEPARATOR}")
    print("  CLASSIFICATION REPORT")
    print(SEPARATOR)
    print(classification_report(y_test, predictions, target_names=class_names))
 
 
# ── MAIN PIPELINE ────────────────────────────────────────────
def main():
    print(SEPARATOR)
    print("  DecodeLabs — Project 2: Data Classifier")
    print("  Algorithm: K-Nearest Neighbors  |  K =", K)
    print(SEPARATOR)
 
    # Step 1 — Load
    X, y, names = load_data()
    print(f"\n[✓] Dataset loaded  →  {len(X)} samples, {X.shape[1]} features, {len(names)} classes")
    print(f"    Classes: {list(names)}")
 
    # Step 2 — Split
    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"\n[✓] Split complete  →  Train: {len(X_train)}  |  Test: {len(X_test)}")
 
    # Step 3 — Scale
    X_train, X_test = scale_features(X_train, X_test)
    print(f"[✓] Features scaled  →  Mean ≈ 0, Variance = 1")
 
    # Step 4 — Train
    model = train_model(X_train, y_train)
    print(f"[✓] Model trained  →  KNN  (k={K})")
 
    # Step 5 — Evaluate
    evaluate(model, X_test, y_test, names)
 
 
if __name__ == "__main__":
    main()