
// Self Join query on Employee table

SELECT employee_table.id AS Employee_Id, employee_table.employee_name AS Employee_Name, manager_table.employee_name AS Manager_Name
FROM Employees employee_table
JOIN Employees manager_table ON employee_table.manager_id = manager_table.employee_id 
where employee_table.id = 101 
