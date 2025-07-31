-- Write your PostgreSQL query statement below

with n as (select s.student_id, s.student_name, t.subject_name from subjects t cross join students s)

select n.student_id, n.student_name, n.subject_name, coalesce(count(e.subject_name),0) as attended_exams
from n left join examinations e on n.student_id = e.student_id and n.subject_name = e.subject_name
group by n.student_id, n.student_name, n.subject_name 
order by n.student_id, n.subject_name;
