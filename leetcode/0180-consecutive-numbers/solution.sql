-- Runtime: 661 ms
-- Memory: 0B

# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs 
) t
where num = prev_num
and num = prev_prev_num