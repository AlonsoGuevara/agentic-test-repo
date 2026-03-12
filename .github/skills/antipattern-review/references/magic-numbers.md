# Magic Numbers

**Severity**: Medium

## Description
Hard-coded numerical constants in code without explanation or named symbolic reference. Magic numbers reduce code readability, increase maintenance burden, and make it difficult to understand the significance of specific values. They become particularly problematic when the same constant appears multiple times across the codebase.

## Detection
- Numerical literals in code (e.g., `if (count > 5)`, `sleep(3000)`, `buffer = new Array(256)`)
- Repeated identical constants across multiple locations
- Numbers used in conditionals, array sizes, timeouts, or calculations without context
- Common culprits: `0`, `1`, `-1`, `256`, `1000`, `3600`, `8080`

## Remediation
Replace magic numbers with named constants or variables that explain their purpose.

**Before:**
```
function processData(items):
    if length(items) > 100:  # What's special about 100?
        timeout = 3000       # Milliseconds? Seconds?
        batchSize = 50
        for i = 0 to length(items) step batchSize:
            # ...
```

**After:**
```
const MAX_ITEMS_THRESHOLD = 100
const PROCESSING_TIMEOUT_MS = 3000
const BATCH_SIZE = 50

function processData(items):
    if length(items) > MAX_ITEMS_THRESHOLD:
        timeout = PROCESSING_TIMEOUT_MS
        for i = 0 to length(items) step BATCH_SIZE:
            # ...
```

Or use an enum for domain-specific constants:
```
enum HttpStatus:
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500
```
