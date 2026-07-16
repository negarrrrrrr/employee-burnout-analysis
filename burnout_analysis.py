import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("burnout.csv")

print(df.head())
df.info()
print(df.describe())

# Research Question 1:
# Does work-life balance differ across burnout levels?

work_life_grouped = (
    df.groupby("burnout_level")["work_life_balance"]
    .mean()
)

work_life_grouped = work_life_grouped.reindex(
    ["Low", "Moderate", "High"]
)

print(work_life_grouped)

plt.figure(figsize=(6, 4))

work_life_grouped.plot(kind="bar")

plt.title("Average Work-Life Balance by Burnout Level")
plt.xlabel("Burnout Level")
plt.ylabel("Average Work-Life Balance")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("work_life_balance_by_burnout.png")
plt.show()


# Research Question 2:
# Do average burnout scores differ across gender groups?

gender_grouped = (
    df.groupby("gender")["burnout_score"]
    .mean()
)

print(gender_grouped)

plt.figure(figsize=(6, 4))

gender_grouped.plot(kind="bar")

plt.title("Average Burnout Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Burnout Score")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("burnout_by_gender.png")
plt.show()

# Research Question 3:
# Which variables are most strongly associated with burnout?

burnout_corr = df.corr(numeric_only=True)["burnout_score"]

corr_without_burnout = burnout_corr.drop("burnout_score")

top5_names = (
    corr_without_burnout
    .abs()
    .sort_values(ascending=False)
    .head(5)
    .index
)

top5_corr = corr_without_burnout.loc[top5_names]

print(top5_corr)

plt.figure(figsize=(8, 5))

top5_corr.sort_values().plot(kind="barh")

plt.title("Top 5 Variables Associated with Burnout")
plt.xlabel("Correlation with Burnout Score")
plt.ylabel("Variable")

plt.axvline(0)

plt.tight_layout()
plt.savefig("top5_burnout_correlations.png")
plt.show()

# Research Question 4:
# Do people who sleep more have lower burnout?

sleep_corr = df["sleep_hours"].corr(df["burnout_score"])

print("Correlation between sleep hours and burnout:")
print(sleep_corr)

sample_df = df.sample(n=5000, random_state=42)

plt.figure(figsize=(7, 5))

plt.scatter(
    sample_df["sleep_hours"],
    sample_df["burnout_score"],
    alpha=0.2
)

plt.title("Sleep Hours and Burnout Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Burnout Score")

plt.tight_layout()
plt.savefig("sleep_hours_and_burnout.png")
plt.show()

# Research Question 5:
# Does manager support differ across burnout levels?

manager_grouped = (
    df.groupby("burnout_level")["manager_support"]
    .mean()
)

manager_grouped = manager_grouped.reindex(
    ["Low", "Moderate", "High"]
)

print(manager_grouped)

plt.figure(figsize=(6, 4))

manager_grouped.plot(kind="bar")

plt.title("Average Manager Support by Burnout Level")
plt.xlabel("Burnout Level")
plt.ylabel("Average Manager Support")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("manager_support_by_burnout.png")
plt.show()

# Research Question 6:
# Do employees who seek professional help report different burnout scores?

help_grouped = (
    df.groupby("seeks_professional_help")["burnout_score"]
    .mean()
)

print(help_grouped)

plt.figure(figsize=(6, 4))

help_grouped.plot(kind="bar")

plt.title("Average Burnout Score by Professional Help-Seeking")
plt.xlabel("Sought Professional Help")
plt.ylabel("Average Burnout Score")

plt.xticks([0, 1], ["No", "Yes"], rotation=0)

plt.tight_layout()
plt.savefig("professional_help_and_burnout.png")
plt.show()

# Research Question 7:
# Do overtime hours differ across burnout levels?

overtime_grouped = (
    df.groupby("burnout_level")["overtime_hours"]
    .mean()
)

overtime_grouped = overtime_grouped.reindex(
    ["Low", "Moderate", "High"]
)

print(overtime_grouped)

plt.figure(figsize=(6, 4))

overtime_grouped.plot(kind="bar")

plt.title("Average Overtime Hours by Burnout Level")
plt.xlabel("Burnout Level")
plt.ylabel("Average Overtime Hours")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("overtime_by_burnout.png")
plt.show()
