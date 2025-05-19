import pandas as pd

# Lade deinen Datensatz lokal
df = pd.read_csv("dataset.csv")

# Alle numerischen Features (für Plots)
numeric_features = df.select_dtypes(include='number').columns.tolist()

# Alle vorhandenen Genres (unique)
unique_genres = sorted(df["track_genre"].dropna().unique())

# Ausgabe für Copy-Paste in dein translations.py
print("🎯 Numeric features:")
for f in numeric_features:
    print(f'    "{f}": {{"en": "{f.capitalize()}", "de": "TODO"}},')

print("\n🎶 Genres:")
for g in unique_genres:
    print(f'    "{g}": {{"en": "{g}", "de": "TODO"}},')