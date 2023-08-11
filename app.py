# Import the necessary modules
from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__)


data = pd.read_excel('data/data.xlsx')
data.replace(np.nan, '', regex=True)
unique_tokens = data['Level'].unique()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html', unique_tokens=unique_tokens)

@app.route('/get_data', methods=['GET'])
def get_data():
    selected_token = request.args.get('token')
    if selected_token:
        selected_data = data[data['Level'] == int(selected_token)]
        selected_data_json = selected_data.to_json(orient='records')
        return selected_data_json
    else:
        return jsonify({'error': 'Token not provided'})

@app.route('/page2', methods=['GET'])
def page2():
    return render_template('page2.html', data=data)


@app.route('/get_data_name', methods=['GET'])
def get_data_name():
    search_term = request.args.get('token')
    if search_term:
        # Convert 'Token Name' column to lowercase and compare
        search_term_lower = search_term.lower()
        filtered_data = data[data['Token Name'].str.lower() == search_term_lower]

        # Check if any data is found
        if not filtered_data.empty:
            search_term_json = filtered_data.to_json(orient='records')
            return search_term_json
        else:
            return jsonify({'error': 'No matching data found'})
    else:
        return jsonify({'error': 'Search term is required'})



@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
