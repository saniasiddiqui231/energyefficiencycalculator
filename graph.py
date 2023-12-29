import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('solar_data.csv', parse_dates=['timestamp'])

plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['irradiance'], label='Irradiance')
plt.plot(df['timestamp'], df['temperature'], label='Temperature')
plt.plot(df['timestamp'], df['power_output'], label='Power Output')
plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.legend()
plt.title('Solar Cell Data Monitoring')
plt.show()
