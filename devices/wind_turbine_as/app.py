from flask import Flask,render_template,request
import pandas as pd
# import matplotlib.pyplot as plt
from graph import plot_graph

app = Flask(__name__)

input_data = pd.read_csv("./data/wind_turbine_input.csv")
w_speed=pd.read_csv('./data/wind_turbine_input.csv', usecols=['Wind speed m/s'])
p_out=pd.read_csv('./data/wind_turbine_input.csv', usecols=['output(kW)'])

@app.route('/',methods=['GET', 'POST'])
def rotor_rad():
    if request.method == 'POST':
        rotor_radius = float(request.form.get('rotorRadius'))
        
        def calculate_efficiency(power_out):
            efficiency = round((power_out / power_input) * 100, 2)
            eff_data.append(efficiency)

        eff_data = []
        k=len(input_data)
        
        for i in range(0,k):
            wind_speed = w_speed.loc[i].item()
            power_out = p_out.loc[i].item()
            if wind_speed<3 or wind_speed>20:
                eff_data.append(0)
            else:
                power_input = 0.5*3.14*1.204*rotor_radius*wind_speed
                calculate_efficiency(power_out)
        
        dict = {'Efficiency': eff_data}
        df = pd.DataFrame(dict)
        df.to_csv('./data/wind_turbine_data.csv')
        plot_graph()
        
    data = pd.read_csv('./data/wind_turbine_data.csv')
    data.reset_index()
    data.drop(columns="Unnamed: 0", inplace=True)
    data.index = data.index + 1
        
    return render_template('wind_turbine_index.html', tables=[data.to_html()], titles=[''])


### Flask
if __name__ == '__main__':
    app.run(host='localhost', port=int(5000), debug=True)