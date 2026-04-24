import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("march_madness_data.csv")

# Preview data
print(df.head())
print(df.columns)

# Graph 1: Seed vs average round reached
seed_round = df.groupby("SEED")["ROUND_REACHED"].mean()

plt.figure()
seed_round.plot(kind="bar")
plt.title("Average Tournament Round Reached by Seed")
plt.xlabel("Seed")
plt.ylabel("Average Round Reached")
plt.tight_layout()
plt.savefig("seed_vs_round.png")
plt.show()

# Graph 2: Offensive efficiency vs round reached
plt.figure()
plt.scatter(df["OFFENSIVE_EFFICIENCY"], df["ROUND_REACHED"])
plt.title("Offensive Efficiency vs Tournament Success")
plt.xlabel("Offensive Efficiency")
plt.ylabel("Round Reached")
plt.tight_layout()
plt.savefig("off_efficiency_vs_round.png")
plt.show()

# Graph 3: Upsets by round
upsets = df[df["UPSET"] == 1].groupby("ROUND").size()

plt.figure()
upsets.plot(kind="bar")
plt.title("Number of Upsets by Round")
plt.xlabel("Round")
plt.ylabel("Number of Upsets")
plt.tight_layout()
plt.savefig("upsets_by_round.png")
plt.show()
