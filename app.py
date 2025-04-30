import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("🎵 Spotify Analysis Tool")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

# Show raw data option
if st.checkbox("Show raw dataset"):
    st.write(df.head())

# Available audio feature columns
feature_columns = [
    'danceability', 'energy', 'valence', 'acousticness',
    'instrumentalness', 'liveness', 'speechiness',
    'tempo', 'loudness', 'duration_ms', 'popularity'
]

# Genre selection
genres = df["track_genre"].dropna().unique()
selected_genre = st.selectbox("🎧 Select a genre:", sorted(genres))

# Feature selection
selected_feature = st.selectbox("📈 Select a feature to analyze:", feature_columns)

# Filter dataset
filtered_df = df[df["track_genre"] == selected_genre]

# Statistics display
st.subheader(f"Statistics for '{selected_feature}' in genre '{selected_genre}'")
col1, col2 = st.columns(2)
col1.metric("Average", f"{filtered_df[selected_feature].mean():.2f}")
col2.metric("Standard Deviation", f"{filtered_df[selected_feature].std():.2f}")

# Histogram
st.subheader(f"Distribution of '{selected_feature}'")
fig, ax = plt.subplots()
ax.hist(filtered_df[selected_feature], bins=20, edgecolor='black')
ax.set_xlabel(selected_feature)
ax.set_ylabel('Number of Songs')
st.pyplot(fig)
