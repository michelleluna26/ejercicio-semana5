from distutils.log import debug
from flask import Flask, redirect, render_template, request, url_for
from Person import Person
from db import (
    insertNewPerson,
    selectAllPersons,
    selectPersonBy,
    deletePersonBy,
    updatePerson,
)


app = Flask(__name__)


@app.route("/")
def home():
    personlist = selectAllPersons()
    return render_template("home.html", persons=personlist)


@app.route("/new", methods=["GET", "POST"])
def new_person():
    if request.method == "GET":
        return render_template("new.html")
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary)
        insertNewPerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/show/<int:id>")
def show_person(id):
    person = selectPersonBy(id)
    return render_template("show.html", person=person)


@app.route("/delete/<int:id>")
def delete_person(id):
    deletePersonBy(id)
    return redirect(url_for("home"))


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_person(id):
    if request.method == "GET":
        person = selectPersonBy(id)
        return render_template("update.html", person=person)
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary, id)
        updatePerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
