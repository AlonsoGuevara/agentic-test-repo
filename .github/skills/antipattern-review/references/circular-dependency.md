# Circular Dependency

**Severity**: High

## Description
Module A depends on module B, and module B depends on module A (or a longer cycle). Circular dependencies create tight coupling, make code difficult to test, understand, and refactor. They can also cause issues with initialization order and module loading.

## Detection
- Import statements that directly or indirectly create a cycle
- Classes in the same module importing each other
- Service A importing Service B which imports Service A
- `deepcopy` or other tricks used to avoid circular import errors
- Circular references in object graphs
- Module-level side effects during imports that depend on other modules

## Remediation
Break cycles by extracting common logic, introducing interfaces/abstract classes, or using dependency injection. Restructure the module hierarchy.

**Before:**
```
// userService module
import OrderService

class UserService:
    function __init__():
        this.orderService = OrderService()
    
    function getUserOrders(userId):
        return this.orderService.getOrdersByUser(userId)

// orderService module
import UserService

class OrderService:
    function __init__():
        this.userService = UserService()
    
    function getOrdersByUser(userId):
        user = this.userService.getUser(userId)
        // ...
```

**After:**
```
// models module
class User:
    // domain object

class Order:
    // domain object

// userService module
class UserService:
    function __init__(repository):
        this.repository = repository
    
    function getUser(userId):
        return this.repository.getUser(userId)

// orderService module
class OrderService:
    function __init__(repository):
        this.repository = repository
    
    function getOrdersByUser(userId):
        return this.repository.getOrders(userId: userId)

// app module - Dependency injection at composition root
userService = UserService(userRepository)
orderService = OrderService(orderRepository)
```
