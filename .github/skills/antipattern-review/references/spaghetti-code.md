# Spaghetti Code

**Severity**: High

## Description
Code with a complex, tangled flow of control that is difficult to understand and follow. Spaghetti code typically features excessive use of `goto`, deep nesting, intertwined logic, and unclear flow. Modern languages avoid `goto`, but similar problems arise from deeply nested conditions, loops, and callbacks (callback hell).

## Detection
- Functions/methods with excessive nesting (>3 levels)
- Deep callback chains or promise chains without proper abstraction
- Mixed concerns in single functions (multiple responsibilities)
- Convoluted control flow with multiple exit points
- Comments needed to explain what code does (vs. why)
- High cyclomatic complexity (many branching paths)
- Unclear variable names that don't indicate their purpose

## Remediation
Break complex logic into smaller, focused functions. Use clear variable names. Flatten callback chains with async/await or promises. Extract sub-routines.

**Before:**
```
function process(data):
    result = []
    for each item in data:
        if item.type == "A":
            if item.value > 0:
                for each sub in item.children:
                    if sub.valid:
                        if sub.count < 10:
                            result.add(sub.transform())
        else if item.type == "B":
            if item.priority > 5:
                result.add(item)
    return result
```

**After:**
```
function isValidItem(item):
    return item.type == "A" && item.value > 0

function processChildren(item):
    processed = []
    for each child in item.children:
        if child.valid && child.count < 10:
            processed.add(child.transform())
    return processed

function processPriorityItem(item):
    return item.type == "B" && item.priority > 5

function process(data):
    result = []
    for each item in data:
        if isValidItem(item):
            result.addAll(processChildren(item))
        else if processPriorityItem(item):
            result.add(item)
    return result
```
