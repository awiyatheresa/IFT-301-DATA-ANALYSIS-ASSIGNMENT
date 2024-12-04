# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:12:11 2024

@author: THERESA AWIYA
"""
import matplotlib.pyplot as plt

# Step 1: Define the data in the specified order
ingredients = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
proportions = [0.275, 0.175, 0.075, 0.275, 0.175]

# Step 2: Create the figure with a specified size
plt.figure(figsize=(8, 5))  # Adjust the width and height as needed

# Step 3: Create the horizontal bar chart
plt.barh(ingredients, proportions, color='purple')

# Step 4: Customize the chart
plt.title('Proportions of Food Ingredients')
plt.xlabel('Proportion of Total')
plt.ylabel('Ingredients')
plt.xlim(0, 0.3)  # Set x-axis limit to accommodate the proportions
plt.grid(axis='x')  # Add grid lines for better readability

# Step 5: Display the chart
plt.show()