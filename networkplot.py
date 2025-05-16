import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Last inn CSV-data
filbane = "networkbandpass.csv"
df = pd.read_csv(filbane, skiprows=21)

# Ekstraher frekvens og amplitude i dB
frekvens = df.iloc[:, 0]
amplitude_db = df.iloc[:, 1]

# Finn toppunktet (minste demping)
peak_idx = amplitude_db.idxmax()
f0 = frekvens[peak_idx]
a0 = amplitude_db[peak_idx]

# Finn -3 dB punkter (≈ 3 dB under topp)
grense = a0 - 3
lavere_sider = np.where(amplitude_db[:peak_idx] <= grense)[0]
høyere_sider = np.where(amplitude_db[peak_idx:] <= grense)[0] + peak_idx

# Velg nærmeste punkter til -3 dB på hver side
f_l = frekvens[lavere_sider[-1]]
a_l = amplitude_db[lavere_sider[-1]]

f_h = frekvens[høyere_sider[0]]
a_h = amplitude_db[høyere_sider[0]]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(frekvens, amplitude_db, label="$|H(f)|$", color='steelblue')
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Demping (dB)")
plt.title("Amplituderespons (Bode-plott)")

# Marker toppunkt (f0)
plt.scatter(f0, a0, color='red', label=fr"$f_0$: {f0:.2f} Hz, {a0:.2f} dB", zorder=5)

# Marker -3 dB punkter
plt.scatter([f_l, f_h], [a_l, a_h], color='green',
            label=fr"$f_L$: {f_l:.2f} Hz, {a_l:.2f}dB" + "\n" + fr"$f_H$: {f_h:.2f} Hz, {a_h:.2f} dB",
            zorder=5)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
