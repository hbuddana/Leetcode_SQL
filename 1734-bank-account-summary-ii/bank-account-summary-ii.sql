# Write your MySQL query statement below
select U.name, sum(T.amount) as balance 
from Users U
join Transactions T on U.account = T.account
group by U.name
having sum(T.amount) > 10000