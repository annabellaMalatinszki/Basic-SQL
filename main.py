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
    menu = ["Mentor Id", "Mentor name", "School", "Country"]
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
    """Show the result of a query that returns the number of the mentors 
    per country ordered by the name of the countries.
    """
    title = "Number of Mentors per Country"
    menu = ["Country", "Number of mentors"]
    mentors_by_country = get_mentors_by_country()
    return render_template("list.html", title=title, menu=menu, data=mentors_by_country)


@app.route("/contacts")
def display_school_and_contact_person():
    """Show the result of a query that returns the name of the school plus the name
    of contact person at the school (from the mentors table) ordered by the name of the school.abs
    """
    title = "Contact Persons"
    menu = ["School", "Contact Person"]
    school_contact_person = get_school_contact_person()
    return render_template("list.html", title=title, menu=menu, data=school_contact_person)


@app.route("/applicants")
def display_applicants():
    """Show the result of a query that returns the first name and the code of the applicants plus 
    the creation_date of the application (joining with the applicants_mentors table) ordered by 
    the creation_date in descending order.
    """
    title = "Applicants after 2016-01-01"
    menu = ["Application Code", "First name", "Creation Date"]
    applicants = get_applicants()
    return render_template("list.html", title=title, menu=menu, data=applicants)


@app.route("/applicants_and_mentors")
def display_applicants_and_mentors():
    """Show the result of a query that returns the first name and the code of the applicants plus
     the name of the assigned mentor (joining through the applicants_mentors table) ordered by 
     the applicants id column.
     """
    title = "Applicants and Mentors"
    menu = ["Applicant Id", "Application Code", "First Name", "Assigned Mentor"]
    applicants_and_mentors = get_applicants_and_mentors()
    return render_template("list.html", title=title, menu=menu, data=applicants_and_mentors)


if __name__ == '__main__':
    app.run(debug=True)
