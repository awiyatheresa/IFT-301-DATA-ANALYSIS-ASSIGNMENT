# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:49:43 2024

@author: THERESA AWIYA
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for plant growth with music
growth_with_music = [
    304, 257, 174, 214, 69,
    317, 387, 47, 157, 0,
    332, 308, 317, 286, 236,
    299, 206, 278, 188, 43,
    0, 0, 0, 0, 0
]

# Data for plant growth without music
growth_without_music = [
    292, 270, 47, 288, 324,
    292, 364, 316, 287, 75,
    282, 149, 274, 319, 213,
    3, 324, 2, 128, 219,
    94, 164, 0, 0, 0
]

# Combine data into a DataFrame for easier plotting
data = {
    'Condition': ['With Music'] * len(growth_with_music) + ['Without Music'] * len(growth_without_music),
    'Growth': growth_with_music + growth_without_music
}

df = pd.DataFrame(data)

# Create a histogram of plant growth
plt.figure(figsize=(12, 5))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(growth_with_music, bins=10, alpha=0.5, label='With Music', color='skyblue', edgecolor='black')
plt.hist(growth_without_music, bins=10, alpha=0.5, label='Without Music', color='salmon', edgecolor='black')
plt.title('Histogram of Plant Growth')
plt.xlabel('Growth (mm)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y')

# Create a side-by-side dot plot
plt.subplot(1, 2, 2)
sns.stripplot(x='Condition', y='Growth', data=df, jitter=True, color='purple', size=8)
plt.title('Side-by-Side Dot Plot of Plant Growth')
plt.xlabel('Condition')
plt.ylabel('Growth (mm)')
plt.grid(axis='y')

plt.tight_layout()
plt.show()
