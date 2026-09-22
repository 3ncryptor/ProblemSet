# 258. Add Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Topic](https://img.shields.io/badge/Topic-Simulation-blue) ![Topic](https://img.shields.io/badge/Topic-Number_Theory-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-09-22T11:38:41.259Z |
| Platform | leetcode |

## Problem Statement

<p>Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code>

## Solution

```py
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num

        summ = 0

        while num > 0:
            digit = num % 10
            summ += digit 
            num = num // 10

        return self.addDigits(summ)

```

[View on LeetCode](https://leetcode.com/problems/add-digits/)
