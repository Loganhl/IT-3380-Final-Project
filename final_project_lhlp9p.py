import mysql.connector

def get_employee_per_country(mycursor):
    print("\nEmployers hired per country.\n--------------------------")
    country = input("Enter a country name to view the number of employees in each country, or 'ALL' to view all countries: ")
    if country.upper() == "ALL":
        print('\n')
        sql_query = "SELECT * FROM EmployeesPerCountry;"
    else:
        sql_query = f"SELECT * FROM EmployeesPerCountry WHERE country_name = '{country}';"

    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {country}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} employees")

def get_manager_per_department(mycursor):
    print("\nManagers per department.\n--------------------------")
    managerdept = input("Enter a department name to view the number of managers in each department, or 'ALL' to view all departments: ")
    if managerdept.upper() == "ALL":
        print('\n')
        sql_query = "SELECT department_name, COUNT(department_name) AS 'Number of Managers' FROM managers GROUP BY department_name ORDER BY COUNT(department_name) DESC;"
    else:
        sql_query = f"SELECT department_name, COUNT(department_name) AS 'Number of Managers' FROM managers WHERE department_name = '{managerdept}' GROUP BY department_name ORDER BY COUNT(department_name) DESC;"
    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {managerdept}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} managers")

def get_dependent_per_job(mycursor):
    print("\nDependent per job.\n--------------------------")
    depperjob = input("Enter a job title to view the number of dependents per job title, or 'ALL' to view all job titles: ")
    if depperjob.upper() == "ALL":
        sql_query = "SELECT * FROM DependentsByJobTitle;"
    else:
        sql_query = f"SELECT * FROM DependentsByJobTitle WHERE job_title = '{depperjob}' OR '{depperjob}' = 'ALL';"
    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {depperjob}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} dependents")

def get_hiring(mycursor):
    print("\nHiring data by year and department.\n--------------------------")
    year = input("Enter a year to view hiring data for, or 'ALL' to view all years: ")
    department = input("Enter a department name to view hiring data for, or 'ALL' to view all departments: ")
    if year.upper() == "ALL" and department.upper() == "ALL":
        sql_query = "SELECT * FROM DepartmentHiresByYear;"
    elif year.upper() == "ALL":
        sql_query = f"SELECT * FROM DepartmentHiresByYear WHERE department_name = '{department}';"
    elif department.upper() == "ALL":
        sql_query = f"SELECT * FROM DepartmentHiresByYear WHERE year = {year};"
    else:
        sql_query = f"SELECT * FROM DepartmentHiresByYear WHERE year = {year} AND department_name = '{department}';"
    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {year} and {department}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} - Employees Hired: {record[2]}")

def get_average_salary_per_job(mycursor):
    print("\nAverage salary per job.\n--------------------------")
    job_title = input("Enter a job title to view the average salary, or 'ALL' to view all job salaries: ")
    if job_title.upper() == "ALL":
        sql_query = "SELECT * FROM AvgSalaryByJobTitle;"
    else:
        sql_query = f"SELECT * FROM AvgSalaryByJobTitle WHERE job_title = '{job_title}';"

    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {job_title}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} average salary.")

def get_average_salary_per_department(mycursor):
    print("\nAverage salary per department.\n--------------------------")
    department = input("Enter a department name to view the average salary, or 'ALL' to view all department salaries: ")
    if department.upper() == "ALL":
        print('\n')
        sql_query = "SELECT department_name, AVG(salary) AS 'Average Salary' FROM employees e JOIN departments d ON e.department_id = d.department_id GROUP BY department_name ORDER BY AVG(salary) DESC;"
    else:
        sql_query = f"SELECT department_name, AVG(salary) AS 'Average Salary' FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE department_name = '{department}' GROUP BY department_name;"

    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No records found for {department}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} salary.")

def get_employee_dependents(mycursor):
    print("\nEmployee Dependents.\n--------------------------")
    employee_name = input("Enter an employee's first and last name to view their dependents, or enter 'ALL' to view all employees' dependents: ")

    if employee_name.upper() == "ALL":
        sql_query = "SELECT e.first_name, e.last_name, COUNT(d.dependent_id) AS 'Number of Dependents' FROM employees e LEFT JOIN dependents d ON d.employee_id = e.employee_id GROUP BY e.employee_id;"
    else:
        sql_query = f"SELECT e.first_name, e.last_name, COUNT(d.dependent_id) AS 'Number of Dependents' FROM employees e LEFT JOIN dependents d ON d.employee_id = e.employee_id WHERE e.first_name = '{employee_name.split()[0]}' AND e.last_name = '{employee_name.split()[1]}' GROUP BY e.employee_id;"

    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No dependents found for {employee_name}")
    else:
        for record in query_result:
            print(f"{record[0]} {record[1]}: {record[2]} dependents.")

