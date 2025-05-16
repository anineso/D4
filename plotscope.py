import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scopeulin.csv", skiprows=19)


x1 = df["Channel 1 (V)"]
y = df["Channel 2 (V)"]
t = df["Time (s)"]

mid_index = len(t) // 2
window = 500  

start = max(mid_index - window, 0)
end = min(mid_index + window, len(t))

plt.figure(figsize=(10, 5))
plt.plot(t[start:end], x1[start:end], label='$x_1(t)$')
plt.plot(t[start:end], y[start:end], label='$y(t)$')
plt.xlabel("Tid (s)")
plt.ylabel("Spenning (V)")
plt.title("Zoomet signalplot: $x_1(t)$ og $y(t)$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

