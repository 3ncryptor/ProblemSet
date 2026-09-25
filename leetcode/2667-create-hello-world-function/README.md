# 2667. Create Hello World Function

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Language](https://img.shields.io/badge/Language-javascript-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 37 ms |
| Memory | 52.7 MB |
| Submission Date | 2026-09-25T19:12:19.835Z |
| Platform | leetcode |

## Problem Statement

Write a function&nbsp;<code>createHelloWorld</code>.&nbsp;It should return a new function that always returns&nbsp;<code>&quot;Hello World&quot;</code>.
<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> args = []
<strong>Output:</strong> &quot;Hello World&quot;
<strong>Explanation:</strong>
const f = createHelloWorld();
f(); // &quot;Hello World&quot;

The function returned by createHelloWorld should always return &quot;Hello World&quot;.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> args = [{},null,42]
<strong>Output:</strong> &quot;Hello World&quot;
<strong>Explanation:</strong>
const f = createHelloWorld();
f({}, null, 42); // &quot;Hello World&quot;

Any arguments could be passed to the function but it should still always return &quot;Hello World&quot;.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= args.length &lt;= 10</code>

## Solution

```js
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

//  const createHelloWord = function(){
    // return "Hello World"
//  }
```

[View on LeetCode](https://leetcode.com/problems/create-hello-world-function/)
