import data_manager


def get_mentor_name_school_country():
    SQL = """ SELECT mentors.id, CONCAT(mentors.first_name, ' ', mentors.last_name) AS mentor_name, schools.name, schools.country
            FROM mentors
            INNER JOIN schools
            ON mentors.city = schools.city;"""
    result = data_manager.send_query(SQL)
    return result


def get_mentor_name_all_schools_country():
    SQL = """ SELECT mentors.id, CONCAT(mentors.first_name, ' ', mentors.last_name) AS mentor_name, schools.name, schools.country
            FROM mentors
            RIGHT JOIN schools
            ON mentors.city = schools.city;"""
    result = data_manager.send_query(SQL)
    return result


def get_mentors_by_country():
    SQL = """ SELECT schools.country, COUNT(mentors.id)
            FROM schools
            LEFT JOIN mentors
            ON schools.city = mentors.city
            GROUP BY schools.country;"""
    result = data_manager.send_query(SQL)
    return result


def get_school_contact_person():
    SQL = """SELECT schools.name, CONCAT(mentors.first_name, ' ', mentors.last_name) AS mentor_name
            FROM schools
            INNER JOIN mentors
            ON schools.contact_person = mentors.id
            ORDER BY schools.name;"""
    result = data_manager.send_query(SQL)
    return result
