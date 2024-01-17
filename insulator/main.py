import pandas as pd

# importing the columns from csv file
df = pd.read_csv('./data/input.csv')
n = pd.read_csv('./data/input.csv', usecols=['n'])
v_disc1 = pd.read_csv('./data/input.csv', usecols={'v_disc1'})

eff_data = []

# making user input the string voltage
v_string = float(input('Enter the string voltage (in kVs) (>60kV & <100kV): '))

# defining the function to calculate the efficiency and print it
def efficiency(n_val,v_disc1_val):
    eff = round(v_string/(n_val*v_disc1_val)*100, 2)
    # print(eff, "%")
    eff_data.append(eff)

k = len(df)

# loop for assigning the values of number of discs and voltage in nearest disc to conductor
for i in range(0,k):
    num_of_turns = n.loc[i].item()
    volt_disc1 = v_disc1.loc[i].item()
    efficiency(num_of_turns,volt_disc1)
    
dict = {'Efficiency': eff_data}
df = pd.DataFrame(dict)
df.to_csv('./data/output.csv')