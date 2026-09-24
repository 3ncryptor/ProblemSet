# 2974. Minimum Number Game

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Simulation-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.3 MB |
| Submission Date | 2026-09-24T09:16:40.780Z |
| Platform | leetcode |

## Problem Statement

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of <strong>even</strong> length and there is also an empty array <code>arr</code>. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:</p>

<ul>
	<li>Every round, first Alice will remove the <strong>minimum</strong> element from <code>nums</code>, and then Bob does the same.</li>
	<li>Now, first Bob will append the removed element in the array <code>arr</code>, and then Alice does the same.</li>
	<li>The game continues until <code>nums</code> becomes empty.</li>
</ul>

<p>Return <em>the resulting array </em><code>arr</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums = [5,4,2,3]
<strong>Output:</strong> [3,2,5,4]
<strong>Explanation:</strong> In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums = [2,5]
<strong>Output:</strong> [5,2]
<strong>Explanation:</strong> In round one, first Alice removes 2 and then Bob removes 5. Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= nums.length &lt;= 100</code>
- <code>1 &lt;= nums[i] &lt;= 100</code>
- <code>nums.length % 2 == 0</code>

## Solution

```py
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        while len(nums) > 0:
            # Alice's Turn
            alicePop = nums.pop(0)
            # Bob's Turn
            bobPop = nums.pop(0)
            # append to arr
            arr.extend([bobPop, alicePop])
        
        return arr
        
```

[View on LeetCode](https://leetcode.com/problems/minimum-number-game/)
