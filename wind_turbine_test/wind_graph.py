import pandas as pd
import matplotlib.pyplot as plt
from wind_main import const_eff

plt.figure(figsize=(10, 6))
df=pd.read_csv('windcsv.csv')

sdx=pd.read_csv('windcsv.csv', usecols=['windSpeed(m/s)'])
sdy=const_eff

plt.plot(sdx,sdy)
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Efficiency')
plt.show()
