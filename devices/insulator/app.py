from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

input_data = pd.read_csv('./data/input.csv')
n = pd.read_csv('./data/input.csv', usecols=['n'])
v_disc1 = pd.read_csv('./data/input.csv', usecols={'v_disc1'})

@app.route('/',methods=['GET', 'POST'])
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
        df.to_csv('./data/output.csv')

    data = pd.read_csv('./data/output.csv')
    data.reset_index()
    data.drop(columns='Unnamed: 0', inplace=True)
    data.index = data.index + 1

    return render_template('insulator.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run(host='localhost', port=int(5000), debug=True)