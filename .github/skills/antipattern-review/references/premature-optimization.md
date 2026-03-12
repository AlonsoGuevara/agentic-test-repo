# Premature Optimization

**Severity**: Medium

## Description
Optimizing code for performance before identifying actual bottlenecks. This wastes time, introduces unnecessary complexity, makes code harder to understand and maintain, and often doesn't improve real-world performance. Remember: "premature optimization is the root of all evil."

## Detection
- Complex algorithms used where simple ones would suffice
- Micro-optimizations (e.g., avoiding function calls, manual loop unrolling)
- Complex caching strategies without evidence of cache misses
- Low-level optimizations at the expense of readability
- Optimization comments explaining why something was written unclearly
- No profiling or metrics justifying the optimization
- Complex data structures for theoretical performance gains

## Remediation
Write clear, simple code first. Profile the actual application to identify real bottlenecks. Optimize only where measurements show it matters. Keep code readable; clarity often outweighs small performance gains.

**Before:**
```
// Premature optimization - complex, hard to read, probably not the bottleneck
function findUser(users, userId):
    // Manually optimizing array search without profiling
    left = 0
    right = length(users) - 1
    while left <= right:
        mid = (left + right) / 2
        if users[mid].id == userId:
            return users[mid]
        else if users[mid].id < userId:
            left = mid + 1
        else:
            right = mid - 1
    return null

function sumItems(items):
    // Avoiding function calls for minor speed - but probably not a bottleneck
    total = 0
    for each item in items:
        total += item.price * item.qty  // Avoiding method access
    return total

function cacheEverything():
    // Cache every computation without knowing if it helps
    cache = {}
    // hundreds of cache decay logic...
```

**After:**
```
// Simple, clear, readable - optimize only if profiling shows it's needed
function findUser(users, userId):
    // Simple, readable - if lookup is slow, use database indexing instead
    for each user in users:
        if user.id == userId:
            return user
    return null

function sumItems(items):
    // Clear intent, readable
    total = 0
    for each item in items:
        total += item.calculateLineTotal()
    return total

// Use built-in data structures strategically if needed
function findUserFast(usersByIdMap, userId):
    // Only if profiling shows dict lookup is faster (usually is)
    return usersByIdMap.get(userId)

// Cache only where it's measured to matter
function expensiveComputation(x):
    // Cache only after profiling shows this function is the bottleneck
    return complexAlgorithm(x)
```

**Best Practice:**
1. Write clear code using sensible algorithms
2. Profile the application to find actual bottlenecks
3. Optimize only the functions where time is spent
4. Measure improvement before and after
5. Trade clarity for performance only when gains are significant
