# 1550. Three Consecutive Odds

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 4 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-09-23T04:48:55.669Z |
| Platform | leetcode |

## Problem Statement

Given an integer array <code>arr</code>, return <code>true</code>&nbsp;if there are three consecutive odd numbers in the array. Otherwise, return&nbsp;<code>false</code>.
<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> arr = [2,6,4,1]
<strong>Output:</strong> false
<b>Explanation:</b> There are no three consecutive odds.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> arr = [1,2,34,3,4,5,7,23,12]
<strong>Output:</strong> true
<b>Explanation:</b> [5,7,23] are three consecutive odds.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= arr.length &lt;= 1000</code>
- <code>1 &lt;= arr[i] &lt;= 1000</code>

## Solution

```py
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # oddNumber
        def oddNumber(x):
            if x % 2 != 0:
                return True
        for i in range(0, len(arr)-2):
            if oddNumber(arr[i]) and oddNumber(arr[i+1]) and oddNumber(arr[i+2]):
                return True

        return False

        
```

[View on LeetCode](https://leetcode.com/problems/three-consecutive-odds/)
