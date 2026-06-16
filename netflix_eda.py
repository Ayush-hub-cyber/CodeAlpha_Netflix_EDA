import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic Information
print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Movies vs TV Shows
counts = df['type'].value_counts()

plt.figure(figsize=(6,4))
counts.plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("movies_vs_tvshows.png")
plt.show()

# Top 10 Countries
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(8,5))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("top_countries.png")
plt.show()

print("EDA Completed Successfully!")
# Content Release Trend

release_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
release_counts.plot(kind='line')

plt.title("Netflix Content Released Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.savefig("release_trend.png")
plt.close()

print("Release Trend Chart Created!")