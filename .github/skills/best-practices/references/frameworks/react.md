# React Best Practices

## Component Design
- Prefer functional components with hooks over class components.
- Keep components small and focused — one responsibility per component.
- Extract reusable logic into custom hooks.
- Use composition over prop drilling — leverage Context, compound components, or render props.

## State Management
- Keep state as local as possible — lift only when shared.
- Use `useReducer` for complex state logic with multiple sub-values.
- Avoid unnecessary state — derive values from existing state/props when possible.
- Use a state management library (Zustand, Jotai, Redux Toolkit) only when Context isn't enough.

## Hooks
- Follow the Rules of Hooks — only call at the top level, only in React functions.
- Memoize expensive computations with `useMemo`, not all computations.
- Use `useCallback` for functions passed to optimized child components.
- Keep dependency arrays accurate — don't suppress ESLint warnings.

## Rendering
- Use `key` props correctly — stable, unique identifiers, never array indices for dynamic lists.
- Avoid inline object/array creation in JSX — it causes unnecessary re-renders.
- Use `React.memo` only when profiling shows a component re-renders unnecessarily.
- Prefer early returns and guard clauses over deeply nested conditionals in JSX.

## TypeScript Integration
- Define prop types with interfaces, not inline types.
- Use `React.FC` sparingly — prefer explicit props typing with return type inference.
- Type event handlers explicitly: `React.ChangeEvent<HTMLInputElement>`.
- Use discriminated unions for component variants.

## Side Effects
- Keep `useEffect` focused on one concern per effect.
- Always clean up subscriptions, timers, and event listeners in the cleanup function.
- Avoid setting state in useEffect when it can be done during rendering or in event handlers.
- Use `AbortController` for fetch requests in effects.

## Forms
- Use controlled components for forms that need validation or dynamic behavior.
- Consider libraries like React Hook Form or Formik for complex forms.
- Validate on blur or submit — not on every keystroke for large forms.

## Testing
- Test behavior, not implementation — use React Testing Library.
- Query by role, label, or text — avoid testing internal state or implementation details.
- Test user interactions: click, type, submit — not component lifecycle.
- Mock API calls at the network level (MSW) rather than mocking fetch/axios.

## Performance
- Use React DevTools Profiler to identify bottlenecks before optimizing.
- Lazy load routes and heavy components with `React.lazy` and `Suspense`.
- Virtualize long lists with libraries like `react-window` or `@tanstack/react-virtual`.
- Avoid premature optimization — measure first.

## Project Organization
- Group files by feature/domain, not by type (components/, hooks/, utils/).
- Co-locate tests, styles, and types with their components.
- Use barrel exports (`index.ts`) sparingly to avoid circular dependencies.
