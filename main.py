import datetime
import db.people
import application.salary


if __name__ == '__main__':
    print(datetime.datetime.now())
    db.people.get_employees()
    application.salary.calculate_salary()


