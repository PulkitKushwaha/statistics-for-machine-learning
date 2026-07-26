import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean = 0
std_dev = 1

# Generate x values
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)

# Normal Distribution PDF
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(
    -0.5 * ((x - mean) / std_dev) ** 2
)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=3, color="steelblue")

# Mean line
plt.axvline(mean, color="red", linestyle="--", label="Mean (μ)")

# Labels
plt.title("Normal Distribution", fontsize=16)
plt.xlabel("Value")
plt.ylabel("Probability Density")

# Clean style
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()

# Save image
plt.savefig("normal-distribution.png", dpi=300)
plt.show()