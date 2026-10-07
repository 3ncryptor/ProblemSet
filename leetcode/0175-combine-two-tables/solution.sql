-- Runtime: 455 ms
-- Memory: 0B

# Write your MySQL query statement below
Select firstName, lastName, city, state
From Person p
LEFT JOIN Address a
ON p.personId = a.personId
