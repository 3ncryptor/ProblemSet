# 3232. Find if Digit Game Can Be Won

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Math-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-09-24T04:20:25.000Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array of <strong>positive</strong> integers <code>nums</code>.</p>

<p>Alice and Bob are playing a game. In the game, Alice can choose <strong>either</strong> all single-digit numbers or all double-digit numbers from <code>nums</code>, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is <strong>strictly greater</strong> than the sum of Bob&#39;s numbers.</p>

<p>Return <code>true</code> if Alice can win this game, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>Alice cannot win by choosing either single-digit or double-digit numbers.</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5,14]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Alice can win by choosing single-digit numbers which have a sum equal to 15.</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,5,5,25]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Alice can win by choosing double-digit numbers which have a sum equal to 25.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= nums.length &lt;= 100</code>
- <code>1 &lt;= nums[i] &lt;= 99</code>

## Solution

```py
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleDigitSum = 0
        doubleDigitSum = 0
        for i in nums:
            if i >= 10:
                doubleDigitSum += i
            else:
                singleDigitSum += i

        return True if singleDigitSum > doubleDigitSum else True if singleDigitSum < doubleDigitSum else False
    
```

[View on LeetCode](https://leetcode.com/problems/find-if-digit-game-can-be-won/)
