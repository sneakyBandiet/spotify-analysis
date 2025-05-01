import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.title("🎵 Spotify Analysis Tool (Interactive with Plotly)")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

# Show raw data
if st.checkbox("Show raw dataset"):
    st.write(df.head())

# Feature list for analysis
feature_columns = df.select_dtypes(include='number').columns.tolist()
feature_columns.remove("Unnamed: 0")

# Genre and feature selection
genres = df["track_genre"].dropna().unique()
selected_genre = st.selectbox("🎧 Select a genre:", sorted(genres))
selected_feature = st.selectbox("📈 Select a feature to analyze:", feature_columns)

# Filter data
filtered_df = df[df["track_genre"] == selected_genre]

# Display statistics
st.subheader(f"Statistics for '{selected_feature}' in genre '{selected_genre}'")
col1, col2 = st.columns(2)
col1.metric("Average", f"{filtered_df[selected_feature].mean():.2f}")
col2.metric("Standard Deviation", f"{filtered_df[selected_feature].std():.2f}")

# Interactive Plotly histogram
st.subheader(f"Distribution of '{selected_feature}'")
fig = px.histogram(
    filtered_df,
    x=selected_feature,
    nbins=20,
    title=f"{selected_feature.capitalize()} distribution in {selected_genre}",
    template="plotly_white"
)
fig.update_layout(
    xaxis_title=selected_feature,
    yaxis_title="Number of Songs",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)
