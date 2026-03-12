# Cargo Cult Programming

**Severity**: Medium

## Description
Writing code by copying patterns, idioms, or techniques without understanding why they're used. Developers ritualistically include code, constructs, or patterns they've seen elsewhere without comprehending their purpose or necessity. This leads to unnecessary complexity, dead code, and incorrect usage of patterns.

## Detection
- Code similar to tutorials or Stack Overflow snippets without adaptation
- Libraries imported but not used (dead imports)
- Patterns applied everywhere regardless of context
- Comments like "I don't know why this is here but removing it breaks things"
- Boilerplate code that doesn't match the actual problem
- Patterns used incorrectly or for the wrong use case
- No clear reason for architectural decisions when asked

## Remediation
Understand the "why" before copying patterns. Verify every import and function call serves a purpose. Tailor patterns to your actual problem, don't apply generic solutions universally. Ask "what problem does this solve?" before using it.

**Before:**
```
// Cargo cult: Copied from many projects, included everywhere
class BaseRepository:
    async function getById(id):
        // This gets used... somewhere?
    
    async function getAll():
        // Not sure when this is called
    
    async function save(entity):
        // Maybe?

// Copied middleware pattern without understanding it
app.use(function(request, response, next):
    // What does this do? Don't remember
    response.setHeader("Cache-Control", "no-cache")
    next()
)

// Unused imports from template
import UUID from "uuid"
import EventEmitter from "events"
import Logger from "logging"
// ...actually not used in this file

// Decorator because it's trendy
@deprecated  // Why? It's still being used!
class UserService:
    // ...
```

**After:**
```
// Clear, purposeful design for actual use cases
class UserRepository:
    // Only methods actually needed
    async function findById(id):
        return this.db.users.findOne(id: id)

// Intentional middleware with clear purpose
app.use(function(request, response, next):
    // Cache busting for API responses to prevent stale data
    response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate")
    next()
)

// Only import what's used
import { v4 as uuidv4 } from "uuid"

const userId = uuidv4()

// Decorators used appropriately with clear semantics
@requiresAuth  // This service requires authentication
class UserService:
    // ...
```

**Questions to Ask Before Copying:**
- What problem does this solve?
- Do I actually have that problem?
- Is this pattern appropriate for my case?
- Can I understand and explain this to someone else?
- Can I remove this without breaking anything?
