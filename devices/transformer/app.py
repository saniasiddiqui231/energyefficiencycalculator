from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

input_data=pd.read_csv('inputdata.csv')
secondary_voltage = pd.read_csv('inputdata.csv',usecols=["secondary_voltage(Volts)"])
secondary_current = pd.read_csv('inputdata.csv',usecols=["secondary_current(Amperes)"])
iron_losses = pd.read_csv('inputdata.csv',usecols=["iron_losses"])
power_factor=pd.read_csv('inputdata.csv',usecols=["power_factor"])


@app.route('/',methods=['GET', 'POST'])
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
        df.to_csv('outputdata.csv')

    data = pd.read_csv('outputdata.csv')
    data.reset_index()
    data.drop(columns="Unnamed: 0", inplace=True)  # Reset index without adding a new column
    data.index = data.index + 1

    # Check if 'data' is not None before calling 'to_html'
    return render_template('transformerindex.html',tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run(debug=True)