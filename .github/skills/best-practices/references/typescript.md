# TypeScript Best Practices

## Code Style
- Use `camelCase` for variables and functions, `PascalCase` for types, interfaces, and classes.
- Prefer `const` over `let`; never use `var`.
- Use semicolons consistently (or configure a formatter like Prettier to handle it).

## Type Safety
- Enable `strict: true` in `tsconfig.json`.
- Avoid `any` — use `unknown` when the type is truly uncertain, then narrow.
- Prefer interfaces for object shapes; use type aliases for unions, intersections, and mapped types.
- Use discriminated unions for state modeling.

## Project Structure
- Organize by feature or domain, not by file type.
- Use barrel files (`index.ts`) sparingly — they can cause circular dependencies.
- Keep `tsconfig.json` strict and explicit about paths and module resolution.

## Error Handling
- Use typed error classes or result types instead of throwing generic `Error`.
- Handle promise rejections — never leave promises unhandled.
- Use `try/catch` at boundaries (API handlers, event listeners), not deep in business logic.

## Functions
- Keep functions small and focused on one task.
- Use explicit return types for public/exported functions.
- Prefer named functions over anonymous for better stack traces.
- Use default parameters instead of short-circuit logic.

## Null Safety
- Prefer `undefined` over `null` for consistency (unless an API requires `null`).
- Use optional chaining (`?.`) and nullish coalescing (`??`).
- Avoid non-null assertions (`!`) — narrow the type properly instead.

## Testing
- Use a testing framework like Vitest or Jest.
- Write tests that describe behavior, not implementation.
- Mock external dependencies at boundaries, not deep internals.
- Use `describe`/`it` blocks with clear, descriptive names.

## Dependencies
- Keep `dependencies` vs `devDependencies` accurate.
- Use a lockfile (`package-lock.json`, `pnpm-lock.yaml`).
- Audit dependencies regularly for security vulnerabilities.

## Documentation
- Use JSDoc comments for exported functions and types.
- Document complex type parameters and generics.
- Keep README updated with setup, build, and test instructions.

## Security
- Never hardcode secrets — use environment variables.
- Validate all external input at system boundaries (API routes, form inputs).
- Sanitize output to prevent XSS when rendering user content.
- Use parameterized queries for database operations.

## Async Patterns
- Use `async/await` over raw promises and callbacks.
- Use `Promise.all` for independent concurrent operations.
- Avoid mixing `async/await` with `.then()` chains in the same function.
- Always handle errors in async functions — unhandled rejections crash Node.js.

## Immutability
- Prefer `readonly` for properties that shouldn't change.
- Use `Readonly<T>`, `ReadonlyArray<T>` for immutable data structures.
- Use spread/destructuring for object and array copies instead of mutation.
