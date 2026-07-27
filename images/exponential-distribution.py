import numpy as np
import matplotlib.pyplot as plt

lam = 0.5

x = np.linspace(0, 15, 1000)
y = lam * np.exp(-lam * x)

plt.figure(figsize=(10, 6))

plt.plot(
    x,
    y,
    linewidth=3,
    color="darkorange"
)

plt.fill_between(
    x,
    y,
    color="orange",
    alpha=0.3
)

# Highlight short wait region
plt.axvspan(
    0,
    3,
    color="green",
    alpha=0.15,
    label="Short Waits (Common)"
)

# Highlight long wait region
plt.axvspan(
    8,
    15,
    color="red",
    alpha=0.12,
    label="Long Waits (Rare)"
)

plt.title(
    "Exponential Distribution - The Statistics of Waiting",
    fontsize=16
)

plt.xlabel("Waiting Time")
plt.ylabel("Probability Density")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    "exponential-distribution.png",
    dpi=300
)

plt.show()