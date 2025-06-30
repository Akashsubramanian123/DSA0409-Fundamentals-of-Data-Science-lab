import numpy as np
import scipy.stats as stats
np.random.seed(42)
drug_group = np.random.normal(loc=10, scale=4, size=25)
placebo_group = np.random.normal(loc=3, scale=3, size=25)
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    margin = stats.t.ppf((1 + confidence) / 2., n-1) * std_err
    return mean, mean - margin, mean + margin
drug_mean, drug_ci_lower, drug_ci_upper = confidence_interval(drug_group)
placebo_mean, placebo_ci_lower, placebo_ci_upper = confidence_interval(placebo_group)
print("💊 Drug Group:")
print(f"Mean Reduction: {drug_mean:.2f} mmHg")
print(f"95% Confidence Interval: ({drug_ci_lower:.2f}, {drug_ci_upper:.2f}) mmHg")
print("\n💤 Placebo Group:")
print(f"Mean Reduction: {placebo_mean:.2f} mmHg")
print(f"95% Confidence Interval: ({placebo_ci_lower:.2f}, {placebo_ci_upper:.2f}) mmHg")
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 5))
means = [drug_mean, placebo_mean]
errors = [
    drug_mean - drug_ci_lower,
    placebo_mean - placebo_ci_lower
]
plt.bar(['Drug', 'Placebo'], means, yerr=errors, capsize=10,
        color=['royalblue', 'lightcoral'], edgecolor='black')
plt.title("Mean Blood Pressure Reduction with 95% CI")
plt.ylabel("Reduction in BP (mmHg)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 5))
plt.boxplot([drug_group, placebo_group], labels=['Drug', 'Placebo'],
            patch_artist=True,
            boxprops=dict(facecolor='lightblue'),
            medianprops=dict(color='darkblue'))
plt.title("Boxplot of Blood Pressure Reduction")
plt.ylabel("Reduction in BP (mmHg)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()