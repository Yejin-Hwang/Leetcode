-- Write your PostgreSQL query statement below
with cte as (select p.project_id, p.employee_id, e.experience_years from project p join employee e on p.employee_id = e.employee_id
)

select project_id, round(avg(experience_years)::numeric,2) as average_years 
from cte 
group by project_id