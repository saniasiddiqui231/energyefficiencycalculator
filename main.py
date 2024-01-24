from flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# wind turbine inputs
input_data = pd.read_csv("./devices/wind_turbine_as/data/wind_turbine_input.csv")
w_speed=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_input.csv', usecols=['Wind speed m/s'])
p_out=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_input.csv', usecols=['output(kW)'])

# transformer inputs
input_data=pd.read_csv('./devices/transformer/inputdata.csv')
secondary_voltage = pd.read_csv('./devices/transformer/inputdata.csv',usecols=["secondary_voltage(Volts)"])
secondary_current = pd.read_csv('./devices/transformer/inputdata.csv',usecols=["secondary_current(Amperes)"])
iron_losses = pd.read_csv('./devices/transformer/inputdata.csv',usecols=["iron_losses"])
power_factor=pd.read_csv('./devices/transformer/inputdata.csv',usecols=["power_factor"])

# insulator inputs
input_data = pd.read_csv('./devices/insulator/data/input.csv')
n = pd.read_csv('./devices/insulator/data/input.csv', usecols=['n'])
v_disc1 = pd.read_csv('./devices/insulator/data/input.csv', usecols={'v_disc1'})

# solar cell inputs



## app.routes and functions for devices
@app.route('/wind_turbine',methods=['GET', 'POST'])
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
        df.to_csv('./devices/wind_turbine_as/data/wind_turbine_data.csv')
        
        # def plot_graph():
        #     plt.figure(figsize=(10,6))
        #     x=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_input.csv', usecols=['Wind speed m/s'])
        #     y=pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_data.csv', usecols=['Efficiency'])

        #     plt.plot(x,y)
        #     plt.xlabel('Wind Speed (m/s)')
        #     plt.ylabel('Efficiency (in %)')
        #     plt.savefig('./devices/wind_turbine_as/static/graph.png')

        # plot_graph()
        
    data = pd.read_csv('./devices/wind_turbine_as/data/wind_turbine_data.csv')
    data.reset_index()
    data.drop(columns="Unnamed: 0", inplace=True)
    data.index = data.index + 1
        
    return render_template('wind_turbine_index.html', tables=[data.to_html()], titles=[''])

@app.route('/transformer',methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        np = float(request.form.get('np'))
        ns = float(request.form.get('ns'))
        winding_resistance = float(request.form.get('winding_resistance'))
        coupling_factor = float(request.form.get('coupling_factor'))

        n = np / ns

        k=len(input_data)
        eff_data = []
        for i in range(0,k):  #calculating the copper loss
           sc=secondary_current.loc[i].item()
           iron=iron_losses.loc[i].item()
           sv=secondary_voltage.loc[i].item()
           pf=power_factor.loc[i].item()
           primary_current = sc * n * coupling_factor   #calculating primary current
           loss = ((primary_current ** 2) * winding_resistance) + ((sc ** 2) * winding_resistance)
          
           power_output = sc * sv * pf
           efficiency = round(((power_output) / (power_output+loss+iron)) * 100, 2)  # calculating the final efficiency
           eff_data.append(efficiency)

        dict = {'efficiency': eff_data}
        df = pd.DataFrame(dict)
        df.to_csv('./devices/transformer/outputdata.csv')

    data = pd.read_csv('./devices/transformer/outputdata.csv')
    data.reset_index()
    data.drop(columns="Unnamed: 0", inplace=True)  # Reset index without adding a new column
    data.index = data.index + 1

    # Check if 'data' is not None before calling 'to_html'
    return render_template('transformer_index.html',tables=[data.to_html()], titles=[''])

@app.route('/insulator',methods=['GET', 'POST'])
def insulator():
    if request.method == 'POST':
        v_string = float(request.form.get('vString'))
        
        eff_data = []
            
        def efficiency(n_val,v_disc1_val):
            eff = round(v_string/(n_val*v_disc1_val)*100, 2)
            eff_data.append(eff)
            
        k = len(input_data)
        
        for i in range(0,k):
            num_of_turns = n.loc[i].item()
            volt_disc1 = v_disc1.loc[i].item()
            efficiency(num_of_turns,volt_disc1)
            
        dict = {'Efficiency': eff_data}
        df = pd.DataFrame(dict)
        df.to_csv('./devices/insulator/data/output.csv')

    data = pd.read_csv('./devices/insulator/data/output.csv')
    data.reset_index()
    data.drop(columns='Unnamed: 0', inplace=True)
    data.index = data.index + 1

    return render_template('insulator_index.html', tables=[data.to_html()], titles=[''])

@app.route('/',methods=['GET', 'POST'])
def index():
    render_template('index.html')

# final app.run command
if __name__ == '__main__':
    # app.run(host='localhost', port=int(5000), debug=True)
    app.run(debug=True)