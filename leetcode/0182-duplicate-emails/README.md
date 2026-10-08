# 182. Duplicate Emails

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Database-blue) ![Language](https://img.shields.io/badge/Language-mysql-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 409 ms |
| Memory | 0B |
| Submission Date | 2026-10-08T08:51:44.318Z |
| Platform | leetcode |

## Problem Statement

<p>Table: <code>Person</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
</pre>

<p>&nbsp;</p>

<p>Write a solution to report all the duplicate emails. Note that it&#39;s guaranteed that the email&nbsp;field is not NULL.</p>

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
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
<strong>Output:</strong> 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
<strong>Explanation:</strong> a@b.com is repeated two times.
</pre>
```

## Constraints

_No constraints provided._

## Solution

```sql
select email as Email
from Person
group by email
having count(*) > 1
```

[View on LeetCode](https://leetcode.com/problems/duplicate-emails/)
