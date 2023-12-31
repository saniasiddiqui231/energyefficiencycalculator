import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(20,6))
x=pd.read_csv('input.csv', usecols=['Wind speed m/s'])
y=pd.read_csv('output.csv', usecols=['efficiency'])

plt.plot(x,y)
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Efficiency (in %)')
plt.show()