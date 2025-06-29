import numpy as np
import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "History", "Computer"]
np.random.seed(42)
student_scores = np.random.randint(50, 101, size=(32, 5))
average_scores = np.mean(student_scores, axis=0)
highest_avg_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_index]
print("Average Scores by Subject:")
for subj, avg in zip(subjects, average_scores):
    print(f"{subj}: {avg:.2f}")
print(f"\nSubject with the highest average: {highest_avg_subject} ({average_scores[highest_avg_index]:.2f})")
plt.figure(figsize=(8, 5))
bars = plt.bar(subjects, average_scores, color='skyblue')
bars[highest_avg_index].set_color('orange')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval:.1f}', ha='center', fontsize=10)
plt.title("Average Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
