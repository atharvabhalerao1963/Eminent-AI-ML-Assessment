Technical Memo
Evaluation Metric Selection

This project involves predictive maintenance on a highly imbalanced dataset where only 0.5% of records represent machine failures. Therefore, Accuracy was not used because a model predicting every observation as healthy would still achieve approximately 99.5% accuracy while failing to identify actual failures.

Instead, Precision, Recall, F1 Score, ROC-AUC, and PR-AUC were used. Among these, PR-AUC was selected as the primary optimization metric because it focuses on performance on the minority failure class. ROC-AUC can appear overly optimistic in highly imbalanced datasets, whereas PR-AUC provides a more realistic assessment of failure detection capability.

Model comparison showed that the Tuned Random Forest with SMOTE achieved the best performance, with a ROC-AUC of 0.9937 and a PR-AUC of 0.6222.

Cost-Sensitive Threshold Adjustment

The business requirement states that the cost of a False Negative (missing a machine failure) is 100 times higher than the cost of a False Positive (unnecessary maintenance inspection).

The theoretical decision threshold can be calculated as:

Threshold = Cost(FP) / (Cost(FP) + Cost(FN))

Threshold = 1 / (1 + 100) ≈ 0.01

However, empirical evaluation showed that a threshold of 0.01 generated excessive false positives. Therefore, threshold analysis was performed across multiple operating points. A threshold of 0.25 was selected as the production recommendation because it achieved a strong balance between Precision (32.8%) and Recall (81.0%), aligning model performance with business objectives.

selected_threshold = 0.25
y_pred = (y_prob_best >= selected_threshold).astype(int)