import pandas as pd 
import csv

# opening the csv file
df = pd.read_csv('solar_data.csv')

# specifying the x and y axes for plotting and sorting the data in ascending

sdx = pd.read_csv('solar_data.csv', usecols=['Voltage']).sort_values(by='Voltage', ascending=True)
sdy = pd.read_csv('solar_data.csv', usecols=['Current'])

# adding a power column in the csv table for calculating maximum power

df['Power'] = df['Voltage'] * df['Current']
df.to_csv('solar_data.csv', index=False)

# finding open circuit voltage and short circuit current
k=len(df)
for i in range(0,k):
    if sdx.loc[i].item()==0.0:
        ssc=sdy.loc[i].item()
        break
for i in range(0,k):
    if sdy.loc[i].item()==0.0:
        ocv = sdx.loc[i].item()
        break

'''
calculating fill factor: 

The fill factor represents how "square" the I-V curve is, and it indicates how effectively the solar panel utilizes its 
theoretical potential to produce power.

A higher fill factor (closer to 1) is generally better, suggesting a more efficient panel with less internal resistance losses.

For example: The fill factor of a solar panel is 0.67, 
which indicates that it's utilizing about 67% of its theoretical potential to produce power.

'''

fill_factor = (df['Power'].max()/(ssc * ocv))

# taking input power into account for efficiency calculation
P_in = float(input('enter input power used for readings: '))

# calculating efficiency
efficiency = ((ssc * ocv * fill_factor) / P_in) * 100

print("the fill factor is: ", fill_factor, " and the efficiency is: ", efficiency,"%")
