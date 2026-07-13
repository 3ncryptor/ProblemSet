# 4. Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Binary_Search-blue) ![Topic](https://img.shields.io/badge/Topic-Divide_and_Conquer-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.6 MB |
| Submission Date | 2026-07-13T08:10:56.851Z |
| Platform | leetcode |

## Problem Statement

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>nums1.length == m</code>
- <code>nums2.length == n</code>
- <code>0 &lt;= m &lt;= 1000</code>
- <code>0 &lt;= n &lt;= 1000</code>
- <code>1 &lt;= m + n &lt;= 2000</code>
- <code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code>

## Solution

```py
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 1:
            return nums1[length // 2]
        else:
            mid1, mid2 = nums1[length // 2 - 1], nums1[length // 2]
            return (mid1 + mid2) / 2.0
```

[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
