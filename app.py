from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

with open('weather_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_str = request.form['date']
        
        try:
            date = pd.to_datetime(date_str, format='%d-%m-%Y')
            month = date.month
            day = date.day
            year = date.year
        
            input_data = np.array([[month, day, year]])
            
            predictions = model.predict(input_data)
            
            tmin, tmax, tavg, prcp = predictions[0]
            
            return render_template('result.html', predictions={
                'tmin': tmin,
                'tmax': tmax,
                'tavg': tavg,
                'prcp': prcp
            }, date=date_str)
        
        except Exception as e:
            return str(e)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
