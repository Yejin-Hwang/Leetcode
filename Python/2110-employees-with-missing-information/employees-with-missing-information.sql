-- Write your PostgreSQL query statement below
with cte as (select COALESCE(e.employee_id, s.employee_id) AS employee_id, e.name, s.salary
from employees e full join salaries s on e.employee_id = s.employee_id) 

select employee_id 
from cte where name is null or salary is null order by employee_id asc; 