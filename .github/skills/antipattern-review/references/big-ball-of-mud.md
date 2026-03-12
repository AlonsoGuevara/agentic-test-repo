# Big Ball of Mud

**Severity**: High

## Description
A codebase with no clear structure, organization, or architectural boundaries. Code is tightly coupled, difficult to understand, expensive to modify, and nearly impossible to test. Systems start with good architecture but gradually degrade as changes are made without proper refactoring.

## Detection
- No clear layering or separation of concerns
- Functions/classes with mixed responsibilities (database, business logic, UI)
- Difficult to explain the architecture or where to find related code
- Tight coupling between modules (can't test one without the others)
- No clear API boundaries between components
- Sporadic use of design patterns without overall strategy
- Large files with 1000+ lines of mixed code
- Comments suggesting "this needs refactoring but it works"
- New features require changes in many unrelated files

## Remediation
Incrementally refactor toward a clear architecture. Introduce layers, boundaries, and design patterns. Decouple tightly coupled components using interfaces and dependency injection. Extract functions until each has a single responsibility.

**Before:**
```
// big_ball_of_mud module - ~2000 LOC with everything mixed
class SystemManager:
    function __init__(dbConnectionString):
        // Creates database connection
        this.conn = createConnection(dbConnectionString)
    
    function processUserRequest(rawRequest):
        // Parses request, validates, executes business logic, updates DB, sends response
        data = parseJson(rawRequest)
        
        // Validation
        if data.userId == null:
            return "invalid"
        
        // Business logic
        if data.action == "buy":
            user = this.conn.execute("SELECT * FROM users WHERE id=?", data.userId)
            if user.balance < data.amount:
                return "insufficient_funds"
            // More logic... hundreds more lines
            this.conn.execute("UPDATE users SET balance = balance - ? WHERE id = ?", 
                            data.amount, data.userId)
            // Email notification, logging, etc.
            // ...
```

**After:**
```
// models module
class User:
    function __init__(id, name, balance):
        this.id = id
        this.name = name
        this.balance = balance
    
    function canAfford(amount):
        return this.balance >= amount

// repositories module
class UserRepository:
    function __init__(dbConnection):
        this.db = dbConnection
    
    function getUser(userId):
        return this.db.query(User).filter(id: userId).first()
    
    function saveUser(user):
        this.db.update(user)

// services module
class PurchaseService:
    function __init__(userRepo, orderRepo, notificationService):
        this.userRepo = userRepo
        this.orderRepo = orderRepo
        this.notifier = notificationService
    
    function processPurchase(userId, amount):
        user = this.userRepo.getUser(userId)
        if not user.canAfford(amount):
            throw InsufficientFundsError()
        
        user.balance = user.balance - amount
        this.userRepo.saveUser(user)
        this.notifier.sendPurchaseConfirmation(user)
        return {success: true}

// api module
class PurchaseHandler:
    function __init__(purchaseService):
        this.service = purchaseService
    
    function post(request):
        data = request.json
        try:
            result = this.service.processPurchase(data.userId, data.amount)
            return {status: "success", data: result}, 200
        catch InsufficientFundsError:
            return {error: "Insufficient funds"}, 400
```
