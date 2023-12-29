import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
df=pd.read_csv('solar_data.csv')

#specifying the x and y axes for plotting and sorting the data in ascending
sdx=pd.read_csv('solar_data.csv', usecols=['Voltage']).sort_values(by='Voltage', ascending=True)
sdy=pd.read_csv('solar_data.csv', usecols=['Current'])

#plots for visual representaion
plt.plot(sdx,sdy)
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.show()

plt.legend()
plt.title('Solar Cell I-V characteristics')
plt.show()
