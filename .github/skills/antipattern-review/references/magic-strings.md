# Magic Strings

**Severity**: Medium

## Description
Hard-coded string literals in code that have special meaning but lack context or centralized definition. Magic strings are similar to magic numbers but using string constants. They create maintenance issues when the same string must be changed across multiple locations and make code intent unclear.

## Detection
- String literals repeated multiple times in code (e.g., `if (status === "PENDING")`)
- Strings used as keys, identifiers, or status values without constants
- API calls with hard-coded paths or identifiers
- Configuration values embedded in source code
- Event names or message keys as string literals

## Remediation
Extract magic strings to named constants, enums, or configuration files.

**Before:**
```
function handleOrder(order):
    if order.status == "pending":
        sendNotification(order.customerId, "Your order is being processed")
        updateDatabase("orders", order.id, status: "processing")
    if order.type == "express":
        priority = "high"
```

**After:**
```
const ORDER_STATUS = {
    PENDING: "pending",
    PROCESSING: "processing",
    COMPLETED: "completed"
}

const ORDER_TYPE = {
    STANDARD: "standard",
    EXPRESS: "express"
}

const MESSAGES = {
    ORDER_PROCESSING: "Your order is being processed"
}

function handleOrder(order):
    if order.status == ORDER_STATUS.PENDING:
        sendNotification(order.customerId, MESSAGES.ORDER_PROCESSING)
        updateDatabase("orders", order.id, status: ORDER_STATUS.PROCESSING)
    if order.type == ORDER_TYPE.EXPRESS:
        priority = "high"
```
