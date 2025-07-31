-- Write your PostgreSQL query statement below
select s.product_id, t.first_year, s.quantity, s.price
from sales s join( 
    select product_id, min(year) as first_year  
    from sales 
    group by product_id 
)t on t.product_id = s.product_id and s.year = t.first_year;