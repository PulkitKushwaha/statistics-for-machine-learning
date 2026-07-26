# create_histogram_image.py

import matplotlib.pyplot as plt

bins = ["0-10", "10-20", "20-30", "30-40", "40-50"]
freq = [2, 5, 8, 4, 1]

plt.figure(figsize=(8, 5))
plt.bar(bins, freq)

plt.title("Histogram Example")
plt.xlabel("Bins")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram-example.png", dpi=300)
plt.show()