-- Runtime: 2809 ms
-- Memory: 0B

Select (
    Select Distinct salary
    from Employee
    Order by salary DESC
    Limit 1 offset 1
) as SecondHighestSalary