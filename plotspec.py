import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("ulinearspec.csv", skiprows=40)
frekvens = df["Frequency (Hz)"]
X_db = df["Trace 1 (dBṼ)"]
Y_db = df["Trace 2 (dBṼ)"]

# Finn toppfrekvensen i X_db for å finne f0 (fundamental)
peak_index = X_db.idxmax()
f0 = frekvens[peak_index]

# Overharmoniske
harmonics = [f0 * n for n in range(1, 5)]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Venstre: x(t)
axs[0].plot(frekvens, X_db, color='blue')
axs[0].scatter([f0], [X_db[peak_index]], color='orange', zorder=5)
axs[0].set_title("$x(t)$")
axs[0].set_xlabel("Frekvens (Hz)")
axs[0].set_ylabel("Amplitude (dB)")

# Høyre: y(t)
axs[1].plot(frekvens, Y_db, color='orange')
for n, f_h in enumerate(harmonics):
    idx = np.argmin(np.abs(frekvens - f_h))
    axs[1].scatter(frekvens[idx], Y_db[idx], color='blue', zorder=5,
                   label=f"{n+1}f = {int(round(f_h))} Hz")
axs[1].legend()
axs[1].set_title("$y(t)$")
axs[1].set_xlabel("Frekvens (Hz)")
axs[1].set_ylabel("Amplitude (dB)")

plt.tight_layout()
plt.show()
