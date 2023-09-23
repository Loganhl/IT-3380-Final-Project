--1.  Write a query to create a view named “EmployeesPerCountry” that shows the country_name and the number of employees 
--from that country in a column called “Number of Employees”. Display your results in descending order of bunber of employees
CREATE VIEW EmployeesPerCountry AS
SELECT c.country_name, COUNT(e.employee_id) As "Number of Employees"
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN locations l ON l.location_id = d.location_id
JOIN countries c ON c.country_id = l.country_id
GROUP BY c.country_id
ORDER BY COUNT(e.employee_id) DESC;

-- Query the EmployeesPerCountry to show the number of employees from the United Kingdom .
SELECT * FROM EmployeesPerCountry
WHERE country_name = "United Kingdom";

--2. Write a query to create a view named “managers” to display all the managers and the number of employees they manage in a column called "Number of Reports". 
--Include the manager’s name (first, last), email, job title, and department name, and the number of emplyees they manage. 
CREATE VIEW managers AS
SELECT e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN jobs j ON e.job_id = j.job_id
WHERE e.employee_id IN (SELECT manager_id from employees);


--Query the managers view to show the number of managers in each department.
SELECT department_name, COUNT(department_name) AS "Number of Managers"
FROM managers
GROUP BY department_name
ORDER BY COUNT(department_name) DESC;


--3. Write a query to create a view named DependentsByJobTitle to get a count of how many dependents there are for each job title. 
-- Show job titles even if they do not have dependents. Place the number of dependents in a column called "Number of Dependents".
CREATE VIEW DependentsByJobTitle AS
SELECT j.job_title, COUNT(d.dependent_id) AS "Number of Dependents"
FROM jobs j
JOIN employees e ON e.job_id = j.job_id
LEFT JOIN dependents d ON d.employee_id = e.employee_id
GROUP BY j.job_title
ORDER BY COUNT(d.dependent_id) DESC;


--Query the DependentsByJobTitle view to show the job titles(s) with the largest number of dependents. 
--This should show the job title and the number of dependents.
SELECT *
FROM DependentsByJobTitle
WHERE `Number of Dependents` = (SELECT MAX(`Number of Dependents`) FROM DependentsByJobTitle);

--4. Write a query to create a view named DepartmentHiresByYear that calculates the number of employees hired each year in each department, Order results by department name. 
-- Remember the SQL $year function, and you will have to group by two columns.
CREATE VIEW DepartmentHiresByYear AS  
SELECT YEAR(e.hire_date) AS "year", d.department_name, COUNT(e.employee_id) AS "Employees Hired"
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
GROUP BY YEAR(e.hire_date), d.department_name
ORDER BY d.department_name;

-- Query the DepartmentHiresByYear view to show department hires in 1998.
SELECT *
FROM DepartmentHiresByYear
WHERE year = 1998;

--5. Write a query to create a view named “AvgSalaryByJobTitle” to calculate the average salary for each job title. 
-- Display the job title, average salary in a column named "Average salary", and number of employees with that title in a column called "Number of Employees"
-- display results in descending order by average salary
CREATE VIEW AvgSalaryByJobTitle AS
SELECT j.job_title, AVG(e.salary) AS "Average Salary", COUNT(j.job_title) AS "Number of Employees"
FROM jobs j
JOIN employees e ON j.job_id = e.job_id
GROUP BY j.job_title
ORDER BY AVG(e.salary) DESC;

-- Query the AvgSalaryByJobTitle view to show the average salary for the Programmers.
SELECT * FROM AvgSalaryByJobTitle WHERE job_title = "Programmer";


--6. Write a query to create a view named “AvgSalaryByDepartment” to calculate average salaries for each department. 
-- Display the department name, average salary in a column named "Average salary", and number of employees with that title in a column called "Number of Employees"
CREATE VIEW AvgSalaryByDepartment AS
SELECT d.department_name, AVG(e.salary) AS "Average Salary", COUNT(d.department_name) AS "Number of Employees"
FROM departments d, employees e
WHERE e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY AVG(e.salary) DESC;

--Query the AvgSalaryByDepartment view to show the department name and average salary for the department with the lowest average salary.
SELECT *
FROM AvgSalaryByDepartment
WHERE `Average Salary` IN (SELECT MIN(`Average Salary`) FROM AvgSalaryByDepartment);

--OR
SELECT *
FROM AvgSalaryByDepartment
ORDER BY `Average Salary`
LIMIT 1;

--7. Write a query to create a view named “EmployeeDependents” that calculates the number of dependents each employees has. 
--This query should show employees even if they have 0 dependents. 
--Display the employee name (first, last), email, phone number, and number of dependents. Hint: left or right join. 
CREATE VIEW EmployeeDependents AS
SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.dependent_id) AS "Number of Dependents"
FROM employees e
LEFT JOIN dependents d ON d.employee_id = e.employee_id
GROUP BY e.employee_id;


--Query the EmployeeDependents view to show employees with no children". 
--Show employee name (first, last), email, phone number, and number of dependents.
SELECT * FROM EmployeeDependents WHERE `Number of Dependents` = 0;

--8. Write a query to create a view named “CountryLocation” that calculates the number of locations in each region. 
--This query should show regions even if they have 0 locations. Display the region name and number of locations in descending order by number of locations. 
CREATE VIEW LocationByRegion AS
SELECT r.region_name, COUNT(l.location_id) AS "Number of Locations"
FROM regions r
JOIN countries c ON r.region_id = c.region_id
LEFT JOIN locations l ON c.country_id = l.country_id
GROUP BY r.region_name
ORDER BY COUNT(l.location_id) DESC;

--Query the LocationByRegion view to show regions with no locations". Show region name and number of locations.
SELECT * FROM LocationByRegion WHERE `Number of Locations` = 0;


