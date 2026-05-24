# Project 2 — Data Classification Using AI 🔬
**DecodeLabs | Industrial Training Kit | Batch 2026**

---

## Overview
A supervised machine learning pipeline that classifies Iris flower species using the **K-Nearest Neighbors (KNN)** algorithm. This project introduces the full ML workflow — loading data, feature scaling, train-test splitting, model training, and evaluation using a Confusion Matrix and F1 Score.

---

## Objective
Build a complete classification pipeline that trains a model on labeled data and accurately predicts the species of unseen flower samples.

---

## Dataset — The Iris Benchmark

| Property | Value |
|---|---|
| **Samples** | 150 (balanced) |
| **Classes** | 3 (Setosa, Versicolor, Virginica) |
| **Features** | 4 (Sepal Length, Sepal Width, Petal Length, Petal Width) |
| **Source** | `sklearn.datasets.load_iris()` |

---

## Key Concepts

| Concept | Description |
|---|---|
| **Train-Test Split** | 80% train / 20% test, shuffled to remove order bias |
| **Feature Scaling** | `StandardScaler` normalizes features to Mean=0, Variance=1 |
| **KNN Algorithm** | Classifies by majority vote of K=5 nearest neighbors |
| **Confusion Matrix** | Shows TP, FP, FN, TN for each class |
| **F1 Score** | Harmonic mean of Precision and Recall |

---

## IPO Pipeline

```
INPUT                  PROCESS               OUTPUT
──────────             ──────────────        ──────────────
Iris Dataset     →     Train-Test Split  →   Confusion Matrix
Feature Scaling        KNN (K=5)             F1 Score
                       Model Training        Classification Report
```

---

## Project Structure

```
project2/
└── classifier.py
```

---

## Requirements

```bash
pip install scikit-learn
```

---

## How to Run

```bash
python classifier.py
```

---

## Sample Output

```
==================================================
  DecodeLabs — Project 2: Data Classifier
  Algorithm: K-Nearest Neighbors  |  K = 5
==================================================

[✓] Dataset loaded  →  150 samples, 4 features, 3 classes
    Classes: ['setosa', 'versicolor', 'virginica']

[✓] Split complete  →  Train: 120  |  Test: 30
[✓] Features scaled  →  Mean ≈ 0, Variance = 1
[✓] Model trained  →  KNN (k=5)

==================================================
  CONFUSION MATRIX
==================================================
               setosa    versicolor  virginica
setosa             10           0           0
versicolor          0           9           0
virginica           0           0          11

==================================================
  CLASSIFICATION REPORT
==================================================
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
```

---

## Results

| Metric | Score |
|---|---|
| **Accuracy** | 100% |
| **F1 Score (macro avg)** | 1.00 |
| **Misclassifications** | 0 / 30 |

---

## Checklist ✅

- [x] Dataset loaded and explored
- [x] Data split into 80/20 train-test sets
- [x] Features scaled with StandardScaler
- [x] KNN model trained with K=5
- [x] Confusion Matrix printed
- [x] F1 Score and Classification Report printed
- [x] Modular pipeline functions

---

## Skills Demonstrated
`Supervised Learning` · `Data Preprocessing` · `Feature Scaling` · `KNN Algorithm` · `Model Evaluation` · `Scikit-Learn`