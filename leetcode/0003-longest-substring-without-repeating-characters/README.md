# 3. Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sliding_Window-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 7 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-07-15T16:58:53.692Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3. Note that <code>&quot;bca&quot;</code> and <code>&quot;cab&quot;</code> are also correct answers.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
- <code>s</code> consists of English letters, digits, symbols and spaces.

## Solution

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        sett=set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[left])
                left+=1
            w = (r - left) + 1
            longest= max(longest , w)

            sett.add(s[r])
        return longest
```

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
