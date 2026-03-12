# Anemic Domain Model

**Severity**: Medium

## Description
Domain objects (entities) contain only data (fields/properties) with no behavior. Business logic lives elsewhere (in separate "Service" or "Manager" classes), violating object-oriented design principles. This results in code that treats objects as mere data containers, increasing coupling and reducing encapsulation.

## Detection
- Classes with only getters/setters and no other methods
- Separate *Service or *Manager classes that operate on data objects
- No business logic in domain objects
- Database-like object structures (entities with columns as properties)
- Mapper or DAO patterns that create objects but leave logic elsewhere
- Domain objects passed between multiple services that manipulate them

## Remediation
Move business logic into the domain objects themselves. Objects should encapsulate both data and the behavior that operates on that data.

**Before:**
```
// Anemic domain model - just data
class Order:
    id: int
    items: List<Item>
    total: Decimal
    status: string
    
    function getId():
        return id
    function setId(id):
        this.id = id
    function getItems():
        return items
    function setItems(items):
        this.items = items
    // ... more getters/setters

// Logic lives in separate service
class OrderService:
    function calculateTotal(order):
        total = 0
        for each item in order.getItems():
            total += item.getPrice() * item.getQuantity()
        return total
    
    function canShip(order):
        return order.getStatus() == "PAID"
    
    function applyDiscount(order, discount):
        order.setTotal(order.getTotal() - discount)
```

**After:**
```
// Rich domain model - data + behavior
class Order:
    id: int
    items: List<Item>
    total: Decimal
    status: OrderStatus
    
    function __init__(id):
        this.id = id
        this.items = []
        this.status = OrderStatus.DRAFT
    
    function addItem(item):
        items.add(item)
        recalculateTotal()
    
    function getTotal():
        return total
    
    private function recalculateTotal():
        total = 0
        for each item in items:
            total += item.calculateLineTotal()
    
    function canShip():
        return status == OrderStatus.PAID
    
    function applyDiscount(discount):
        if discount > total:
            throw IllegalArgumentException("Discount exceeds total")
        total = total - discount
    
    function markAsPaid():
        this.status = OrderStatus.PAID
```
