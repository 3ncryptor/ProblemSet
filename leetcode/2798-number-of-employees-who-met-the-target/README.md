# 2798. Number of Employees Who Met the Target

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-09-23T04:16:45.829Z |
| Platform | leetcode |

## Problem Statement

<p>There are <code>n</code> employees in a company, numbered from <code>0</code> to <code>n - 1</code>. Each employee <code>i</code> has worked for <code>hours[i]</code> hours in the company.</p>

<p>The company requires each employee to work for <strong>at least</strong> <code>target</code> hours.</p>

<p>You are given a <strong>0-indexed</strong> array of non-negative integers <code>hours</code> of length <code>n</code> and a non-negative integer <code>target</code>.</p>

<p>Return <em>the integer denoting the number of employees who worked at least</em> <code>target</code> <em>hours</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> hours = [0,1,2,3,4], target = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The company wants each employee to work for at least 2 hours.
- Employee 0 worked for 0 hours and didn&#39;t meet the target.
- Employee 1 worked for 1 hours and didn&#39;t meet the target.
- Employee 2 worked for 2 hours and met the target.
- Employee 3 worked for 3 hours and met the target.
- Employee 4 worked for 4 hours and met the target.
There are 3 employees who met the target.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> hours = [5,1,4,2,2], target = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> The company wants each employee to work for at least 6 hours.
There are 0 employees who met the target.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= n == hours.length &lt;= 50</code>
- <code>0 &lt;=&nbsp;hours[i], target &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if target <= i:
                count += 1

        return count
```

[View on LeetCode](https://leetcode.com/problems/number-of-employees-who-met-the-target/)
