# 177. Nth Highest Salary

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Database-blue) ![Language](https://img.shields.io/badge/Language-mysql-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 410 ms |
| Memory | 0B |
| Submission Date | 2026-10-10T11:42:50.885Z |
| Platform | leetcode |

## Problem Statement

<p>Table: <code>Employee</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
</pre>

<p>&nbsp;</p>

<p>Write a solution to find the <code>n<sup>th</sup></code> highest <strong>distinct</strong> salary from the <code>Employee</code> table. If there are less than <code>n</code> distinct salaries, return&nbsp;<code>null</code>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
<strong>Output:</strong> 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
<strong>Output:</strong> 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
</pre>
```

## Constraints

_No constraints provided._

## Solution

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary
      from Employee
      order by salary DESC
      limit 1 offset N

  );
END
```

[View on LeetCode](https://leetcode.com/problems/nth-highest-salary/)
