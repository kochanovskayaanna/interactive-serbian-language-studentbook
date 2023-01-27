from flask import render_template, Flask, request
import pandas as pd
app = Flask(__name__, template_folder=".")
from jinja2 import Template

letters = ["letter-a", "letter-b", "letter-v", "letter-g", "letter-d", "letter-dj", "letter-e", "letter-ž", "letter-z",
    "letter-i", "letter-j", "letter-k", "letter-l", "letter-lj", "letter-m", "letter-n", "letter-nj", "letter-o",
    "letter-p", "letter-r", "letter-s", "letter-t", "letter-ć", "letter-u", "letter-f", "letter-h",
    "letter-c", "letter-č", "letter-dž", "letter-š"]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/useful.html')
def useful():
    return render_template('useful.html')

@app.route('/alphabet.html')
def alphabet():
    alpha_csv = pd.read_csv('alphabet.csv', delimiter=';')
    alpha_list = alpha_csv.to_dict(orient='records')
    return render_template('alphabet.html', alpha_list=alpha_list, letters=letters)

@app.route('/biti.html')
def biti():
    return render_template('biti.html')

if __name__ == "__main__":
    app.run()
