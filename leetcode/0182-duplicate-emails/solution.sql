-- Runtime: 409 ms
-- Memory: 0B

select email as Email
from Person
group by email
having count(*) > 1