# analysis.py
# Author: 23f2003824@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "CAC": [223.32, 225.64, 228.43, 230.02]
}
industry_target = 150
average_cac = 226.85

df = pd.DataFrame(data)

# Step 2: Print basic stats
print("Quarterly CAC data:")
print(df)
print(f"\nAverage CAC (2024): {average_cac}")
print(f"Industry Target: {industry_target}")

# Step 3: Visualization
sns.set_style("whitegrid")
plt.figure(figsize=(6, 4))

# Plot CAC trend
sns.lineplot(data=df, x="Quarter", y="CAC", marker="o", linewidth=2.5, color="blue", label="CAC")

# Plot industry target line
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (150)")

# Labels and title
plt.title("Customer Acquisition Cost (CAC) - 2024 Trend", fontsize=14, weight="bold")
plt.xlabel("Quarter")
plt.ylabel("CAC ($)")
plt.legend()

plt.tight_layout()
plt.savefig("cac_trend.png", dpi=120)
plt.close()

print("✅ Analysis complete. Visualization saved as cac_trend.png")
