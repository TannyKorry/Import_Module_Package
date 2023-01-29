import datetime
import application.db.people as people
import application.salary as salary


if __name__ == '__main__':
    print(datetime.datetime.now())
    people.get_employees()
    salary.calculate_salary()


