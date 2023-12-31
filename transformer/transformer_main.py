import pandas as pd


# reading csv file and taking inputs from user

df=pd.read_csv('transformer1.csv')


np = int(input("Enter the turns in primary coil: "))
ns = int(input("Enter the turns in secondary coil: "))
winding_resistance = float(input("Enter the resistance in a coil: "))
iron_loss = int(input("Enter the iron loss or core loss of the transformer: ")) #core/iron loss is constant for a specific transformer. 
 
# stray losses are typically a small fraction of the total losses in a well-designed transformer hence we'll neglect it.

# defining variables for convinience

secondary_voltage = df["secondary_voltage(Volts)"]
secondary_current = df["secondary_current(Amperes)"]

#calculating the turns ratio

n = np / ns

# defining conditions for step-up(ns>np) and step-down(ns<np) transformer

if ns > np:
    primary_voltage = secondary_voltage / n #calculating primary voltage
    primary_current = secondary_current * n #calculating primary current
    
    def copper_loss():    #calculating the copper loss
        loss = ((primary_current ** 2) * winding_resistance) + ((secondary_current ** 2) * winding_resistance)
        return loss
    
    losses=copper_loss()
    power_output = secondary_current * secondary_voltage * df['power_factor']   
    efficiency = ((power_output) / (power_output+losses+iron_loss)) * 100  # calculating the final efficiency
    print(efficiency)
    
    

elif ns<np:  
    primary_voltage1 = secondary_voltage*n  #calculating primary voltage
    primary_current1 = secondary_current/n  #calculating primary current

    def copper_loss1():    #calculating copper loss
        loss1 = ((primary_current1 ** 2) * winding_resistance) + ((secondary_current ** 2) * winding_resistance)
        return loss1
    
    losses1 = copper_loss1()
    power_output1 = secondary_current * secondary_voltage * df['power factor']
    efficiency = ((power_output1) / (power_output1 + losses1 + iron_loss)) * 100   #calculating final efficiency
    print(efficiency)
    
    
else:
    print("Not defined") 

    






    


   
    




