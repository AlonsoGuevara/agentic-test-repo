# Pandas Best Practices

## Data Loading
- Use `dtype` parameter when reading CSVs to enforce types upfront.
- Use `parse_dates` for date columns instead of converting after load.
- Prefer `read_parquet` over `read_csv` for large datasets — faster and type-safe.

## Data Manipulation
- Use vectorized operations over `iterrows()` or `apply()` when possible.
- Chain operations with method chaining for readability: `.pipe()`, `.assign()`, `.query()`.
- Use `.loc[]` and `.iloc[]` for explicit indexing — avoid chained indexing (`df[col][row]`).

## Memory Efficiency
- Downcast numeric types with `pd.to_numeric(downcast=...)`.
- Use `category` dtype for low-cardinality string columns.
- Process large files in chunks with `chunksize` parameter.

## Missing Data
- Use `pd.isna()` / `pd.notna()` for null checks.
- Be explicit about fill strategies: `fillna()`, `interpolate()`, or `dropna()`.
- Document assumptions about missing data handling.

## GroupBy & Aggregation
- Use `.agg()` with named aggregations for clarity.
- Prefer `.transform()` when you need results aligned to the original index.
- Avoid groupby inside loops — restructure as a single groupby operation.

## Index Management
- Reset index after filtering or grouping to keep a clean integer index.
- Use meaningful indices only when the index will be used for lookups or joins.
- Avoid `inplace=True` — it's being deprecated and harms readability.

## Testing DataFrames
- Use `pd.testing.assert_frame_equal()` for comparing DataFrames in tests.
- Test edge cases: empty DataFrames, single-row, all-null columns.
- Validate schema (column names, dtypes) as part of data pipeline tests.

## Performance
- Profile with `df.info(memory_usage='deep')` to understand memory usage.
- Use `numpy` operations directly for heavy numerical computation.
- Consider `polars` for performance-critical data pipelines.
