# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) AS count_no_trans
from Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
where t.transaction_id IS NULL
group by v.customer_id; 