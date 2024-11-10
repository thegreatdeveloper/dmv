import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


np.random.seed(42)
data = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'value': np.random.randn(100),
    'value2': np.random.randn(100),
    'x': np.arange(100),
    'y': np.random.randn(100).cumsum(),
    'territory': np.random.choice(['EMEA', 'APAC', 'Japan'], 100),
    'quantityordered': np.random.randint(1, 100, 100)
})

# Set the style for Seaborn
sns.set_style("whitegrid")

# 1. Line Plot
plt.figure(figsize=(15, 10))
plt.subplot(3, 4, 1)
plt.plot(data['x'], data['y'])
plt.title("Line Plot")

# 2. Bar Plot
plt.subplot(3, 4, 2)
sns.barplot(x='category', y='value', data=data)
plt.title("Bar Plot")

# 3. Histogram
plt.subplot(3, 4, 3)
plt.hist(data['value'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram")

# 4. Box Plot
plt.subplot(3, 4, 4)
sns.boxplot(x='territory', y='quantityordered', data=data)
plt.title("Box Plot")

# 5. Scatter Plot
plt.subplot(3, 4, 5)
plt.scatter(data['x'], data['y'], color='purple')
plt.title("Scatter Plot")

# 6. Heatmap
plt.subplot(3, 4, 6)
corr = data[['value', 'value2', 'quantityordered']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Heatmap")

# 7. Violin Plot
plt.subplot(3, 4, 7)
sns.violinplot(x='category', y='value', data=data)
plt.title("Violin Plot")

# 8. Pair Plot
# (Pair plots usually don't fit well in subplots but are shown here as an example)
plt.subplot(3, 4, 8)
sns.pairplot(data[['value', 'value2', 'quantityordered']])
plt.title("Pair Plot")

# 9. Pie Chart
plt.subplot(3, 4, 9)
category_counts = data['category'].value_counts()
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
plt.title("Pie Chart")

# 10. KDE Plot (Kernel Density Estimate)
plt.subplot(3, 4, 10)
sns.kdeplot(data['value'], shade=True)
plt.title("KDE Plot")

# 11. Grouped Bar Plot
# Creating grouped data for the plot
grouped_data = data.groupby(['territory', 'category'])['quantityordered'].mean().unstack()

plt.subplot(3, 4, 11)
grouped_data.plot(kind='bar', stacked=False, ax=plt.gca())
plt.title("Grouped Bar Plot")
plt.xlabel("Territory")
plt.ylabel("Average Quantity Ordered")
plt.legend(title="Category")

plt.tight_layout()
plt.show()
