# Busy Waiting

**Severity**: Medium

## Description
Repeatedly polling or checking a condition in a loop without yielding CPU time, wasting CPU cycles. Instead of waiting efficiently (via callbacks, events, or blocking calls), busy-waiting continuously checks a condition in a tight loop, consuming 100% of a CPU core unnecessarily.

## Detection
- `while` loops that check a condition without sleep
- Polling loops with no `sleep()`, `await`, or blocking call
- High CPU usage from code that appears to be idle
- `time.sleep()` calls with very short intervals (< 10ms)
- Spinning until a condition becomes true
- Checking queue/buffer in a loop without blocking

## Remediation
Use proper synchronization mechanisms: callbacks, event handlers, condition variables, channels, async/await, or blocking queue operations.

**Before:**
```
// Bad: Busy waiting - wastes 100% CPU
function waitForData():
    while dataAvailable == false:
        pass  // CPU-intensive spinning!
    return getData()

function checkForUpdates():
    while true:
        if newDataFlag:  // Polling without sleep
            processData()
        // No sleep = 100% CPU usage
```

**After:**
```
// Good: Event-based
function waitForData():
    event = createEvent()
    event.wait()  // Blocks efficiently until signaled
    return getData()

// Or with async/await
async function waitForData():
    await dataReady.wait()
    return getData()

// Or with Queue (blocking)
function checkForUpdates():
    queue = createQueue()
    while true:
        data = queue.getWithTimeout(timeout: 1000)  // Blocks efficiently
        processData(data)

// Or with callback
function onDataAvailable(callback):
    dataSource.subscribe(callback)
    // callback invoked when data arrives, no polling
```
