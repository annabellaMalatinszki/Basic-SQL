from flask import Flask, render_template, redirect, request, url_for
from logic import *

app = Flask(__name__)


@app.route("/")
def display_main_page():
    return render_template("index.html")


@app.route("/mentors")
def display_mentors_and_schools():
    """Return the name of the mentors plus the name and country of the school
    ordered by the mentors id column.
    """
    title = "Mentors and Schools"
    menu = ["Mentor Id", "Mentor name", "City", "Country"]
    mentors_and_schools = get_mentor_name_school_country()
    return render_template("list.html", title=title, menu=menu, data=mentors_and_schools)


@app.route("/all_school")
def display_mentors_and_all_schools():
    """Return the name of the mentors plus the name and country of the school
    ordered by the mentors id column, plus all schools even without assigned mentors.
    """
    title = "Mentors and All Schools"
    menu = ["Mentor Id", "Mentor name", "City", "Country"]
    mentors_and_all_schools = get_mentor_name_all_schools_country()
    return render_template("list.html", title=title, menu=menu, data=mentors_and_all_schools)


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
