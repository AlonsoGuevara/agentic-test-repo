# Insecure Dependencies

**Severity**: Medium

## Description
Insecure dependencies occur when an application uses third-party libraries, frameworks, or components with known security vulnerabilities. Attackers actively scan for applications using vulnerable versions and exploit known CVEs. This risk is compounded by transitive dependencies — your direct dependency may itself depend on a vulnerable library. Failure to regularly audit and update dependencies leaves applications exposed to well-documented attack vectors.

## Detection
- Dependency manifests without version pinning: `requests`, `flask` instead of `requests==2.31.0`
- Use of wildcard or greater-than version specifiers: `>=1.0`, `*`, `latest`
- Dependencies not updated for extended periods (check last-modified dates of lock files)
- Missing lock files (`requirements.txt` without hashes, `package.json` without `package-lock.json`)
- Known vulnerable packages being imported or required
- Dependencies pulled from untrusted or custom registries without integrity verification
- Absence of automated dependency scanning in CI/CD pipeline
- Keywords to look for: version specifiers in `requirements.txt`, `pyproject.toml`, `package.json`, `Gemfile`, `go.mod`

## Remediation
Pin dependency versions, use lock files, and regularly scan for known vulnerabilities. Integrate automated dependency auditing into the CI/CD pipeline.

**Before:**
```
# requirements.txt
flask
requests>=1.0
pyyaml
cryptography
```

**After:**
```
# requirements.txt — pinned versions
flask==3.0.2
requests==2.31.0
pyyaml==6.0.1
cryptography==42.0.5

# Add to CI/CD pipeline:
# - Run dependency audit tool on every build
# - Set up automated alerts for new CVEs in dependencies
# - Generate and commit lock files with hashes
```
