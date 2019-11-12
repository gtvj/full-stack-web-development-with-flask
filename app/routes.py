from app import app
from flask import render_template, request

some_data = [{ "name": 'Item one', "id": "1" }, { "name": 'Item two', "id": "2" }]

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", new_user=False, title="Home page")


@app.route('/thoughts')
def thoughts():
    return render_template("thoughts.html", title="Thoughts page")


@app.route('/data')
def data():

    print(some_data)
    return render_template("data.html", some_data=some_data)


@app.route('/people')
@app.route('/people/<user>')
def people(user="Clarence"):
    return render_template("people.html", user=user)

@app.route('/add_person', methods=["GET", "POST"])
def add_person():
    name = request.form.get('name')
    return render_template("add_person.html", name=name)