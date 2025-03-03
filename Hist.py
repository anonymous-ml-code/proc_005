import matplotlib.pyplot as plt
import numpy as np

# Data
models = ['ResNet-18 (ImageNet1K)', 'VIT-B/16 (ImageNet1K)', 'VIT-B/16 (ImageNet21K)', 'VIT-G/14 (JFT)', 'VIT-B/16 (ImageNet1K) Compressed']
values = [75.2, 19.8, 12.5, 7.5, 0.95]

# Create histogram
plt.figure(figsize=(10, 6))
bars = plt.barh(models, values, color='skyblue', edgecolor='black')

# Beautify the plot
plt.title('Median Sample Distance Comparison for Backbones', fontsize=16, fontweight='bold')
plt.xlabel('Sample Pair Distance in 128 Dimensional Space', fontsize=14)
plt.ylabel('Backbone with pre-trained dataset', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add value labels on bars
for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             f'{bar.get_width()}', va='center', fontsize=12)

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.savefig('./feature_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
