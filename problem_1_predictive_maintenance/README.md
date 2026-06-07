# Problem 1: Predictive Maintenance using Machine Learning

## Overview

This project addresses a predictive maintenance problem for a manufacturing environment. The objective is to identify potential machine failures using sensor readings while handling a highly imbalanced dataset where only 0.5% of observations represent actual failures.

The solution focuses on:

* End-to-End Machine Learning Pipeline
* Imbalanced Data Handling
* Feature Engineering
* Model Selection & Hyperparameter Tuning
* Cost-Sensitive Decision Making
* Production-Oriented Threshold Optimization

---

## Business Problem

Manufacturing machines generate thousands of sensor readings continuously. Detecting failures before they occur can significantly reduce downtime and maintenance costs.

However, machine failures are rare events, creating a highly imbalanced classification problem.

### Dataset Characteristics

* Total Samples: 100,000
* Features: 20 simulated sensor readings
* Target Variable: Machine Failure
* Failure Rate: 0.5%
* Healthy Machines: 99.5%

The dataset was generated using Scikit-Learn's `make_classification()` function to simulate real-world sensor data.

---

## Project Workflow

Requirement Gathering
→ Data Generation
→ Exploratory Data Analysis (EDA)
→ Outlier Detection & Treatment
→ Feature Engineering
→ Train-Test Split
→ Model Development
→ Hyperparameter Tuning
→ Threshold Optimization
→ Business Evaluation

---

## Data Preprocessing

### Outlier Treatment

A custom Scikit-Learn transformer (`IQRCapper`) was implemented to cap extreme values using the Interquartile Range (IQR) method.

Benefits:

* Preserves dataset size
* Reduces impact of extreme values
* Prevents information loss caused by row deletion

### Feature Scaling

StandardScaler was used to standardize numerical features.

---

## Handling Class Imbalance

The dataset contains only 0.5% failure cases.

Two strategies were used:

### Logistic Regression

* `class_weight='balanced'`

### Random Forest

* SMOTE (Synthetic Minority Oversampling Technique)

SMOTE generates synthetic minority-class samples to improve learning on rare failure events.

---

## Models Evaluated

### Model 1: Logistic Regression

Used as a baseline model.

### Model 2: Random Forest + SMOTE

Used to capture complex non-linear relationships among sensor readings.

### Hyperparameter Tuning

RandomizedSearchCV with Stratified 5-Fold Cross Validation was used to optimize:

* n_estimators
* max_depth
* min_samples_split
* min_samples_leaf

Optimization Metric:

* Average Precision (PR-AUC)

Best Parameters:

```python
{
    'model__n_estimators': 300,
    'model__min_samples_split': 5,
    'model__min_samples_leaf': 2,
    'model__max_depth': None
}
```

---

## Evaluation Metrics

Accuracy was intentionally excluded because it can be misleading for highly imbalanced datasets.

Metrics used:

* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC (Primary Metric)

PR-AUC was selected because it focuses on minority-class performance and provides a more realistic evaluation than ROC-AUC in highly imbalanced scenarios.

---

## Final Results

| Metric    | Logistic Regression | RF + SMOTE | Final Tuned RF + SMOTE (Threshold = 0.25) |
| --------- | ------------------: | ---------: | ----------------------------------------: |
| Precision |              0.0201 |     0.1181 |                                    0.3279 |
| Recall    |              0.8100 |     0.7500 |                                    0.8100 |
| F1 Score  |              0.0393 |     0.2041 |                                    0.4669 |
| ROC-AUC   |              0.9004 |     0.9781 |                                    0.9937 |
| PR-AUC    |              0.0954 |     0.3726 |                                    0.6222 |

---

## Threshold Optimization

The assignment specifies that the cost of a False Negative is 100 times higher than the cost of a False Positive.

Theoretical Threshold:

```text
Threshold = Cost(FP) / (Cost(FP) + Cost(FN))

Threshold = 1 / (1 + 100)

Threshold ≈ 0.01
```

However, empirical evaluation showed that a threshold of 0.01 generated excessive false positives.

A threshold analysis was performed across multiple operating points.

Final Production Threshold:

```python
0.25
```

Selected because it provided a strong balance between:

* Failure Detection (Recall)
* False Alarm Reduction (Precision)

---

## Key Learnings

* Class imbalance significantly impacts model evaluation.
* PR-AUC is often more informative than Accuracy and ROC-AUC for rare-event detection.
* Hyperparameter tuning can substantially improve minority-class performance.
* Threshold selection should be aligned with business costs rather than relying solely on the default 0.5 threshold.
* Production ML systems require both statistical performance and business-aware decision making.

---

## Repository Structure

```text
problem_1_predictive_maintenance/
│
├── notebooks/
│   └── predictive_maintenance.ipynb
│
├── reports/
│   └── technical_memo.md
│
├── images/
│
└── README.md
```

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/predictive_maintenance.ipynb
```

and run all cells sequentially.

---

## Author

Atharva Bhalerao

Mid-Level AI/ML & Python Engineer Assessment Submission
