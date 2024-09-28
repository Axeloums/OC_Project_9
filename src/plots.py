import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_prep import df_politique_new

region_counts = df_politique_new["Region"].value_counts()
region_counts
sns.countplot(data=df_politique_new, y="Region", order=region_counts.index)
plt.tight_layout()
plt.show()
