# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:04:04 2024

@author: THERESA AWIYA
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for females
female_heights = [175, 158, 166, 175, 160, 165, 166, 170, 170, 172]
female_breath_times = [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66]

# Data for males
male_heights = [184, 182, 180, 191, 189, 181, 180, 170, 176, 185]
male_breath_times = [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]

# Combine data into a DataFrame for easier plotting
data = {
    'Sex': ['Female'] * len(female_breath_times) + ['Male'] * len(male_breath_times),
    'Breath_Held': female_breath_times + male_breath_times
}

df = pd.DataFrame(data)

# Create a histogram of breath-holding times
plt.figure(figsize=(10, 5))
plt.hist(df['Breath_Held'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Breath Holding Times')
plt.xlabel('Time Held (s)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Create a side-by-side dot plot
plt.figure(figsize=(10, 5))
sns.stripplot(x='Sex', y='Breath_Held', data=df, jitter=True, color='purple', size=8)
plt.title('Side-by-Side Dot Plot of Breath Holding Times by Sex')
plt.xlabel('Sex')
plt.ylabel('Time Held (s)')
plt.grid(axis='y')
plt.show()