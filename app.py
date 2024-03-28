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
    return render_template('Maps.html')

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
