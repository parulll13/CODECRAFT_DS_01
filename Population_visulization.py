import pandas as pd

df = pd.read_csv("C:/Users/Parul/PycharmProjects/Internship/API_SP.POP.TOTL_DS2_en_csv_v2_38144/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)
print(df[['Country Name', '2022']].head())

# Select relevant columns
data = df[['Country Name', '2022']].dropna()

# Rename columns for clarity
data.columns = ['Country', 'Population']

# Optional: sort by population
data = data.sort_values(by='Population', ascending=False)

# View top 10 countries
top10 = data.head(10)
print(top10)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(top10['Country'], top10['Population'], color='skyblue')
plt.title('Top 10 Most Populous Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

import seaborn as sns

plt.figure(figsize=(10, 5))
sns.histplot(data['Population'], bins=20, kde=True, color='orange')
plt.title('Histogram of Country Populations (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()




