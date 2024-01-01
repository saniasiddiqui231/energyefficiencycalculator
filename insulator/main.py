import pandas as pd

df = pd.read_csv('input.csv')
n = pd.read_csv('input.csv', usecols=['n'])
v_disc1 = pd.read_csv('input.csv', usecols={'v_disc1'})

v_string = float(input('Enter the string voltage (in kVs) (>60kV & <100kV): '))


def efficiency(n_val,v_disc1_val):
    eff = round(v_string/(n_val*v_disc1_val)*100, 2)
    print(eff, "%")

k = len(df)

for i in range(0,k):
    num_of_turns = n.loc[i].item()
    volt_disc1 = v_disc1.loc[i].item()
    efficiency(num_of_turns,volt_disc1)