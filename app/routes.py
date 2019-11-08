from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", new_user=False, title="Home page")


@app.route('/thoughts')
def thoughts():
    return render_template("thoughts.html", title="Thoughts page")