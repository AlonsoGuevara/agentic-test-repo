# Insecure Cryptography

**Severity**: High

## Description
Insecure cryptography encompasses the use of weak, broken, or improperly implemented cryptographic algorithms and practices. This includes using deprecated algorithms (MD5, SHA1, DES, RC4), generating weak random numbers for security purposes, improper key management, hardcoded initialization vectors, use of ECB mode, and rolling custom cryptography instead of using vetted libraries. Weak cryptography can lead to data breaches, forged tokens, and broken confidentiality.

## Detection
- Use of deprecated hash functions for security purposes: `MD5`, `SHA1`
- Use of broken symmetric ciphers: `DES`, `3DES`, `RC4`, `Blowfish`
- ECB block cipher mode (does not provide semantic security)
- Hardcoded initialization vectors (IVs) or nonces
- Use of non-cryptographic random number generators for security-sensitive values: `random()`, `Math.random()`, `rand()`
- Key sizes below recommended minimums (RSA < 2048 bits, AES < 128 bits)
- Custom cryptographic implementations instead of standard libraries
- Passwords hashed without salt or with a static salt
- Keywords to look for: `MD5`, `SHA1`, `DES`, `RC4`, `ECB`, `random()`, `Math.random()`, `rand()`, `static_iv`, `hardcoded_key`

## Remediation
Use modern, vetted cryptographic algorithms and libraries. Use cryptographically secure random number generators. Follow current best practices for key sizes and modes of operation.

**Before:**
```
function generateToken():
    return toString(random())  # Non-cryptographic RNG

function encryptData(data, key):
    cipher = createCipher("DES", "ECB", key)  # Weak algorithm, weak mode
    return cipher.encrypt(data)

function hashData(input):
    return md5(input)  # Broken hash function
```

**After:**
```
function generateToken():
    return toHex(cryptographicRandomBytes(32))  # CSPRNG

function encryptData(data, key):
    iv = cryptographicRandomBytes(16)  # Random IV per encryption
    cipher = createCipher("AES-256", "GCM", key, iv)  # Strong algorithm, authenticated mode
    return iv + cipher.encrypt(data) + cipher.getAuthTag()

function hashData(input):
    return sha256(input)  # Modern hash function
```
