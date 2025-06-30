import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
# 🔢 Simulated data: blood pressure reduction (in mmHg)
np.random.seed(42)
# Placebo group (less effect)
placebo = np.random.normal(loc=2, scale=1.5, size=30)
treatment = np.random.normal(loc=5, scale=1.8, size=30)
t_stat, p_value = ttest_ind(treatment, placebo)
print("🔍 Hypothesis Testing Result")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")
alpha = 0.05
if p_value < alpha:
    print("✅ Statistically significant difference (reject null hypothesis).")
else:
    print("❌ Not statistically significant (fail to reject null hypothesis).")
means = [np.mean(placebo), np.mean(treatment)]
stds = [np.std(placebo), np.std(treatment)]
plt.figure(figsize=(6, 5))
bars = plt.bar(['Placebo', 'Treatment'], means, yerr=stds, capsize=10,
               color=['lightcoral', 'lightgreen'], edgecolor='black')
plt.text(0.5, max(means)+1, f'p = {p_value:.4f}', ha='center', fontsize=12, color='black')
plt.title("Effectiveness of Treatment vs Placebo")
plt.ylabel("Reduction in Symptom Score")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
import scipy.stats as stats
shapiro_placebo = stats.shapiro(placebo)
shapiro_treatment = stats.shapiro(treatment)
print("\n🧪 Shapiro-Wilk Normality Test:")
print(f"Placebo:  p = {shapiro_placebo.pvalue:.4f} → {'Normal' if shapiro_placebo.pvalue > 0.05 else 'Not normal'}")
print(f"Treatment: p = {shapiro_treatment.pvalue:.4f} → {'Normal' if shapiro_treatment.pvalue > 0.05 else 'Not normal'}")
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
stats.probplot(placebo, dist="norm", plot=plt)
plt.title("Q-Q Plot: Placebo")
plt.subplot(1, 2, 2)
stats.probplot(treatment, dist="norm", plot=plt)
plt.title("Q-Q Plot: Treatment")
plt.tight_layout()
plt.show()