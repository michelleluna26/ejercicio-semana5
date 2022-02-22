from distutils.log import debug
from flask import Flask, render_template
from db import insertNewPerson, selectAllPersons


app = Flask(__name__)


@app.route("/")
def home():
    personlist = selectAllPersons()
    return render_template("home.html", persons=personlist)


@app.route("/new")
def new_person():
    return render_template("new.html")


@app.route("/insert")
def insert_person():
    insertNewPerson()


if __name__ == "__main__":
    app.run(debug=True)
