from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", new_user=False, title="Home page")


@app.route('/thoughts')
def thoughts():
    return render_template("thoughts.html", title="Thoughts page")


@app.route('/data')
def data():
    some_data = [{ "name": 'Item one', "id": "1" }, { "name": 'Item two', "id": "2" }]

    print(some_data)

    return render_template("data.html", some_data=some_data)