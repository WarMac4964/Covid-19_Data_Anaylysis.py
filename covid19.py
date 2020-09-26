import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./Italy data set/national_data - national_data.csv")
df.head()

sns.relplot(x='total_cases', y='resigned_healed', data=df,)
plt.xlabel("Total Cases")
plt.ylabel("Recovered")
plt.title("Total Cases and Recovered")
plt.savefig('Total Cases and Recovered.png')


sns.relplot(x='total_cases', y='deceased', data=df,)
plt.xlabel("Total Cases")
plt.ylabel("Deaths")
plt.title("Total Cases and Deaths")
plt.savefig('Total Cases and Deaths.png')

sns.relplot(x='total_cases', y='hospitalized_with_symptoms', data=df,)
plt.xlabel("Total Cases")
plt.ylabel("Hospitalized with Symptoms")
plt.title("Total Cases and HwS")
plt.savefig('Total Cases and HwS.png')
plt.show()
