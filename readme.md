# Musik im Wandel: Analyse und Visualisierung von Audio-Features und Trends

## General
Dieses Projekt untersucht den Spotify-Tracks-Datensatz mit Python  
Es nutzt `pandas` für Datenanalyse und `plotly.express` und `streamlit` für Visualisierungen.

- Quelle: (https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)  
- Format: CSV (Komma-separiert)
- Grösse: ca. 20MB
- Anzahl Zeilen: ca. 114'000 Songs
---
### 🧱 Struktur des Datensatzes (wichtige Spalten)

| Spalte           | Typ        | Beschreibung |
|------------------|------------|--------------|
| `track_id`       | Text (ID)  | Eindeutige Spotify-ID des Songs |
| `track_name`     | Text       | Titel des Songs |
| `artists`        | Text       | Künstlername(n) |
| `album_name`     | Text       | Name des Albums |
| `track_genre`    | Text       | Musikgenre (z. B. pop, rock, edm, jazz) |
| `explicit`       | Bool       | Enthält der Song explizite Inhalte (True/False)? |
| `duration_ms`    | Zahl       | Dauer des Songs in Millisekunden |
| `popularity`     | Zahl       | Beliebtheit von 0 (unbeliebt) bis 100 (sehr beliebt) |
| `key`            | Zahl (0–11)| Tonart (C=0, C♯=1, ..., B=11) |
| `mode`           | 0 oder 1   | Moll (0) oder Dur (1) |
| `time_signature` | Zahl       | Taktart (z. B. 4 = 4/4-Takt) |
---
### 🎵 Audio-Features (numerisch, automatisch von Spotify analysiert)

| Spalte              | Wertebereich     | Bedeutung |
|---------------------|------------------|-----------|
| `danceability`      | 0.0 – 1.0        | Wie tanzbar der Song ist |
| `energy`            | 0.0 – 1.0        | Wie energiegeladen/laut der Song wirkt |
| `valence`           | 0.0 – 1.0        | Wie positiv oder fröhlich ein Song klingt |
| `acousticness`      | 0.0 – 1.0        | Anteil an akustischen Instrumenten |
| `instrumentalness`  | 0.0 – 1.0        | Wahrscheinlichkeit, dass es sich um ein Instrumentalstück handelt |
| `liveness`          | 0.0 – 1.0        | Wie „live“ der Song klingt (Publikum etc.) |
| `speechiness`       | 0.0 – 1.0        | Anteil von gesprochenem Wort (z. B. Rap) |
| `tempo`             | BPM              | Geschwindigkeit in Beats per Minute |
| `loudness`          | Dezibel (negativ)| Durchschnittliche Lautstärke |
| `duration_ms`       | Millisekunden    | Länge des Songs |
| `popularity`        | 0 – 100          | Beliebtheit auf Spotify (relativ) |
--- 
### 🎶 Beispielhafte Genres im Datensatz

Hier sind einige häufig vorkommende Genres im Datensatz:

- pop  
- edm  
- rock  
- hip hop  
- jazz  
- classical  
- r&b  
- house  
- techno  
- dubstep  
- folk  
- trap  
- blues  
- country  
- reggae  
- soul  
- punk  
- metal  

> ℹ️ Der Datensatz enthält **über 100 unterschiedliche Genres**, viele davon in englischer Bezeichnung.
---
## 🔧 Installation & Ausführung
1. Github Desktop installieren und sich anmelden mit github account

2. Repository klonen  
   ```bash
   git clone https://github.com/sneakyBandiet/spotify-analysis.git
   cd spotify-analysis 
3. Virtuelle Umgebung erstellen
    `python -m venv .venv`

4. Umgebung aktivieren
    `.venv\Scripts\Activate.ps1` oder `.venv\Scripts\activate.bat`

5. Abhängigkeiten installieren (matplot, pandas):
    `pip install -r requirements.txt`

6. Starten: 
    `streamlit run app.py`