import pandas as pd
import matplotlib.pyplot as plt

# Datensatz laden
df = pd.read_csv('dataset.csv')

# Erste 5 Zeilen anzeigen
print("Erste fünf Zeilen des Datensatzes:")
print(df.head())

# Verteilung der Popularität
plt.figure(figsize=(10, 6))
plt.hist(df['popularity'], bins=20, edgecolor='black')
plt.title('Verteilung der Song-Popularität')
plt.xlabel('Popularität')
plt.ylabel('Anzahl Songs')
plt.grid(True)
plt.tight_layout()
plt.show()