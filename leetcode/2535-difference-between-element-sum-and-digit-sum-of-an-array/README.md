# 2535. Difference Between Element Sum and Digit Sum of an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 11 ms |
| Memory | 19.5 MB |
| Submission Date | 2026-09-24T09:07:38.489Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a positive integer array <code>nums</code>.</p>

<ul>
	<li>The <strong>element sum</strong> is the sum of all the elements in <code>nums</code>.</li>
	<li>The <strong>digit sum</strong> is the sum of all the digits (not necessarily distinct) that appear in <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>absolute</strong> difference between the <strong>element sum</strong> and <strong>digit sum</strong> of </em><code>nums</code>.</p>

<p><strong>Note</strong> that the absolute difference between two integers <code>x</code> and <code>y</code> is defined as <code>|x - y|</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,15,6,3]
<strong>Output:</strong> 9
<strong>Explanation:</strong> 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 2000</code>
- <code>1 &lt;= nums[i] &lt;= 2000</code>

## Solution

```py
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        normalSum = 0
        for i in nums:
            normalSum += i

        digitWiseSum = 0
        for i in nums:
            while i > 0:
                digit = i % 10
                i //= 10
                digitWiseSum += digit

        return abs(normalSum - digitWiseSum)
            
        
```

[View on LeetCode](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/)
