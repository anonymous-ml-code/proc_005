import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
plt.rcParams['font.family'] = 'serif'

# Generate hypothetical data
bandwidths = np.array([0.05, 0.1, 0.2, 0.3, 0.5])
dimensions = np.array([32, 64, 128, 256])
accuracy = np.array([
    [76.2, 82.1, 88.4, 85.3],  # h=0.05
    [81.5, 89.2, 93.1, 90.8],  # h=0.1
    [85.3, 91.4, 90.5, 88.7],  # h=0.2
    [83.1, 89.7, 88.2, 86.4],  # h=0.3
    [79.8, 85.6, 84.1, 82.3],  # h=0.5
])

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Create heatmap
heatmap = sns.heatmap(
    accuracy,
    annot=True,
    fmt=".1f",
    cmap="viridis",
    cbar_kws={'label': 'Validation Accuracy (%)'},
    ax=ax,
    linewidths=0.5,
    linecolor="white"
)

# Customize labels
ax.set_xticklabels(dimensions)
ax.set_yticklabels(bandwidths)
ax.set_xlabel("Embedding Dimension (p)", fontsize=12)
ax.set_ylabel("Bandwidth (h)", fontsize=12)
ax.set_title("CIFAR-10 Validation Accuracy vs. Hyperparameters", pad=20)

# Add contour lines for optimal region
x = np.arange(accuracy.shape[1]) + 0.5
y = np.arange(accuracy.shape[0]) + 0.5
ax.contour(x, y, accuracy, levels=5, colors="white", linewidths=0.5)

# Highlight optimal point
optimal_h_idx = 1  # h=0.1
optimal_p_idx = 2  # p=128
ax.scatter(
    optimal_p_idx + 0.5, optimal_h_idx + 0.5,
    marker="*", s=300, color="gold", edgecolor="black"
)

# Adjust layout
plt.tight_layout()
plt.savefig("hyperparam_grid.png", dpi=300, bbox_inches="tight")
plt.show()