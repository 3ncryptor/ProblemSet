# 180. Consecutive Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Database-blue) ![Language](https://img.shields.io/badge/Language-mysql-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 661 ms |
| Memory | 0B |
| Submission Date | 2026-10-08T08:46:28.252Z |
| Platform | leetcode |

## Problem Statement

<p>Table: <code>Logs</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
</pre>

<p>&nbsp;</p>

<p>Find all numbers that appear at least three times consecutively.</p>

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
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
<strong>Output:</strong> 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
<strong>Explanation:</strong> 1 is the only number that appears consecutively for at least three times.
</pre>
```

## Constraints

_No constraints provided._

## Solution

```sql
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
```

[View on LeetCode](https://leetcode.com/problems/consecutive-numbers/)
