from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:route>')
def dynamic_route(route):
    return render_template(route)
