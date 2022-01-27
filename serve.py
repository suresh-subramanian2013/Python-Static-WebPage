from os import environ 
from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config['user'] = environ.get('USERNAME')
app.config['passw'] = environ.get('PASSWORD')

@app.route("/")
def hello():

    return render_template('index.html', user=environ.get('USERNAME'), passw=environ.get('PASSWORD'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
  
