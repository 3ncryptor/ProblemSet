# 577. Employee Bonus

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Database-blue) ![Language](https://img.shields.io/badge/Language-mysql-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1186 ms |
| Memory | 0B |
| Submission Date | 2026-10-16T17:33:24.535Z |
| Platform | leetcode |

## Problem Statement

<p>Table: <code>Employee</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
</pre>

<p>&nbsp;</p>

<p>Table: <code>Bonus</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
</pre>

<p>&nbsp;</p>

<p>Write a solution to report the name and bonus amount of each employee who satisfies either of the following:</p>

<ul>
	<li>The employee has a bonus <strong>less than</strong> <code>1000</code>.</li>
	<li>The employee did not get any bonus.</li>
</ul>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
<strong>Output:</strong> 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
</pre>
```

## Constraints

_No constraints provided._

## Solution

```sql
# Write your MySQL query statement below
select e.name, b.bonus
from Employee e
left join bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null
```

[View on LeetCode](https://leetcode.com/problems/employee-bonus/)
