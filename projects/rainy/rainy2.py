import numpy as np
import pandas as pd

data = pd.read_csv("./projects/Seattle2014.csv")
print(data.head())

rainfall = data["PRCP"].values
inches = rainfall/254
print(inches.shape)

import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.hist(inches, 40)
plt.show()