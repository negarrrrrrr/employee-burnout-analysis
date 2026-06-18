import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("burnout.csv")

# 1. Burnout Distribution
print("Burnout Distribution:")
print(df["burnout_level"].value_counts())

# 2. Stress vs Burnout
df.groupby("burnout_level")["stress_level"].mean().plot(kind="bar")
plt.title("Average Stress by Burnout Level")
plt.ylabel("Stress Level")
plt.show()

# 3. Sleep vs Burnout
df.groupby("burnout_level")["sleep_hours"].mean().plot(kind="bar")
plt.title("Average Sleep Hours by Burnout Level")
plt.ylabel("Sleep Hours")
plt.show()

# 4. Work Hours vs Burnout
df.groupby("burnout_level")["work_hours_per_week"].mean().plot(kind="bar")
plt.title("Average Work Hours by Burnout Level")
plt.ylabel("Work Hours Per Week")
plt.show()

