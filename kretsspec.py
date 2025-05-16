# Importer nødvendige biblioteker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Les CSV-data, start fra linje 37
df = pd.read_csv("kretsspec.csv", skiprows=36)

# Ekstraher frekvens og amplitudespor for utgangssignal
frekvens = df["Frequency (Hz)"]
amplitude = df["Trace 2 (dBṼ)"]

# Finn topppunkt i spekteret
peak_idx = amplitude.idxmax()
f_peak = frekvens[peak_idx]
a_peak = amplitude[peak_idx]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(frekvens, amplitude, label=r"utgangssignal $\hat{x}_2$", color='orange')
plt.scatter(f_peak, a_peak, color='gold', s=60, label=fr"$f_2$ = {int(round(f_peak))} Hz")

plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude(dB)")
plt.title("Spektrum av $\hat{x}_2(t)$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
