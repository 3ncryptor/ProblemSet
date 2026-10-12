-- Runtime: 862 ms
-- Memory: 0B

delete p1
from Person p1
JOIN person p2
on p1.email = p2.email
and p1.id > p2.id