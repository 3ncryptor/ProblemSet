# 39. Combination Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Backtracking-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 7 ms |
| Memory | 19.5 MB |
| Submission Date | 2026-07-29T17:57:10.970Z |
| Platform | leetcode |

## Problem Statement

<p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the <span data-keyword="frequency-array">frequency</span> of at least one of the chosen numbers is different.</p>

<p>The test cases are generated such that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= candidates.length &lt;= 30</code>
- <code>2 &lt;= candidates[i] &lt;= 40</code>
- All elements of <code>candidates</code> are <strong>distinct</strong>.
- <code>1 &lt;= target &lt;= 40</code>

## Solution

```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        def helper(ind, target):
            if ind == len(candidates):
                if target == 0:
                    res.append(sol[:])
                return

            # not pick
            helper(ind + 1, target)

            # pick
            if candidates[ind] <= target:
                sol.append(candidates[ind])
                helper(ind, target - candidates[ind])
                sol.pop()

            return res

        result = helper(0, target)
        return result
```

[View on LeetCode](https://leetcode.com/problems/combination-sum/)
