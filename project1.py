import pandas as pd
df = pd.read_csv("burnout.csv")

import matplotlib.pyplot as plt
df.groupby("burnout_level")["work_hours_per_week"].mean().plot(kind="bar")

plt.title("Average Work Hours by Burnout Level")
plt.ylabel("Work_Hours_Per_Week")

plt.show()

