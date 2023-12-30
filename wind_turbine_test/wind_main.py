import pandas as pd

#reading the csv file

df=pd.read_csv('windcsv.csv')
ws=pd.read_csv('windcsv.csv', usecols={'windSpeed(m/s)'})

#making user enter the input cp and rotor radius

cp=float(input("Enter the Power Coefficient (0 to 0.593): "))
rr=float(input("Enter the Rotor Radius (50m to 150m): "))
inputPower=int(input("Enter the rated Input Power (30M to 150M): "))

k=len(df)

#defining the values of variables by reading them from csv

for i in range(0,k):
    windSpd=ws.loc[i].item()
    outputPower=0.5*3.14*1.204*cp*rr*ws

#defining the function to calculate the efficiency

def calc_eff(outputPower, inputPower):
    eff=round((outputPower/inputPower)*100, 2)
    return eff

#printint the final value of effiency percentage

const_eff=calc_eff(outputPower, inputPower)

print("The efficiency of Wind Turbine is", calc_eff(outputPower, inputPower), "%")