import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from translations import ui_translations
from translations import feature_labels, genre_labels

# 🌐 Language selection
lang = st.sidebar.selectbox("🌐 Language / Sprache", options=["en", "de"])
t = ui_translations[lang]  # Current language dict

# App title
st.title(t["title"])

# 📄 Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

# ✅ Show raw data
if st.checkbox(t["show_data"]):
    st.dataframe(df, use_container_width=True, height=800)

# 🎯 Feature list (numeric only, excluding index column)
feature_columns = df.select_dtypes(include='number').columns.tolist()
if "Unnamed: 0" in feature_columns:
    feature_columns.remove("Unnamed: 0")

# 🔤 Translate feature labels
translated_feature_options = {
    feature_labels[f][lang]: f for f in feature_columns if f in feature_labels
}
selected_feature_label = st.selectbox(t["select_feature"], list(translated_feature_options.keys()))
selected_feature = translated_feature_options[selected_feature_label]
selected_feature_display = feature_labels[selected_feature][lang]

# 🎶 Translate genre labels
available_genres = df["track_genre"].dropna().unique()
translated_genre_options = {
    genre_labels.get(g, {lang: g})[lang]: g for g in sorted(available_genres)
}

# 🎶 Mehrere Genres auswählbar (max. 2)
selected_genres_labels = st.multiselect(
    t["select_genre_multiple"],
    list(translated_genre_options.keys()),
    default=[list(translated_genre_options.keys())[0]]
)

# Stoppen, wenn Auswahl leer oder zu groß
if len(selected_genres_labels) == 0:
    st.warning("Please select at least one genre.")
    st.stop()
elif len(selected_genres_labels) > 2:
    st.warning("Please select no more than 2 genres.")
    st.stop()

# Interne Genres (für DataFrame)
selected_genres = [translated_genre_options[g] for g in selected_genres_labels]

# 🔍 Filter data für genres
filtered_df = df[df["track_genre"].isin(selected_genres)]

# 📊 Show statistics
st.subheader(t["stats_title"].format(feature=selected_feature_display, genre=selected_genres_labels))
col1, col2 = st.columns(2)
col1.metric(t["avg"], f"{filtered_df[selected_feature].mean():.2f}")
col2.metric(t["std"], f"{filtered_df[selected_feature].std():.2f}")

# Anzahl der Bins wie im Histogramm (Kategorien)
num_bins = 20

# Min/Max des Features
min_val = filtered_df[selected_feature].min()
max_val = filtered_df[selected_feature].max()

# Bin-Grenzen berechnen
bins = np.linspace(min_val, max_val, num_bins + 1)

# 📈 Interactive histogram with Plotly
bin_size = bins[1] - bins[0]

# Plotly: Vergleich in einem Histogramm
fig = px.histogram(
    filtered_df,
    x=selected_feature,
    color="track_genre",
    barmode="overlay",  # "group" für nebeneinander
    title=t["distribution_title"].format(feature=selected_feature_display),
    template="plotly_white"
)

fig.update_traces(opacity=0.6)
fig.update_layout(
    xaxis_title=selected_feature_display,
    yaxis_title=t["y_axis"],
    bargap=0.1
)
fig.update_traces(xbins=dict(start=bins[0], end=bins[-1], size=bin_size))

st.plotly_chart(fig, use_container_width=True)

# 📊 Interaktiver Abschnitt: Songs im ausgewählten Histogramm-Bin anzeigen
# Label-Liste erzeugen
bin_labels = [f"{bins[i]:.2f} – {bins[i+1]:.2f}" for i in range(len(bins)-1)]
selected_bin_label = st.selectbox("🔎 Select a bin to view songs in this range:", bin_labels)

selected_bin_index = bin_labels.index(selected_bin_label)
bin_start = bins[selected_bin_index]
bin_end = bins[selected_bin_index + 1]

# Spaltenlayout für bis zu 2 Genres
# Breitenverhältnis bei zwei Genres: z. B. 1:1 → gleich breit (aber mit mehr Platz)
if len(selected_genres_labels) == 2:
    cols = st.columns([1.2, 1.2])  # Größer als Standard
else:
    cols = st.columns([2])  # Einzeltabelle: volle Breite

for idx, genre_label in enumerate(selected_genres_labels):
    genre_key = translated_genre_options[genre_label]

    songs_in_bin = df[
        (df["track_genre"] == genre_key) &
        (df[selected_feature] >= bin_start) &
        (df[selected_feature] < bin_end)
    ].sort_values(by=selected_feature, ascending=False)

    count = len(songs_in_bin)

    with cols[idx]:
        st.markdown(f"### 🎧 {count} songs<br>in **{genre_label}**", unsafe_allow_html=True)

        if count > 0:
            st.dataframe(
                songs_in_bin[["track_name", "artists", selected_feature]].head(100),
                use_container_width=True
            )
        else:
            st.info(f"No songs in this range.")