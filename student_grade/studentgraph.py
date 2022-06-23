from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import style
df = pd.read_csv("student-mat.csv",sep=";")

a = ["G1","G3"]
new_df = df[a]
p = "G1"
style.use("ggplot")
plt.scatter(new_df[p],new_df["G3"])
plt.xlabel(p)
plt.ylabel("Final Grade")
plt.show()