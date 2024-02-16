import matplotlib.pyplot as plt
import geohash

# Posizione geografica (latitudine, longitudine), se presenti geohash a riga 12, non utilizzerà questi valori
lat = 0.5520
lon = 0.05218

# Calcolo del geohash
gh = geohash.encode(lat, lon)

# Lista dei geohash, lasciarlo vuoto se si vuole utilizzare il sistema tramite coordinate lan,lon
geohashes = []

# Preparazione dei dati per la visualizzazione
data = []
if not geohashes:
    data.append((lon, lat, gh))
else:
    for gh in geohashes:
        lat, lon = geohash.decode(gh)
        data.append((lon, lat, gh))

# Visualizzazione dei punti sulla mappa
plt.figure(figsize=(10, 6))
for lon, lat, gh in data:
    plt.scatter(lon, lat, color='red')
    plt.text(lon, lat, gh, fontsize=8, ha='left')

plt.xlim(0, 1)  # Imposta i limiti dell'asse x da 0 a 1
plt.ylim(0, 1)  # Imposta i limiti dell'asse y da 0 a 1
plt.title('Posizione geografica - Geohash')
plt.grid(True)
plt.show()
