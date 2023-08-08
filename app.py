# Import the necessary modules
from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)


data = pd.read_excel('data/data.xlsx')
unique_tokens = data['Token Number'].unique()

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
        selected_data = data[data['Token Number'] == int(selected_token)]
        selected_data_json = selected_data.to_json(orient='records')
        return selected_data_json
    else:
        return jsonify({'error': 'Token not provided'})

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
