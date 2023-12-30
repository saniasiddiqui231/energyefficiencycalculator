import csv
import pandas as ps

# reading the csv file

data = ps.read_csv("wind_turbine.csv")
w_speed=ps.read_csv('wind_turbine.csv', usecols=['Wind speed m/s'])

k=len(data)
for i in range(0,k):
    power_out=w_speed.loc[i].item()


# declaring constant variables and taking inputs from user
    
radius = 30
wind_density = 1.225
PI = 3.14
wind_speed = int(input("Enter the speed of wind: "))

# defining a function calculating efficiency

def calculate_efficiency(power_out, power_input):
           efficiency = (power_out / power_input) * 100
           return efficiency

# constraints of wind_velocity
if wind_speed<3 or wind_speed>20:
      print("Output power is zero at this speed.")
else:
      power_input = float(input("Enter the input power: "))
      efficiency = calculate_efficiency(power_out, power_input)
      print(efficiency)