def get_locations_per_region(mycursor):
    print("\nView Location Data by Region.\n--------------------------")
    user_choice = input("Enter 'ALL' to view number of locations for all regions, or enter the name of a specific region to view its number of locations: ")

    if user_choice.upper() == "ALL":
        sql_query = "SELECT r.region_name, COUNT(l.location_id) AS 'Number of Locations' FROM regions r JOIN countries c ON r.region_id = c.region_id LEFT JOIN locations l ON c.country_id = l.country_id GROUP BY r.region_name ORDER BY COUNT(l.location_id) DESC;"
    else:
        sql_query = f"SELECT r.region_name, COUNT(l.location_id) AS 'Number of Locations' FROM regions r JOIN countries c ON r.region_id = c.region_id LEFT JOIN locations l ON c.country_id = l.country_id WHERE r.region_name = '{user_choice}' GROUP BY r.region_name;"

    mycursor.execute(sql_query)

    query_result = mycursor.fetchall()

    if len(query_result) == 0:
        print(f"No locations found for {user_choice}")
    else:
        for record in query_result:
            print(f"{record[0]}: {record[1]} locations.")

def add_dependent(mycursor):
    print("\nAdd Dependent.\n--------------------------")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    relationship = input("Enter dependent's relationship: ")
    employee_id = input("Enter the ID: ")

    mycursor.execute(f"SELECT employee_id FROM employees WHERE employee_id = {employee_id}")
    employee_exists = mycursor.fetchone()

    if not employee_exists:
        print(f"Error: Employee with ID {employee_id} does not exist.")
        return

    insert_query = f"INSERT INTO dependents (first_name, last_name, relationship, employee_id) VALUES ('{first_name}', '{last_name}', '{relationship}', {employee_id})"
    mycursor.execute(insert_query)
    mycursor.execute("COMMIT")

    print(f"{first_name} {last_name} has been added as a dependent to employee with ID {employee_id}.")

def add_job(mycursor):
    print("\nAdd Job.\n--------------------------")

    job_title = input("Enter job title: ")

    min_salary = int(input("Enter minimum salary: "))
    max_salary = int(input("Enter maximum salary: "))

    if min_salary > max_salary:
        print("Error: Minimum salary cannot be greater than maximum salary.")
        return

    insert_query = f"INSERT INTO jobs (job_title, min_salary, max_salary) VALUES ('{job_title}', {min_salary}, {max_salary})"
    mycursor.execute(insert_query)
    mycursor.execute("COMMIT")

    print(f"{job_title} has been added as a job with a minimum salary of {min_salary} and a maximum salary of {max_salary}.")

def delete_employee(mycursor):
    print("\nDelete Employee.\n--------------------------")
    emp_id = input("Enter the employee's ID: ")

    query = f"SELECT * FROM employees WHERE employee_id = {emp_id}"
    mycursor.execute(query)
    result = mycursor.fetchone()
    if not result:
        print(f"Employee with ID {emp_id} does not exist.")
        return
    
    delete_query = f"DELETE FROM employees WHERE employee_id = {emp_id}"
    mycursor.execute(delete_query)
    mycursor.execute("COMMIT")

    print(f"Employee with ID {emp_id} has been deleted.")


def delete_dependent(mycursor):
    print("\nDelete Dependent.\n--------------------------")
    dependent_id = int(input("Enter dependent's ID: "))

    query = f"SELECT * FROM dependents WHERE dependent_id = {dependent_id}"
    mycursor.execute(query)
    dependent = mycursor.fetchone()

    if not dependent:
        print(f"Error: Dependent with ID {dependent_id} does not exist.")
        return

    delete_query = f"DELETE FROM dependents WHERE dependent_id = {dependent_id}"
    mycursor.execute(delete_query)
    mycursor.execute("COMMIT")

    print(f"Dependent with ID {dependent_id} has been deleted.")

def first_name(mycursor):
    print("\nUpdate Employee First Name.\n--------------------------")
    emp_id = input("Enter employee ID: ")
    first_name = input("Enter new first name: ")
    check_query = f"SELECT * FROM employees WHERE employee_id = '{emp_id}'"
    mycursor.execute(check_query)
    result = mycursor.fetchone()

    if not result:
        print(f"Error: Employee with ID {emp_id} does not exist.")
        return

    update_query = f"UPDATE employees SET first_name = '{first_name}' WHERE employee_id = '{emp_id}'"
    mycursor.execute(update_query)
    mycursor.execute("COMMIT")

    print(f"First name of employee with ID {emp_id} has been updated to {first_name}.")


