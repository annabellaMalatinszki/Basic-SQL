from flask import Flask, render_template, redirect, request, url_for
from logic import *

app = Flask(__name__)


@app.route("/")
def display_main_page():
    return render_template("index.html")


@app.route("/mentors")
def display_mentors_and_schools():
    pass


@app.route("/all_school")
def display_mentors_and_all_schools():
    pass


@app.route("/mentors_by_country")
def display_mentors_by_country():
    pass


@app.route("/contacts")
def display_school_and_contact_person():
    pass


@app.route("/applicants")
def display_applicants():
    pass


@app.route("/applicants_and_mentors")
def display_applicants_and_mentors():
    pass


if __name__ == '__main__':
    app.run(debug=True)
