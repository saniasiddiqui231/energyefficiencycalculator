import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')

def plot_graph():
    plt.figure(figsize=(10,6))
    x=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_input.csv', usecols=['Wind speed m/s'])
    y=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_data.csv', usecols=['Efficiency'])

    plt.plot(x,y)
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Efficiency (in %)')
    plt.savefig('./static/graph.png')
    