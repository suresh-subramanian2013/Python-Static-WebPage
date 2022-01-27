from os import environ 
from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config['tc_user'] = environ.get('TC_USERNAME')
app.config['tc_passw'] = environ.get('TC_PASSWORD')

@app.route("/")
def hello():

    return render_template('index.html', user=environ.get('TC_USERNAME'), passw=environ.get('TC_PASSWORD'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
  