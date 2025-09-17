import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("data/metadata.csv")

# ----------------------------
# Part 1: Data Exploration
# ----------------------------
print("Data shape:", df.shape)
print(df.info())
print(df.head())

# Missing values
print("Missing values:\n", df.isnull().sum())

# ----------------------------
# Part 2: Data Cleaning
# ----------------------------
df = df.dropna(subset=["title", "abstract", "publish_time"])
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df = df.dropna(subset=["publish_time"])
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

# ----------------------------
# Part 3: Analysis & Visualizations
# ----------------------------
# Publications per year
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
year_counts.plot(kind="bar", color="skyblue")
plt.title("Publications per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top journals
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals")
plt.xlabel("Count")
plt.show()

# Word cloud from titles
text = " ".join(df["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# Distribution by source
top_sources = df["source_x"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_sources.values, y=top_sources.index, palette="magma")
plt.title("Top 10 Sources")
plt.xlabel("Count")
plt.show()
