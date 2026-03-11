import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")

np.random.seed(42)
data = np.random.randn(100)

print(f"Data jsou typ: {type(data)}")

print(f"Prumer: {data.mean():.4f}")
print(f"Std. odch.: {data.std():.4f}")

plt.figure(figsize=(8, 4))
plt.hist(data, bins=20, edgecolor="black", alpha=0.7)
plt.title("Test: Histogram náhodných dat")
plt.xlabel("Hodnota")
plt.ylabel("Frekvence")
plt.savefig("test_histogram.png", dpi=150)
plt.show()
print("Setup OK! Vše funguje.")