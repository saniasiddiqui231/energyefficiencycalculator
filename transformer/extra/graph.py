import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_params = pd.read_csv('transformer1.csv')
df_eff = pd.read_csv('transformer12.csv')

v1 = df_params['secondary_current(Amperes)']
y1 = df_eff['efficiency']

plt.figure(figsize=(10,6))
plt.plot(v1, y1, linestyle='-', color='blue')
plt.xlabel('Current')
plt.ylabel('Eff')
plt.title('Current vs Eff')
plt.show()

