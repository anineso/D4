# Etter reset: importer nødvendige biblioteker og last inn filen på nytt
import pandas as pd
import matplotlib.pyplot as plt

# Les inn CSV-filen med skip fra linje 25
df = pd.read_csv("bandscope.csv", skiprows=24)

# Ekstraher kolonner
tid = df["Time (s)"]
x1 = df["Channel 1 (V)"]
x2_hat = df["Channel 2 (V)"]

# Lag scope-aktig plott
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Øvre plott: x1(t)
ax1.plot(tid, x1, label="inngangssignal $x_1(t)$", color='steelblue')
ax1.set_ylabel("Spenning (V)")
ax1.legend()
ax1.grid(True)

# Nedre plott: x̂2(t)
ax2.plot(tid, x2_hat, label="utgangssignal $\hat{x}_2(t)$", color='orange')
ax2.set_xlabel("Tid (s)")
ax2.set_ylabel("Spenning (V)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
