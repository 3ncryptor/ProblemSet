# 1822. Sign of the Product of an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-09-24T04:01:06.992Z |
| Platform | leetcode |

## Problem Statement

<p>Implement a function <code>signFunc(x)</code> that returns:</p>

<ul>
	<li><code>1</code> if <code>x</code> is positive.</li>
	<li><code>-1</code> if <code>x</code> is negative.</li>
	<li><code>0</code> if <code>x</code> is equal to <code>0</code>.</li>
</ul>

<p>You are given an integer array <code>nums</code>. Let <code>product</code> be the product of all values in the array <code>nums</code>.</p>

<p>Return <code>signFunc(product)</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [-1,-2,-3,-4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The product of all values in the array is 144, and signFunc(144) = 1
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [1,5,0,2,-3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The product of all values in the array is 0, and signFunc(0) = 0
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> nums = [-1,1,-1,1,-1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The product of all values in the array is -1, and signFunc(-1) = -1
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 1000</code>
- <code>-100 &lt;= nums[i] &lt;= 100</code>

## Solution

```py
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        prod = 1
        for i in nums:
            prod *= i

        def signFunc(x):
            return 1 if x > 0 else -1 if x < 0 else 0

        return signFunc(prod)
        
```

[View on LeetCode](https://leetcode.com/problems/sign-of-the-product-of-an-array/)
