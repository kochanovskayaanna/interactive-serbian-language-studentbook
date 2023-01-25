from flask import render_template, Flask, request
app = Flask(__name__, template_folder=".")

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/useful.html')
def useful():
    return render_template('useful.html')

@app.route('/alphabet.html')
def alphabet():
    return render_template('alphabet.html')

if __name__ == "__main__":
    app.run()


#
#
# @app.route('/')
#
#
# @app.route('/')
#
# @app.route('/')
