# 2114. Maximum Number of Words Found in Sentences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19.2 MB |
| Submission Date | 2026-09-25T01:00:57.505Z |
| Platform | leetcode |

## Problem Statement

<p>A <strong>sentence</strong> is a list of <strong>words</strong> that are separated by a single space&nbsp;with no leading or trailing spaces.</p>

<p>You are given an array of strings <code>sentences</code>, where each <code>sentences[i]</code> represents a single <strong>sentence</strong>.</p>

<p>Return <em>the <strong>maximum number of words</strong> that appear in a single sentence</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> sentences = [&quot;alice and bob love leetcode&quot;, &quot;i think so too&quot;, <u>&quot;this is great thanks very much&quot;</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
- The first sentence, &quot;alice and bob love leetcode&quot;, has 5 words in total.
- The second sentence, &quot;i think so too&quot;, has 4 words in total.
- The third sentence, &quot;this is great thanks very much&quot;, has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> sentences = [&quot;please wait&quot;, <u>&quot;continue to fight&quot;</u>, <u>&quot;continue to win&quot;</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= sentences.length &lt;= 100</code>
- <code>1 &lt;= sentences[i].length &lt;= 100</code>
- <code>sentences[i]</code> consists only of lowercase English letters and <code>&#39; &#39;</code> only.
- <code>sentences[i]</code> does not have leading or trailing spaces.
- All the words in <code>sentences[i]</code> are separated by a single space.

## Solution

```py
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxx = 0

        for i in sentences:
            words = i.split()
            maxx = max(maxx, len(words))

        return maxx

        
```

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)
