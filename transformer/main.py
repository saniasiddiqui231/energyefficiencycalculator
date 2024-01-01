import pandas as pd


# reading csv file and taking inputs from user

df=pd.read_csv('inputdata.csv')
eff_data = []

np = int(input("Enter the turns in primary coil: "))
ns = int(input("Enter the turns in secondary coil: "))
winding_resistance = float(input("Enter the resistance in a coil(o.oo1 - 20 ohm): "))
coupling_factor = float(input("Enter the coupling factor(0-1): "))
 
# stray losses are typically a small fraction of the total losses in a well-designed transformer hence we'll neglect it.

# defining variables for convinience

secondary_voltage = df["secondary_voltage(Volts)"]
secondary_current = df["secondary_current(Amperes)"]
iron_losses = df["iron_losses"]

#calculating the turns ratio

n = np / ns

primary_voltage = secondary_voltage / (coupling_factor * n) #calculating primary voltage
primary_current = secondary_current * n * coupling_factor   #calculating primary current
    
def copper_loss():    #calculating the copper loss
    loss = ((primary_current ** 2) * winding_resistance) + ((secondary_current ** 2) * winding_resistance)
    return loss
    
losses=copper_loss()
power_output = secondary_current * secondary_voltage * df['power_factor']   
efficiency = ((power_output) / (power_output+losses+iron_losses)) * 100  # calculating the final efficiency
print(efficiency)
eff_data.append(efficiency)


dict = {'efficiency': eff_data}
df = pd.DataFrame(dict)
df.to_csv('outputdata.csv', index=False)



    
    


    






    


   
    




