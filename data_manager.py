import psycopg2

connect_str = "dbname='annabell' user='annabell' host='localhost'"
conn = psycopg2.connect(connect_str)
conn.autocommit = True
cursor = conn.cursor()


def get_mentor_names():
    """Get the full names of all mentors"""
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    mentor_names = cursor.fetchall()
    return mentor_names


def get_mentor_nicknames(city):
    """Get nickname of mentors from a given city"""
    cursor.execute("""SELECT nick_name FROM mentors WHERE city=(%s);""",
                   (city, ))
    mentor_nicknames = cursor.fetchall()
    return mentor_nicknames


def get_name_number_by(search_by, criteria):
    """Get full applicant name and phone number by the given criteria"""

    if search_by == "first_name":
        cursor.execute("""SELECT first_name, last_name FROM applicants
                        WHERE first_name = (%s);""",
                       (criteria, ))

    elif search_by == "last_name":
        cursor.execute("""SELECT first_name, last_name FROM applicants
                        WHERE last_name = (%s);""",
                       (criteria, ))

    elif search_by == "email":
        cursor.execute("""SELECT first_name, last_name FROM applicants
                        WHERE email LIKE %s;""",
                       ('%' + criteria + '%', ))

    elif search_by == "app_code":
        cursor.execute("""SELECT first_name, last_name FROM applicants
                        WHERE application_code = (%s);""",
                       (criteria, ))

    rows = cursor.fetchall()
    full_name = "{} {}".format(rows[0][0], rows[0][1])

    if search_by == "first_name":
        cursor.execute("""UPDATE applicants
                        SET full_name = %s
                        WHERE first_name = %s;""",
                       (full_name, criteria))
        cursor.execute("""SELECT full_name, phone_number FROM applicants
                        WHERE first_name = (%s);""",
                       (criteria, ))

    elif search_by == "last_name":
        cursor.execute("""UPDATE applicants
                        SET full_name = %s
                        WHERE last_name = %s;""",
                       (full_name, criteria))
        cursor.execute("""SELECT full_name, phone_number FROM applicants
                        WHERE last_name = (%s);""",
                       (criteria, ))

    elif search_by == "email":
        cursor.execute("""UPDATE applicants
                        SET full_name = %s
                        WHERE email LIKE %s;""",
                       (full_name, '%' + criteria + '%'))
        cursor.execute("""SELECT full_name, phone_number FROM applicants
                        WHERE email LIKE (%s);""",
                       ('%' + criteria + '%', ))

    elif search_by == "app_code":
        cursor.execute("""UPDATE applicants
                        SET full_name = %s
                        WHERE application_code = %s;""",
                       (full_name, criteria))
        cursor.execute("""SELECT full_name, phone_number FROM applicants
                        WHERE application_code = (%s);""",
                       (criteria, ))

    full_name_and_phone_number = cursor.fetchall()
    return full_name_and_phone_number


def add_new_applicant_data(first_name, last_name, phone_number, email, application_code):
    """Add new applicant to database """
    cursor.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                    VALUES (%s, %s, %s, %s, %s);""",
                   (first_name, last_name, phone_number, email, application_code))
    cursor.execute("""SELECT * FROM applicants
                    WHERE application_code = (%s);""",
                   (application_code, ))
    new_applicant = cursor.fetchall()
    return new_applicant


def update_applicant_data(first_name, last_name, new_phone_number):
    """ Update phone number of an applicant by first and last name """
    cursor.execute("""SELECT first_name, last_name FROM applicants
                    WHERE first_name = (%s) AND last_name = (%s);""",
                   (first_name, last_name))
    rows = cursor.fetchall()
    full_name = "{} {}".format(rows[0][0], rows[0][1])
    cursor.execute("""UPDATE applicants
                    SET full_name = %s, phone_number = %s 
                    WHERE first_name = %s AND last_name = (%s);""",
                   (full_name, new_phone_number, first_name, last_name))
    cursor.execute("""SELECT full_name, phone_number FROM applicants
                    WHERE first_name = (%s) AND last_name = (%s);""",
                   (first_name, last_name))
    updated_data = cursor.fetchall()
    return updated_data


def delete_applicant_by_email(email):
    """ Delete applicant based on email address """
    cursor.execute("""SELECT first_name, last_name FROM applicants
                    WHERE email LIKE (%s);""",
                   ("%" + email, ))
    deleted_user = cursor.fetchall()
    cursor.execute("""DELETE FROM applicants
                    WHERE email LIKE (%s);""",
                   ("%" + email, ))
    return deleted_user
