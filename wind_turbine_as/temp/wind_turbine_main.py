import pandas as pd

rotor_rad = float(input("Enter the rotor radius (more than 17 meters): "))

data = pd.read_csv("wind_turbine_input.csv")
w_speed=pd.read_csv('wind_turbine_input.csv', usecols=['Wind speed m/s'])
p_out=pd.read_csv('wind_turbine_input.csv', usecols=['output(kW)'])

eff_data = []

def calculate_efficiency(power_out):
      efficiency = round((power_out / power_input) * 100, 2)
      eff_data.append(efficiency)

k=len(data)

for i in range(0,k):
      wind_speed = w_speed.loc[i].item()
      power_out = p_out.loc[i].item()
      if wind_speed<3 or wind_speed>20:
            eff_data.append(0)
      else:
            power_input = 0.5*3.14*1.204*rotor_rad*wind_speed
            calculate_efficiency(power_out)
      
dict = {'efficiency': eff_data}
