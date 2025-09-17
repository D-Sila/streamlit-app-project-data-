import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df = df.dropna(subset=["title", "abstract", "publish_time"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df = df.dropna(subset=["publish_time"])
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# ----------------------------
# Streamlit Layout
# ----------------------------
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research publications from the CORD-19 dataset.")

# Sidebar filters
st.sidebar.header("Filters")
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.sidebar.slider("Select year range", year_min, year_max, (2020, 2021))

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered_df.head(20))

# Publications per year
st.subheader("Publications by Year")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis", ax=ax)
ax.set_title("Top 10 Journals")
ax.set_xlabel("Count")
st.pyplot(fig)

# Word Cloud
st.subheader("Word Cloud of Titles")
text = " ".join(filtered_df["title"].dropna().astype(str).tolist())
if text:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Top Sources
st.subheader("Top Sources")
top_sources = filtered_df["source_x"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=top_sources.values, y=top_sources.index, palette="magma", ax=ax)
ax.set_title("Top 10 Sources")
ax.set_xlabel("Count")
st.pyplot(fig)

st.write("---")
st.write("Built with Streamlit ✨")