def last_name(mycursor):
    print("\nUpdate Employee First Name.\n--------------------------")
    emp_id = input("Enter employee ID: ")
    last_name = input("Enter new last name: ")
    check_query = f"SELECT * FROM employees WHERE employee_id = '{emp_id}'"
    mycursor.execute(check_query)
    result = mycursor.fetchone()

    if not result:
        print(f"Error: Employee with ID {emp_id} does not exist.")
        return

    update_query = f"UPDATE employees SET last_name = '{last_name}' WHERE employee_id = '{emp_id}'"
    mycursor.execute(update_query)
    mycursor.execute("COMMIT")

    print(f"Last name of employee with ID {emp_id} has been updated to {last_name}.")

def update_min_salary(mycursor):
    print("\nUpdate Job Minimum Salary.\n--------------------------")
    job_id = input("Enter job ID: ")
    min_salary = input("Enter new minimum salary: ")

    check_query = f"SELECT job_id FROM jobs WHERE job_id = {job_id}"
    mycursor.execute(check_query)
    result = mycursor.fetchone()
    if not result:
        print(f"Error: Job with ID {job_id} does not exist.")
        return

    update_query = f"UPDATE jobs SET min_salary = {min_salary} WHERE job_id = {job_id}"
    mycursor.execute(update_query)
    mycursor.execute("COMMIT")

    print(f"Minimum salary for job with ID {job_id} has been updated to {min_salary}.")

def update_max_salary(mycursor):
    print("\nUpdate Job Maximum Salary.\n--------------------------")
    job_id = input("Enter job ID: ")
    max_salary = input("Enter new maximum salary: ")

    check_query = f"SELECT job_id FROM jobs WHERE job_id = {job_id}"
    mycursor.execute(check_query)
    result = mycursor.fetchone()
    if not result:
        print(f"Error: Job with ID {job_id} does not exist.")
        return

    update_query = f"UPDATE jobs SET max_salary = {max_salary} WHERE job_id = {job_id}"
    mycursor.execute(update_query)
    mycursor.execute("COMMIT")

    print(f"Maxmimum salary for job with ID {job_id} has been updated to {max_salary}.")






def print_menu():
    print("\nChoose an option\n-----------------------")
    print("\nVIEW DATA\n-----------------------")
    print("1. View employee count data per country.")
    print("2. View manager count by department.")
    print("3. View dependent data per job title.")
    print("4. View hiring data by year and department.")
    print("5. View average Salary data by job title.")
    print("6. View salary Salary data by department.")
    print("7. View dependent data by employee.")
    print("8. View location data by region.")

    print("\nADD DATA\n-----------------------")
    print("9. Add a dependent.")
    print("10. Add a job.")

    print("\nDELETE DATA\n-----------------------")
    print("11. Delete an employee.")
    print("12. Delete an dependent.")

    print("\nUPDATE DATA\n-----------------------")
    print("13. Update employee first name.")
    print("14. Update employee last name.")
    print("15. Update job minimum salary.")
    print("16. Update job maximum salary.")

    print("\nEXIT\n-----------------------")
    print("17. Exit Application\n")
    return

def get_user_choice():
    print_menu()
    while(True):
        try:
            the_choice = int(input("Enter Choice: "))
            if(the_choice < 1 or the_choice > 17):
                print(f"Invalid input: Enter a value between 1 and 17.\n")
                continue
            break
        except Exception as err:
            print(f"An error has occured: {err}\n")
            continue

    return the_choice

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        user_choice = get_user_choice()
        if(user_choice == 1):
            get_employee_per_country(mycursor)
        elif(user_choice == 2):
            get_manager_per_department(mycursor)
        elif(user_choice == 3):
            get_dependent_per_job(mycursor)
        elif(user_choice == 4):
            get_hiring(mycursor)
        elif(user_choice == 5):
            get_average_salary_per_job(mycursor)
        elif(user_choice == 6):
            get_average_salary_per_department(mycursor)
        elif(user_choice == 7):
            get_employee_dependents(mycursor)
        elif(user_choice == 8):
            get_locations_per_region(mycursor)
        elif(user_choice == 9):
            add_dependent(mycursor)
        elif(user_choice == 10):
            add_job(mycursor)
        elif(user_choice == 11):
            delete_employee(mycursor)
        elif(user_choice == 12):
            delete_dependent(mycursor)
        elif(user_choice == 13):
            first_name(mycursor)
        elif(user_choice == 14):
            last_name(mycursor)
        elif(user_choice == 15):
            update_min_salary(mycursor)
        elif(user_choice == 16):
            update_max_salary(mycursor)
        elif(user_choice == 17):
            print("Bye Bye!!!")
            break



main()