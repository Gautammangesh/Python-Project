from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components
import dash_html_components

app = Flask(__name__)

@app.route('/')
def home():
    # Call function to plot graphs
    return render_template('index.html')

@app.route('/maps')
def maps():
    # Assume you have a pandas DataFrame called 'data' with columns 'years' and 'number_of_bodies'
    # You should replace this with your actual data loading and processing logic
    data = pd.DataFrame({
        'years': [2018, 2019, 2020, 2021],
        'number_of_bodies': [100, 120, 90, 110]
    })

    # Convert Series to lists
    years = data['years'].tolist()
    number_of_bodies = data['number_of_bodies'].tolist()
    
    return render_template('Maps.html', years=years, number_of_bodies=number_of_bodies)


@app.route('/analysis')
def analysis():
    # Call function to plot graphs
    return render_template('Analysis.html')

@app.route('/research')
def research():
    # Call function to plot graphs
    return render_template('Research.html')

@app.route('/features')
def features():
    # Call function to plot graphs
    return render_template('Features.html')


if __name__ == '__main__':
    app.run(debug=True)
